#!/usr/bin/env python3
"""Build a widely-distributable EPUB3 ebook from a book's Markdown manuscript.

    python3 books/pipeline/build_epub.py --book <slug>

Sibling to build.py, not a variant of it: same book.yaml, same chapter
Markdown, same four bracket devices ([AUTHOR-INPUT], [PULLQUOTE],
[TAKEAWAYS], [KEY-INSIGHT]), but a completely different conversion path.
build.py goes Markdown -> LaTeX -> xelatex for the KDP print interior.
This goes Markdown -> HTML -> Pandoc's native EPUB3 writer, because EPUB
has no LaTeX involvement at all and Pandoc's HTML escaping rules for the
bracket markers are different (and much simpler) than its LaTeX escaping
rules. See the two regex blocks below and books/docs/01-production-
playbook.md if you're tempted to reuse build.py's LaTeX regexes here:
they will not match.

EPUB3, not MOBI: Amazon's KDP now accepts and converts EPUB directly, and
MOBI/AZW3 upload has been deprecated on their end. Producing MOBI as well
would need calibre's ebook-convert or kindlegen, neither installed in
this environment; EPUB3 alone covers KDP, Apple Books, Kobo, and Google
Play Books, which is what "widely distributable" means in practice.
"""

from __future__ import annotations

import argparse
import re
import shutil
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from book import REPO_ROOT, Book, parse_book  # noqa: E402

BOOKS_DIR = REPO_ROOT / "books"
THEME_DIR = BOOKS_DIR / "theme"
FONT_DIR = REPO_ROOT / "theme" / "vendor" / "fonts"

# Pandoc's HTML writer does not defensively escape a leading `[`, and does
# not rewrite `||` into anything, unlike its LaTeX writer (build.py's
# regexes account for both of those LaTeX-specific quirks; neither
# applies here). Every marker below is matched in the plain, unescaped
# form Pandoc actually emits for `-t html`, wrapped in the <p> tag Pandoc
# gives any standalone paragraph.
AUTHOR_INPUT_HTML_RE = re.compile(r"<p>\[AUTHOR-INPUT:(.*?)\]</p>", re.S)
PULLQUOTE_HTML_RE = re.compile(r"<p>\[PULLQUOTE:(.*?)\]</p>", re.S)
KEY_INSIGHT_HTML_RE = re.compile(r"<p>\[KEY-INSIGHT:(.*?)\|\|(.*?)\]</p>", re.S)
TAKEAWAYS_HTML_RE = re.compile(
    r"<p>\[TAKEAWAYS\]</p>\s*(<ul>.*?</ul>)\s*<p>\[/TAKEAWAYS\]</p>", re.S)


