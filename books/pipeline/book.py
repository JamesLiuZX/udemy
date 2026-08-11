"""Manuscript model for the KDP book pipeline: parses book.yaml plus its
chapter Markdown files, and computes the two things LaTeX needs from Python
rather than from key-value class options: trim/margin geometry and a page
count estimate for pacing while writing.
"""

from __future__ import annotations

import re
from dataclasses import dataclass, field
from pathlib import Path

import yaml

REPO_ROOT = Path(__file__).resolve().parents[2]

# KDP paperback interior gutter (inside margin), banded by total page count.
# More pages means more spine curvature eating into the inside margin.
# (upper bound of band, gutter in inches), checked in ascending order.
GUTTER_BANDS = [
    (150, 0.375),
    (300, 0.5),
    (500, 0.625),
    (700, 0.75),
    (828, 0.875),
]

TRIM_PRESETS = {
    # slug: (width_in, height_in, words_per_page at kdp-book.cls defaults)
    "6x9": (6.0, 9.0, 320),
    "5.5x8.5": (5.5, 8.5, 280),
    "5x8": (5.0, 8.0, 240),
    "8.5x11": (8.5, 11.0, 480),
}

AUTHOR_INPUT_RE = re.compile(r"\[AUTHOR-INPUT:(.*?)\]", re.S)


def gutter_for_pages(pages: int) -> float:
    for upper, gutter in GUTTER_BANDS:
        if pages <= upper:
            return gutter
    return GUTTER_BANDS[-1][1]


@dataclass
class Chapter:
    id: str
    title: str
    path: Path
    text: str = ""

    @property
    def word_count(self) -> int:
        stripped = AUTHOR_INPUT_RE.sub(" ", self.text)
        stripped = re.sub(r"^#.*$", " ", stripped, flags=re.M)   # headings
        stripped = re.sub(r"[|>*_`#-]", " ", stripped)
        return len(stripped.split())

    def author_inputs(self) -> list[str]:
        return [m.group(1).strip() for m in AUTHOR_INPUT_RE.finditer(self.text)]


@dataclass
class Book:
    slug: str
    path: Path
    meta: dict
    chapters: list[Chapter] = field(default_factory=list)

    @property
    def title(self) -> str:
        return self.meta["title"]

    @property
    def dir(self) -> Path:
        return self.path.parent

    @property
    def trim(self) -> str:
        return self.meta.get("trim", "6x9")

    @property
    def lang(self) -> str:
        """'en' (default) or 'zh'. Drives the kdp-book.cls [zh] option and
        the back-matter chapter-title table in build.py; every other book
        in the repo omits this key and gets the unchanged English path."""
        return self.meta.get("lang", "en")

    @property
    def target_pages(self) -> tuple[int, int]:
        lo, hi = self.meta.get("target_pages", [300, 500])
        return (int(lo), int(hi))

    @property
    def verified(self) -> bool:
        return bool(self.meta.get("verified", False))

    @property
    def style(self) -> dict:
        return self.meta.get("style", {}) or {}

    @property
    def word_count(self) -> int:
        return sum(c.word_count for c in self.chapters)

    def estimated_pages(self) -> float:
        _, _, wpp = TRIM_PRESETS.get(self.trim, TRIM_PRESETS["6x9"])
        return self.word_count / wpp

    def margins(self, pages: int | None = None) -> dict:
        """Geometry for config.tex. `pages` should be the real rendered page
        count on a second pass; the target band midpoint is the best guess
        before a first render exists."""
        w, h, _ = TRIM_PRESETS.get(self.trim, TRIM_PRESETS["6x9"])
        if pages is None:
            lo, hi = self.target_pages
            pages = round((lo + hi) / 2)
        return {
            "width_in": w,
            "height_in": h,
            "gutter_in": gutter_for_pages(pages),
            "outer_in": 0.75,
            "top_in": 0.75,
            "bottom_in": 0.75,
            "band_pages": pages,
        }

    def author_input_markers(self) -> list[tuple[str, str]]:
        out = []
        for c in self.chapters:
            for note in c.author_inputs():
                out.append((c.id, note))
        return out


def parse_book(book_yaml_path: str | Path) -> Book:
    path = Path(book_yaml_path).resolve()
    meta = yaml.safe_load(path.read_text(encoding="utf-8"))
    book_dir = path.parent
    chapters = []
    for c in meta.get("chapters", []):
        cpath = book_dir / c["file"]
        text = cpath.read_text(encoding="utf-8") if cpath.exists() else ""
        chapters.append(Chapter(id=str(c["id"]), title=c["title"], path=cpath, text=text))
    return Book(slug=meta["slug"], path=path, meta=meta, chapters=chapters)


if __name__ == "__main__":
    import sys

    b = parse_book(sys.argv[1])
    lo, hi = b.target_pages
    print(f"{b.title!r}  {b.word_count} words  ~{b.estimated_pages():.0f}pp "
          f"(target {lo}-{hi})  trim={b.trim}  margins={b.margins()}")
    markers = b.author_input_markers()
    if markers:
        print(f"{len(markers)} unresolved [AUTHOR-INPUT] marker(s):")
        for cid, note in markers:
            print(f"  [{cid}] {note[:80]}")
