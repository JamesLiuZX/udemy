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

# Delivery and continuity thresholds (docs/04-quality-bar.md §7).
MIN_SENTENCE_RHYTHM_STDEV = 4.0    # words; below this, sentence length reads as generated
MAX_STATIC_FRAME_SECONDS = 90      # one slide's narration, at the course wpm
FIGURE_FLOOR_MINUTES = 4.0         # TTS lectures past this need a figure/diagram/table/metrics slide
MAX_BULLETS_SHARE = 0.5
MIN_OPENER_RUN = 3                 # consecutive lectures sharing an opener layout
MIN_DIRECT_ADDRESS_PER_100 = 1.0   # "you"/"your" per 100 narration words
QUESTION_FLOOR_MINUTES = 4.0       # lectures past this need at least one "?"

FIGURE_LAYOUTS = {"figure", "diagram", "table", "metrics"}

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


# ---------------------------------------------------------------------------
# delivery and continuity (docs/04-quality-bar.md §7)
# ---------------------------------------------------------------------------

_SENTENCE_SPLIT = re.compile(r"(?<=[.!?])\s+")
_YOU = re.compile(r"\byou(r|rs)?\b", re.I)
_ALPHA_WORD = re.compile(r"[A-Za-z]+")
_NUMERIC = re.compile(r"\d+(?:\.\d+)?%?")

_NUM_WORDS = {
    "zero": "0", "one": "1", "two": "2", "three": "3", "four": "4",
    "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9",
    "ten": "10", "eleven": "11", "twelve": "12", "thirteen": "13",
    "fourteen": "14", "fifteen": "15", "sixteen": "16", "seventeen": "17",
    "eighteen": "18", "nineteen": "19", "twenty": "20", "thirty": "30",
    "forty": "40", "fifty": "50", "sixty": "60", "seventy": "70",
    "eighty": "80", "ninety": "90", "hundred": "100",
}

_STORY_STOPWORDS = {
    "the", "a", "an", "of", "to", "and", "or", "in", "on", "at", "for",
    "with", "is", "are", "it", "that", "this", "as", "by", "be", "than",
}


def _sentences(text: str) -> list[str]:
    return [s.strip() for s in _SENTENCE_SPLIT.split(text.strip()) if s.strip()]


def _normalize_numbers(text: str) -> str:
    """Spell-out numbers ("six", "twenty") to digits, so a line written for the
    ear ("Two, three, three, four, five.") can be compared against a bible value
    written as digits ("2, 3, 3, 4, 5")."""
    return _ALPHA_WORD.sub(lambda m: _NUM_WORDS.get(m.group(0).lower(), m.group(0)), text)


def _story_keywords(meaning: str) -> set[str]:
    words = _ALPHA_WORD.findall(meaning.lower())
    return {w for w in words
            if len(w) > 3 and w not in _STORY_STOPWORDS and w not in _NUM_WORDS}


def _check_rhythm(lec, rep: Report) -> None:
    counts = [c for c in (len(_WORD.findall(s)) for s in _sentences(lec.narration)) if c]
    if len(counts) < 4:
        return
    sd = statistics.pstdev(counts)
    if sd < MIN_SENTENCE_RHYTHM_STDEV:
        rep.warn(f"[{lec.id}] sentence-length stdev {sd:.1f} words "
                 f"(<{MIN_SENTENCE_RHYTHM_STDEV:.0f}) — uniform rhythm reads as generated.")


def _check_static_frames(lec, wpm: int, rep: Report) -> None:
    for i, slide in enumerate(lec.slides, start=1):
        secs = slide.word_count / wpm * 60
        if secs > MAX_STATIC_FRAME_SECONDS:
            rep.warn(f"[{lec.id}] slide {i} ({slide.layout}): ~{secs:.0f}s of "
                     f"narration on one frame (>{MAX_STATIC_FRAME_SECONDS:.0f}s) "
                     f"— split the slide or add a build.")


def _check_figure_floor(lec, wpm: int, rep: Report) -> None:
    if lec.voice == "human":
        return
    minutes = lec.estimated_seconds(wpm) / 60
    if minutes <= FIGURE_FLOOR_MINUTES:
        return
    if any(s.layout in FIGURE_LAYOUTS for s in lec.slides):
        return
    rep.warn(f"[{lec.id}] {minutes:.1f} min with no figure/diagram/table/metrics "
             f"slide — text-heavy drift.")


def _check_bullets_share(lec, rep: Report) -> None:
    total = len(lec.slides)
    if not total:
        return
    share = sum(1 for s in lec.slides if s.layout == "bullets") / total
    if share > MAX_BULLETS_SHARE:
        rep.warn(f"[{lec.id}] {share:.0%} of slides are 'bullets' "
                 f"(>{MAX_BULLETS_SHARE:.0%}) — vary the layouts.")


