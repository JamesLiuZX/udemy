# Status and chapter map

Not part of the build. Working notes for continuing this manuscript across
sessions, mirroring how courses/ai-for-pms/CLAUDE.md tracked "current state
and what to do next" while that course was being written.

## 2026-08-11: TOC number-column fix verified, both proofs recommitted

Author directive: a fix landed in `books/theme/kdp-book.cls` (commit
`be1fcbe`, shared across all seven titles) widening memoir's TOC chapter/
section/subsection number columns and page-number margin, because
two-digit section numbers (e.g. "14.10") were colliding with entry titles
and three-digit page numbers were crowding the leader dots in shipped
proofs. The author couldn't compile locally and asked this session to
verify, adjust the em-based widths if anything still collided, and
recommit both `stop-guessing` proofs.

**Verification.** Rebuilt both editions from source (this fix was already
an ancestor of this session's own rebased commit, pulled in automatically,
not a separate pull). English: 179 pages, unchanged. Chinese: 157 pages,
unchanged. Rendered every page of both books' full table of contents at
150dpi (English: 5 pages, chapters 1-17 plus four appendices and two
back-matter entries; Chinese: 5 pages, same structure with 目录/附录
headings) and visually inspected each one. Finding: **no collisions in
either edition, no width adjustment needed.** Every section number,
one-digit or two, sits with a clean gap before its title; every page
number, one to three digits, sits clear of the leader dots. Chapters in
this particular book top out at nine subsections (8.9, the highest), so
the exact "14.10" collision the fix targeted doesn't occur here, but the
column widths were still visibly tight enough beforehand in earlier
renders (see the two-digit "11.x"/"12.x"/etc. entries and 100+ page
numbers on TOC pages 3-5) that the fix reads as a real, needed correction,
not a no-op for this title.

**Recommitted** `proofs/stop-guessing.pdf` and `proofs/stop-guessing-zh.pdf`
from these rebuilds, both bytes now reflecting the widened TOC columns, in
a single commit alongside this note.

## 2026-08-11: Simplified Chinese edition shipped as a second PDF

Author directive: translate the complete book into idiomatic Simplified
Chinese and ship it as `proofs/stop-guessing-zh.pdf`, a second, independent
edition alongside the English one, not a replacement for it.

