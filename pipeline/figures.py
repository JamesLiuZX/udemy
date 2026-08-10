"""Deterministic SVG figures for slides.

Charts are generated from data, not drawn and not produced by an image model, so
a figure cannot come out with mangled labels or invented numbers. Everything is
inline SVG using the deck's own tokens.

Palette note
------------
The two-series pair is blue #2E6DB4 / orange #C1741A. The deck's semantic green
and red were the obvious first choice and were rejected: validated against the
dataviz checks they fail CVD separation (deutan ΔE 7.1, inside the 6–8 floor)
and the green drops under the chroma floor. Blue/orange passes every check
(protan ΔE 23.5, tritan 25.4, normal 28.1).

These figures are rendered into video frames, so there is no hover layer to fall
back on: every value a learner needs is directly labelled or readable from the
axis.
"""

from __future__ import annotations

import html
from dataclasses import dataclass

# Deck tokens
INK = "#14181D"
INK_SOFT = "#45505E"
INK_FAINT = "#788594"
RULE = "#DAE0E7"
SURFACE = "#FFFFFF"
PANEL = "#F5F7F9"

# Validated categorical pair (see module docstring)
S1 = "#2E6DB4"      # slot 1
S2 = "#C1741A"      # slot 2
S1_TINT = "#D8E5F4"
MUTED = "#C3CCD6"   # de-emphasised marks

SANS = "Plex, system-ui, sans-serif"     # never the display serif, per marks spec

W = 1656            # slide content width


def _esc(s: str) -> str:
    return html.escape(str(s), quote=True)


def _txt(x, y, s, *, size=24, fill=INK_SOFT, weight=400, anchor="start",
         tnum=False) -> str:
    extra = ' font-variant-numeric="tabular-nums"' if tnum else ""
    return (f'<text x="{x:.1f}" y="{y:.1f}" font-family="{SANS}" '
            f'font-size="{size}" font-weight="{weight}" fill="{fill}" '
            f'text-anchor="{anchor}"{extra}>{_esc(s)}</text>')


def _open(h: int) -> str:
    return (f'<svg viewBox="0 0 {W} {h}" width="100%" height="{h}" '
            f'xmlns="http://www.w3.org/2000/svg" role="img">')


# ---------------------------------------------------------------------------
# dot plot — identity of individual judgements, and the spread between them
# ---------------------------------------------------------------------------

@dataclass
class Series:
    label: str
    values: list[float]
    note: str = ""


