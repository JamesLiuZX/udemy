# Working in books/

Amazon KDP print/ebook publishing system. Manuscript source becomes a
typeset, print-ready PDF (interior) via LaTeX, with a quality gate that
blocks anything not ready to upload.

This is a sibling system to the Udemy course pipeline one directory up, not
a variant of it. Different medium, different failure modes, different
rules. Read this file before your first edit here even if you know the
video side well; do not assume its rules carry over.

---

## 1. The rule that protects the account

Amazon KDP requires disclosure of AI-generated content at submission (the
publishing dashboard asks directly whether a book is AI-generated, and
whether it is AI-assisted). KDP draws a real distinction between the two:

- **AI-generated**: produced by AI with no meaningful human creative
  control over the content. Must be disclosed.
- **AI-assisted**: a human wrote, substantially edited, or directively
  guided the content, using AI as a tool. Generally does not require
  reader-facing disclosure, but you still declare it in the dashboard.

KDP also actively enforces against low-quality, mass-produced AI content,
and self-help is one of the categories it watches hardest, because a
generic, uncredentialed AI self-help book is exactly the spam pattern it's
policing. Enforcement here is account-level, not book-level: it can cost
you publishing rights entirely, not just one title.

**Verify current KDP content guidelines before you actually publish.**
Policy specifics move; what's encoded here is the shape of the rule, not
a guarantee it is still worded this way today.

Two things are therefore load-bearing, the direct analogue of the video
side's `verified` and `[INSTRUCTOR-INPUT]`:

1. Every manuscript carries `verified: false` in `book.yaml` until a human
   reads the whole thing and signs off. **Never set `verified: true`
   yourself.** It is the author's signature, and for a self-help title it
   is also the thing separating a real book from the spam pattern KDP
   polices.
2. `[AUTHOR-INPUT: ...]` marks content only the real author can supply:
   their own story, their actual credentials, a case they personally
   worked, an opinion they'd defend under their own name. **Never invent
   content to fill one.** A self-help book with fabricated lived experience
   isn't a shortcut, it's a different, worse book. Leaving it blocking the
   build is correct behaviour.

`qc.py` fails on both. A QC run that reports only these is a **pass**, not
a problem to fix.

---

## 2. The loop

```bash
# 1. Write or edit books/<slug>/manuscript/<NN>-<chapter-slug>.md

# 2. Build the interior PDF
python3 books/pipeline/build.py --book <slug>

# 3. LOOK AT THE RENDERED PAGES. Not optional, same discipline as the video
#    side's §3. Open a spread, not just page 1.
python3 books/pipeline/build.py --book <slug> --open-pages 1,2,45,46,120,121

# 4. Authoring checks
python3 books/pipeline/qc.py --book <slug>

# 5. Release gate: page count in range, fonts embedded, no build warnings
python3 books/pipeline/qc.py --book <slug> --release
```

`build/` is gitignored, same rule as the video side. The interior PDF is
regenerable from the manuscript; never commit it.

---

## 3. Always look at the rendered page

A LaTeX document that compiles cleanly is not a document that reads
cleanly. Overfull `\hbox` warnings are the obvious failures; the dangerous
ones are silent: a widow line alone at the top of a page, a chapter
opener that lands on a verso page instead of recto, a running head that
repeats the wrong chapter title after a mid-chapter section break, a table
that KDP will re-flow strangely at their proof stage.

Check specifically: the first spread of every chapter (running heads,
opener spacing), any page with a table or figure (KDP has no lenience for
content in the gutter or bleed), and the front matter (copyright page,
half title, TOC page-number accuracy after a full rebuild).

Do not report a chapter as done without having viewed its rendered pages.

---

## 4. Authoring a manuscript

Copy `books/_template/` to start a new title. `book.yaml` is the source of
truth: trim size, target page count, front/back matter list, chapter
order. Chapters are plain Markdown in `manuscript/`, one file per chapter,
converted to LaTeX by Pandoc and assembled by `build.py` into the master
document that compiles with `kdp-book.cls`.

### Writing rules, in priority order

1. **Say something a reader could act on by page 3 of every chapter.**
   Self-help fails when it restates the premise for forty pages before
   giving the reader anything to do differently. State the claim, then
   earn it.
2. **Open every chapter on a scene, not a summary.** "Two people try AI
   for the first time" beats "Many people struggle with AI adoption."
   Commit to one concrete moment, specific enough that a reader pictures
   an actual room, before zooming out to the argument. A chapter that
   opens by naming the abstract category first has already lost the
   reader most likely to recommend the book onward.
3. **A claim needs a source: a study, a named mechanism, or the author's
   own tested experience.** If it's the author's experience, it's an
   `[AUTHOR-INPUT: ...]`, not something to invent on their behalf.
4. **No LLM tells.** "delve", "in today's fast-paced world", "unlock your
   potential", "game-changer", "it's important to note", "in conclusion",
   "a testament to". `qc.py` flags these; they read as generic in fiction
   and non-fiction alike and are the single fastest way a reader (or a KDP
   quality reviewer) pattern-matches a book as AI spam.
5. **Name the limit of the advice.** What kind of reader this doesn't work
   for, or when the technique fails. Non-negotiable in self-help
   specifically: advice presented as universal is both less credible and
   more likely to actually harm a reader for whom it's the wrong fit.
6. **Concrete before abstract**, same instinct as the video side. A named
   scenario beats a generic one. Vary sentence length on purpose: a run of
   same-length sentences is what makes competent prose read as flat.
   Follow a long, subordinate-clause sentence with a short one. Let a
   fragment land sometimes. That's what makes a paragraph.
