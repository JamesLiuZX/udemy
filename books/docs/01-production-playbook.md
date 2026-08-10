# Production playbook

Format reference for `book.yaml` and chapter Markdown. Start a new title by
copying `books/_template/` rather than writing these from scratch.

---

## 1. `book.yaml`

```yaml
slug: your-book-slug
title: "The visible title"
subtitle: "Optional subtitle"
author: "Real author name"
genre: self-help              # self-help | ai-and-technology | business | ...
trim: "6x9"                    # inches; drives kdp-book.cls margins
target_pages: [300, 500]       # [min, max]; qc.py --release fails outside this
verified: false                 # never set true except by the author

style:
  spellcheck_lang: en_US        # en_US | en_GB, per-book choice
  em_dash: allow                 # allow | avoid — a consistency check, not a ban

description: |
  Back-cover / KDP listing copy. Not part of the interior PDF.

front_matter:
  - half_title
  - title_page
  - copyright
  - dedication        # optional; omit the file and the entry to skip
  - toc

chapters:
  - id: "01"
    title: "Chapter title as it should appear"
    file: manuscript/01-chapter-slug.md
  - id: "02"
    title: "..."
    file: manuscript/02-chapter-slug.md

back_matter:
  - acknowledgments
  - about_the_author
```

`build.py` reads this top to bottom to assemble the master LaTeX document:
front matter in order, then chapters in order, then back matter in order.

## 2. Chapter Markdown

Plain Markdown, one file per chapter. Pandoc converts it to LaTeX; nothing
book-pipeline-specific to learn beyond standard Markdown, deliberately,
because the bulk of 300-500 pages needs to be easy to keep writing.

```markdown
# Chapter title

Opening paragraph. State the claim early; don't spend a page circling it.

## A section heading

Body text. **Bold** for a term being defined, *italic* for emphasis.

> A block quote, for a quoted source or a pull-quote moment.

[AUTHOR-INPUT: the specific story about the client who tried this and
it backfired, and what actually happened]

- A list
- Works the way you'd expect

A table, when a comparison genuinely earns one:

| Approach | When it works | When it doesn't |
| --- | --- | --- |
| ... | ... | ... |
```

Supported: headings (`#`/`##`/`###`, mapped to chapter/section/subsection),
bold, italic, block quotes, ordered/unordered lists, tables, footnotes
(`[^1]` / `[^1]: text`). Anything Pandoc's Markdown reader supports works;
this is intentionally not a custom DSL the way the slide format is.

## 3. `[AUTHOR-INPUT: ...]`

Same rule as the video side's `[INSTRUCTOR-INPUT]`, applied to print:
marks a claim, story, or credential only the real author can supply.
`qc.py` fails the build while any remain. Never resolve one by inventing
plausible-sounding content; leave it blocking until the author writes it.

## 4. Estimating length

`book.py` estimates page count from word count using a words-per-page
constant calibrated to 6"×9" trim at the class's default body size
(roughly 300-330 words/page for justified body text at that trim with
`kdp-book.cls`'s default margins). It's an estimate for pacing while
writing, not a substitute for rendering and checking the real page count,
which shifts with how much of the manuscript is dialogue, lists, tables,
or headings versus dense prose.

## 5. Build commands

```bash
# Full interior PDF
python3 books/pipeline/build.py --book your-book-slug

# Single chapter, fast iteration (skips full front/back matter assembly)
python3 books/pipeline/build.py --book your-book-slug --only 03

# Authoring checks
python3 books/pipeline/qc.py --book your-book-slug

# Release gate
python3 books/pipeline/qc.py --book your-book-slug --release
```
