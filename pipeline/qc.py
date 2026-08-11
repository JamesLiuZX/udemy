#!/usr/bin/env python3
"""Quality gate. Blocks a release build on anything that would cost a rating,
trigger a rejection, or embarrass you in a review.

    python3 pipeline/qc.py --course courses/ai-for-pms            # authoring checks
    python3 pipeline/qc.py --course courses/ai-for-pms --release  # + built artifacts

Two severities:
  FAIL  — do not submit. Policy violations and hard technical standards.
  WARN  — fix before you'd call it finished. Craft issues.
"""

from __future__ import annotations

import argparse
import html
import json
import re
import shutil
import statistics
import subprocess
import sys
from dataclasses import dataclass, field
from pathlib import Path

import yaml

sys.path.insert(0, str(Path(__file__).resolve().parent))

import captions as cap
from lecture import load_course
from markup import render as render_markup
from video import measure_loudness, probe

# Udemy technical standards (we target above the floor, and check the floor).
MIN_TOTAL_MINUTES = 30
MIN_LECTURES = 5
MIN_HEIGHT = 720
TARGET_ASPECT = 16 / 9
LUFS_RANGE = (-18.0, -14.0)
MAX_TRUE_PEAK = -1.0

# Craft thresholds.
MAX_LECTURE_MINUTES = 12
MAX_NARRATION_SLIDE_OVERLAP = 0.25      # narration must not just read the slide

# docs/04-quality-bar.md §7 — rhythm, density, and voice checks.
MIN_SENTENCE_STDEV = 4.0                # below this, sentence rhythm reads uniform
MAX_SLIDE_SECONDS = 90                  # a static frame beyond this is "podcast with slides"
MIN_MINUTES_FOR_FIGURE = 4              # TTS lectures past this need a figure/diagram/table
MAX_BULLETS_SHARE = 0.5                 # no lecture is more than half bullets slides
MIN_YOU_PER_100_WORDS = 1.0             # direct-address floor
MIN_MINUTES_FOR_QUESTION = 4            # monologue drift past this needs a "?"
_VISUAL_LAYOUTS = {"figure", "diagram", "table", "metrics"}

# LLM tells and empty filler. Deliberately excludes words like "actually" and
# "of course", which are ordinary spoken English and read as natural narration.
FILLER = re.compile(
    r"\b(basically|obviously|simply put|as we all know|needless to say|"
    r"it goes without saying|delve|in today's fast-paced world|"
    r"unlock the power|game-?changer|revolutioniz|it's important to note|"
    r"in conclusion|tapestry|testament to)\w*\b", re.I)

# Words hunspell won't know but that are correct in this domain.
ALLOW = {
    "ai", "llm", "llms", "rag", "prd", "prds", "pm", "pms", "api", "apis", "kpi",
    "kpis", "openai", "anthropic", "chatgpt", "claude", "gpt", "embeddings",
    "embedding", "tokenizer", "tokenization", "tokens", "eval", "evals",
    "hallucination", "hallucinations", "reranker", "rerank", "reranking",
    "chunking", "vector", "vectors", "dataset", "datasets", "runbook",
    "roadmap", "stakeholder", "stakeholders", "onboarding", "workflow",
    "workflows", "dashboards", "instrumentation", "observability", "latency",
    "throughput", "p95", "p99", "lufs", "srt", "mp4", "udemy", "mcp",
    "multimodal", "finetune", "finetuning", "prompt", "prompts", "prompting",
    "agentic", "deflection", "guardrail", "guardrails", "backtest", "gdpr",
    "pii", "config", "yaml", "json", "sql", "csv", "url", "urls",
    # hunspell splits hyphenated compounds, so both halves must be known
    "kickoff", "offs", "tradeoff", "tradeoffs", "ship", "red", "teaming",
    "pts", "cutoff", "groundable", "leaderboard", "leaderboards",
    "overcorrecting", "walkthrough", "walkthroughs", "offboarding",
    # Python identifiers, shown verbatim in the 4.7 code listing
    "defaultdict", "int", "len",
}


@dataclass
class Report:
    fails: list[str] = field(default_factory=list)
    warns: list[str] = field(default_factory=list)

    def fail(self, msg: str) -> None:
        self.fails.append(msg)

    def warn(self, msg: str) -> None:
        self.warns.append(msg)


