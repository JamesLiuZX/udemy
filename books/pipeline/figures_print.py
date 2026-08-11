#!/usr/bin/env python3
"""Print-profile figures for book interiors (docs/09-visual-standard.md §3).

    python3 books/pipeline/figures_print.py --book <slug>            # all specs
    python3 books/pipeline/figures_print.py --book <slug> --only x   # one spec

Reads every books/<slug>/figures/*.yaml spec and renders a grayscale,
B&W-print-safe PNG next to it, which the chapter Markdown then embeds with
an ordinary image reference:

    ![Caption for the figure.](books/<slug>/figures/<name>.png){width=100%}

The path is repo-root-relative on purpose: build.py compiles LaTeX with
cwd = repo root, and build_epub.py passes --resource-path so Pandoc's
EPUB writer resolves the identical path. One source file feeds both
outputs.

Same principle as the course side's pipeline/figures.py: charts are
generated from data, never drawn and never image-generated, so a figure
cannot ship with a mangled label or an invented number. Values that are a
pure function of a parameter (compounding curves, a crossover point) are
computed here rather than transcribed, so the figure cannot drift from
the arithmetic it illustrates.

Print constraints this module enforces by construction:
- Grayscale only. KDP prints standard paperback interiors in B&W; a hue
  would silently become an unchosen gray. Series separate by line weight,
  dash pattern, and direct labels, never by color alone.
- Direct labels over legends where possible (same rule as the slide
  figures: nothing a reader needs may hide in a lookup).
- Solid hairline grids, chart text in IBM Plex Sans (the fonts must be
  visible to fontconfig; rsvg-convert resolves them by family name).

Kinds:
- decay:     whole-chain success p^n for several per-step reliabilities
- crossover: a flat per-user revenue line against a cost line that scales
             with usage, with the break-even point computed and marked
"""

from __future__ import annotations

import argparse
import html
import shutil
import subprocess
import sys
from pathlib import Path

import yaml

sys.path.insert(0, str(Path(__file__).resolve().parent))
from book import REPO_ROOT  # noqa: E402

# Grayscale ink ramp (print-safe; no hues anywhere in this module)
INK = "#111111"
INK_MID = "#555555"
INK_SOFT = "#7A7A7A"
GRID = "#DDDDDD"
BG = "#FFFFFF"

# CJK fallback covers zh-edition figure specs; fontconfig resolves per glyph.
SANS = "IBM Plex Sans, Noto Sans CJK SC"
MONO = "IBM Plex Mono, Noto Sans Mono CJK SC"

# Canvas is designed at 300 px/inch for a 4.25 in text-block width, so the
# type sizes below print at roughly 8-10 pt when the figure is placed at
# full text width.
W = 1275


def _esc(s: str) -> str:
    return html.escape(str(s), quote=True)


def _txt(x: float, y: float, s: str, *, size: int = 34, fill: str = INK_MID,
         weight: int = 400, anchor: str = "start", family: str = SANS) -> str:
    return (f'<text x="{x:.1f}" y="{y:.1f}" font-family="{_esc(family)}" '
            f'font-size="{size}" font-weight="{weight}" fill="{fill}" '
            f'text-anchor="{anchor}">{_esc(s)}</text>')


def _open(h: int) -> str:
    return (f'<svg viewBox="0 0 {W} {h}" width="{W}" height="{h}" '
            f'xmlns="http://www.w3.org/2000/svg" role="img">'
            f'<rect width="{W}" height="{h}" fill="{BG}"/>')


# Series styling for B&W: weight + dash + marker, never color alone.
SERIES_STYLE = [
    {"stroke": INK, "width": 5.0, "dash": None},
    {"stroke": INK_MID, "width": 5.0, "dash": "14 10"},
    {"stroke": INK_SOFT, "width": 5.0, "dash": "3 9"},
]


def _frame(x0, y0, x1, y1, y_ticks, y_fmt, x_ticks, x_fmt, x_of, y_of):
    """Axes, solid hairline grid, tick labels. Returns list of SVG parts."""
    parts = []
    for v in y_ticks:
        yy = y_of(v)
        parts.append(f'<line x1="{x0}" y1="{yy:.1f}" x2="{x1}" y2="{yy:.1f}" '
                     f'stroke="{GRID}" stroke-width="1.5"/>')
        parts.append(_txt(x0 - 16, yy + 11, y_fmt(v), anchor="end", size=32))
    for v in x_ticks:
        xx = x_of(v)
        parts.append(_txt(xx, y1 + 46, x_fmt(v), anchor="middle", size=32))
    parts.append(f'<line x1="{x0}" y1="{y1}" x2="{x1}" y2="{y1}" '
                 f'stroke="{INK}" stroke-width="2.5"/>')
    return parts