def dotplot(series: list[Series], *, lo: int = 1, hi: int = 5,
            axis_label: str = "", height: int | None = None,
            tick_step: int = 1) -> str:
    """One row per series, dots stacked where values repeat.

    The teaching point is the *width* of each row, so each row carries a spread
    bracket and its range is stated in words. Colour is secondary: rows are
    directly labelled, so the figure survives greyscale and CVD entirely.

    `tick_step` controls gridline spacing: the default of 1 suits a 1-5
    rubric scale, but a wide range (e.g. 0-100 for a percentage) needs a
    coarser step or the hairline grid draws a tick per integer and the axis
    turns into an unreadable smear."""
    pad_l, pad_r = 300, 90
    top = 40
    r = 15                                    # ≥ 8px marks
    step = 2 * r + 6                          # stack pitch, keeps a 6px gap
    below = 118                               # bracket + its caption
    axis_gap = 40

    plot_w = W - pad_l - pad_r
    span = max(hi - lo, 1)

    def x_of(v: float) -> float:
        return pad_l + (v - lo) / span * plot_w

    # Rows are laid out from measured content, not a fixed pitch: repeated values
    # stack upward, so a row with four dots on one value is much taller than a
    # row with none. A fixed row height puts one row's dots through the row
    # above's spread bracket.
    layout: list[tuple[Series, float]] = []
    cursor = top
    for s in series:
        freq: dict[float, int] = {}
        for v in s.values:
            freq[v] = freq.get(v, 0) + 1
        stack = (max(freq.values(), default=1) - 1) * step
        cy = cursor + stack + r
        layout.append((s, cy))
        cursor = cy + below

    axis_y = cursor + axis_gap
    h = height or int(axis_y + (58 if axis_label else 28))

    out = [_open(h)]

    # Recessive solid hairline grid, one per tick. Never dashed.
    for t in range(lo, hi + 1, tick_step):
        x = x_of(t)
        out.append(f'<line x1="{x:.1f}" y1="{top - 16}" x2="{x:.1f}" '
                   f'y2="{axis_y - 32}" stroke="{RULE}" stroke-width="1"/>')
        out.append(_txt(x, axis_y, t, size=23, fill=INK_FAINT,
                        anchor="middle", tnum=True))

    if axis_label:
        out.append(_txt(W - pad_r, axis_y + 42, axis_label, size=22,
                        fill=INK_FAINT, anchor="end"))

    for i, (s, cy) in enumerate(layout):
        colour = (S1, S2)[i % 2]

        out.append(_txt(pad_l - 44, cy + 6, s.label, size=27, fill=INK,
                        weight=600, anchor="end"))
        if s.note:
            out.append(_txt(pad_l - 44, cy + 42, s.note, size=22,
                            fill=INK_FAINT, anchor="end"))

        # spread bracket: the actual subject of the figure
        if s.values:
            x0, x1 = x_of(min(s.values)), x_of(max(s.values))
            by = cy + 56
            out.append(f'<line x1="{x0:.1f}" y1="{by}" x2="{x1:.1f}" y2="{by}" '
                       f'stroke="{colour}" stroke-width="2"/>')
            for xe in (x0, x1):
                out.append(f'<line x1="{xe:.1f}" y1="{by - 9}" x2="{xe:.1f}" '
                           f'y2="{by + 9}" stroke="{colour}" stroke-width="2"/>')
            rng = max(s.values) - min(s.values)
            word = "no spread" if rng == 0 else f"spread of {rng:g}"
            out.append(_txt((x0 + x1) / 2, by + 36, word, size=22,
                            fill=INK_FAINT, anchor="middle"))

        # stack repeats upward, 2px surface ring so overlaps stay separable
        seen: dict[float, int] = {}
        for v in sorted(s.values):
            k = seen.get(v, 0)
            seen[v] = k + 1
            out.append(f'<circle cx="{x_of(v):.1f}" cy="{cy - k * step:.1f}" '
                       f'r="{r}" fill="{colour}" stroke="{SURFACE}" '
                       f'stroke-width="2"/>')

    out.append("</svg>")
    return "".join(out)


# ---------------------------------------------------------------------------
# histogram with an acceptance threshold
# ---------------------------------------------------------------------------

def histogram(bins: list[tuple[str, float]], *, threshold: int | None = None,
              threshold_label: str = "", note: str = "",
              height: int = 470) -> str:
    """Magnitude across ordered bins, with everything at or above `threshold`
    (a 1-based bin index) emphasised and the rest held back in grey.

    Emphasis rather than a hue per bin: the story is one boundary, not eight
    identities."""
    pad_l, pad_r = 96, 90
    # threshold_label sits above the bars, at the top of the SVG. Without
    # extra headroom its ascenders clip against the viewBox edge (y=0).
    has_label = threshold is not None and threshold_label
    pad_t = 60 if has_label else 34
    base = height - 92
    plot_w = W - pad_l - pad_r
    n = max(len(bins), 1)
    slot = plot_w / n
    bw = slot - 22                              # gap between bars, not borders

    top_v = max([v for _, v in bins] + [1])
    out = [_open(height)]

    # baseline only; no dashed rules anywhere
    out.append(f'<line x1="{pad_l}" y1="{base}" x2="{W - pad_r}" y2="{base}" '
               f'stroke="{RULE}" stroke-width="1"/>')

    for i, (label, v) in enumerate(bins):
        x = pad_l + i * slot + 11
        bh = (v / top_v) * (base - pad_t)
        passing = threshold is not None and (i + 1) >= threshold
        fill = S1 if passing else MUTED
        out.append(f'<rect x="{x:.1f}" y="{base - bh:.1f}" width="{bw:.1f}" '
                   f'height="{bh:.1f}" rx="4" fill="{fill}"/>')
        out.append(_txt(x + bw / 2, base + 36, label, size=23, fill=INK_FAINT,
                        anchor="middle"))

    if threshold is not None:
        xt = pad_l + (threshold - 1) * slot
        line_top = 8 if has_label else pad_t - 16
        out.append(f'<line x1="{xt:.1f}" y1="{line_top}" x2="{xt:.1f}" '
                   f'y2="{base + 8}" stroke="{INK}" stroke-width="2"/>')
        if threshold_label:
            out.append(_txt(xt + 16, pad_t - 20, threshold_label, size=24,
                            fill=INK, weight=600))

    if note:
        out.append(_txt(pad_l, height - 20, note, size=22, fill=INK_FAINT))

    out.append("</svg>")
    return "".join(out)