# ---------------------------------------------------------------------------
# policy
# ---------------------------------------------------------------------------

def check_policy(course: dict, rep: Report) -> None:
    """The checks that protect the account, not just the rating."""
    disclosure = course.get("ai_disclosure", "").strip()
    required = "This course contains the use of artificial intelligence."

    if disclosure != required:
        rep.fail(
            f"course.yaml ai_disclosure must be exactly {required!r} "
            f"(got {disclosure!r})"
        )

    desc = " ".join(str(course.get("description", "")).split())
    if not desc:
        rep.warn("No landing-page description in course.yaml yet.")
    elif required.lower() not in desc.lower():
        rep.fail(
            "The AI disclosure is missing from the course description. Udemy "
            "requires it when AI tools are used; put it at the end."
        )
    elif not desc.rstrip().rstrip(".").endswith(required.rstrip(".")):
        rep.warn("AI disclosure is present but not at the end of the description "
                 "(Udemy's recommended placement).")

    outcomes = course.get("outcomes", [])
    if len(outcomes) > 7:
        rep.warn(f"{len(outcomes)} outcomes listed; courses score better with 4-7.")
    if len(outcomes) < 3:
        rep.warn("Fewer than 3 outcomes — the landing page will feel thin.")


# ---------------------------------------------------------------------------
# authoring
# ---------------------------------------------------------------------------

_WORD = re.compile(r"[A-Za-z][A-Za-z'-]+")


def _slide_text(slide) -> str:
    rendered = render_markup(slide.body)
    text = re.sub(r"<[^>]+>", " ", rendered)
    # Figures (figures.py) HTML-escape their text for correct SVG output,
    # e.g. an apostrophe becomes &#x27;. Undo that before spellchecking, or
    # hunspell sees the literal entity instead of the word it belongs to.
    text = html.unescape(text)
    for k in ("kicker", "lead", "note", "attrib"):
        if slide.meta.get(k):
            text += " " + slide.meta[k]
    return " ".join(text.split())


NGRAM = 4


def _ngrams(text: str, n: int = NGRAM) -> set[tuple[str, ...]]:
    words = [w.lower() for w in _WORD.findall(text)]
    return {tuple(words[i:i + n]) for i in range(len(words) - n + 1)}


def _overlap(narration: str, slide_text: str) -> float:
    """Fraction of the slide's 4-word phrases that recur verbatim in narration.

    Narration reading the bullets aloud is the most-cited complaint about
    slide-based courses. Phrase overlap detects that directly: reading aloud
    scores high, genuine paraphrase scores near zero.

    (A bare word-set comparison was tried first and proved useless — narration
    legitimately reuses a slide's key terms, so any real lecture scored ~60%.)
    """
    sg = _ngrams(slide_text)
    if len(sg) < 4:
        return 0.0
    return len(sg & _ngrams(narration)) / len(sg)


def _spellcheck(texts: list[str], lang: str = "en_US") -> set[str]:
    """Slide typos are a documented reason learners disengage, so this is a FAIL
    not a warning. Dictionary is configurable — the scripts are written in one
    English and must be checked against that same one."""
    exe = shutil.which("hunspell")
    if not exe:
        return set()
    blob = "\n".join(texts)
    try:
        out = subprocess.run([exe, "-d", lang, "-l"], input=blob.encode(),
                             capture_output=True, timeout=180).stdout.decode()
    except Exception:
        return set()
    bad = set()
    for w in out.split():
        lw = w.lower().strip("'-")
        if lw in ALLOW or len(lw) <= 2 or any(ch.isdigit() for ch in lw):
            continue
        # CamelCase / product names are usually intentional
        if w[:1].isupper() and any(c.isupper() for c in w[1:]):
            continue
        bad.add(w)
    return bad


def _slide_has_visual(slide) -> bool:
    """A figure, diagram, table or metrics band, however it's authored — as the
    slide's own layout, or embedded in the body of another layout (a ```figure
    block on a two-col slide, a ::: metrics container, a raw pipe table)."""
    if slide.layout in _VISUAL_LAYOUTS:
        return True
    body = slide.body
    if "```figure" in body or "```mermaid" in body or "::: metrics" in body:
        return True
    pipe_lines = [ln for ln in body.splitlines() if ln.strip().startswith("|")]
    return len(pipe_lines) >= 2


_YOU = re.compile(r"\b(you|your|yours|you're|you'll|you've|you'd)\b", re.I)