def html_escape(s: str) -> str:
    return (s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;"))


def convert_devices(html: str) -> str:
    # Pandoc's HTML reader round-trips a <div class="..."> faithfully (it
    # has a native Div AST node with attributes) but does NOT preserve a
    # class on a nested <p> (no such node in its AST), so a label styled
    # only via `.label { }` silently loses its styling on the way to
    # EPUB. <strong>/<em> survive the round-trip reliably instead, so the
    # label and source use those rather than depending on inner classes.
    html = AUTHOR_INPUT_HTML_RE.sub(
        lambda mo: (f'<div class="callout author-input">'
                    f'<p><strong>AUTHOR INPUT NEEDED</strong></p>'
                    f'<p>{mo.group(1).strip()}</p></div>'), html)
    html = PULLQUOTE_HTML_RE.sub(
        lambda mo: f'<div class="pullquote"><p>{mo.group(1).strip()}</p></div>', html)
    html = KEY_INSIGHT_HTML_RE.sub(
        lambda mo: (f'<div class="callout key-insight">'
                    f'<p><strong>KEY INSIGHT</strong></p>'
                    f'<p>{mo.group(1).strip()}</p>'
                    f'<p><em>{mo.group(2).strip()}</em></p></div>'), html)
    html = TAKEAWAYS_HTML_RE.sub(
        lambda mo: (f'<div class="callout takeaways">'
                    f'<p><strong>KEY TAKEAWAYS</strong></p>{mo.group(1)}</div>'), html)
    return html


def pandoc_chapter_html(md_path: Path) -> str:
    exe = shutil.which("pandoc")
    if not exe:
        raise SystemExit("pandoc not found. Install it: apt-get install pandoc")
    result = subprocess.run(
        [exe, str(md_path), "-f", "markdown+smart", "-t", "html"],
        capture_output=True, text=True,
    )
    if result.returncode != 0:
        raise SystemExit(f"pandoc failed on {md_path}:\n{result.stderr}")
    return convert_devices(result.stdout)


def front_matter_html(book: Book) -> str:
    # Deliberately does NOT emit its own <h1>Title</h1>: Pandoc's epub3
    # writer auto-generates a title page from the --metadata title/
    # subtitle/author flags (confirmed by direct test; it renders a
    # dedicated titlepage section with the right semantic classes), and
    # an extra hand-rolled title heading here would just duplicate it as
    # a second, differently-styled "chapter 1". Copyright and dedication
    # get their own <h1> each, which is what makes them their own
    # sections in the EPUB rather than getting swept into whatever
    # follows.
    meta = book.meta
    parts = []

    rights = meta.get("rights_note",
                       "All rights reserved. No part of this book may be reproduced, "
                       "distributed, or transmitted in any form without prior written "
                       "permission from the author, except brief quotations used in "
                       "critical reviews.")
    disclosure = meta.get("ai_disclosure_text",
                           "This book was written with AI assistance under the author's "
                           "direction, outline, and review. Statistics and case studies "
                           "are drawn from cited public sources; any claim of personal "
                           "experience is the author's own.")
    isbn = meta.get("isbn_note", "ISBN: [assigned at KDP publishing step]")
    year = meta.get("year", "2026")
    parts.append("<h1>Copyright</h1>")
    parts.append(
        f'<p>Copyright &#169; {year} {html_escape(meta.get("author", ""))}</p>'
        f'<p>{html_escape(rights)}</p>'
        f'<p>{html_escape(disclosure)}</p>'
        f'<p>{html_escape(isbn)}</p>'
    )
    if meta.get("dedication"):
        parts.append("<h1>Dedication</h1>")
        parts.append(f'<p style="text-align:center;font-style:italic;">'
                      f'{html_escape(meta["dedication"])}</p>')
    return "\n".join(parts)


def back_matter_html(book: Book) -> str:
    meta = book.meta
    out = []
    for item in meta.get("back_matter", []):
        src = book.dir / "back-matter" / f"{item}.md"
        if not src.exists():
            continue
        # Every back-matter file, like every chapter, opens with its own
        # `# Title` line, which pandoc_chapter_html() below already turns
        # into an <h1>. Emitting a second, hand-rolled <h1> here (as this
        # used to do) doubled the EPUB's nav/TOC and doubled the title
        # printed inside the chapter itself, since --epub-chapter-level=1
        # treats every <h1> as a new TOC entry.
        out.append(pandoc_chapter_html(src))
    return "\n".join(out)


def build_master_html(book: Book) -> str:
    parts = [front_matter_html(book)]
    for c in book.chapters:
        if not c.text.strip():
            continue
        # c.path's markdown already opens with its own `# Title` line
        # (verified against book.yaml's title for every chapter); pandoc
        # converts that into this section's <h1>. Do not add a second one
        # here, see the matching comment in back_matter_html().
        parts.append(pandoc_chapter_html(c.path))
    parts.append(back_matter_html(book))
    return "\n".join(parts)


def run_pandoc_epub(html: str, book: Book, out_path: Path) -> None:
    exe = shutil.which("pandoc")
    tmp_html = out_path.with_suffix(".src.html")
    tmp_html.write_text(
        f"<html><head><meta charset='utf-8'></head><body>\n{html}\n</body></html>",
        encoding="utf-8",
    )

    cmd = [
        exe, str(tmp_html), "-f", "html", "-t", "epub3",
        "--css", str(THEME_DIR / "epub.css"),
        "--epub-chapter-level=1",
        "--toc", "--toc-depth=1",
        "--metadata", f"title={book.title}",
        "--metadata", f"subtitle={book.meta.get('subtitle', '')}",
        "--metadata", f"author={book.meta.get('author', '')}",
        "--metadata", f"lang=en-{'GB' if book.style.get('spellcheck_lang') == 'en_GB' else 'US'}",
        "-o", str(out_path),
    ]
    for weight, path in [
        ("normal", "texgyreschola-regular.otf"),
        ("bold", "texgyreschola-bold.otf"),
        ("italic", "texgyreschola-italic.otf"),
        ("bold-italic", "texgyreschola-bolditalic.otf"),
    ]:
        font_path = FONT_DIR / path
        if font_path.exists():
            cmd.extend(["--epub-embed-font", str(font_path)])

    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        raise SystemExit(f"pandoc epub build failed:\n{result.stderr}")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--book", required=True, help="slug under books/, or a path to book.yaml")
    ap.add_argument("--out", default=str(REPO_ROOT / "build" / "books"))
    args = ap.parse_args()

    from build import resolve_book_yaml  # noqa: E402 (reuse, avoid duplicating path logic)
    book_yaml = resolve_book_yaml(args.book)
    book = parse_book(book_yaml)

    out_dir = Path(args.out) / book.slug
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / f"{book.slug}.epub"

    html = build_master_html(book)
    run_pandoc_epub(html, book, out_path)

    size_kb = out_path.stat().st_size / 1024
    print(f"\n  {book.title!r}  ->  {out_path.relative_to(REPO_ROOT)}  ({size_kb:.0f} KB)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