# ---------------------------------------------------------------------------
# sampling schematic — the course's central image
# ---------------------------------------------------------------------------

def sampling(height: int = 430) -> str:
    """Function beside distribution: one input, one output versus one input and
    a spread of outputs. Schematic rather than plotted, because the point is the
    shape of the behaviour, not any particular numbers."""
    mid = W / 2
    out = [_open(height)]
    cy = 232

    def panel(x0: float, title: str, sub: str, colour: str) -> list[str]:
        p = [_txt(x0, 44, title, size=30, fill=INK, weight=600),
             _txt(x0, 82, sub, size=23, fill=INK_FAINT)]
        # input token
        p.append(f'<rect x="{x0}" y="{cy - 42}" width="188" height="84" rx="5" '
                 f'fill="{PANEL}" stroke="{RULE}" stroke-width="1"/>')
        p.append(_txt(x0 + 94, cy + 8, "Same input", size=25, fill=INK_SOFT,
                      anchor="middle"))
        # arrow
        ax0, ax1 = x0 + 206, x0 + 322
        p.append(f'<line x1="{ax0}" y1="{cy}" x2="{ax1 - 14}" y2="{cy}" '
                 f'stroke="{INK_FAINT}" stroke-width="2"/>')
        p.append(f'<path d="M{ax1 - 14} {cy - 8} L{ax1} {cy} L{ax1 - 14} '
                 f'{cy + 8} Z" fill="{INK_FAINT}"/>')
        return p

    # left: a function
    out += panel(96, "A function", "What you have shipped your whole career", S1)
    out.append(f'<circle cx="{96 + 392}" cy="{cy}" r="17" fill="{S1}" '
               f'stroke="{SURFACE}" stroke-width="2"/>')
    out.append(_txt(96 + 392, cy + 62, "One output", size=25, fill=INK,
                    weight=600, anchor="middle"))
    out.append(_txt(96 + 392, cy + 96, "Every single time", size=22,
                    fill=INK_FAINT, anchor="middle"))

    # divider
    out.append(f'<line x1="{mid + 6}" y1="24" x2="{mid + 6}" y2="{height - 30}" '
               f'stroke="{RULE}" stroke-width="1"/>')

    # right: a distribution
    rx = mid + 108
    out += panel(rx, "A distribution", "What an AI feature actually is", S2)
    # scattered draws, deterministic offsets so the render never changes
    draws = [(-96, -8), (-52, 34), (-40, -46), (4, 6), (18, -62), (30, 52),
             (62, -22), (74, 30), (104, -4), (116, -54)]
    ox = rx + 392
    for dx, dy in draws:
        out.append(f'<circle cx="{ox + dx * 0.82:.1f}" cy="{cy + dy * 0.82:.1f}" '
                   f'r="14" fill="{S2}" fill-opacity="0.85" stroke="{SURFACE}" '
                   f'stroke-width="2"/>')
    out.append(_txt(ox, cy + 122, "A range of outputs", size=25, fill=INK,
                    weight=600, anchor="middle"))
    out.append(_txt(ox, cy + 156, "You are seeing one draw", size=22,
                    fill=INK_FAINT, anchor="middle"))

    out.append("</svg>")
    return "".join(out)


# ---------------------------------------------------------------------------
# spec dispatch (used by the ```figure markup block)
# ---------------------------------------------------------------------------

def render(spec: dict) -> str:
    kind = str(spec.get("kind", "")).strip()

    if kind == "dotplot":
        series = [
            Series(label=s.get("label", ""), values=list(s.get("values", [])),
                   note=s.get("note", ""))
            for s in spec.get("series", [])
        ]
        return dotplot(series, lo=int(spec.get("lo", 1)),
                       hi=int(spec.get("hi", 5)),
                       axis_label=spec.get("axis_label", ""),
                       tick_step=int(spec.get("tick_step", 1)))

    if kind == "histogram":
        bins = [(b.get("label", ""), float(b.get("value", 0)))
                for b in spec.get("bins", [])]
        t = spec.get("threshold")
        return histogram(bins, threshold=int(t) if t is not None else None,
                         threshold_label=spec.get("threshold_label", ""),
                         note=spec.get("note", ""))

    if kind == "sampling":
        return sampling()

    raise ValueError(
        f"unknown figure kind {kind!r}. Known: dotplot, histogram, sampling")
