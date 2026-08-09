"""Narration + slide timings → .srt captions.

Captions matter twice over: accessibility, and watch-time on autoplay-muted
previews. Udemy accepts .srt per lecture.

Timing model
------------
Audio is synthesised per *slide*, which keeps prosody natural across sentence
boundaries. Within a slide, sentence start/end times are apportioned by character
count. That lands captions within roughly a word of true position — well inside
what reads correctly — without paying for per-sentence synthesis or a forced
aligner.
"""

from __future__ import annotations

import re
from dataclasses import dataclass

# Split on sentence enders, but don't break on common abbreviations or decimals.
_SPLIT = re.compile(r"(?<=[.!?])\s+(?=[A-Z0-9\"'])")
_ABBREV = re.compile(r"\b(e\.g|i\.e|vs|etc|Dr|Mr|Ms|Fig|No|approx)\.$", re.I)

MAX_CHARS_PER_CUE = 84          # ~2 lines at readable width
MAX_CUE_SECONDS = 6.0


@dataclass
class Cue:
    index: int
    start: float
    end: float
    text: str


def split_sentences(text: str) -> list[str]:
    rough = _SPLIT.split(" ".join(text.split()))
    out: list[str] = []
    for part in rough:
        if out and _ABBREV.search(out[-1]):       # re-join false break
            out[-1] = f"{out[-1]} {part}"
        else:
            out.append(part)
    return [s.strip() for s in out if s.strip()]


def _wrap(sentence: str) -> list[str]:
    """Break an over-long sentence into cue-sized chunks on word boundaries."""
    if len(sentence) <= MAX_CHARS_PER_CUE:
        return [sentence]
    words, chunks, cur = sentence.split(), [], ""
    for w in words:
        if cur and len(cur) + 1 + len(w) > MAX_CHARS_PER_CUE:
            chunks.append(cur)
            cur = w
        else:
            cur = f"{cur} {w}".strip()
    if cur:
        chunks.append(cur)
    return chunks


def cues_for_segments(segments: list[tuple[str, float, float]]) -> list[Cue]:
    """segments: (narration_text, start_seconds, end_seconds) per slide."""
    cues: list[Cue] = []
    n = 1
    for text, start, end in segments:
        text = " ".join(text.split())
        span = max(end - start, 0.001)
        if not text:
            continue

        pieces: list[str] = []
        for sentence in split_sentences(text):
            pieces.extend(_wrap(sentence))
        if not pieces:
            continue

        total = sum(len(p) for p in pieces) or 1
        t = start
        for piece in pieces:
            share = len(piece) / total
            dur = min(span * share, MAX_CUE_SECONDS)
            cues.append(Cue(n, t, min(t + dur, end), piece))
            t += span * share
            n += 1
    return cues


def _ts(seconds: float) -> str:
    if seconds < 0:
        seconds = 0.0
    ms = int(round(seconds * 1000))
    h, ms = divmod(ms, 3_600_000)
    m, ms = divmod(ms, 60_000)
    s, ms = divmod(ms, 1000)
    return f"{h:02d}:{m:02d}:{s:02d},{ms:03d}"


def to_srt(cues: list[Cue]) -> str:
    blocks = [
        f"{c.index}\n{_ts(c.start)} --> {_ts(c.end)}\n{c.text}\n"
        for c in cues
    ]
    return "\n".join(blocks)
