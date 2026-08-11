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

## What's left, and it's all author-only by design

- Read the full English and zh manuscripts and set `verified: true` in
  `book.yaml` and `book-zh.yaml` separately (a sign-off on one edition
  does not carry over to the other). This is the author's signature, not
  a build step, and this session has correctly never touched it.
- Cover design for both editions (needs final page count, which is now
  locked: 185pp English, 167pp zh).
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
