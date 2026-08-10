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
import subprocess
import sys
from dataclasses import dataclass, field
from pathlib import Path

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
