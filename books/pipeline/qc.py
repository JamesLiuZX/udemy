#!/usr/bin/env python3
"""Quality gate for a KDP manuscript. Mirrors the video course's qc.py: same
two severities, same rule that a pass reporting only sign-off/author-input
gates is correct, not a bug.

    python3 books/pipeline/qc.py --book <slug>            # authoring checks
    python3 books/pipeline/qc.py --book <slug> --release  # + built PDF checks

  FAIL  — do not publish. Policy and structural problems.
  WARN  — fix before you'd call a chapter finished. Craft issues.
"""

from __future__ import annotations

import argparse
import re
import shutil
import subprocess
import sys
from dataclasses import dataclass, field
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from book import Book, gutter_for_pages, parse_book  # noqa: E402
from build import REPO_ROOT, pdf_page_count, resolve_book_yaml  # noqa: E402

# LLM tells, tuned for long-form self-help / non-fiction prose rather than
# spoken narration. Deliberately excludes common ordinary words.
FILLER = re.compile(
    r"\b(basically|obviously|simply put|as we all know|needless to say|"
    r"it goes without saying|delve|in today's fast-paced world|"
    r"unlock (?:your|the) (?:potential|power)|unleash your|game-?changer|"
    r"revolutioniz|it's important to note|in conclusion|tapestry|"
    r"testament to|navigate the complexities|in the realm of|"
    r"transform your life|at the end of the day)\w*\b", re.I)

# Words hunspell won't know but that are correct in this domain. Grows the
# same way the video side's does: add as real content triggers a false hit.
ALLOW = {
    "ai", "llm", "llms", "kdp", "isbn", "ebook", "audiobook", "chatgpt",
    "openai", "anthropic", "workflow", "workflows", "mindset", "self",
    "config", "yaml",
    # ai-employee: character names and real words hunspell's en_US list
    # doesn't carry. See the comment above: grows per real content hit.
    "priya", "priya's", "renata", "renata's", "another's", "automatable",
    "automaticity", "disqualifiers", "foodborne", "misclassifications",
    "onboarded", "onboarding", "overclaim", "overhyped", "pairing's",
    "salesy", "thrus", "underperform", "underuse", "unfile", "unretained",
    "whatever's", "ravi", "ravi's", "else's", "farrah", "triages", "malik",
    "teodora", "rebalancing", "priyanka", "overclaimed", "disqualifier",
    "reputational", "mistriaged", "pre", "stockout", "listicle's",
    "pushback", "whoever's", "strawman", "undertested", "renaldo",
    "misattributed", "reframing", "aditi", "yuki", "odalys", "dropdown",
    "zillow", "underpriced", "felix", "yusuf", "yusuf's",
    "malik's", "renaldo's", "soo",
    # ai-for-the-rest-of-us: character names and real words hunspell's
    # en_US list doesn't carry.
    "marisol", "marisol's", "diego", "diego's", "sofia", "sofia's",
    "pixma", "autocorrect", "chatbot", "chatbots", "grandkids", "olds",
    "reframe", "reframed", "roading", "résumé", "stovetop", "timeframe",
    "tradeoff", "walkability",
    # stop-guessing: real proper nouns (case parties, researchers, products)
    # and real domain words hunspell's en_US list doesn't carry. Verified by
    # hand against the manuscript, not typos.
    "arup", "buolamwini", "elon", "gebru", "gerstner", "nabla", "okafor",
    "recommender", "timnit", "zestimate", "zillow's", "asker's",
    "bootcamps", "data's", "eval", "evals", "ibuying", "leaderboard",
    "misclassifying", "mistranscribe", "offboarding", "overcorrect",
    "overcorrection", "oversized", "paroxetine", "rebooking", "klarna",
    "klarna's", "siemiatkowski", "moffatt", "mmlu", "ragas", "agentic",
    "yucheng", "chunyuan", "roadmap", "roadmaps", "robotaxis", "rollout",
    "rollouts", "todo", "unbuilt", "uncited", "unescaped", "untrusted",
    "watchlist", "watchlisted", "recoverably", "redesign's", "reframes",
    "relitigating", "requester's", "rebranded",
}

AUTHOR_INPUT_RE = re.compile(r"\[AUTHOR-INPUT:(.*?)\]", re.S)
KEY_INSIGHT_RE = re.compile(r"\[KEY-INSIGHT:(.*?)\]", re.S)
KEY_INSIGHT_WELLFORMED_RE = re.compile(r"\[KEY-INSIGHT:.*?\|\|.*?\]", re.S)


@dataclass
class Report:
    fails: list[str] = field(default_factory=list)
    warns: list[str] = field(default_factory=list)

    def fail(self, msg: str) -> None:
        self.fails.append(msg)

    def warn(self, msg: str) -> None:
        self.warns.append(msg)


def _spellcheck(texts: list[str], lang: str) -> set[str]:
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
        if w[:1].isupper() and any(c.isupper() for c in w[1:]):
            continue
        bad.add(w)
    return bad