**KDP policy check, live-searched, not assumed.** Ran three separate live
searches against KDP's own help pages and current community reporting.
Finding, consistent across all three: **Amazon KDP does not support
paperback books in Chinese, Simplified or Traditional, at all.** This is a
platform-level format restriction, not a content-policy judgment call.
Chinese is supported for Kindle eBooks (Traditional Chinese fully, with
Simplified Chinese getting Enhanced Typesetting support), but the paperback
interior pipeline this repo builds has no KDP paperback destination to
upload to in this language, regardless of manuscript quality. Sources:
[KDP Book Supported Languages](https://kdp.amazon.com/en_US/help/topic/G200673300),
[KDP Chinese (Traditional) Beta](https://kdp.amazon.com/en_US/help/topic/G27T64E65VM6JWKK),
[KDP Community: how can I publish a paperback in Simplified Chinese on
KDP?](https://kdpcommunity.com/s/question/0D52T00005GxOuESAV/how-can-i-publish-a-paperback-in-simplified-chinese-on-kdp?language=en_US)
(community answer: you can't, confirmed by KDP staff replies in-thread).
**Consequence for this book:** `stop-guessing-zh` targets Google Play
Books, Apple Books, and direct/lead-gen distribution. It is explicitly
**not** a KDP upload, and `book-zh.yaml`'s ISBN line and description were
written without any KDP-specific language. If KDP's policy changes in the
future (Simplified Chinese ebook support already exists and could extend
to print), the EPUB this pipeline already produces would be the asset to
reconsider uploading, not the PDF.

**Translation.** All 17 chapters plus all 6 back-matter pieces (4
appendices, notes and sources, about the author) translated into
professional, idiomatic zh-CN for a business reader, not machine-literal.
Wordplay and rhetorical structure were recreated rather than transliterated
(e.g. chapter 1's "I'm sold" / "看起来好像可以" framing). Technical terms
are bilingual on first use inside a chapter and Chinese-only after, e.g.
评测集（golden set）, 评分标准（rubric）, 影响半径（blast radius）, and stay
consistent across all 17 chapters via a glossary held across the whole
translation pass. Product names, company names, and code identifiers stay
in English (Zillow, Whisper, Klarna, GPT-4, LMArena). `[KEY-INSIGHT: ...]`
citations translate the claim into Chinese and keep the source title,
publication name, and case name in their original language so a reader can
still find and verify the primary document, per the standing sourcing
discipline; only the date format was localized. Chinese punctuation
conventions (，。：、《》「」) are used throughout. The translation was
written with **zero em dashes**: `book-zh.yaml: style.em_dash` stays
`avoid`, the same repo-wide default every other book uses, including the
two other Chinese editions that already existed in this repo when this
one was finished (`ai-employee-zh`, `one-person-business-zh`, both
independently written with no em dashes at all). An early draft of this
edition used a single em-dash-rendered 破折号 for asides, on the reasoning
that it's legitimate Chinese punctuation and not an English-specific AI
tell; caught this against the sibling-book convention during the pull
described below and rewrote every instance (140+ occurrences across 16
files) into colons, commas, parentheses, or split sentences instead, to
keep the em-dash gate meaningful and uniform across every book and every
language edition rather than carving out a per-book exception.

**Typesetting, and a mid-flight convergence with two sibling sessions.**
Built opt-in CJK support into the shared pipeline, then hit merge
conflicts on `git pull --rebase`: two other sessions, working on
`ai-employee-zh` and `one-person-business-zh` in parallel, had
independently built the same feature. Their version was already more
mature (used by two other books, not one) and used a cleaner mechanism:
`book.yaml: lang: zh` (a `Book.lang` property already in `book.py`) drives
`kdp-book.cls`'s `[zh]` class option directly, rather than this session's
first draft, which used a separate `cjk: true` flag and an
`\ifdefined\BookCJK` conditional block appended at the end of the class
file. Resolved every conflict in favor of the established convention,
deleted this session's now-redundant `cjk`/`back_matter_dir`/
`back_matter_titles` `Book` properties (superseded by `lang` and by
`build.py` reading `back_matter_titles` straight off `book.yaml`), and
switched `book-zh.yaml` from `cjk: true` / `back_matter_dir: back-matter-zh`
to `lang: zh` (the back-matter directory is now found automatically from
`lang`, no explicit key needed). Re-verified after resolving: `stop-guessing`
(English), `ai-employee-zh`, and `one-person-business-zh` all still build
cleanly. CJK typesetting uses Noto Serif/Sans CJK SC (`fonts-noto-cjk` via
apt, OFL-licensed, resolved by fontconfig family name rather than vendored
as extracted `.ttc` faces) via `xeCJK`, with `\XeTeXlinebreaklocale "zh"`
for correct Chinese line-breaking, a translated `\contentsname`, and
translated box labels (关键洞察, 要点总结, 作者补充信息) and chapter-number
furniture (第N章), all gated behind `\if@kdpzh`, defined once, next to
each macro's English default, not in a separate trailing block.

**Build and visual verification.** Full build: `别再猜它有没有效`, **157
pages**, EPUB built cleanly (447 KB, valid), `qc.py --release`: 2 fail (the
required `verified: false` gate, and page count below the [180, 240] target
band), 1 warn (qc.py's page-count *estimator* reads as ~5pp for this book;
that estimator is word-count-based and not calibrated for Chinese text,
which has no whitespace word boundaries, so its pre-build guess is
meaningless here — the real, built page count is 157, confirmed from the
actual compiled PDF, not the estimator). Gutter margin correctly picked
0.5in for the 151-300 page band. Visually inspected, at 150dpi, the title
page, copyright page (byline, AI-disclosure line, ISBN placeholder), table
of contents, a chapter opener (第1章, correct blue rule and section
numbering), a KEY-INSIGHT box (关键洞察, correct green box and bilingual
source line), a PULLQUOTE (correct centered blue serif), a TAKEAWAYS box
(要点总结, correct blue box), a regular content table, an appendix
worksheet table, and the About the Author page (关于作者, last page,
faithful, unembellished translation of James Liu's real bio, no
AUTHOR-INPUT box). No tofu boxes, no missing glyphs, no overflow. LaTeX
log shows 35 `Overfull \hbox` warnings (all sub-2pt, cosmetic, and fewer
than the English build's 102) and the same `multiply defined` label
warning class the English build already has from repeated back-matter
headings across appendices, a pre-existing pandoc-anchor quirk, not
something this edition introduced.

**Honest shortfall, not padded.** 157 pages is below the [180, 240] target
band, the same situation the English byline rebuild hit this session (179
pages) after acknowledgments was removed. This is not a defect introduced
by the translation: CJK typesetting is inherently denser per page than the
Latin original at the same trim size and font size, and no content was
compressed or cut to make the translation fit. Flagging this honestly
rather than padding, consistent with this project's standing rule against
inflating page count with restated material. Left as an open item for the
author below.

**Files.** New: `books/stop-guessing/book-zh.yaml`,
`manuscript-zh/01-*.md` through `17-*.md`, `back-matter-zh/*.md` (6
files). Modified (backward-compatible, opt-in only):
`books/theme/kdp-book.cls`, `books/pipeline/book.py`,
`books/pipeline/build.py`.

**What's left, and only the author can do it:**
1. Read the full Chinese manuscript (`proofs/stop-guessing-zh.pdf`) and
   confirm the translation faithfully represents the book before treating
   it as a real second edition; `book-zh.yaml`'s `verified: false` is
   untouched and stays false until that happens, exactly like the English
   edition.
2. Decide whether the 157-page count (vs. the [180, 240] target) is
   acceptable for this edition, or whether it should be brought in line,
   the same open decision already pending on the English edition's
   179-page count.
3. Confirm actual upload targets and mechanics for Google Play Books,
   Apple Books, and any direct/lead-gen channel before distribution;
   nothing in this pipeline has touched those platforms' own submission
   requirements.
4. `book-zh.yaml`'s `isbn_note` reads "国际标准书号（ISBN）：[发布时分配]"
   (assigned at publication); a real ISBN, if one is obtained for this
   edition, needs to replace that placeholder before final release.

## 2026-08-11: English proofs rebuilt with the real author byline

Author directive: `book.yaml`'s `author` field and
`back-matter/about_the_author.md` were updated outside this session (by
the author, before this pull) to the real byline, "James Liu," with a
real, author-supplied bio (Silicon Valley and ByteDance AI product
experience, NUS Computing with distinction specializing in AI, a year at
Stanford). `back-matter/acknowledgments.md` was removed from
`book.yaml`'s `back_matter:` list in the same prior update. This session's
job was mechanical: rebuild the interior PDF and EPUB against the new
byline and confirm they render correctly, not to write any new author
content (none was invented, per standing instruction).

**Rebuild.** Full PDF and EPUB rebuild from the already-updated source.
**179 pages** (down from 181 in the last build, a direct, expected
consequence of removing the acknowledgments back-matter item, not a bug in
this rebuild). `qc.py --release`: 2 fail (`verified: false`, and the page
count now sitting 1 page below the [180, 240] band), 0 warn. Visually
confirmed the title page and copyright page carry "James Liu" correctly,
and the About the Author page (now the last page in the book, since
acknowledgments no longer precedes it) renders the real bio cleanly with
no `[AUTHOR-INPUT: ...]` box remaining.

**Honest shortfall, not padded.** The 179-page count is a direct
consequence of the author's own decision to drop acknowledgments, not
something this session introduced or should quietly correct by inflating
other chapters. Flagged here rather than fixed unilaterally, consistent
with this project's standing rule against padding page count with
restated material. The author should decide whether to accept 179 pages,
write a replacement back-matter piece, or expand a chapter that genuinely
has more to say.

**Committed** `proofs/stop-guessing.pdf` (the same author-requested
exception to the never-commit-`build/`-artifacts rule as the editorial
pass below), matching the byline in the rebuilt PDF.

## 2026-08-11 (editorial pass): manuscript complete, print-ready pending sign-off

Editor directive from the author: a full editorial pass over the finished
[180, 240]-page manuscript, structural and line edit, citation
verification, resolve any remaining `[AUTHOR-INPUT: ...]` the sanctioned
way, then ship a readable deliverable. `verified: false` was explicitly
**not** touched, per standing instruction; it stays false until the real
author reads the book end to end.

**Structural edit.** Read all 17 chapters and all 5 back-matter pieces in
full, in order, checking continuity, chapter numbering, cross-references,
and repeated material. Ran `grep -noiE "[Cc]hapters? (one|...|seventeen)"`
against every manuscript and back-matter file and manually checked every
match against the actual current chapter map; all resolved correctly, no
stale references survived the earlier renumbering pass. No padding found:
every chapter carries specific, non-repeated content, and the recurring
structural devices (`Say the honest caveat`, `Notice that...`, `Where this
goes next`) appear a handful of times across 17 chapters, consistent with
an intentional stylistic signature rather than filler.

**Line edit and proofread.** Installed `hunspell` + `hunspell-en-us`
temporarily (not normally installed in this environment, see the toolchain
note below) to run a real spellcheck pass, then manually reviewed every
flagged word. Found and fixed five genuine issues:
- Two British spellings that had slipped past the `en_US` style setting:
  "maths" -> "math" (twice, chapter 7) and "defence" -> "defense"
  (chapter 8).
- "judgement" -> "judgment" in `book.yaml`'s KDP description field (not
  part of the interior PDF, but still en_US-inconsistent).
- Two awkward word choices that read as errors on a close pass:
  "coverable" (chapter 7, reworded to "a task whose blast radius can't be
  bounded") and "checkpointed" (chapter 7's table, reworded to "even with
  a checkpoint added"), plus "informationally" in chapter 2, reworded to
  "purely to inform a homeowner's estimate."
Everything else hunspell flagged (Arup, Buolamwini, Gebru, Gerstner,
Nabla, Okafor, Timnit, Zillow, Zestimate, iBuying, chatbot(s), eval,
leaderboard, misclassifying, mistranscribe, offboarding, overcorrect(ion),
Recommender, asker's, data's, bootcamps) is a real proper noun or a real
English/tech word absent from the en_US dictionary, verified by hand, not
a typo. Uninstalled hunspell again afterward to restore `qc.py`'s
documented graceful no-op fallback, matching the "clean apart from the
verified gate" release bar and the shared-pipeline scope discipline held
throughout this project (growing the shared `ALLOW` list in
`books/pipeline/qc.py` is out of scope for a stop-guessing-only session).
Checked em dashes (`grep -rn "—"`, zero remaining), banned-tell phrases,
and double-space/repeated-word patterns across every file: clean.

**Citation verification.** All 30 `[KEY-INSIGHT: ...]` citations were
already live-searched at writing time across earlier sessions. For this
pass, re-verified six of the higher-risk ones live (specific quotes or
exact figures, where memory drift is most likely): the Klarna CEO quote
("we went too far... we focused too much on cost"), MD Anderson's
original "six-month, $2.4 million" IBM Watson pilot scope, Amazon's
hiring tool detail ("penalized graduates of two all-women's colleges"),
and the Microsoft Copilot CW1226324 bug (already triple-sourced when
written). All six confirmed accurate against multiple independent
sources. No corrections needed.

**`[AUTHOR-INPUT: ...]` markers.** `grep -rn "AUTHOR-INPUT" manuscript/`
returns zero matches: no chapter carries one, so there was nothing to
restructure per books/CLAUDE.md §1's sanctioned path (replace a personal
anecdote with verified research or the book's own running examples).
The only two markers left are in `back-matter/acknowledgments.md` and
`back-matter/about_the_author.md`, both structurally author-exclusive
content (a real name, a real thank-you list) that no research substitute
can honestly fill. Left both blocking, exactly as books/CLAUDE.md
sanctions ("Leaving it blocking the build is correct behaviour"), and
listed as a remaining author action below. `book.yaml`'s `author: "Your
Name"` placeholder is untouched for the same reason.

**Final release build.** Full PDF (181 pages, unchanged from the last
session's build; the line edits didn't shift the page count), EPUB
(valid zip, fonts embedded), `qc.py --release`: **1 fail, 0 warn**, only
the `verified: false` gate. Visually spot-checked front matter (half
title, title page, dedication, TOC), every chapter opener, and several
table/box pages across the full page range: all recto, all correctly
running-headed, no widow/orphan, no table overflow. Committed the
interior PDF to `proofs/stop-guessing.pdf`, a deliberate, author-
requested exception to the normal never-commit-`build/`-artifacts rule,
specifically so the author can read the finished interior directly on
GitHub without running the toolchain themselves. `build/` itself stays
gitignored and untracked.

**What's left, and only the author can do it:**
1. Read all 17 chapters end to end in `proofs/stop-guessing.pdf` (or
   rebuild from source) and set `verified: true` in `book.yaml` once
   every claim and anecdote is one they'd personally defend. This is the
   single remaining blocking gate.
2. Fill in `back-matter/acknowledgments.md` and
   `back-matter/about_the_author.md` with real content, and set a real
   `author:` in `book.yaml` in place of the "Your Name" placeholder.
3. Spot-check the fast-moving citations in
   `back-matter/notes_and_sources.md` immediately before upload; the
   Microsoft Copilot bug (Feb 2026) and the Gartner 2025 prediction are
   the two most likely to have moved further by print time.
4. Generate the KDP cover once the final page count (currently 181, may
   shift slightly if the author's own read prompts further edits) is
   locked, per books/CLAUDE.md §6.
5. Complete KDP's publishing-dashboard AI-disclosure questionnaire
   (AI-assisted, per the copyright page's existing disclosure line) at
   actual upload time.

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

## 2026-08-11 (later same day): closing the page-count gap with two untapped course sections

A checkpoint full build after every chapter above was expanded still landed at
**125 pages** against the `[180, 240]` target, a 55-115 page gap. Stretching
the four planned back-matter appendices far enough to close that gap alone
would have meant 14-21 real pages each, past the point where they'd still
read as genuine fillable worksheets rather than disguised extra chapters,
which is exactly the padding-by-a-different-route this expansion is not
supposed to do. The honest fix is more chapters, not longer appendices, and
two entire course sections have never been drawn on by this book at all:

- **Section 2, "Speaking Engineer Without Faking It"** (8 lectures): the
  prompt/RAG/fine-tune/agent decision tree, embeddings without the math,
  latency and the p95 conversation, and reading a benchmark table
  critically. Genuinely different material from anything chapters 1-10
  cover, and it's the vocabulary gap the book's own chapter 10 (Managing
  the Room) gestures at without ever teaching directly.
- **Section 5, "RAG and Knowledge Systems"** (10 lectures): why RAG exists,
  the pipeline stages, chunking decisions, retrieval quality metrics (hit
  rate, MRR, precision), and the six places RAG breaks in production
  including permissions and freshness. RAG is the single most common way a
  real AI feature reaches outside its own model, and this book had never
  once mentioned it by name.

Three new chapters, drawn from that material, inserted **after chapter 10
and before the closing sequence** (Objections, Field Notes, First Ninety
Days, Where This Breaks), which keeps the closing sequence's own internal
order and relationships intact and only pushes their numbers up by three:

| # | Title | Status |
| --- | --- | --- |
| 11 | Speaking Engineer Without Faking It | **new**, adapts 2.2, 2.3, 2.5, 2.6, 2.7 |
| 12 | Why RAG, and How to Measure It | **new**, adapts 5.1, 5.2, 5.3, 5.4 |
| 13 | Where RAG Breaks in Production | **new**, adapts 5.5, 5.6, 5.7 |
| 14 | Objections and Pushback | renumbered from 11 |
| 15 | Field Notes: Three Worked Case Studies | renumbered from 12 |
| 16 | The First Ninety Days | renumbered from 13 |
| 17 | Where This Breaks | renumbered from 14 |

Files: `11-objections-and-pushback.md` -> `14-...`, `12-field-notes-...md`
-> `15-...`, `13-the-first-ninety-days.md` -> `16-...`,
`14-where-this-breaks.md` -> `17-...` (all `git mv`'d in reverse order to
avoid collisions, history preserved). `book.yaml`'s `chapters:` list
updated to match, new chapters 11-13 filed with new manuscript filenames.

**Cross-references touched, found via
`grep -noE "[Cc]hapter (one|two|...|seventeen)" manuscript/*.md` before and
after, the same discipline the first renumbering pass established:**

- `02-seven-shapes.md`: "chapter thirteen's discovery sprint" -> "chapter
  sixteen's" (First Ninety Days moved from 13 to 16).
- `10-managing-the-room.md`: its closing "Where this goes next" used to
  describe old chapter 11 (Objections). Rewritten to describe the new
  chapter 11 (Speaking Engineer) instead, since that's what actually
  follows it now.
- `01-the-accountability-gap.md`: its closing roadmap paragraph named every
  chapter by ordinal word through "Fourteen, the last chapter." Rewritten
  to name all seventeen, inserting the vocabulary and RAG chapters in
  their real position between Ten and the renumbered closing sequence.
- The renumbered files themselves (now 14, 15, 16, 17): each chapter's own
  self-references to its neighbours and to "how many chapters this book
  has spent" bumped by three (e.g. old ch13's "turns twelve chapters of
  method" -> "turns fifteen chapters", old ch14's "spent thirteen
  chapters" -> "spent sixteen chapters"), and each "Where this goes next"
  transition re-pointed at its actual new neighbour.
- New chapters 11, 12, 13 each get their own "Where this goes next"
  closing the chain: 11 -> 12, 12 -> 13, 13 -> 14 (back to Objections,
  the room).

Re-ran the same grep after all edits landed to confirm no stale ordinal
survived; this is the second time this exact failure mode (a book that
cross-references itself by chapter number breaking silently on reorder)
has come up, and it will come up again if the outline changes further.

Gutter band is unaffected: midpoint of `[180, 240]` is still 210,
comfortably inside the 151-300 -> 0.5in band already documented above.

## 2026-08-11 (final): expansion complete, 181 pages, release-clean

The three new chapters landed the full book at 125 pages, still short of the
band. Rather than stretch the four appendices into disguised extra chapters,
wrote them at genuine worksheet length (instructions, a blank template, one
worked example using this book's recurring case, a closing checklist) and
added a fifth back-matter piece, `notes_and_sources`, collecting all 30
`[KEY-INSIGHT: ...]` citations from the 17 chapters by chapter, each with the
specific fact worth remembering and its full source. This is genuine,
useful reference material for a book that cites this many real, checkable
sources, not padding: an annotated bibliography is a standard nonfiction
convention, and it's the honest way to close the last few pages of a real
gap rather than re-inflating a chapter that was already complete at its
length. `book.yaml`'s `back_matter:` list now reads appendix A-D, then
`notes_and_sources`, then acknowledgments, then about-the-author.

Two build issues surfaced and were fixed while writing the appendices,
both scoped to the new files, no shared-pipeline changes:
- `- [ ] checklist` markdown syntax produces `\item[$\square$]`, which
  needs `amssymb` and isn't loaded by `kdp-book.cls`. Fixed by using plain
  `- ` bullets for every "before you call this done" checklist, matching
  the convention every other chapter in this book already uses.
- Appendix A's first draft used an 8-column worked-example table, which
  overflowed the 6x9 trim by up to 19pt in several cells. Fixed by
  dropping the redundant Bucket column (already encoded in the Case ID
  prefix) and shortening cell text; the same fix (shorter Notes-column
  text) resolved a smaller overflow in Appendix C's worked table. Checked
  via `grep -oP "Overfull \\\\hbox \(\K[0-9.]+(?=pt too wide)" master.log
  | sort -rn` after every rebuild; the two overfulls still over 20pt
  after the fix are both pre-existing, in chapter six's margin-trap
  table, unrelated to this session's changes, and out of scope to fix
  here.

**Final numbers:**
- Full PDF build: 181 pages (`[180, 240]` target). Gutter margin correctly
  0.5in for the 151-300pp band, confirmed by `qc.py --release`'s
  gutter-consistency check passing silently.
- EPUB build: valid zip, fonts embedded (`texgyreschola` regular/bold/
  italic/bold-italic as OTF), builds clean with no `--only` flag.
- `qc.py --book stop-guessing --release`: **1 fail, 0 warn** — only
  `verified: false`, the sign-off gate that is never mine to close.
- Total manuscript: 17 numbered chapters, 4 worksheet appendices, 1
  sources appendix, plus acknowledgments and about-the-author (both still
  genuine `[AUTHOR-INPUT: ...]`-gated stubs, correctly left blocking).

**What's left for the human author**, unchanged in kind from the original
handoff, larger in scope now that the manuscript is longer:
1. Read all 17 chapters end to end and set `verified: true` once every
   claim and anecdote is one they'd personally defend.
2. Fill in `back-matter/acknowledgments.md` and
   `back-matter/about_the_author.md` with real content; both are still
   `[AUTHOR-INPUT: ...]` stubs and will keep blocking `qc.py --release`'s
   sign-off gate until they are.
3. Decide on `author` in `book.yaml` (currently the placeholder "Your
   Name") and set a real one before any KDP upload.
4. Spot-check the roughly 30 live-searched citations in
   `back-matter/notes_and_sources.md` before publication; several
   describe fast-moving stories (a February 2026 Microsoft bug fix, a
   2025 Gartner prediction) that may have moved further by the time this
   book goes to print, exactly the currency caveat that section itself
   names.
5. Generate the cover once page count is locked at 181 (or wherever a
   final human pass leaves it), per `books/CLAUDE.md` §6: cover design is
   a separate, later step needing the final page count for spine width.

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
