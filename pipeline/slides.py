"""Slide → standalone HTML page (1920×1080), ready for screenshotting.

Each slide becomes its own HTML file with absolute file:// asset paths, so the
renderer needs no web server and no network. KaTeX and Mermaid are vendored under
theme/vendor and initialised synchronously on load.
"""

from __future__ import annotations

from pathlib import Path

from markup import render as render_markup

THEME_DIR = Path(__file__).resolve().parent.parent / "theme"

_PAGE = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>{title}</title>
<link rel="stylesheet" href="{theme}/deck.css">
<link rel="stylesheet" href="{theme}/vendor/katex/katex.min.css">
<script defer src="{theme}/vendor/katex/katex.min.js"></script>
<script defer src="{theme}/vendor/katex/auto-render.min.js"></script>
<script src="{theme}/vendor/mermaid/mermaid.min.js"></script>
</head>
<body>
<div class="slide layout-{layout} {extra}">
  {kicker}
  {sec_num}
  {body}
  {lead}
  {attrib}
  <div class="slide-foot">
    <span class="mark">{mark}</span>
    <span class="num">{num}</span>
  </div>
</div>
<script>
  // Mermaid: printed-diagram palette matching the deck tokens.
  if (window.mermaid) {{
    mermaid.initialize({{
      startOnLoad: true,
      theme: 'base',
      securityLevel: 'loose',
      fontFamily: 'Plex, system-ui, sans-serif',
      themeVariables: {{
        background: '#FFFFFF',
        primaryColor: '#F5F7F9',
        primaryTextColor: '#14181D',
        primaryBorderColor: '#1B4F8F',
        lineColor: '#788594',
        secondaryColor: '#E9F0F9',
        tertiaryColor: '#FFFFFF',
        fontSize: '22px',
        clusterBkg: '#F5F7F9',
        clusterBorder: '#DAE0E7'
      }}
    }});
  }}
  window.addEventListener('load', function () {{
    if (window.renderMathInElement) {{
      renderMathInElement(document.body, {{
        delimiters: [
          {{left: '\\\\[', right: '\\\\]', display: true}},
          {{left: '\\\\(', right: '\\\\)', display: false}}
        ],
        throwOnError: false
      }});
    }}
    document.documentElement.setAttribute('data-ready', '1');
  }});
</script>
</body>
</html>
"""


def slide_html(slide, *, index: int, total: int, mark: str, title: str = "",
               figure: str = "") -> str:
    meta = slide.meta
    body = render_markup(slide.body)

    # Numbered figure caption, so diagrams are referenceable the way a textbook's
    # are ("as we saw in Figure 5.2") rather than floating unlabelled.
    if meta.get("figcap"):
        label = f"<b>Figure {figure}</b>" if figure else ""
        body += f'<div class="figcap">{label}{meta["figcap"]}</div>'

    kicker = f'<div class="kicker">{meta["kicker"]}</div>' if meta.get("kicker") else ""
    lead = f'<p class="lead">{meta["lead"]}</p>' if meta.get("lead") else ""
    attrib = f'<div class="attrib">{meta["attrib"]}</div>' if meta.get("attrib") else ""
    sec_num = f'<div class="sec-num">{meta["sec_num"]}</div>' if meta.get("sec_num") else ""

    # Density guard: shrink type before content can overflow the 1080px frame.
    extra = meta.get("class", "")
    if _is_dense(slide):
        extra = (extra + " dense").strip()

    return _PAGE.format(
        title=title or f"slide {index}",
        theme=THEME_DIR.as_uri(),
        layout=slide.layout,
        extra=extra,
        kicker=kicker,
        sec_num=sec_num,
        body=body,
        lead=lead,
        attrib=attrib,
        mark=mark,
        num=f"{index:02d} / {total:02d}",
    )


def _is_dense(slide) -> bool:
    """Heuristic for 'this slide has too much on it to render at full size'.

    Also a content smell: if it trips often, the slide is doing too much and
    should be split. qc.py surfaces the count."""
    bullets = sum(1 for ln in slide.body.splitlines() if ln.strip().startswith(("-", "*")))
    chars = len(slide.body)
    return bullets >= 6 or chars > 620


def write_slides(lecture, out_dir: Path, mark: str) -> list[Path]:
    out_dir.mkdir(parents=True, exist_ok=True)
    paths: list[Path] = []
    total = len(lecture.slides)
    fig_n = 0
    for i, slide in enumerate(lecture.slides, start=1):
        figure = ""
        if slide.meta.get("figcap"):
            fig_n += 1
            figure = f"{lecture.id}.{fig_n}"
        p = out_dir / f"slide-{i:03d}.html"
        p.write_text(
            slide_html(slide, index=i, total=total, mark=mark,
                       title=lecture.title, figure=figure),
            encoding="utf-8",
        )
        paths.append(p)
    return paths