def check_rhythm_and_delivery(lec, rep: Report, wpm: int) -> None:
    """docs/04-quality-bar.md §7: rhythm, density and direct-address checks that
    catch uniform, essay-voice, or monologue-drift narration before it's rendered."""
    tag = f"[{lec.id}]"
    narration = lec.narration
    words = narration.split()

    if lec.voice != "human":
        sentences = cap.split_sentences(narration)
        counts = [len(s.split()) for s in sentences if s.split()]
        if len(counts) >= 3:
            stdev = statistics.stdev(counts)
            if stdev < MIN_SENTENCE_STDEV:
                rep.warn(f"{tag} sentence-length stdev {stdev:.1f} words "
                         f"(<{MIN_SENTENCE_STDEV:g}) across the narration — "
                         f"uniform rhythm reads as generated. Swing sentence "
                         f"lengths more; let a short one land like a drum hit.")

    if words:
        you_rate = len(_YOU.findall(narration)) / len(words) * 100
        if you_rate < MIN_YOU_PER_100_WORDS:
            rep.warn(f"{tag} {you_rate:.1f} 'you/your' per 100 words "
                     f"(<{MIN_YOU_PER_100_WORDS:g}) — drifting into essay voice "
                     f"instead of talking to the learner.")

    est_min = lec.estimated_seconds(wpm) / 60
    if est_min > MIN_MINUTES_FOR_QUESTION and "?" not in narration:
        rep.warn(f"{tag} {est_min:.1f} min with no '?' in the narration — "
                 f"monologue drift. A question is how a teacher holds attention.")

    for i, slide in enumerate(lec.slides, start=1):
        slide_seconds = slide.word_count / wpm * 60
        if slide_seconds > MAX_SLIDE_SECONDS:
            rep.warn(f"{tag} slide {i}: {slide_seconds:.0f}s of narration on one "
                     f"static frame (>{MAX_SLIDE_SECONDS}s) — split the slide or "
                     f"add a build.")

    if lec.slides:
        bullets_share = sum(1 for s in lec.slides if s.layout == "bullets") / len(lec.slides)
        if bullets_share > MAX_BULLETS_SHARE:
            rep.warn(f"{tag} {bullets_share:.0%} of slides are 'bullets' "
                     f"(>{MAX_BULLETS_SHARE:.0%}) — add a figure, table or diagram "
                     f"to break up the density.")

    if lec.voice != "human" and est_min > MIN_MINUTES_FOR_FIGURE:
        if not any(_slide_has_visual(s) for s in lec.slides):
            rep.warn(f"{tag} {est_min:.1f} min with no figure, diagram, table or "
                     f"metrics slide (>{MIN_MINUTES_FOR_FIGURE} min) — text-heavy "
                     f"drift under production pressure.")


def check_opener_diversity(lectures, rep: Report) -> None:
    """docs/04-quality-bar.md §7: 3 consecutive lectures opening on the same
    slide layout is the agenda-opener monotony tell. Warn once per streak."""
    run: list = []
    for lec in lectures:
        if not lec.slides:
            run = []
            continue
        layout = lec.slides[0].layout
        if run and run[-1][1] == layout:
            run.append((lec, layout))
        else:
            run = [(lec, layout)]
        if len(run) == 3:
            ids = ", ".join(l.id for l, _ in run)
            rep.warn(f"[{ids}] three consecutive lectures open on a '{layout}' "
                     f"slide — agenda-opener monotony. Vary the opener pattern "
                     f"(docs/04 §3).")


# Words too generic to anchor a continuity match on their own (a running case's
# meaning line is prose, not a keyword list — this trims it to the specific
# nouns worth matching against).
_CONTINUITY_STOP = {
    "reviewers", "score", "scores", "scoring", "spread", "without", "before",
    "after", "above", "below", "fewer", "misses", "fatigues", "consequence",
    "makes", "common", "explicit", "formally", "retold", "collapses", "steps",
}


