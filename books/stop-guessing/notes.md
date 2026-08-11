# Status and chapter map

Not part of the build. Working notes for continuing this manuscript across
sessions, mirroring how courses/ai-for-pms/CLAUDE.md tracked "current state
and what to do next" while that course was being written.

## Status

- Chapters 01 through 03 are written and verified-pending-signoff: built
  individually with `--only`, rendered pages visually inspected (chapter
  opener, KEY INSIGHT box, PULLQUOTE, table, KEY TAKEAWAYS box all confirmed
  rendering correctly, no overflow/widow/orphan on inspected pages), `qc.py`
  clean beyond the `verified: false` gate. (This file previously said only
  01 existed; 02 and 03 were written and committed in a prior session and
  this file just hadn't been updated to match. Corrected 2026-08-11.)
  - 01 The Accountability Gap: 2,645 words, 8 pages standalone.
  - 02 Seven Shapes: 5 pages standalone.
  - 03 The Spec Nobody Can Argue With: 5 pages standalone.
  Note: page counts from `--only` builds are per-chapter standalone
  renders (chapter numbering restarts at 1 in that mode, expected per
  build.py's design, not a bug) and will differ from each chapter's real
  position once assembled in a full build.
- `target_pages` was originally guessed at [220, 280] before any real
  chapter existed, matching a typical full-length business book. Chapter
  01 at a genuinely complete, unpadded length (states the thesis, two
  worked examples, a runnable exercise, a preview of the rest of the book,
  names its own limits) came in at 7 real pages, calibrating real density
  to roughly 378 words/page. Padding every future chapter by 2-3x to hit
  the original target would violate the same no-padding discipline the
  video course held throughout, so `target_pages` was rebased to
  [120, 170]: a tight, focused field guide, which also fits the book's
  own subtitle better than a 280-page tome would have. If later chapters
  naturally run longer (the golden set or risk register chapters likely
  will, given how much more ground they cover), let the estimate move
  again rather than force it. Re-check against the KDP gutter band
  (0.375" through 150pp, 0.5" from 151pp) once the real total is close.
- **All 12 chapters are now written, verified-pending-signoff, and the full
  book builds clean.** (Status as of the session that finished the
  manuscript, 2026-08-11.) Chapters 04-12 were each built individually
  with `--only`, every page visually inspected, `qc.py` clean beyond the
  `verified: false` gate. Full-book build: `python3 books/pipeline/build.py
  --book stop-guessing` -> 97 pages. EPUB: `python3
  books/pipeline/build_epub.py --book stop-guessing` -> builds clean,
  valid zip, 38 files. `qc.py --book stop-guessing --release` -> only the
  `verified: false` gate fails; page count, gutter margin, and font
  embedding all pass.
- `back-matter/acknowledgments.md` and `back-matter/about_the_author.md`
  didn't exist for this book (only `_template/` had them, and the
  template's filename is `about-the-author.md` with a hyphen while
  `book.yaml`'s `back_matter:` list says `about_the_author` with an
  underscore, which is what `build.py` actually looks up). Without them,
  the full build silently ended at chapter 12 with no back matter at all.
  Created both here as `[AUTHOR-INPUT: ...]`-gated stubs, same convention
  as every other real-story marker in this book: never fill these in with
  an invented bio or a fabricated thank-you list. They render as visible
  "AUTHOR INPUT NEEDED" boxes and are currently the two open items
  blocking a genuine release, alongside `verified: false` itself.
- `target_pages` moved twice as real content accumulated. [220, 280] (pre-
  chapter-1 guess) -> [120, 170] (after chapter 1 alone, see below) ->
  **[85, 110]** (after all 12 chapters existed and the full build came in
  at 94 pages before back matter, 97 after). This is not a shortfall to
  patch by padding chapters: total manuscript word count across all 12
  chapters is 23,920 words, consistent with the book's own subtitle ("field
  guide") and the no-padding discipline stated in `books/CLAUDE.md` and
  held throughout. If a real human pass adds material, let the band move
  again rather than force it back up artificially. Gutter margin at 97pp
  is correctly 0.375in (24-150pp band); re-check only if a future edit
  pushes the total past 150.
- Work one chapter at a time to the same bar as Chapters 01-03 was held for
  every later chapter too: write, build `--only <id>`, inspect the
  rendered pages, `qc.py`, then move on. Same discipline as the video
  course's "work one lecture at a time," now applied end to end.
- Toolchain note: this environment needed `pandoc`, `texlive-xetex`,
  `texlive-latex-extra`, `texlive-fonts-recommended` (fixes a missing
  `pzdr`/URW-Dingbats font error from hyperref), `latexmk`, and
  `poppler-utils` (`pdfinfo`/`pdftoppm`/`pdffonts`) installed via apt
  before `build.py`/`qc.py --release` would run. `hunspell` was
  deliberately left uninstalled: `qc.py`'s spellcheck no-ops gracefully
  without it (by design), and with it installed the en_US dictionary
  false-positives on real words already in these chapters (Zillow,
  Zestimate, iBuying, chatbot, roadmap, ...). Fixing that properly means
  growing `ALLOW` in `books/pipeline/qc.py`, which is shared across all
  three books being written in parallel on this branch right now and out
  of scope for a stop-guessing-only session; flagging it here rather than
  editing that file.

## Chapter-to-course map

Each chapter adapts specific lectures rather than summarising the whole
course. Cite the idea, not the video, in the actual prose: a print reader
has never seen "6.6" and the book should never assume they have.

| Chapter | Adapts | Core idea |
| --- | --- | --- |
| 01 The Accountability Gap | 0.1, 0.3, 0.4 | Probability distribution, not a function |
| 02 Seven Shapes | 1.6, 1.7 | Archetypes; when not to use AI at all |
| 03 The Spec Nobody Can Argue With | 3.1, 3.7 | PRD as evaluation thresholds |
| 04 The Golden Set | 4.1, 4.2 | The core artifact everything else depends on |
| 05 Getting Two People to Agree | 4.3, 4.4, 4.8, 4.9 | Rubrics, calibration, reading results honestly |
| 06 What It Actually Costs | 7.2, 7.4, 7.5 | Unit economics, model selection, margin |
| 07 The Reliability Math of Agents | 6.1, 6.3, 6.6, 6.7 | Multi-step failure compounding, blast radius |
| 08 The Risk Register | 8.1-8.6 | The five-category register, red-teaming |
| 09 Metrics That Survive Production | 9.1, 9.2, 9.5 | Adoption/acceptance/deflection, the leadership dashboard |
| 10 Managing the Room | 10.2, 10.3 | Calibrated stakeholder claims, the roadmap that doesn't lie |
| 11 The First Ninety Days | 10.1, 10.7, 11.4 | Discovery sprints, a 30-60-90 plan, a closing self-assessment checklist (11.1-11.3's capstone-brief/worked-solution mechanics are course-specific workshop scaffolding and weren't adapted directly) |
| 12 Where This Breaks | Repo-wide | Honest limits chapter; no equivalent single lecture |

## Things to hold onto while writing the rest

- Every course-side "honest caveat" device becomes prose here, not a
  callout box: state the limit in the chapter's own voice, don't format it
  as a UI element that doesn't exist in print.
- `[AUTHOR-INPUT: ...]` markers are for a real story or credential, one or
  two genuinely load-bearing ones per chapter, not a marker for every
  paragraph. Over-marking is as much a tell as under-marking.
- Keep the "name the cost" instinct from the video side. A self-help /
  business book that never says where the advice fails is exactly the
  pattern KDP's compliance doc (`docs/00-kdp-compliance.md`) warns reads as
  generic AI spam.
