# Status and chapter map

Not part of the build. Working notes for continuing this manuscript across
sessions, mirroring how courses/ai-for-pms/CLAUDE.md tracked "current state
and what to do next" while that course was being written.

## 2026-08-11: author directive, expansion to [180, 240] pages

The author reviewed the completed-but-tight 97-page manuscript and asked for
a substantially fuller book, through substance, never padding. Concretely,
the following are all now in scope:

- `target_pages` raised from `[85, 110]` to **`[180, 240]`**.
- Every existing chapter (01-10, 13, 14) gets a genuine second worked
  example, not a restated first one, chosen for a different domain or
  failure mode than the first so it teaches something the first example
  didn't.
- Every existing chapter gets a second `[KEY-INSIGHT: ...]` where a second
  independently verified claim actually strengthens the argument, sourced
  the same way as the first: live search at writing time, real citation,
  never recalled from memory. Not every chapter needs exactly two if a
  second genuinely well-fitting case can't be found honestly; forcing one
  in would be exactly the padding this expansion is not supposed to be.
- Chapter-end exercises or checklists get added where they earn a place
  (several chapters already had an implicit "try this" habit from the
  video course's own pattern; this makes it a explicit, work-along
  element on the page, consistent with the "field guide" framing).
- Two new chapters, inserted after chapter 10 (see the revised table
  below), plus four appendices in back matter: worksheet-style templates
  a reader can work through directly, rendered as tables with room to
  fill in, not narrated as vaguely as the same content would read as
  prose.
- Thin chapters (02, 03, 10 especially; originally 1,436, 1,172, and
  1,691 words) get expanded on the same terms as new chapters, not just
  chapters written from here forward. **The expansion pass revisits
  already-shipped chapters, it doesn't only apply going forward.**
- Padding is explicitly still banned: no restating a point in different
  words, no inflated transitions, no drop in information density per
  page. If a chapter is honestly complete at its current length once it
  has a real second example and a real second insight, the book grows by
  adding a chapter instead of stretching that one further.

**Revised chapter order** (renumbering only touches the last two of the
original twelve; chapters 01-10 keep their existing files and numbers):

| # | Title | Status |
| --- | --- | --- |
| 01 | The Accountability Gap | expand |
| 02 | Seven Shapes | expand (thin) |
| 03 | The Spec Nobody Can Argue With | expand (thin) |
| 04 | The Golden Set | expand |
| 05 | Getting Two People to Agree | expand |
| 06 | What It Actually Costs | expand |
| 07 | The Reliability Math of Agents | expand |
| 08 | The Risk Register | expand |
| 09 | Metrics That Survive Production | expand |
| 10 | Managing the Room | expand (thin) |
| 11 | Objections and Pushback | **new** |
| 12 | Field Notes: Three Worked Case Studies | **new** |
| 13 | The First Ninety Days | renumbered from 11, expand |
| 14 | Where This Breaks | renumbered from 12, expand |

Files: `11-the-first-ninety-days.md` -> `13-the-first-ninety-days.md` and
`12-where-this-breaks.md` -> `14-where-this-breaks.md` (both `git mv`'d,
history preserved). `book.yaml`'s `chapters:` list updated to match.

Chapter 11 (Objections and Pushback) sits right after Managing the Room on
purpose: it's the direct continuation of "the room," now organised around
the specific pushback lines a PM actually hears (we don't have time for
this, the vendor says 99% accurate, legal will slow us down, our
competitors shipped without any of this) rather than the general
calibration skill chapter 10 already covered. Chapter 12 (Field Notes)
gives three compressed but complete worked examples that run the whole
method (shape check, spec, golden set, cost, risk, metrics) against three
feature types the book's recurring support-ticket-and-refund-agent thread
never touches directly: a document-extraction feature, a lead-scoring
predictor, and an internal coding agent. It's placed before chapter 13
(First Ninety Days) so the reader sees the method applied whole, in
different domains, immediately before being asked to run it themselves.

**Renumbering broke exactly two cross-references, both already fixed as
part of this pass:** chapter 10's "Where this goes next" used to point to
"chapter eleven" meaning the old First Ninety Days; it now points to the
new chapter 11 (Objections and Pushback), and the Objections/Field Notes/
First Ninety Days/Where This Breaks chain was rebuilt so each "where this
goes next" points at its real neighbour. The old chapter 11's "spent nine
chapters" / "ten chapters" self-references and the old chapter 12's "spent
eleven chapters" opening line were updated to twelve and thirteen
respectively to match their new position as chapters 13 and 14. Checked via
`grep -rn "chapter eleven\|chapter twelve\|chapter thirteen\|chapter
fourteen" manuscript/*.md` before considering the renumbering done; rerun
that check after any future chapter reordering, it's cheap and it's the
actual failure mode of moving chapters around in a book that cross-
references itself this much.

**Back matter now includes four appendices**, added before acknowledgments
and about-the-author: `appendix_a_the_golden_set_worksheet`,
`appendix_b_the_risk_register_template`,
`appendix_c_the_model_scorecard_template`,
`appendix_d_the_ninety_day_plan_template`. `build.py`'s
`back_matter_tex()` derives each one's printed heading from its snake_case
item name via `.replace("_", " ").title()` since only `acknowledgments` and
`about_the_author` have hardcoded titles; that's a shared-pipeline
function, out of scope to edit, so item names were chosen to title-case
into something readable without a colon (e.g. `appendix_a_the_golden_set_worksheet`
-> "Appendix A The Golden Set Worksheet") rather than fighting it.

**Gutter band:** no code or class change needed. `kdp-book.cls` never hard-
codes a gutter; `build.py` computes it from `book.margins()`, which reads
`target_pages`'s midpoint before a page count is known and would read the
real measured count on a rebuild once one exists (see `book.py`'s
`gutter_for_pages()` and `GUTTER_BANDS`: 0.375in through 150pp, 0.5in for
151-300pp, matching `books/CLAUDE.md` exactly). Midpoint of the new
`[180, 240]` is 210, comfortably inside the 151-300 band, so the very next
full build already picks up 0.5in automatically. Re-run `qc.py --release`
once the manuscript is complete and stable and confirm its gutter-
consistency check (compares the gutter actually used against what the real
final page count wants) passes silently, the same check that already
caught nothing wrong at 97 pages.

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
| 11 Objections and Pushback | Repo-wide, esp. 1.7, 4.1, 10.2 | New for the expansion; the specific pushback lines a PM hears, answered from tools already in the book |
| 12 Field Notes: Three Worked Case Studies | Repo-wide | New for the expansion; the method run whole against three feature types outside the book's recurring example |
| 13 The First Ninety Days | 10.1, 10.7, 11.4 | Discovery sprints, a 30-60-90 plan, a closing self-assessment checklist (11.1-11.3's capstone-brief/worked-solution mechanics are course-specific workshop scaffolding and weren't adapted directly) |
| 14 Where This Breaks | Repo-wide | Honest limits chapter; no equivalent single lecture |

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