def _check_direct_address(lec, rep: Report) -> None:
    wc = lec.word_count
    if wc < 50:
        return
    rate = len(_YOU.findall(lec.narration)) / wc * 100
    if rate < MIN_DIRECT_ADDRESS_PER_100:
        rep.warn(f"[{lec.id}] {rate:.2f} 'you/your' per 100 words "
                 f"(<{MIN_DIRECT_ADDRESS_PER_100:.0f}) — drifting into essay voice.")


def _check_question_presence(lec, wpm: int, rep: Report) -> None:
    minutes = lec.estimated_seconds(wpm) / 60
    if minutes <= QUESTION_FLOOR_MINUTES:
        return
    if "?" not in lec.narration:
        rep.warn(f"[{lec.id}] no '?' in {minutes:.1f} min of narration — "
                 f"monologue drift.")


def _check_opener_diversity(lectures, rep: Report) -> None:
    """Scans the whole course in curriculum order for runs of consecutive
    lectures whose first slide shares a layout — one warning per run, not
    per lecture, so a run of 5 doesn't produce 3 overlapping warnings."""
    run_start = 0
    n = len(lectures)
    for i in range(1, n + 1):
        same = (i < n and lectures[i].slides and lectures[run_start].slides
                and lectures[i].slides[0].layout == lectures[run_start].slides[0].layout)
        if not same:
            run_len = i - run_start
            if run_len >= MIN_OPENER_RUN:
                ids = ", ".join(l.id for l in lectures[run_start:i])
                layout = lectures[run_start].slides[0].layout
                rep.warn(f"Opener layout '{layout}' repeats {run_len} lectures "
                         f"in a row ({ids}) — agenda-opener monotony.")
            run_start = i


def _check_story_continuity(lectures, bible: dict, rep: Report) -> None:
    """Simple literal match against story-bible.yaml's `numbers` list: a
    sentence that talks about the same fact (>=2 keywords from its `meaning`)
    and states some number, but not the canonical value, is a continuity bug
    or a false positive from loose phrasing — check by eye either way."""
    entries = []
    for n in (bible or {}).get("numbers", []) or []:
        value = str(n.get("value", "")).strip()
        meaning = str(n.get("meaning", "")).strip()
        kws = _story_keywords(meaning)
        if value and len(kws) >= 2:
            entries.append((_normalize_numbers(value), kws, meaning))
    if not entries:
        return

    for lec in lectures:
        for sent in _sentences(lec.narration):
            norm = _normalize_numbers(sent)
            if not _NUMERIC.search(norm):
                continue
            low = norm.lower()
            for value, kws, meaning in entries:
                # Require (nearly) the whole keyword set, not just any two. This
                # course teaches evaluation vocabulary all the way through, so
                # generic overlap ("same", "rubric", "pass rate") recurs in dozens
                # of unrelated sentences; only a near-paraphrase of one specific
                # bible entry's meaning is a real continuity-drift candidate.
                hits = sum(1 for k in kws if k in low)
                if hits < max(3, len(kws) - 1):
                    continue
                if value.lower() in low:
                    continue
                rep.warn(f"[{lec.id}] possible story continuity drift: matches "
                         f"'{meaning}' (bible value {value!r}) but reads "
                         f"{sent[:100]!r}")


def check_lectures(lectures, course: dict, rep: Report, story_bible: dict | None = None) -> None:
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

        _check_rhythm(lec, rep)
        _check_static_frames(lec, wpm, rep)
        _check_figure_floor(lec, wpm, rep)
        _check_bullets_share(lec, rep)
        _check_direct_address(lec, rep)
        _check_question_presence(lec, wpm, rep)

    _check_opener_diversity(lectures, rep)
    _check_story_continuity(lectures, story_bible, rep)

    lang = course.get("production", {}).get("spellcheck_lang", "en_US")
    bad = _spellcheck(slide_texts, lang)
    if bad:
        rep.fail(f"Possible slide typos [{lang}] (fix, or add to ALLOW in qc.py): "
                 f"{', '.join(sorted(bad)[:25])}")


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

def _load_story_bible(course_dir: Path) -> dict:
    path = course_dir / "story-bible.yaml"
    if not path.exists():
        return {}
    return yaml.safe_load(path.read_text(encoding="utf-8")) or {}


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--course", required=True)
    ap.add_argument("--out", default="build")
    ap.add_argument("--release", action="store_true",
                    help="also check built MP4s/SRTs against Udemy standards")
    args = ap.parse_args()

    course_dir = Path(args.course)
    course, lectures = load_course(course_dir)
    story_bible = _load_story_bible(course_dir)
    rep = Report()

    check_policy(course, rep)
    check_lectures(lectures, course, rep, story_bible)
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
