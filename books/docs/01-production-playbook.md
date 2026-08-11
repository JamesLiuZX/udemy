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

## 3. Pull quotes and key-takeaway boxes

Two more bracket markers, same convention as `[AUTHOR-INPUT: ...]`: plain
text in the source, rewritten into a styled LaTeX block by `build.py`
after Pandoc runs. Use both. A chapter that's five pages of unbroken body
paragraphs reads as a textbook no matter how good the writing is; these
two devices are what make a page look like it came from an edited book
instead of a Word document with a heading style applied.

**Pull quote**, one per chapter at minimum, pulled verbatim from a line
you already wrote rather than composed fresh: pick the single sentence in
the chapter with the most bite and set it big.

```markdown
[PULLQUOTE: The line goes here, verbatim from body text above it.]
```

**Key takeaways**, one per chapter, at the very end: three to five short
bullets a reader could screenshot. The list needs a blank line after the
opening marker and before the closing one, or Pandoc reads the `- item`
lines as a lazy continuation of the marker's own paragraph instead of a
list, and it renders as one run-on sentence with literal hyphens in it.

```markdown
[TAKEAWAYS]

- First point, short enough to scan
- Second point
- Third point

[/TAKEAWAYS]
```

Don't overuse either. A pull quote every page stops being a pull quote
and starts being a font size. One well-chosen pull quote and one closing
takeaways box per chapter is the target, not a ceiling to push past.

## 4. `[KEY-INSIGHT: claim || source]`

A researched, cited statistic or case study, for when the real author has
no personal anecdote to give (the normal case for the titles currently in
this repo). Green box, claim first, then the source in a smaller line
underneath.

```markdown
[KEY-INSIGHT: A Canadian tribunal held Air Canada liable for a refund
policy its own chatbot invented on the spot || Source: Moffatt v. Air
Canada, 2024 BCCRT 149 (Feb. 14, 2024).]
```

The claim and source are separated by `||`. Watch for one Pandoc quirk:
it rewrites a literal `||` in the source Markdown into `\textbar\textbar{}`
in its LaTeX output rather than passing the pipe characters through, so
`build.py`'s regex matches that escaped form, not raw pipes, when
converting the marker. If you're ever debugging why a `[KEY-INSIGHT: ...]`
rendered as plain bracket text on the page instead of a box, check the
generated `.tex` in `build/books/<slug>/chapters/` for this first.

**Every claim inside one of these must be independently verified with an
actual search before it's written down.** Full sourcing standard,
including what to do when you can't confirm an exact quote, in
`books/docs/02-research-and-sourcing.md`. Read it before writing your
first one.

## 5. `[AUTHOR-INPUT: ...]`

Same rule as the video side's `[INSTRUCTOR-INPUT]`, applied to print:
marks a claim, story, or credential only the real author can supply.
`qc.py` fails the build while any remain. Never resolve one by inventing
plausible-sounding content; leave it blocking until the author writes it.
Reach for `[KEY-INSIGHT: ...]` first unless there's a genuine personal
story to tell here; see `books/CLAUDE.md` §1 for why the default flipped.

## 6. Estimating length

`book.py` estimates page count from word count using a words-per-page
constant calibrated to 6"×9" trim at the class's default body size
(roughly 300-330 words/page for justified body text at that trim with
`kdp-book.cls`'s default margins). It's an estimate for pacing while
writing, not a substitute for rendering and checking the real page count,
which shifts with how much of the manuscript is dialogue, lists, tables,
or headings versus dense prose.

## 7. Build commands

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