7. **Default to minimal em dashes.** `book.yaml: style.em_dash` still
   takes `allow` or `avoid`, and `avoid` is the default for new books
   started after this line was written: KDP paperbacks aren't read aloud
   the way lectures are, so an em dash isn't the same tell here it is on
   the video side, but a reader who's just spent a year seeing AI text
   flagged by its em dashes notices them in a book too, and this system
   would rather a sentence get rebuilt with a colon, a period, or
   parentheses than give a reader that flicker of doubt. `allow` remains
   available per book if an author genuinely wants the em dash back as a
   stylistic choice; don't switch a book to it by default.

Unlike the video side, there is no fixed pacing model. A chapter's length
is however long the argument actually takes, subject to the book's overall
`target_pages` range in `book.yaml`.

---

## 5. The design system

Continuity with the video course's identity, translated to print: a book
that looks like it came from an editor, not a template.

| Role | Face |
| --- | --- |
| Body, headings, running heads | TeX Gyre Schola (same family as the course; already vendored) |
| Code, data, worksheet fragments | IBM Plex Mono |

Accent colour for chapter numerals and part-title furniture is the same
ink blue, `#1B4F8F`, used only where colour survives to print (chapter
numbers, rule lines). The interior is otherwise black on white: KDP prints
most paperback interiors in black and white by default, and colour
interior printing is a separate, more expensive KDP product. Confirm which
one a given title is before leaning on colour for anything meaning-bearing.

**Typesetting non-negotiables**, enforced in `kdp-book.cls`:

- No widows or orphans (`\widowpenalty10000 \clubpenalty10000`).
- `microtype` on, for character protrusion and font expansion.
- Chapter openers start recto (right-hand page); `memoir`'s
  `\cleardoublepage` handles this, do not remove it to save a blank page.
- Running heads: book title on verso, chapter title on recto. Never the
  author's name on both, it wastes the one piece of free navigation a
  print reader has.
- Section heads (`##`) print in the ink-blue accent, not black. A chapter
  with five plain-black subheadings and nothing else reads as a Word
  document; the colour is doing real work making the page look edited.

**A page is not allowed to be five straight paragraphs of body text.**
Every chapter needs at least one `[PULLQUOTE: ...]` and closes with one
`[TAKEAWAYS]` box (syntax and rendering in
`books/docs/01-production-playbook.md` §3). These aren't decoration on
top of finished writing, they're part of what makes a KDP nonfiction title
look like it came from a publisher rather than a template, alongside the
`\authorinput` box the gate already forces. Plan where they land while
drafting a chapter, not as a pass tacked on afterward.

---

## 6. KDP production facts that will cost you time if ignored

- **Trim size is 6" × 9" by default.** Standard for self-help and
  business nonfiction, and what `kdp-book.cls` assumes unless a book
  overrides `trim` in `book.yaml`. Changing trim after a manuscript is
  substantially written means a full re-layout pass, not a recompile.
- **The gutter (inside) margin scales with page count**, because more
  pages means more spine curvature eating into the inside margin. KDP's
  paperback table, baked into `kdp-book.cls` as `pages-band` options:

  | Page count | Gutter |
  | --- | --- |
  | 24-150 | 0.375" |
  | 151-300 | 0.5" |
  | 301-500 | 0.625" |
  | 501-700 | 0.75" |

  A book that grows past a band boundary during editing needs its margin
  band bumped and a full re-render. Check final page count against the
  band before final export, not just against `target_pages`.
- **All fonts must be embedded.** `xelatex` with `fontspec` does this by
  default for the vendored OTF/TTF faces; it silently stops being true if
  a chapter's LaTeX ever references a system font by name instead of
  through the class's font commands. Don't do that.
- **KDP wants a separate interior file and cover file.** This pipeline
  only produces the interior. Cover design (which needs the final page
  count to compute spine width) is a separate, later step once page count
  is locked.
- **US vs UK spelling is a per-book choice, not a repo default.** The
  video course is `en_GB` because the instructor writes in British
  English. Books default to `en_US` in `book.yaml: style.spellcheck_lang`
  because most self-help buyers on KDP are on the US store, but check this
  deliberately per title rather than assuming it.

---

## 7. Definition of done for a chapter

- [ ] Opens on a concrete scene, not a category summary
- [ ] At least one `[PULLQUOTE: ...]` and a closing `[TAKEAWAYS]` box,
      both visually confirmed in the render, not just present in source
- [ ] Rendered pages **visually inspected**, not just compiled without
      LaTeX errors
- [ ] `qc.py` reports no warnings, and no failures other than the sign-off
      and `[AUTHOR-INPUT]` gates
- [ ] Every non-obvious claim has a named source or is explicitly the
      author's own tested experience, flagged for their sign-off
- [ ] The chapter says what it doesn't apply to, somewhere in its own text
- [ ] Runs recto, running heads correct, no widow/orphan on inspected pages

Report honestly. If a chapter is written but not visually checked, say so.

---

## 8. Repo map

```
books/CLAUDE.md              This file
books/docs/00-kdp-compliance.md      KDP AI-disclosure + content policy notes
books/docs/01-production-playbook.md Format reference, chapter structure
books/theme/kdp-book.cls     The LaTeX document class: trim, margins, type
books/pipeline/               book.py, build.py, qc.py
books/_template/              Copy this to start a new title
books/<slug>/book.yaml        Per-book source of truth
books/<slug>/manuscript/*.md  One file per chapter
```

Same minimal-dependency philosophy as the video side: Python only needs
PyYAML. Everything else shells out to Pandoc and `latexmk`/`xelatex` on
purpose.

---

## 9. Git

Same branch and repo as the video course: `claude/keep-writing-apht23`.
This is one repo with two independent production lines in it, not two
repos. Do not commit `build/`.