def check_story_continuity(lectures, story_bible_path: Path, rep: Report) -> None:
    """docs/04-quality-bar.md §7 and §2: a number canonical in story-bible.yaml
    that shows up in narration paired with a different value is exactly the
    drift long-form generated writing is prone to. Simple literal match: find
    narration sentences that share enough of a canonical number's topic words
    and contain a number, then check that number against the ledger."""
    if not story_bible_path.exists():
        return
    bible = yaml.safe_load(story_bible_path.read_text(encoding="utf-8")) or {}
    numbers = bible.get("numbers", [])

    entries = []
    for n in numbers:
        value = str(n.get("value", "")).strip()
        meaning = str(n.get("meaning", "")).strip()
        if not value or not meaning:
            continue
        keywords = sorted({
            w.strip(",.").lower() for w in meaning.split()
            if len(w.strip(",.")) >= 6 and w.strip(",.").lower() not in _CONTINUITY_STOP
        })
        if keywords:
            entries.append((value, keywords, meaning))
    if not entries:
        return

    num_re = re.compile(r"\d[\d,]*\.?\d*%?")
    # "4.2's golden set", "back in 7.4" — lecture cross-references, not case-study
    # numbers. This course's ids are always section.lecture, so a bare N.N (no
    # unit) is a citation, not a value; a preceding "lecture/figure/section" word
    # catches the rest.
    LECTURE_ID = re.compile(r"^\d{1,2}\.\d{1,2}$")
    LECTURE_WORD = re.compile(r"(?:lecture|figure|fig\.?|section|chapter)\s*$", re.I)

    for lec in lectures:
        for sentence in cap.split_sentences(lec.narration):
            low = sentence.lower()
            for value, keywords, meaning in entries:
                need = 1 if len(keywords) == 1 else 2
                if sum(1 for k in keywords if k in low) < need:
                    continue
                found = [
                    m.group() for m in num_re.finditer(sentence)
                    if not LECTURE_ID.match(m.group())
                    and not LECTURE_WORD.search(sentence[max(0, m.start() - 12):m.start()])
                ]
                if not found:
                    continue
                value_tokens = {v.strip().rstrip("%") for v in value.split(",")}
                if any(f.rstrip("%").replace(",", "") in value_tokens or f in value
                       for f in found):
                    continue
                rep.warn(f"[{lec.id}] narration has {', '.join(found)} near "
                         f"'{meaning}' but story-bible.yaml records {value!r} for "
                         f"it — check for continuity drift.")


def check_lectures(lectures, course: dict, rep: Report) -> None:
    if not lectures:
        rep.fail("No lecture sources found. Nothing to check.")
        return

    wpm = course.get("production", {}).get("words_per_minute", 150)
    slide_texts: list[str] = []

    for lec in lectures:
        tag = f"[{lec.id}]"

        if not lec.verified:
            rep.fail(f"{tag} verified: false — you have not signed off this script. "
                     f"Read it and set verified: true once every claim is one you "
                     f"can personally defend.")

        raw = lec.path.read_text(encoding="utf-8")
        if "[INSTRUCTOR-INPUT" in raw:
            n = raw.count("[INSTRUCTOR-INPUT")
            rep.fail(f"{tag} has {n} unfilled [INSTRUCTOR-INPUT] marker(s). "
                     f"These are the moments the course depends on you for.")

        est = lec.estimated_seconds(wpm) / 60
        if est > MAX_LECTURE_MINUTES:
            rep.warn(f"{tag} estimated {est:.1f} min (>{MAX_LECTURE_MINUTES}); "
                     f"consider splitting.")
        if est < 1.0 and lec.voice != "human":
            rep.warn(f"{tag} estimated {est:.1f} min — very short for a lecture.")

        for i, slide in enumerate(lec.slides, start=1):
            st = _slide_text(slide)
            slide_texts.append(st)

            if slide.narration.strip():
                ov = _overlap(slide.narration, st)
                if ov > MAX_NARRATION_SLIDE_OVERLAP:
                    rep.warn(f"{tag} slide {i}: narration repeats {ov:.0%} of the "
                             f"slide text — it will sound like reading aloud.")
            elif lec.voice != "human":
                rep.warn(f"{tag} slide {i}: no narration.")

            if len(st) > 700:
                rep.warn(f"{tag} slide {i}: {len(st)} chars of slide text — dense.")

        fill = FILLER.findall(lec.narration)
        if fill:
            rep.warn(f"{tag} filler/LLM-tell phrases: "
                     f"{', '.join(sorted({f.lower() for f in fill}))}")

        # Em dashes are one of the strongest written tells of generated text, and
        # they correspond to nothing a speaker actually does. House rule: none in
        # anything a learner reads or hears.
        dashes = sum(s.body.count("—") + s.narration.count("—") for s in lec.slides)
        if dashes:
            rep.fail(f"{tag} contains {dashes} em dash(es) in learner-facing copy. "
                     f"Use a colon, a full stop, or brackets.")

        check_rhythm_and_delivery(lec, rep, wpm)

    lang = course.get("production", {}).get("spellcheck_lang", "en_US")
    bad = _spellcheck(slide_texts, lang)
    if bad:
        rep.fail(f"Possible slide typos [{lang}] (fix, or add to ALLOW in qc.py): "
                 f"{', '.join(sorted(bad)[:25])}")

    check_opener_diversity(lectures, rep)