def render_decay(spec: dict) -> str:
    probs = spec.get("probs", [0.90, 0.95, 0.99])
    max_steps = int(spec.get("steps", 10))
    h = int(spec.get("height", 860))
    x0, x1 = 130, W - 320
    y0, y1 = 60, h - 120

    def x_of(step: float) -> float:
        return x0 + (step - 1) / (max_steps - 1) * (x1 - x0)

    def y_of(v: float) -> float:
        return y1 - (v - 0.0) / 1.0 * (y1 - y0)

    parts = [_open(h)]
    parts += _frame(x0, y0, x1, y1,
                    [0.25, 0.50, 0.75, 1.00], lambda v: f"{v:.0%}",
                    list(range(1, max_steps + 1)), lambda v: str(int(v)),
                    x_of, y_of)
    parts.append(_txt((x0 + x1) / 2, h - 28, spec.get("x_label", "Steps in the chain"),
                      anchor="middle", size=34, fill=INK, weight=600))
    parts.append(_txt(x0 - 16, y0 - 24, spec.get("y_label", "Whole-task success rate"),
                      anchor="start", size=34, fill=INK, weight=600))

    for i, p in enumerate(probs):
        st = SERIES_STYLE[i % len(SERIES_STYLE)]
        pts = [(x_of(n), y_of(p ** n)) for n in range(1, max_steps + 1)]
        d = "M " + " L ".join(f"{x:.1f} {y:.1f}" for x, y in pts)
        dash = f' stroke-dasharray="{st["dash"]}"' if st["dash"] else ""
        parts.append(f'<path d="{d}" fill="none" stroke="{st["stroke"]}" '
                     f'stroke-width="{st["width"]}"{dash} stroke-linecap="round"/>')
        for n in (1, max_steps):
            x, y = x_of(n), y_of(p ** n)
            parts.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="7" fill="{st["stroke"]}"/>')
        end_v = p ** max_steps
        per_tpl = spec.get("per_step_label", "{p} per step")
        end_tpl = spec.get("ends_at_label", "ends at {v}")
        parts.append(_txt(x1 + 18, y_of(end_v) - 10,
                          per_tpl.format(p=f"{p:.0%}"),
                          size=30, fill=st["stroke"], weight=600))
        parts.append(_txt(x1 + 18, y_of(end_v) + 28,
                          end_tpl.format(v=f"{end_v:.0%}"),
                          size=30, fill=st["stroke"], weight=400))
    return "".join(parts) + "</svg>"


