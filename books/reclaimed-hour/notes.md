# Status and chapter map

Not part of the build. Working notes for continuing across sessions, same
pattern as the other books.

## Status

- 2026-08-11: toolchain verified in this container (pandoc, texlive-xetex,
  latexmk, fonts-noto-cjk, texlive-lang-chinese all installed; chapter 01
  builds and visually inspects clean).
- 2026-08-11: outline expanded from 10 chapters to 19 and `target_pages`
  raised from `[110, 160]` to `[180, 240]`, matching this book's siblings
  (`ai-employee`, `stop-guessing`) at the same target band. The original
  10-chapter arc undershoots 180-240pp by roughly half at this book's prose
  density (chapters 1-2 run ~1,000-1,200 words each); rather than padding
  every chapter to an unnatural length, the outline gained nine new
  chapters that earn their place: a failure-pattern chapter, three worked
  case studies in full, a chapter for when the real problem isn't time at
  all, a measurement chapter, a manager/team-scaling chapter, an
  objections/FAQ chapter, and a worksheets chapter, alongside the two
  chapters that were already outlined but not yet drafted as files
  (`telling your team or family`, `a week in the reclaimed life`, both
  pushed later in the arc) and a new short closing chapter. See "Chapter
  map" below for the full new order. `book.yaml` and chapter 01's closing
  "Where this goes next" section are already updated to the new arc.
- Chapter 01 written and verified-pending-signoff: built, rendered pages
  visually inspected, `qc.py` clean beyond the standard gates.
- Chapter 02's `[KEY-INSIGHT]` citation, originally hedged ("original study
  attribution should be verified against the primary source before this
  figure is treated as precise"), has been re-verified and replaced with a
  properly sourced citation: Jiang, Park, Xiao & Zhang, "AI and the
  Extended Workday" (SSRN working paper, 2025), summarized in CEPR VoxEU.
  Note this is a working paper, not yet peer-reviewed as of this writing;
  flagged as such in `back-matter/notes_and_sources.md` too.
- 2026-08-11: all 23 chapters drafted (manuscript/01 through 23). The
  outline grew three times over one session: 10 to 19 chapters first (see
  the entry above), then two more rounds adding two chapters each (17
  "Choosing What to Automate With" / 18 "The Cost of Never Trying", then
  19 "What This Actually Costs" / 20 "Six Months Later") once successive
  full builds kept landing short of 180pp (113, then 123, then 129, then
  137, then 147pp) despite real within-chapter expansion each round.
  Every insertion before the closing trio (lapse-recovery, the week, the
  conclusion) forced a renumbering of that trio and a sweep for internal
  chapter-number references across the manuscript (`01`'s roadmap
  paragraph, `10`'s "named parts" aside, and every "Where this goes next"
  link touching a moved chapter) plus `book.yaml` and
  `back-matter/notes_and_sources.md`. Lesson worth keeping for the next
  book that needs a big page-count jump from a short original outline:
  new chapters converted to pages far more reliably than stretching
  existing chapters did (each carries its own chapter-opener overhead on
  top of real new content); if starting over, going straight to enough
  chapters to hit the target rather than iterating in small increments
  would have saved several rebuild-and-recount cycles. All 19
  `[KEY-INSIGHT]` citations (chapters without one: 16, 19, 21, 22, 23,
  matching the sibling books' pattern for worksheet/cost/case-study/
  closing chapters) were independently verified via live search before
  writing, full list in `back-matter/notes_and_sources.md`.