def check_manuscript(book: Book, rep: Report) -> None:
    if not book.verified:
        rep.fail(f"[{book.slug}] verified: false — the author has not signed off "
                 f"this manuscript. Read it end to end and set verified: true once "
                 f"every claim and every anecdote is one you can personally defend.")

    markers = book.author_input_markers()
    if markers:
        rep.fail(f"[{book.slug}] {len(markers)} unresolved [AUTHOR-INPUT] marker(s) "
                 f"across the manuscript. These are the moments the book depends on "
                 f"the real author for; never fill them in on their behalf.")
        for cid, note in markers[:10]:
            rep.fail(f"  [{cid}] {note[:90]}")

    if not book.chapters:
        rep.fail(f"[{book.slug}] no chapters found in book.yaml.")
        return

    lo, hi = book.target_pages
    est = book.estimated_pages()
    if est < lo * 0.5:
        rep.warn(f"[{book.slug}] ~{est:.0f}pp estimated against a {lo}-{hi}pp "
                 f"target — early days, or a placeholder manuscript.")

    dash_style = book.style.get("em_dash", "allow")
    all_texts: list[str] = []
    for c in book.chapters:
        tag = f"[{book.slug}/{c.id}]"
        if not c.text.strip():
            rep.warn(f"{tag} chapter file is empty: {c.path}")
            continue

        clean_for_check = AUTHOR_INPUT_RE.sub(" ", c.text)
        # Image references: the caption is prose worth spellchecking, the
        # target path/attributes are not ("png", a slug, "width=100%").
        clean_for_check = re.sub(r"!\[([^\]]*)\]\([^)]*\)(\{[^}]*\})?",
                                 r"\1", clean_for_check)

        insights = KEY_INSIGHT_RE.findall(c.text)
        wellformed = len(KEY_INSIGHT_WELLFORMED_RE.findall(c.text))
        if len(insights) != wellformed:
            rep.fail(f"{tag} {len(insights) - wellformed} [KEY-INSIGHT: ...] marker(s) "
                     f"missing the '||' claim/source separator — these will render as "
                     f"raw bracket text instead of a box. Format is "
                     f"[KEY-INSIGHT: claim || source].")
        clean_for_check = KEY_INSIGHT_RE.sub(" ", clean_for_check)
        all_texts.append(clean_for_check)

        fill = FILLER.findall(clean_for_check)
        if fill:
            rep.warn(f"{tag} filler/LLM-tell phrases: "
                     f"{', '.join(sorted({f.lower() for f in fill}))}")

        if dash_style == "avoid":
            dashes = clean_for_check.count("—")
            if dashes:
                rep.fail(f"{tag} contains {dashes} em dash(es); "
                         f"book.yaml style.em_dash is 'avoid'.")

        if not re.search(r"\S", c.text.split("\n", 1)[0] if "\n" in c.text else c.text):
            rep.warn(f"{tag} doesn't open with a heading — check the chapter title "
                     f"renders correctly.")

    # Hunspell tokenizes on whitespace; CJK text has none, so running an
    # en_US/en_GB dictionary against a zh manuscript would either see one
    # giant unspellable "word" per line or nothing at all, not real typos.
    # A translated edition's own language is proofread by the human
    # translation pass, not this ASCII spellchecker.
    if book.meta.get("lang") != "zh":
        lang = book.style.get("spellcheck_lang", "en_US")
        bad = _spellcheck(all_texts, lang)
        if bad:
            rep.fail(f"[{book.slug}] possible typos [{lang}] (fix, or add to ALLOW in "
                     f"books/pipeline/qc.py): {', '.join(sorted(bad)[:25])}")


def check_release(book: Book, out_dir: Path, rep: Report) -> None:
    pdf = out_dir / "master.pdf"
    if not pdf.exists():
        rep.fail(f"[{book.slug}] no built PDF at {pdf}. Run build.py before --release.")
        return

    pages = pdf_page_count(pdf)
    lo, hi = book.target_pages
    if pages < 0:
        rep.warn(f"[{book.slug}] couldn't read page count (pdfinfo missing?).")
    elif not (lo <= pages <= hi):
        rep.fail(f"[{book.slug}] {pages} pages, outside the {lo}-{hi} target band.")
    else:
        print(f"\n  [{book.slug}] {pages} pages, within {lo}-{hi} target.")

    config = out_dir / "config.tex"
    if pages > 0 and config.exists():
        m = re.search(r"\\def\\BookGutter\{([\d.]+)in\}", config.read_text())
        used = float(m.group(1)) if m else None
        correct = gutter_for_pages(pages)
        if used is not None and abs(used - correct) > 1e-9:
            rep.fail(f"[{book.slug}] gutter margin is {used}in, but {pages} actual "
                     f"pages call for {correct}in. Rebuild so config.tex regenerates "
                     f"against the real page count.")

    exe = shutil.which("pdffonts")
    if exe:
        out = subprocess.run([exe, str(pdf)], capture_output=True, text=True).stdout
        for line in out.splitlines()[2:]:
            parts = line.split()
            if len(parts) >= 4 and parts[-3].lower() == "no":
                rep.fail(f"[{book.slug}] font not embedded: {line.strip()} — "
                         f"KDP requires every font embedded in the interior PDF.")

    markers = book.author_input_markers()
    if markers:
        rep.fail(f"[{book.slug}] {len(markers)} [AUTHOR-INPUT] marker(s) still "
                 f"unresolved. Not release-ready.")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--book", required=True)
    ap.add_argument("--out", default=str(REPO_ROOT / "build" / "books"))
    ap.add_argument("--release", action="store_true",
                    help="also check the built PDF against KDP structural requirements")
    args = ap.parse_args()

    book_yaml = resolve_book_yaml(args.book)
    book = parse_book(book_yaml)
    rep = Report()

    check_manuscript(book, rep)
    if args.release:
        check_release(book, Path(args.out) / book.slug, rep)

    print()
    for w in rep.warns:
        print(f"  WARN  {w}")
    for f in rep.fails:
        print(f"  FAIL  {f}")

    print(f"\n  {len(rep.fails)} fail · {len(rep.warns)} warn")
    if rep.fails:
        print("  NOT ready to publish.\n")
        return 1
    print("  Passes the gate.\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
