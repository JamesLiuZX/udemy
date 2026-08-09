"""Slide markup → HTML.

A deliberately small markdown dialect. It covers exactly the constructs the deck
theme styles, and nothing else — which means every slide is guaranteed to land on
a designed layout instead of degrading into unstyled text.

Blocks
------
    # / ## / ###        headings
    - item              bullet list
    1. item             numbered list (renders as .steps)
    | a | b |           table
    ```lang … ```       code block (```mermaid → diagram)
    $$ … $$             display math (KaTeX)
    ::: cols … :::      two-column container
    :: card good        card inside a cols container (good | bad | plain)
    ::: callout … :::   amber "watch out" block
    ::: metrics … :::   big-number slabs:  - VALUE :: caption :: tone

Inline
------
    **bold**   *accent*   `code`   ==highlight==   $math$
"""

from __future__ import annotations

import html
import re

_TONES = {"good", "bad", "warn"}


# --------------------------------------------------------------------------
# inline
# --------------------------------------------------------------------------

def _inline(text: str) -> str:
    """Escape first, then re-introduce the handful of spans we allow. Math is
    pulled out ahead of escaping so TeX backslashes survive intact."""
    math: list[str] = []

    def stash(m: re.Match) -> str:
        math.append(m.group(1))
        return f"\x00M{len(math) - 1}\x00"

    text = re.sub(r"\$([^$\n]+)\$", stash, text)
    out = html.escape(text, quote=False)

    out = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", out)
    out = re.sub(r"(?<!\*)\*([^*\n]+)\*(?!\*)", r"<em>\1</em>", out)
    out = re.sub(r"==(.+?)==", r'<span class="hl">\1</span>', out)
    out = re.sub(r"`([^`\n]+)`", r"<code>\1</code>", out)

    for i, tex in enumerate(math):
        out = out.replace(f"\x00M{i}\x00", f"\\({html.escape(tex, quote=False)}\\)")
    return out


# --------------------------------------------------------------------------
# code highlighting — token-level, enough to read well on a slide
# --------------------------------------------------------------------------

_KEYWORDS = (
    r"\b(def|class|return|import|from|for|while|if|elif|else|in|not|and|or|None|"
    r"True|False|with|as|lambda|yield|try|except|raise|async|await|const|let|var|"
    r"function|export|SELECT|FROM|WHERE|GROUP BY|ORDER BY|JOIN|ON|AS)\b"
)


def _highlight(code: str) -> str:
    out = html.escape(code, quote=False)
    holes: list[str] = []

    def hole(tag: str, body: str) -> str:
        holes.append(f'<span class="{tag}">{body}</span>')
        return f"\x00H{len(holes) - 1}\x00"

    # order matters: comments and strings win over keywords inside them
    out = re.sub(r"(#[^\n]*)", lambda m: hole("c", m.group(1)), out)
    out = re.sub(r"(&quot;[^\n]*?&quot;|&#x27;[^\n]*?&#x27;)",
                 lambda m: hole("s", m.group(1)), out)
    out = re.sub(_KEYWORDS, lambda m: hole("k", m.group(1)), out)
    out = re.sub(r"\b(\d+\.?\d*)\b", lambda m: hole("n", m.group(1)), out)
    out = re.sub(r"\b([a-zA-Z_]\w*)(?=\()", lambda m: hole("f", m.group(1)), out)

    for i, span in enumerate(holes):
        out = out.replace(f"\x00H{i}\x00", span)
    return out


# --------------------------------------------------------------------------
# block parsing
# --------------------------------------------------------------------------

def render(markup: str) -> str:
    lines = markup.splitlines()
    return _render_lines(lines)


