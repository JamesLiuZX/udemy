"""Parse a lecture source file into slides + narration.

One .md file is the single source of truth for a lecture: front-matter metadata,
slide content, and the narration that plays over each slide. Nothing is authored
twice, so a script edit and a slide edit are the same edit.

File shape
----------
    ---
    id: "0.3"
    title: The one idea
    ...front matter (YAML)...
    ---

    @slide statement
    kicker: The core idea
    ## AI features are **distributions**, not functions.
    lead: Which is why acceptance criteria have to change.

    @narrate
    Here is the sentence I want you to remember...

    @slide bullets
    ...

`@slide <layout>` opens a slide; `@narrate` opens the narration for the slide
above it. Narration runs until the next `@slide`.
"""

from __future__ import annotations

import re
from dataclasses import dataclass, field
from pathlib import Path

import yaml

# Layouts the theme knows how to style.
LAYOUTS = {
    "title", "statement", "bullets", "two-col", "table",
    "code", "math", "diagram", "quote", "section", "metrics", "callout",
    "sidenote", "definition", "example", "figure",
}

# Slide-level directives that are metadata rather than body content.
SLIDE_KEYS = {"kicker", "lead", "note", "attrib", "sec_num", "class", "figcap"}

_FRONT_MATTER = re.compile(r"^---\s*\n(.*?)\n---\s*\n", re.DOTALL)


@dataclass
class Slide:
    layout: str
    body: str = ""                      # raw markup, rendered later
    meta: dict = field(default_factory=dict)
    narration: str = ""

    @property
    def word_count(self) -> int:
        return len(self.narration.split())


@dataclass
class Lecture:
    path: Path
    meta: dict
    slides: list[Slide]

    # --- convenience accessors, with sane fallbacks -------------------------
    @property
    def id(self) -> str:
        return str(self.meta.get("id", self.path.stem))

    @property
    def title(self) -> str:
        return self.meta.get("title", self.path.stem)

    @property
    def voice(self) -> str:
        return self.meta.get("voice", "tts")

    @property
    def verified(self) -> bool:
        return bool(self.meta.get("verified", False))

    @property
    def narration(self) -> str:
        return "\n\n".join(s.narration.strip() for s in self.slides if s.narration.strip())

    @property
    def word_count(self) -> int:
        return len(self.narration.split())

    def estimated_seconds(self, wpm: int = 150) -> float:
        """Duration estimate from narration length. Real duration comes from the
        rendered audio; this is for planning and for flagging over-long lectures
        before you spend money on TTS."""
        return self.word_count / wpm * 60.0

    @property
    def slug(self) -> str:
        safe = re.sub(r"[^a-z0-9]+", "-", self.title.lower()).strip("-")
        return f"{self.id.replace('.', '-')}-{safe}"[:80]


def parse_lecture(path: str | Path) -> Lecture:
    path = Path(path)
    text = path.read_text(encoding="utf-8")

    m = _FRONT_MATTER.match(text)
    if not m:
        raise ValueError(f"{path}: missing YAML front matter (must start with '---')")
    meta = yaml.safe_load(m.group(1)) or {}
    body = text[m.end():]

    slides: list[Slide] = []
    current: Slide | None = None
    mode = "slide"             # or "narrate"
    buf: list[str] = []
    # Track fenced regions so an "@slide" inside a code sample is not a directive.
    in_fence = False

    def flush() -> None:
        if current is None:
            return
        chunk = "\n".join(buf).strip("\n")
        if mode == "slide":
            current.body = chunk
        else:
            # A second @narrate under the same slide used to silently
            # overwrite the first, which lost narration without any
            # warning anywhere. Concatenate instead.
            current.narration = (
                f"{current.narration}\n\n{chunk}" if current.narration else chunk
            )

    for raw in body.splitlines():
        stripped = raw.strip()

        if stripped.startswith("```"):
            in_fence = not in_fence

        if not in_fence and stripped.startswith("@slide"):
            flush()
            parts = stripped.split(None, 1)
            layout = parts[1].strip() if len(parts) > 1 else "bullets"
            if layout not in LAYOUTS:
                raise ValueError(
                    f"{path}: unknown slide layout {layout!r}. "
                    f"Known: {', '.join(sorted(LAYOUTS))}"
                )
            current = Slide(layout=layout)
            slides.append(current)
            mode, buf = "slide", []
            continue

        if not in_fence and stripped == "@narrate":
            flush()
            if current is None:
                raise ValueError(f"{path}: @narrate before any @slide")
            mode, buf = "narrate", []
            continue

        buf.append(raw)

    flush()

    # Lift `key: value` directive lines out of each slide body. Authors put these
    # wherever reads naturally (kicker above the heading, lead below it), so we
    # scan the whole body — but never inside a fence, where "note:" is content.
    for s in slides:
        kept: list[str] = []
        fenced = False
        for line in s.body.splitlines():
            t = line.strip()
            if t.startswith("```"):
                fenced = not fenced
            if not fenced:
                km = re.match(r"^([a-z_]+):\s*(.*)$", t)
                if km and km.group(1) in SLIDE_KEYS:
                    s.meta[km.group(1)] = km.group(2).strip()
                    continue
            kept.append(line)
        s.body = "\n".join(kept).strip("\n")

    if not slides:
        raise ValueError(f"{path}: no @slide blocks found")

    return Lecture(path=path, meta=meta, slides=slides)


def load_course(course_dir: str | Path) -> tuple[dict, list[Lecture]]:
    """Load course.yaml plus every lecture under lectures/, ordered by the
    curriculum in course.yaml (not by filename)."""
    course_dir = Path(course_dir)
    course = yaml.safe_load((course_dir / "course.yaml").read_text(encoding="utf-8"))

    by_id: dict[str, Lecture] = {}
    lec_dir = course_dir / "lectures"
    if lec_dir.exists():
        for f in sorted(lec_dir.glob("*.md")):
            lec = parse_lecture(f)
            by_id[lec.id] = lec

    ordered: list[Lecture] = []
    for section in course.get("sections", []):
        for entry in section.get("lectures", []):
            lec = by_id.get(str(entry["id"]))
            if lec:
                lec.meta.setdefault("section", section["id"])
                lec.meta.setdefault("section_title", section["title"])
                lec.meta.setdefault("duration_target", entry.get("duration"))
                ordered.append(lec)

    return course, ordered