- 2026-08-11: full editorial pass complete. `qc.py --release` reports
  only the expected `verified: false` gate (a genuine pass, per
  `books/CLAUDE.md` §1: not a problem to fix, the author's signature).
  Fixed along the way: three filler/LLM-tell phrases ("at the end of the
  day", "obviously" x2) qc.py flagged; zero em dashes confirmed by grep
  (`style.em_dash: avoid`). One real compliance issue caught on visual
  spread review, worth flagging for future sessions on any book: several
  passages had drifted into claiming this book's composite, illustrative
  characters (Marcus, Devon, Priya, Owen, Grace, Ken, Sara, Theo) were
  sourced from real "interviews," "research," or "readers who tested"
  this book, none of which happened. That's a fabricated-sourcing claim,
  the same category of problem `[KEY-INSIGHT]`'s standard exists to
  prevent, just aimed at the book's own production process instead of a
  cited fact. Swept and fixed across chapters 3, 4, 5, 7, 11, 14, 15, 19,
  21 and `back-matter/discussion_guide.md`: removed every "interviewed
  for this book" / "research behind this book" / "readers who tested"
  claim, kept the same composite characters and case studies as plain
  illustrative examples (same device chapter 1's Rachel already used
  correctly, with no sourcing claim attached). Grep pattern worth reusing
  before any future book ships: `interview|this book's research|behind
  this book|readers who (tested|reported|said)|reader named`.
- 2026-08-11: English proofs shipped. Full build confirms 185pp (within
  180-240), fonts embedded (`pdffonts` confirms all 4 faces embedded +
  subset), gutter correctly at 0.5in for the 151-300pp band, TOC visually
  collision-free including three-digit page numbers, spreads spot-checked
  across front matter, multiple chapter openers, KEY-INSIGHT/PULLQUOTE/
  TAKEAWAYS boxes, a worksheet chapter, and back matter, all clean.
  `build_epub.py` produces a 434KB EPUB, spot-checked (nav/TOC order
  correct, 24 chapters present, zero em dashes, KEY-INSIGHT/PULLQUOTE
  markup present). Interior PDF committed to
  `books/reclaimed-hour/proofs/reclaimed-hour.pdf` per the author-
  sanctioned exception to the never-commit-builds rule; EPUB intentionally
  not committed (matches every sibling book's proofs/ directory, PDF
  only).
- 2026-08-11: Simplified Chinese edition shipped. `book-zh.yaml` (slug
  `reclaimed-hour-zh`, `lang: zh`), `manuscript-zh/` (all 24 chapters,
  translated idiomatically, not literally: recreated the English wordplay
  where it existed, kept product/tool names and typed-into-English-tools
  language in English, bilingual-glossed every KEY-INSIGHT citation's
  original-language title per the standard), and `back-matter-zh/` (all
  6 pieces, including notes/sources, discussion guide, quick-start,
  further reading, and the note on how the book was written).
  `target_pages` set to `[150, 190]` for this edition specifically,
  lower than the English `[180, 240]`: CJK setting at this trim runs
  denser per page, same precedent as `ai-employee-zh`'s own lower band.
  Builds at 167pp, within target.
  - Two real bugs caught and fixed during this pass, worth flagging for
    any future zh work in this repo: (1) straight double quotes typed
    directly in zh markdown, when adjacent to CJK characters with no
    Latin word-boundary spacing, defeat pandoc's `markdown+smart` open/
    close detection (its heuristic assumes Latin-script spacing) and
    both quote marks in a pair silently collapse to the closing glyph,
    dropping the opening one, in body text, chapter titles, and TOC/
    running heads alike; the fix is to type real curly quotes (“ ”)
    directly in zh source rather than relying on smart-quote conversion,
    the same convention `ai-employee-zh`'s manuscript already used. Swept
    and fixed across all 24 chapters plus back matter with a script that
    converts straight-quote pairs to curly ones specifically where at
    least one side touches a CJK character, deliberately leaving English
    citation titles (which have normal Latin spacing) untouched. (2) An
    em-dash-as-parenthetical habit crept into several chapters even
    though `book.yaml: style.em_dash: avoid` carries over to this
    edition; qc.py caught these directly (`--release` flags em dashes
    per chapter) and they were replaced with Chinese full-width
    parentheses or restructured sentences.
  - `qc.py --release` now reports only the expected `verified: false`
    gate, plus a benign warning: its word-count-based page estimate
    (used for pacing while writing) undercounts CJK text badly since it
    splits on Latin whitespace, which doesn't exist between Chinese
    words; the real, rendered page count (167pp, confirmed via
    `pdfinfo`) is what actually matters and is within band. Worth
    flagging in `books/pipeline/qc.py`'s own backlog if a future session
    wants to fix the estimator for CJK books generally, not specific to
    this title.
  - Spreads visually inspected across front matter, multiple chapter
    openers, KEY-INSIGHT/PULLQUOTE boxes, section headings with quoted
    terms (where the quote bug would have been most visible), and back
    matter; all clean after the fixes above. Fonts embedded (`pdffonts`
    confirms Noto Serif CJK + TeX Gyre Schola + IBM Plex Mono, all
    embedded and subset). Interior PDF committed to
    `books/reclaimed-hour/proofs/reclaimed-hour-zh.pdf`. No EPUB built
    for this edition: `build_epub.py` has no `lang: zh` support yet
    (hardcodes en-GB/en-US metadata), and no sibling zh edition in this
    repo has shipped one either; PDF-only matches precedent.
  - **KDP does not accept this edition.** KDP does not offer a Simplified
    Chinese paperback upload, and does not list Simplified Chinese as a
    supported Kindle eBook language (only Traditional Chinese, in beta,
    ebook-only). This edition targets Google Play Books, Apple Books, and
    direct/lead-gen distribution instead, the same channel decision every
    other zh edition in this repo has made.

- 2026-08-11: standards update applied, per the author's directive to
  adopt `docs/09-visual-standard.md` (the same visual-standard rewrite
  applied across courses and books). Three additions, all inherited by
  the zh edition as instructed:
  1. **The hook and the nugget** (docs/09 §4). Read all 24 chapters
     against the standard: a one-line hook (why a browser keeps reading
     past the first half page) and a golden nugget (the one concrete,
     usable-today thing). All 24 chapters passed on both counts without
     needing a rewrite — every chapter already opens on a concrete scene
     and already closes on an actionable `[TAKEAWAYS]` box, which turned
     out to already satisfy the standard. The one-line hook/nugget pair
     for every chapter is recorded in the chapter map below (see the
     "Hook" and "Nugget" columns). No chapter needed prose changes for
     this item.
  2. **Visual devices** (docs/09 §3). This book pipeline has no figures.py
     equivalent (no diagram/chart generator, no tikz, no image support in
     `kdp-book.cls`) so every worked visual is a markdown pipe table,
     rendered through the pipeline's existing booktabs styling (same
     mechanism already used once in this book's `book.yaml`-adjacent
     sibling `ai-employee` ch. 12's scoring table). Added exactly one
     worked visual to each of the 24 chapters, every one derived from
     that chapter's own already-published content, no new facts
     introduced: filled worksheets (ch. 3's audit log matches the
     standard's own example verbatim, ch. 4's flinch log, ch. 6's if-then
     plan, ch. 16's resentment-inventory entry), before/after and
     six-week trend grids (ch. 1, ch. 12, ch. 20), comparison tables
     across the book's recurring cast (ch. 5, ch. 7, ch. 9, ch. 10, ch.
     11, ch. 14, ch. 15, ch. 18, ch. 19, ch. 21, ch. 22), and ch. 23's
     day-by-day real-vs-counterfactual week grid, which matches the
     standard's own named example. English rebuilds at 213pp (was 185),
     zh at 183pp (was 167); both still comfortably inside their target
     bands (180-240 / 150-190).
  3. **SOTA rigor, concentrated** (docs/09 §4's "current tools" bar).
     This book is deliberately tool-agnostic by design (ch. 17 states
     the reasoning directly: naming products dates badly), so the pass
     was concentrated in ch. 17 rather than spread across all ~30 generic
     "an AI tool" mentions elsewhere, which stay generic on purpose since
     they describe a fictional persona's task, not a live recommendation.
     Live-searched (web search, August 2026) three tool categories
     relevant to the book's illustrative tasks — recurring-report/
     workflow automation (n8n, Zapier, Make), AI scheduling (Reclaim,
     Motion), and household meal-planning (Plan to Eat, Mealime, Samsung
     Food) — and added them as a dated, honestly-caveated table. One
     finding doubled as an unplanned demonstration of the chapter's own
     thesis: Clockwise, a scheduling tool with real market share in early
     2026, shut down in March 2026 after acquisition; the chapter now
     cites this directly as the real-world case for ch. 15's "what if the
     tool disappears" answer. Behavioral/psychological claims (every
     `[KEY-INSIGHT]`) were untouched — same highest-bar citation standard
     as before, no changes needed.
  - Two smaller issues caught during this pass, fixed in both editions:
    (a) two exact-duplicate section headings (ch. 20 had two sections
    both titled "Where each case actually stood, six months on"; ch. 21
    had two near-identically-titled "what automates" sections) — renamed
    the newly-added one in each case; (b) four pre-existing straight
    single-quotes in the zh manuscript (chs. 6, 7, 15) that touched CJK
    characters directly, the same class of bug documented above for
    double quotes — converted to curly quotes defensively, verified via
    a script that the only remaining straight quotes in `manuscript-zh/`
    are the expected English citation titles inside `Source:` lines.
  - Both editions rebuilt, `qc.py --release` clean apart from the
    expected `verified: false` gate (English) and that same gate plus
    the benign CJK word-count-estimator warning (zh, unchanged from
    before). Spreads visually inspected across roughly a dozen of the
    new tables in both languages, including the TOC (no duplicate/
    colliding entries), the ch. 3 and ch. 17 exemplar tables the
    standard specifically calls out, and a table split across a page
    break (renders with repeated headers, no overflow). Fonts still
    fully embedded in both. Proofs refreshed: `proofs/reclaimed-hour.pdf`
    (213pp) and `proofs/reclaimed-hour-zh.pdf` (183pp).

## What's left, and it's all author-only by design

- Read the full English and zh manuscripts and set `verified: true` in
  `book.yaml` and `book-zh.yaml` separately (a sign-off on one edition
  does not carry over to the other). This is the author's signature, not
  a build step, and this session has correctly never touched it.
- Cover design for both editions (needs final page count, which is now
  locked: 213pp English, 183pp zh).
- The KDP AI-disclosure and content-guidelines questionnaire for the
  English edition (listing sheet already drafted in
  `books/docs/03-kdp-listings.md` §8); no KDP questionnaire applies to
  the zh edition since KDP won't accept it.
- Decide and execute Google Play Books / Apple Books / direct
  distribution for the zh edition once its own sign-off is done.

## Why this book gets extra scrutiny, and what that changes

Self-help is the category `books/docs/00-kdp-compliance.md` §2 flags as
watched hardest by KDP, generic advice with no real credential or tested
experience behind it is the specific spam pattern being policed. This
book leans on `[KEY-INSIGHT: ...]` (real, cited research) rather than
`[AUTHOR-INPUT: ...]` anecdotes by the real author's own choice across
all six of these titles, which makes the sourcing bar in
`books/docs/02-research-and-sourcing.md` even more load-bearing here than
in the business-genre books. Do not let a chapter in this book ship with
a vague, uncited psychological claim ("studies show people feel better
when...") standing in for a real citation.

## The one idea

Every chapter should trace back to this: **automating a task does not
reclaim the hour it used to take. It only frees that hour up to be
recolonized by something else, usually more work, unless the freed time
is deliberately protected.** The reclaiming is a behavioral and
psychological project, not a technical one. A book that stopped at "use
AI to save time" would be indistinguishable from the hustle-productivity
genre this book is deliberately positioned against; the behavioral half
(chapters 2, 5, 6, 7 especially) is what actually makes it a different
book.

## Chapter map

| Chapter | Core idea |
| --- | --- |
| 01 The Hour You Already Lost | Naming the pattern: automate, feel briefly relieved, watch the relief evaporate within a week |
| 02 Why "Just Automate It" Doesn't Work | The core mechanism: freed time gets recolonized by default, not by choice |
| 03 The One-Hour Audit | Practical exercise: finding where time actually goes, not where you assume it goes |
| 04 Automating the Task You Resent Most | Starting point selection, resentment as the signal to follow |
| 05 The Guilt of Having Free Time | Psychological chapter: busyness as identity, why free time feels wrong at first |
| 06 Protecting the Hour Once You Have It | Boundary-setting against the hour being recolonized |
| 07 What You Actually Wanted the Time For | Values clarification, reconnecting with the original point of free time |
| 08 When AI Makes It Worse, Not Better | Honest limits: notification overload, always-available expectations AI can create |
| 09 Common Ways the Hour Gets Recolonized | Pattern chapter: the mechanisms from ch. 2 shown in six real recolonization scenarios |
| 10 Three Hours, Reclaimed in Full | Three composite case studies followed start to finish, worked in full |
| 11 When It's Not Actually About Time | The rarer, harder case: the scarcity was never really the hour, it was something the busyness was protecting the reader from |
| 12 Measuring What You Actually Reclaimed | A lightweight weekly check: how to tell if any of this is actually working |
| 13 The Reclaimed Hour at Work | Scaling the idea past one person: what changes when you're the one modeling it for a team |
| 14 Telling Your Team or Family What Changed | Communicating the new boundary to the people affected by it |
| 15 Objections and Edge Cases | The honest pushback this book hasn't already answered, addressed directly |
| 16 The Templates | Worksheet chapter: the audit, the resentment inventory, the boundary scripts, the weekly review, collected in one place |
| 17 Choosing What to Automate With | Practical tool-selection mechanics; choice-overload research |
| 18 The Cost of Never Trying | The other failure mode: status-quo bias keeping an already-identified fix unstarted for years |
| 19 What This Actually Costs | Honest accounting in money and setup time, not just hours; break-even arithmetic |
| 20 Six Months Later | Longer-horizon check-in on every case in the book; habit-formation research |
| 21 When the Work Isn't a Job at All | The method applied to unpaid household and caregiving labor; cognitive-labor research, and its one honest limit |
| 22 Revisiting an Hour You Lost Again | Relapse is normal, not failure: what to do the week the hour gets away from you again |
| 23 A Week in the Reclaimed Life | Closing: a concrete week, practical and specific, not an abstract promise |
| 24 Conclusion: What You Do With the Time Now | Short closing chapter, the one question the whole book has been building to |

## Hook and nugget, per chapter (docs/09-visual-standard.md §4)

All 24 passed on both counts as originally drafted; none needed a rewrite.
Applies to the zh edition too (same chapters, translated).

| Ch. | Hook (why keep reading past half a page) | Golden nugget (the usable-today thing) |
| --- | --- | --- |
| 01 | Rachel's ninety minutes vanish the same week they're freed, and nobody made her stay | An empty hour needs a decision made about it, actively, or it defaults to whatever's nearest |
| 02 | A 160-year-old economics observation about coal explains exactly why Rachel's Friday refilled itself | Name which of three mechanisms (task expansion, standard creep, availability creep) is eating your freed hour |
| 03 | A confident operations manager guesses his week wrong by nineteen points | Log every task switch in the moment for five days; the category you didn't list going in is usually where the time is |
| 04 | The smallest item on the list gets automated first, on purpose | The flinch test beats raw time spent as a signal for what to automate first |
| 05 | Forty minutes of silence feels like getting away with something | Name your guilt as status, identity, or comparison, then apply the matching fix |
| 06 | A nine-day-old automation is gone by week six, one friendly yes at a time | Write a three-part if-then plan before the request arrives, not during it |
| 07 | A sister's blunt question stops a two-month streak cold: what do you actually do with it? | If the direct question stalls, ask what you did with free time before, what a fully clear day looks like, or what you'd be embarrassed to admit wanting |
| 08 | A manager's compliment ("more bandwidth now") is the trap arriving with a name and a face | Keep freed time invisible until it's protected, and budget real review time as the actual cost |
| 09 | A pattern behind the patterns: six specific doors an hour walks through | Run the end-of-week checklist naming which door took the time |
| 10 | Three ordinary jobs, one identical six-step arc, none of it a clean win | Write your own audit finding, chosen task, guilt flavor, and honest purpose in four sentences |
| 11 | Sometimes the hour isn't taken, it's given away, fast, on purpose | If a protected hour still feels specifically bad no matter how much practice, that's a signal for a therapist, not a script |
| 12 | Three months of "mostly, I think so" turns out to mean nothing stuck | Run four questions weekly, written down and shared; a downward trend is the real signal |
| 13 | Two employees start leaving at 5:45 without ever being told they could | Make your protected block visible, not just real, or your team learns nothing |
| 14 | The identical boundary fails on a random Wednesday, lands instantly at the start of a quarter | Anchor any announcement to a real landmark, in three parts: what's changing, why, what stays the same |
| 15 | The honest rebuttal to twelve chapters of advice, taken on directly | Use the audit to test whether a workload genuinely has no slack before concluding this doesn't apply |
| 16 | Every worksheet in this book, stripped out of the stories and left ready to use | Fill in your own version directly rather than paraphrasing from memory |
| 17 | Three weeks lost comparing tools before a single one gets tried | Pick three options, test against a real task, set a decision deadline before you start |
| 18 | A sister with the identical time-drain, three years unautomated, agreeing the whole time | A forced choice, a real deadline, and one small first exposure break a status-quo default |
| 19 | The honest line-item a book this long owes its reader, in dollars and setup hours | Do the break-even arithmetic before committing setup time to anything |
| 20 | Every case study so far has shown weeks, not the longer haul that actually proves anything | Judge a practice on a six-month horizon, not a six-week one |
| 21 | The biggest share of one parent's week isn't a task at all, it's tracking | Anticipating a need resists automation almost entirely; name who's tracking what, out loud |
| 22 | A five-month streak breaks for two weeks, and the story you tell about it matters more than the break | Name a lapse factually, diagnose which door caused it, restart at the next landmark |
| 23 | A real week, wobble included, close to a year after the audit that started it | The weekly check is what catches a three-week drift before it becomes a three-month fixture |
| 24 | Back to Rachel, the same question asked once more now that there's an actual answer | The real measure of success is one hour, somewhere in your week, you can name as genuinely yours |

## Things to hold onto while writing the rest

- Never let this collapse into a productivity-hack book. The test for
  every chapter: could this exact chapter have been written by a hustle-
  culture productivity book with "AI" find-and-replaced in? If yes,
  rewrite it.
- Chapter 08 (honest limits) is non-negotiable per
  `books/CLAUDE.md`'s writing rules, doubly so in self-help specifically.
  Do not let it shrink to a token paragraph.
- Keep sentences short, second person, concrete scenes, same discipline
  as the other books, but this one can sit with discomfort a beat longer
  than the business-genre books do; self-help earns a slightly more
  reflective pace in places, especially chapters 5 and 7.