def _render_lines(lines: list[str]) -> str:
    out: list[str] = []
    i = 0
    n = len(lines)

    while i < n:
        line = lines[i]
        s = line.strip()

        if not s:
            i += 1
            continue

        # ---- container fence :::
        if s.startswith(":::"):
            kind = s[3:].strip() or "cols"
            depth, j = 1, i + 1
            block: list[str] = []
            while j < n:
                t = lines[j].strip()
                if t.startswith(":::"):
                    if t == ":::":
                        depth -= 1
                        if depth == 0:
                            break
                    else:
                        depth += 1
                block.append(lines[j])
                j += 1
            out.append(_container(kind, block))
            i = j + 1
            continue

        # ---- fenced code / mermaid
        if s.startswith("```"):
            lang = s[3:].strip()
            j = i + 1
            body: list[str] = []
            while j < n and not lines[j].strip().startswith("```"):
                body.append(lines[j])
                j += 1
            code = "\n".join(body)
            if lang == "mermaid":
                out.append(f'<div class="diagram"><pre class="mermaid">'
                           f'{html.escape(code, quote=False)}</pre></div>')
            else:
                out.append(f"<pre><code>{_highlight(code)}</code></pre>")
            i = j + 1
            continue

        # ---- display math
        if s.startswith("$$"):
            j = i
            body: list[str] = []
            if s == "$$":
                j = i + 1
                while j < n and lines[j].strip() != "$$":
                    body.append(lines[j])
                    j += 1
            else:                                   # single-line  $$ x = y $$
                body.append(s.strip("$"))
            tex = "\n".join(body).strip()
            out.append(f'<div class="math-block">\\[{html.escape(tex, quote=False)}\\]</div>')
            i = j + 1
            continue

        # ---- table
        if s.startswith("|"):
            j = i
            rows: list[str] = []
            while j < n and lines[j].strip().startswith("|"):
                rows.append(lines[j].strip())
                j += 1
            out.append(_table(rows))
            i = j
            continue

        # ---- headings
        hm = re.match(r"^(#{1,3})\s+(.*)$", s)
        if hm:
            lvl = len(hm.group(1))
            out.append(f"<h{lvl}>{_inline(hm.group(2))}</h{lvl}>")
            i += 1
            continue

        # ---- lists
        if re.match(r"^[-*]\s+", s):
            j, items = i, []
            while j < n and re.match(r"^[-*]\s+", lines[j].strip()):
                items.append(re.sub(r"^[-*]\s+", "", lines[j].strip()))
                j += 1
            body = "".join(f"<li>{_inline(x)}</li>" for x in items)
            out.append(f"<ul>{body}</ul>")
            i = j
            continue

        if re.match(r"^\d+\.\s+", s):
            j, items = i, []
            while j < n and re.match(r"^\d+\.\s+", lines[j].strip()):
                items.append(re.sub(r"^\d+\.\s+", "", lines[j].strip()))
                j += 1
            body = "".join(f"<li>{_inline(x)}</li>" for x in items)
            out.append(f'<ol class="steps">{body}</ol>')
            i = j
            continue

        # ---- blockquote
        if s.startswith(">"):
            j, parts = i, []
            while j < n and lines[j].strip().startswith(">"):
                parts.append(lines[j].strip().lstrip("> ").strip())
                j += 1
            out.append(f"<blockquote>{_inline(' '.join(parts))}</blockquote>")
            i = j
            continue

        # ---- paragraph
        out.append(f"<p>{_inline(s)}</p>")
        i += 1

    return "\n".join(out)


def _table(rows: list[str]) -> str:
    def cells(r: str) -> list[str]:
        return [c.strip() for c in r.strip().strip("|").split("|")]

    if not rows:
        return ""
    head = cells(rows[0])
    body = [r for r in rows[1:] if not re.match(r"^[\s|:-]+$", r)]

    thead = "".join(f"<th>{_inline(c)}</th>" for c in head)
    tbody = "".join(
        "<tr>" + "".join(f"<td>{_inline(c)}</td>" for c in cells(r)) + "</tr>"
        for r in body
    )
    return f"<table><thead><tr>{thead}</tr></thead><tbody>{tbody}</tbody></table>"


def _container(kind: str, block: list[str]) -> str:
    parts = kind.split()
    name = parts[0]

    if name == "callout":
        label = " ".join(parts[1:]) or "Watch out"
        return (f'<div class="callout"><div class="label">{html.escape(label)}</div>'
                f"{_render_lines(block)}</div>")

    if name == "metrics":
        slabs: list[str] = []
        for line in block:
            t = line.strip()
            if not t.startswith("-"):
                continue
            bits = [b.strip() for b in t.lstrip("-").split("::")]
            val = bits[0] if bits else ""
            cap = bits[1] if len(bits) > 1 else ""
            tone = bits[2] if len(bits) > 2 and bits[2] in _TONES else ""
            slabs.append(
                f'<div class="metric"><div class="val {tone}">{_inline(val)}</div>'
                f'<div class="cap">{_inline(cap)}</div></div>'
            )
        return f'<div class="metrics">{"".join(slabs)}</div>'

    if name == "cols":
        ratio = "ratio-6040" if "6040" in parts else ""
        cards, cur, cur_cls = [], [], None
        for line in block:
            t = line.strip()
            cm = re.match(r"^::\s*card\s*(\w*)$", t)
            if cm:
                if cur_cls is not None:
                    cards.append((cur_cls, cur))
                cur_cls, cur = cm.group(1) or "", []
                continue
            cur.append(line)
        if cur_cls is not None:
            cards.append((cur_cls, cur))

        if not cards:                       # plain two-column split
            return f'<div class="cols {ratio}">{_render_lines(block)}</div>'

        inner = "".join(
            f'<div class="card {cls}">{_render_lines(body)}</div>' for cls, body in cards
        )
        return f'<div class="cols {ratio}">{inner}</div>'

    return f'<div class="{html.escape(name)}">{_render_lines(block)}</div>'