def render_crossover(spec: dict) -> str:
    cost = float(spec["cost_per_use"])
    revenue = float(spec["revenue"])
    x_max = int(spec.get("x_max", 160))
    unit = spec.get("unit", "conversations / month")
    h = int(spec.get("height", 860))
    x0, x1 = 130, W - 60
    y0, y1 = 60, h - 120
    y_max = max(cost * x_max, revenue) * 1.12

    def x_of(v: float) -> float:
        return x0 + v / x_max * (x1 - x0)

    def y_of(v: float) -> float:
        return y1 - v / y_max * (y1 - y0)

    y_step = spec.get("y_tick", 2)
    y_ticks = [t * y_step for t in range(1, int(y_max / y_step) + 1)]
    x_ticks = [t for t in range(0, x_max + 1, spec.get("x_tick", 40))]

    parts = [_open(h)]
    parts += _frame(x0, y0, x1, y1,
                    y_ticks, lambda v: f"${v:.0f}",
                    x_ticks, lambda v: str(int(v)),
                    x_of, y_of)
    parts.append(_txt((x0 + x1) / 2, h - 28, unit, anchor="middle",
                      size=34, fill=INK, weight=600))
    parts.append(_txt(x0 - 16, y0 - 24, spec.get("y_label", "Per user, per month"),
                      anchor="start", size=34, fill=INK, weight=600))

    # Flat revenue line (dashed mid-gray), rising cost line (solid ink)
    parts.append(f'<line x1="{x0}" y1="{y_of(revenue):.1f}" x2="{x1}" '
                 f'y2="{y_of(revenue):.1f}" stroke="{INK_MID}" stroke-width="5" '
                 f'stroke-dasharray="14 10"/>')
    parts.append(_txt(x0 + 14, y_of(revenue) - 16,
                      spec.get("revenue_label", f"Allocated revenue ${revenue:.2f}"),
                      size=32, fill=INK_MID, weight=600))
    parts.append(f'<line x1="{x_of(0):.1f}" y1="{y_of(0):.1f}" x2="{x_of(x_max):.1f}" '
                 f'y2="{y_of(cost * x_max):.1f}" stroke="{INK}" stroke-width="5"/>')
    # Label the cost line low on its run, well clear of the revenue line's
    # own label, rotated to sit along the slope's neighborhood.
    cost_lx = x_max * 0.52
    parts.append(_txt(x_of(cost_lx) + 16, y_of(cost * cost_lx) + 56,
                      spec.get("cost_label", "Model cost"),
                      size=32, fill=INK, weight=600, anchor="start"))

    # Break-even, computed rather than transcribed
    bx = revenue / cost
    parts.append(f'<line x1="{x_of(bx):.1f}" y1="{y_of(revenue):.1f}" '
                 f'x2="{x_of(bx):.1f}" y2="{y1}" stroke="{INK_SOFT}" '
                 f'stroke-width="2" stroke-dasharray="3 9"/>')
    parts.append(f'<circle cx="{x_of(bx):.1f}" cy="{y_of(revenue):.1f}" r="10" '
                 f'fill="{BG}" stroke="{INK}" stroke-width="4"/>')
    be_tpl = spec.get("breakeven_label", "break-even ≈ {n}")
    parts.append(_txt(x_of(bx) + 28, y_of(revenue) + 64,
                      be_tpl.format(n=f"{bx:.0f}"),
                      anchor="start", size=32, fill=INK, weight=600))

    for tier in spec.get("tiers", []):
        tx = float(tier["x"])
        ty = cost * tx
        parts.append(f'<circle cx="{x_of(tx):.1f}" cy="{y_of(ty):.1f}" r="8" '
                     f'fill="{INK}"/>')
        anchor = "end" if tx > x_max * 0.85 else "start"
        dx = -14 if anchor == "end" else 14
        parts.append(_txt(x_of(tx) + dx, y_of(ty) - 18,
                          f'{tier["label"]} (${ty:.2f})',
                          size=30, fill=INK, anchor=anchor))
    return "".join(parts) + "</svg>"


KINDS = {
    "decay": render_decay,
    "crossover": render_crossover,
}


def render_spec(spec_path: Path) -> Path:
    spec = yaml.safe_load(spec_path.read_text(encoding="utf-8"))
    kind = spec.get("kind")
    if kind not in KINDS:
        raise SystemExit(f"{spec_path}: unknown figure kind {kind!r} "
                         f"(have: {', '.join(sorted(KINDS))})")
    svg = KINDS[kind](spec)
    svg_path = spec_path.with_suffix(".svg")
    svg_path.write_text(svg, encoding="utf-8")

    png_path = spec_path.with_suffix(".png")
    exe = shutil.which("rsvg-convert")
    if not exe:
        raise SystemExit("rsvg-convert not found. Install it: "
                         "apt-get install librsvg2-bin")
    # 2x the design resolution: the canvas is already 300 px/in at text
    # width, so the PNG lands at ~600 dpi for line art. Grayscale is
    # guaranteed by the palette, not by a conversion step.
    subprocess.run([exe, "--zoom", "2", "-o", str(png_path), str(svg_path)],
                   check=True)
    return png_path


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--book", required=True, help="slug under books/")
    ap.add_argument("--only", help="render a single spec by stem name")
    args = ap.parse_args()

    fig_dir = REPO_ROOT / "books" / args.book / "figures"
    if not fig_dir.is_dir():
        raise SystemExit(f"No figures directory at {fig_dir}")
    specs = sorted(fig_dir.glob("*.yaml"))
    if args.only:
        specs = [s for s in specs if s.stem == args.only]
    if not specs:
        raise SystemExit(f"No figure specs found in {fig_dir}")
    for s in specs:
        png = render_spec(s)
        print(f"  {s.relative_to(REPO_ROOT)}  ->  {png.name}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