# ---------------------------------------------------------------------------
# built artifacts
# ---------------------------------------------------------------------------

def check_release(out_root: Path, rep: Report) -> None:
    manifest = out_root / "manifest.json"
    if not manifest.exists():
        rep.fail(f"No manifest at {manifest}. Run build.py before --release.")
        return

    data = json.loads(manifest.read_text(encoding="utf-8"))
    lectures = [l for l in data.get("lectures", []) if not l.get("error")]

    if data.get("provider") == "offline":
        rep.fail("Built with the 'offline' espeak scaffold voice. "
                 "Re-build with a production TTS provider before submitting.")

    if len(lectures) < MIN_LECTURES:
        rep.fail(f"{len(lectures)} lectures built; Udemy requires ≥{MIN_LECTURES}.")

    total = sum(l.get("duration", 0) or 0 for l in lectures)
    if total / 60 < MIN_TOTAL_MINUTES:
        rep.fail(f"{total / 60:.1f} min of video; Udemy requires "
                 f"≥{MIN_TOTAL_MINUTES} min.")

    for l in lectures:
        tag = f"[{l.get('id')}]"
        mp4 = out_root / (l.get("video") or "")
        if not mp4.exists():
            rep.fail(f"{tag} missing video {mp4}")
            continue

        info = probe(mp4)
        h, w = info.get("height") or 0, info.get("width") or 0
        if h < MIN_HEIGHT:
            rep.fail(f"{tag} {w}x{h} is below the {MIN_HEIGHT}p minimum.")
        if w and h and abs((w / h) - TARGET_ASPECT) > 0.02:
            rep.fail(f"{tag} aspect {w / h:.3f} is not 16:9 ({TARGET_ASPECT:.3f}).")
        if (info.get("channels") or 0) < 2:
            rep.fail(f"{tag} audio has {info.get('channels')} channel(s); "
                     f"Udemy requires sound in both left and right.")

        loud = measure_loudness(mp4)
        if loud:
            i, tp = loud.get("input_i", 0.0), loud.get("input_tp", 0.0)
            if not (LUFS_RANGE[0] <= i <= LUFS_RANGE[1]):
                rep.warn(f"{tag} loudness {i:.1f} LUFS outside "
                         f"{LUFS_RANGE[0]}..{LUFS_RANGE[1]}.")
            if tp > MAX_TRUE_PEAK:
                rep.fail(f"{tag} true peak {tp:.1f} dBTP exceeds {MAX_TRUE_PEAK}; "
                         f"audio will clip.")

        srt = out_root / (l.get("srt") or "")
        if not srt.exists() or srt.stat().st_size == 0:
            rep.warn(f"{tag} captions missing — upload .srt for every lecture.")

    print(f"\n  built total: {total / 3600:.2f}h across {len(lectures)} lectures")


# ---------------------------------------------------------------------------

def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--course", required=True)
    ap.add_argument("--out", default="build")
    ap.add_argument("--release", action="store_true",
                    help="also check built MP4s/SRTs against Udemy standards")
    args = ap.parse_args()

    course, lectures = load_course(Path(args.course))
    rep = Report()

    check_policy(course, rep)
    check_lectures(lectures, course, rep)
    check_story_continuity(lectures, Path(args.course) / "story-bible.yaml", rep)
    if args.release:
        check_release(Path(args.out) / course["slug"], rep)

    print()
    for w in rep.warns:
        print(f"  WARN  {w}")
    for f in rep.fails:
        print(f"  FAIL  {f}")

    print(f"\n  {len(rep.fails)} fail · {len(rep.warns)} warn")
    if rep.fails:
        print("  NOT ready to submit.\n")
        return 1
    print("  Passes the gate.\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
