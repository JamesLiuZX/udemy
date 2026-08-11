# Status and chapter map

Not part of the build. Working notes for continuing this manuscript across
sessions, same pattern as books/stop-guessing/notes.md.

## 2026-08-11: Chief Quality Editor pass (hook/nugget, SOTA, visual devices)

Same mandate and method as books/stop-guessing/notes.md's entry of the
same date. This book's citations were already live-verified in the recent
editorial pass, so lens B here re-checked only the eight time-sensitive
ones; the deep work was hooks (the back half opened on abstraction) and
worked visuals (fourteen chapters had none).

### Who this book's reader is

A non-technical professional or small-business owner/manager with a
repetitive task and no patience for hype: broader and less
jargon-tolerant than stop-guessing's PM. They already own people-management
instincts (briefing, trials, feedback, firing); the book's job is aiming
those instincts at a tool. Audience check found and fixed the handful of
lapses: "hallucination" now glossed at first use (ch1), "chain API calls"
replaced with plain speech (ch9), "SKU" glossed (ch11), "train a model"
glossed (ch12), "zero-shot" removed (ch21).

### Hook and golden nugget, per chapter (file order)

| Ch | Hook | Nugget |
| --- | --- | --- |
| 01 | Two people, same week, same tool, opposite verdicts, both wrong | Five-question audit of your own last failed AI attempt |
| 02 | Listen to yourself train a hire vs prompt a tool | Write the five-part brief once per recurring task, reuse it |
| 03 | Two managers, two first assignments for a new hire | Four criteria, five attempts, log each in a few words |
| 04 | Maria's 340 line items, checked three wrong ways | Name the seam, check it 100%, sample the rest lightly |
| 05 | Devon's one tool, two jobs, two different failure patterns | A written failure file per task: what/how often/when |
| 06 | Priya's weekly fight with "stunning" and "must-see" | Rewrite the complaint as a rule; save it where the tool looks |
| 07 | The review alleging Renata's cake made someone sick | The four-disqualifier checklist on one running task |
| 08 | Marcus checks the newsletter's seam on the insurance notes | The one-page roster; two checks before any new task |
| 09 | Ola's chain laundered one invented number into a mailing | Map the chain, collapse fake steps, human read at each seam |
| 10 | Jamie's blank note titled "AI: Week One" | The four-week one-page calendar |
| 11 | Bianca's four-word brief comes back generic (opener rebuilt this pass) | The whole method in one continuous story; the comparison table |
| 12 | Naomi's eleven browser tabs of tool roundups | The memory test: correct it, open a new chat, check survival |
| 13 | The client caught it, not the coordinator | One team standard: shared brief, named seam, spoken disclosure |
| 14 | "Nine minutes between site visits and a phone that autocorrects brief to brie" (opener new this pass) | The complacency test: earned trust has a written record |
| 15 | (reference appendix, renders last; no hook by design) | Every template in the book as fillable pages |
| 16 | The confident yes that arrives before the question ends | Two-week total-time log against an honest baseline |
| 17 | The faucet handle vs the leak under the sink (opener new this pass) | Guess the failure pattern before the trial; score your guess |
| 18 | Ingrid's calendar entry for a task she fired (opener new this pass) | Two lines on every fired task: revisit date + what failed |
| 19 | Three businesses, nothing in common, same fix underneath (new) | Match by task shape, not industry; the six-row table |
| 20 | The order eleven times too large that tripped no boundary (new) | Name each tool's shape; write the agent's allowed actions |
| 21 | The quote 30% under cost that read perfectly clean (new) | Reconcile one number against source, ninety seconds |
| 22 | Yusuf, eighteen months of "about to try AI" | Four pre-trial criteria only; deliberation isn't evidence |
| 23 | Back to the two people from chapter one | The honest two-list success metric (kept vs deliberately human) |
| 24 | The testimonial drafts nobody quoted ever approved (new) | The reasonable-person test before anything client-facing |

### What changed this pass

- **Openers rebuilt on eight chapters** (11, 14, 17, 18, 19, 20, 21, 24):
  each had a strong concrete scene sitting mid-chapter and opened on
  abstraction or book-machinery instead; the scene was promoted per
  docs/04 §3's cold-open rule. No new facts introduced anywhere.
- **Missing pullquotes added** (14, 17, 19), each pulled verbatim from
  body text per the house rule. Ch15 stays pullquote-free by design
  (reference matter).
- **Worked visuals added to eleven chapters** (02, 04, 06, 13, 14, 17,
  18, 19, 20, 21, 22, 24), every one a compression of the chapter's own
  existing material: before/after pairs (02, 06, 21), worked comparison
  tables (04, 13, 18, 20, 22), reference tables (14, 17, 19, 24). Ch23
  (conclusion) deliberately left visual-free: a table would undercut the
  closing register, and the reference apparatus lives in ch15. All
  inspected in the rebuilt PDF.
- **Time-sensitive citations re-verified live (8 of 27)**: EU AI Act
  Article 14 gained the July 2026 Digital Omnibus timing hedge
  (enforcement for most high-risk systems deferred to Dec 2027 / Aug
  2028; the requirement itself intact); the S&P Global abandonment
  survey's stated reasons were wrong (actual reported obstacles: cost,
  data privacy, security; not "poor fit / unclear value") and are fixed
  in both places; the FTC fake-review penalty updated from the 2024 cap
  ($51,744) to the current one (over $53,000, inflation-adjusted, 2026
  adjustment cancelled); METR's follow-up status added (redesigned in
  early 2026; the 19% figure remains the best measured result). Glean
  botshitting, ErrorMap v2, OECD SME data, and both JPMC figures
  confirmed unchanged. The one uncited research claim outside a box
  (ch13, why employees hide AI use) tied to its actual source.
- Rebuilt: EN PDF **191pp** (inside [180, 240]) + EPUB; qc --release
  clean apart from the sign-off gate; spellcheck ALLOW grown with five
  hand-verified words. zh edition mirrored (all openers, tables,
  pullquotes, citation fixes), zh PDF rebuilt and inspected, proofs
  recommitted.

Judged NOT worth fixing, and why: ch2/ch3's imperative/hypothetical
openers (concrete within a paragraph; rewriting would trade one good
opening for another); a data-generated figure anywhere in this book (its
numeric material is illustrative worked examples, not datasets; tables
carry them honestly, and a chart would imply measurement that doesn't
exist); ch16's conversational-trap opener (lands within the half page).

Still the author's alone: verified: true, byline back-matter items
already listed in the section below.

## Status — Simplified Chinese edition shipped (159pp), English proofs rebuilt with byline

Two author directives landed after the editorial pass closed the English
edition out at 187pp: (1) set the real byline, James Liu, replacing the
`"Your Name"` placeholder, and drop the placeholder acknowledgments file
in favor of the real About the Author bio the author supplied; (2)
translate the complete book into Simplified Chinese as a second edition.
Both are done. Detail below; short version:

**English proofs rebuilt.** `book.yaml`'s `author` is now `"James Liu"`,
`back-matter/about_the_author.md` carries the real bio he supplied
(not embellished), `back_matter` no longer lists `acknowledgments`.
Rebuilt: 189 pages (within [180, 240]), `qc.py --release` clean apart
from the sign-off gate, EPUB TOC has 28 correctly-titled entries with no
Acknowledgments leftover. Title page, copyright page, and the About the
Author page all visually confirmed. `proofs/ai-employee.pdf` recommitted.
Also fixed one real leftover bug the byline pass surfaced: chapter 11's
closing line still said "underneath both stories" from before the
expansion pass added a third and fourth case study; now reads "all four
stories," in both the English chapter and its zh translation.

**Simplified Chinese edition shipped, as a second, parallel book.**
`book-zh.yaml` (slug `ai-employee-zh`) is a sibling config to `book.yaml`,
not a variant of it: same design system, same four bracket devices, same
`build.py`/`qc.py` pipeline, driven by `lang: zh`, its own
`manuscript-zh/` and `back-matter-zh/` source trees. Full chapter-by-
chapter translation, not a summary: every paragraph, table, KEY-INSIGHT/
PULLQUOTE/TAKEAWAYS box, and citation in all 24 chapters plus both
back-matter files.

- **Typesetting mechanism: reused, not reinvented.** Mid-build, the
  `one-person-business` session independently landed its own `[zh]`
  option on this same shared `books/theme/kdp-book.cls`, a few minutes
  ahead of this one. Per the standing rule for shared-file work
  (coordinate through git, reuse an already-landed mechanism rather than
  ship a second, incompatible one), this session discarded its own
  from-scratch draft (which had vendored two extracted CJK OTF faces
  under `theme/vendor/fonts-cjk/`, since removed) and rebuilt on top of
  theirs after `git pull --rebase`: `book.py` gained a `Book.lang`
  property; `build.py` picks `[zh]` up from it automatically and resolves
  back matter from a `back-matter-<lang>/` directory when one exists
  (falls back to `back-matter/` otherwise, so every English-only book is
  unaffected); `book-zh.yaml` sets `back_matter_titles` to override the
  printed section titles for `notes_and_sources`/`about_the_author`. CJK
  fonts are **not vendored** under their approach: `apt-get install -y
  fonts-noto-cjk texlive-lang-chinese` puts `Noto Serif/Sans CJK SC` on
  the system font path, and `xeCJK` finds them by family name, no `Path`/
  `Extension` fontspec options needed the way the Latin faces use. Their
  box-label and copyright-line Chinese strings match what this edition
  needed too, so no further class changes were required there.
- **One real bug found in their mechanism and fixed as a shared
  improvement**, benefiting both zh editions: `\if@kdpzh\renewcommand{
  \contentsname}{目录}\fi`, placed directly in the class preamble, looked
  correct but silently lost to babel: babel's `[english]` option
  re-applies its own caption strings (`\contentsname` included) via
  `\select@language` at `\begin{document}`, which runs *after* anything
  set earlier in the class file and so wins. First render of this
  edition's table of contents printed "Contents" in English despite the
  override; confirmed by testing, fixed by wrapping the same
  `\renewcommand` in `\AtBeginDocument{...}`, which queues it to fire
  after babel's own hook instead. Rebuilt and confirmed "目录" prints
  correctly; this also silently fixes the same latent bug in
  `one-person-business-zh.pdf`'s table of contents, worth a rebuild there
  too.
- **A real, previously-latent build.py bug**, fixed earlier in this same
  editorial pass and unrelated to the zh work: back matter's chapter/
  section title used to come only from a hardcoded Python dict keyed by
  filename slug, not from the back-matter file's own `# Title` line the
  way chapter titles already work. `back_matter_titles` (the
  one-person-business session's override mechanism, adopted here too)
  composes cleanly with that fix: the dict is still the source of the
  printed title, `back_matter_titles` is a per-book override on top of
  it, and English behaviour is unchanged when a book doesn't set one.
- **Translation quality control**, beyond the individual translation
  passes: a full punctuation audit across all 26 zh files caught two real
  defects a first read missed -- chapter 6 used half-width ASCII
  punctuation throughout instead of full-width Chinese punctuation
  (retranslated from scratch with explicit instructions), and chapter 18
  used straight ASCII quote marks instead of curly Chinese quotes
  (fixed with a script that alternates open/close curly quotes while
  protecting the citation portion of every KEY-INSIGHT box and every
  `back-matter-zh/notes_and_sources.md` entry's trailing italic
  citation, since those stay in their original English form on purpose).
  A second full-book scan after both fixes found zero remaining
  half-width-punctuation or straight-quote instances. Also caught and
  fixed: `notes_and_sources.md`'s section headers read "Chapter N:" in
  English instead of "第N章："; a book.yaml YAML folded-scalar (`>-`)
  quirk that silently inserted a literal space into the copyright page's
  rights/AI-disclosure text at the point I'd wrapped the line, rewritten
  as unwrapped single-line strings; and one inconsistent Chinese term for
  the coined survey word "botshitting" between its in-chapter KEY-INSIGHT
  box and its `notes_and_sources.md` entry, aligned to match.
- **The copyright page's rights/AI-disclosure/ISBN text is translated**,
  not left defaulting to English: `book-zh.yaml` sets its own
  `rights_note`, `ai_disclosure_text`, and `isbn_note` fields (build.py
  otherwise falls back to English-only defaults). The AI-assistance
  disclosure line especially needed this: it is the compliance-critical
  sentence books/CLAUDE.md SS1 requires, and it has to actually be
  readable by this edition's reader, not silently left in English because
  no one overrode the default.
- **KDP will not take this edition.** Live-checked (not assumed): KDP's
  own "Book Supported Languages" help page and its paperback PDF-upload
  path list English, French, German, Italian, Portuguese, Spanish,
  Catalan, Galician, and Basque only; Chinese does not appear for print
  at all. Chinese (Traditional) exists only as a beta *eBook* language,
  with no Simplified Chinese eBook or paperback support found anywhere in
  KDP's current documentation. Multiple KDP Community threads from 2021
  through 2024 ask why Simplified Chinese still isn't supported, with no
  resolution. This edition is not a KDP upload by design: the interior
  PDF (this proof) targets other print/distribution channels, and the
  same manuscript-zh/ source could feed Google Play Books or Apple Books
  through an EPUB path later (not built this pass; only the PDF proof was
  requested) or a direct/lead-gen PDF sale, none of which share KDP's
  language restriction.
- **Target pages recalibrated to reality**, the same way the English
  edition's was earlier: Chinese typesets measurably denser than English
  at equivalent content (full-width punctuation and no inter-word spaces
  both compress line length), so the same manuscript that runs 189pp in
  English renders at 159pp in Chinese. `target_pages` set to `[150, 190]`
  to bracket the real count; the word-count-based pre-render estimate in
  `qc.py` (`~6pp estimated`) is a known, harmless false positive for any
  CJK book, since it splits on whitespace and Chinese has none between
  characters -- the real page count from the built PDF, not that
  estimate, is what actually gates `--release`.
- **Release build**: 159 pages, within [150, 190], gutter correctly at
  0.5in (151-300pp band), `qc.py --release` clean apart from the
  sign-off gate (hunspell is skipped entirely for `lang: zh` books,
  since it isn't CJK-aware and would either flag the whole manuscript or
  nothing at all). All fonts embedded and subset. Rendered spreads
  visually inspected: title page, copyright page, table of contents,
  chapter 1's opener and its KEY-INSIGHT/PULLQUOTE boxes, the four-column
  case-study comparison table in chapter 11, the templates chapter's
  worksheet layout, Notes and Sources, and About the Author.
  `proofs/ai-employee-zh.pdf` committed, same deliberate exception to the
  never-commit-`build/` rule as the English proof.

## Status — expansion complete, target reached (185pp, within [180, 240])

The author raised the target from a tight [65, 90]pp field guide to a
substantially fuller **[180, 240]pp** book. Previous state (10 chapters,
69pp, release-gate clean at the old target) is preserved in git history;
this section tracks the expansion, not a restart.

**The expansion rule, absolute:** grow through substance, never padding.
No restating a point in more words, no inflated prose, no drop in
information density. If a chapter is complete at its current length, the
book grows by adding a new chapter, not by bloating that one. Every added
worked example is a genuinely new, distinct scenario, not a rephrasing of
the existing one. Every added `[KEY-INSIGHT]` is independently verified
against a live search at writing time, same standard as the first pass,
and only added where it strengthens a claim already made, not stapled on
to hit a page count.

**Gutter band mechanic**: `book.py`'s `margins()` picks the gutter from
`target_pages`'s midpoint before a real page count exists, and from the
real rendered page count once `build.py` has actually run (`gutter_for_pages()`
in `books/pipeline/book.py`, table in `book.py:GUTTER_BANDS`). There is no
separate hand-set "pages-band" class option to touch in `kdp-book.cls`
itself; raising `target_pages` to [180, 240] (midpoint 210) already moved
the pre-render guess to the 151-300 band, 0.5in, confirmed via
`Book.margins()`. The real, final gutter locks in on the first full
rebuild once the actual page count is known; `qc.py --release` checks the
built PDF's actual gutter against `gutter_for_pages(real_pages)` and fails
if a stale 0.375in survives a rebuild that crossed the 150pp line.

### Revised outline (updated after measuring real density)

Chapters 01-10 keep their numbers and core argument; each has now been
expanded in place per the plan below, not replaced. With all 10 done, a
full rebuild measures **82pp real** (front matter ~8pp + ~74pp of
chapter content, 20,134 words, ~272 words/page actual density once
KEY-INSIGHT/PULLQUOTE/TAKEAWAYS box whitespace and chapter-opener spacing
are counted, well below the raw 320wpp estimator). That's real,
information-dense progress, not padding, but three chapters alone can't
close a ~100-150pp gap to [180, 240] without either bloating individual
chapters unnaturally long or, correctly, adding more chapters at the same
honest density the first ten established. Expanded to five new chapters
plus a reference appendix chapter, all serving genuine, non-overlapping
reader needs rather than existing to hit a page count:

| Chapter | Addition |
| --- | --- |
| 11 Four Delegations, Worked in Full | New. Two extended, deep case studies (not the same small worked examples used inline elsewhere) that each run the *entire* method start to finish on one real business, showing how brief, trial, spot-check, failure-mode list, standing instruction, disqualifiers, roster, and chaining actually interact in one continuous story rather than one skill at a time. |
| 12 Choosing Your First Tool | New. Practical, tool-agnostic evaluation criteria for picking an AI tool to start with, deliberately not a brand endorsement or a feature comparison that dates within a year: what to check before trusting a vendor with real work (memory/standing-instruction support, data handling, cost structure at real usage volume), consistent with the book's tool-agnostic rule from chapter one. |
| 13 When Your Team Delegates Too | New. Extends the method past the solo reader: what changes when you're not just delegating to AI yourself but teaching direct reports to do the same, including the new failure mode of an employee blindly trusting AI output and presenting it as their own verified work. |
| 14 Objections and Edge Cases | New. FAQ-style chapter, real pushback argued honestly: "I don't have time to write a five-part brief," "the tool changed and broke my failure-mode list," "what about regulated work," "what if I don't trust AI at all," and similar. Each answer names the objection's real merit before answering it, consistent with "name the limit of the advice" already governing the rest of the book. |
| 15 Templates and Worksheets | New. Reference appendix, not narrative: the five-part brief template, the failure-mode list template, the roster template from chapter eight, the four-disqualifier worksheet from chapter seven, a blank 30-day calendar page, and a short glossary, laid out as literal fillable pages with real blank space, which legitimately adds page count at low word density the way a genuine workbook appendix does. No `[KEY-INSIGHT]`/`[PULLQUOTE]`/`[TAKEAWAYS]` expected here; it's reference material, not argument. |

Progress tracker below still lists the original three-chapter numbering
as items to convert; treat "11-13" there as "11, 14, 15" and the two new
insertions (12, 13) as additional rows, updated as each is written.

### Expansion plan per chapter (01-10)

Each chapter gets, where it genuinely earns it (not mechanically all of
the below in every chapter):

- A second worked example, a genuinely distinct scenario from the
  chapter's existing one, integrated into the argument rather than
  tacked on at the end.
- A closing "Try this" exercise or checklist the reader can act on
  immediately, placed before `[TAKEAWAYS]`.
- A second `[KEY-INSIGHT]` only where a second, independently verified
  source materially strengthens a claim already being made (the
  sourcing standard's "one well-chosen citation is the target, not a
  ceiling" still governs; this is not "every chapter gets exactly two").

Progress (updated per chapter as expansion happens):

- [x] 01 The Delegation Problem — added a third worked example (Ravi,
      management thinking applied from day one instead of as a repair),
      a second `[KEY-INSIGHT]` (OpenAI's own "Why Language Models
      Hallucinate" paper, backing the "structural, not a bug" claim), and
      turned the "five-minute check" into an explicit checklist. 2,397 ->
      2,932 words. Rendered pages checked.
- [x] 02 Writing the Job Description — added a second worked example
      (Dana, a weekly hardware-store inventory report, showing the
      five-part brief applied to a non-conversational task) and a second
      `[KEY-INSIGHT]` (the BRIDGE clinical-LLM benchmark on few-shot vs.
      zero-shot across 95 models, backing "the concrete example does more
      work than the other four combined"), plus a "Try this" exercise.
      1,284 -> 1,836 words. Rendered pages checked.
- [x] 03 The Trial Task — upgraded the vague "aggregated... summaries"
      `[KEY-INSIGHT]` to a real, precise primary study (a 2025
      quasi-experimental onboarding study, 200 nurses/assistants, three
      hospitals), added a second worked example (Farrah, a five-attempt
      trial on nonprofit thank-you letters that surfaces a specific,
      fixable gap), and a two-part "Try this" worksheet (criteria
      scorecard + five-attempt run log — confirms blank markdown tables
      render cleanly as fillable pages, useful for chapter 13). 1,156 ->
      1,590 words. Rendered pages checked.
- [x] 04 Checking the Work Without Redoing It — added a second
      `[KEY-INSIGHT]` (Mackworth's classic 1948 vigilance-decrement study,
      backing the previously-uncited "reviewer fatigue" claim), a second
      worked example (James, apartment-maintenance triage, a keyword-level
      seam rather than a category mix-up), and a "Try this: name your
      seam" exercise. 1,597 -> 2,147 words. Rendered pages checked.
- [x] 05 Learning Its Failure Modes — added a second worked example
      (Simone, one task tested across two different newsletter-writing
      tools, the mirror case of Devon's one-tool-two-tasks story) and a
      "Try this: start the file" worksheet. No second `[KEY-INSIGHT]`
      added deliberately: a checklist-length citation search turned up
      only loosely-fitting matches, and forcing a stretched citation in
      would violate the sourcing standard rather than serve it. 1,540 ->
      1,915 words. Rendered pages checked.
- [x] 06 Feedback That Actually Sticks — added a second `[KEY-INSIGHT]`
      (Locke & Latham's goal-setting research, backing "write it as a
      rule, not a complaint"), a second worked example (Malik, six months
      of stacked, never-edited standing instructions actively making
      output worse), and a "Try this: audit your standing instructions"
      exercise. 1,361 -> 1,931 words. Rendered pages checked.
- [x] 07 When to Fire It — added a second worked example (Teodora, a
      financial advisor whose two months of rigorous, correct effort
      still didn't converge on bond-allocation rebalancing notes,
      illustrating criterion four without a rushed process), a second
      `[KEY-INSIGHT]` (Zillow Offers' 2021 shutdown after removing human
      override from its pricing algorithm, illustrating criterion three
      at scale), and a "Try this" disqualification-checklist worksheet.
      1,587 -> 2,254 words. Rendered pages checked.
- [x] 08 Your Second Hire, and Your Third — added a second `[KEY-INSIGHT]`
      (Gallup's 200,000-team span-of-control research, backing the span-
      of-control claim with real numbers), a second worked example
      (Priyanka, a five-task roster actively deciding against adding a
      sixth), and a "Try this: start your roster" worksheet. 1,376 ->
      1,829 words. Rendered pages checked.
- [x] 09 The Team of One — added a second `[KEY-INSIGHT]` (Boehm's classic
      software-engineering defect-cost-escalation research, backing why
      checking at each seam beats checking only at the end), a second
      worked example (Desmond, a seven-step chain cut to three once the
      review overhead itself became the problem), and a "Try this: map
      your chain" worksheet. 1,499 -> 2,004 words. Rendered pages checked.
- [x] 10 A 30-Day Delegation Plan — added a second worked example (Owen,
      a property manager whose week-three disqualifier check correctly
      says no to part of his first task, showing that outcome is the plan
      working, not failing) and a fillable "Your thirty days, on one
      page" calendar worksheet. No second `[KEY-INSIGHT]`: this closing,
      synthesis chapter leans on the method already established rather
      than introducing new evidence. 1,369 -> 1,696 words. Rendered pages
      checked.
- [x] 11 Four Delegations, Worked in Full — new chapter, later corrected:
      the title promised four cases but only shipped two (Bianca, Hector)
      in the first pass. Added case three (Wren, an insurance agent's
      quiet, undramatic success) and case four (Cleo, a hot-sauce
      producer whose task took longest to stabilize because it was
      genuinely two tasks) to actually deliver on the title, updated the
      comparison table to four columns and the closing synthesis to cover
      all four. One `[KEY-INSIGHT]` (JPMorganChase Institute's
      small-business AI adoption data). 2,750 words, 9pp standalone.
      Rendered pages checked.
- [x] 12 Choosing Your First Tool — new chapter. Five durable,
      tool-agnostic evaluation questions (memory/persistence, real cost
      at volume, data handling, honest hedging, workflow fit) instead of
      a ranked list that goes stale within a season. One `[KEY-INSIGHT]`
      (S&P Global's 2025 enterprise AI abandonment survey) and a "Try
      this: score your candidates" worksheet. 1,550 words, 6pp
      standalone. Rendered pages checked.
- [x] 13 When Your Team Delegates Too — new chapter. The new failure mode
      that only appears once a second person is delegating (Wanda's
      marketing agency; an unverified AI draft reaching a client), a
      team-scaled version of the brief/seam/disclosure skills, and the
      manager's role shifting to spot-checking the team's checking. One
      `[KEY-INSIGHT]` (Glean's 2026 "Work AI Index" on "botshitting"), a
      second worked example (the norm catching a real error three months
      later), and a team-standard worksheet. 1,681 words, 6pp standalone.
      Rendered pages checked.
- [x] 14 Objections and Edge Cases — new chapter. Twelve real objections
      argued honestly (time, model drift, regulated work, distrust of AI
      on principle, team disagreement, feeling like overkill, a past bad
      experience, sensitive data, "won't AI just improve," a
      company-mandated tool, "isn't this just common sense," telling
      earned trust from complacency, an ever-growing failure-mode list),
      each conceding real ground rather than a strawman. One
      `[KEY-INSIGHT]` (the EU AI Act's Article 14 human-oversight
      requirement, backing the regulated-work answer with real, current
      law). 1,594 words, 7pp standalone. Rendered pages checked.
- [x] 15 Templates and Worksheets — new chapter. Ten copyable templates
      (brief, trial log, seam worksheet, failure-mode list, standing-
      instruction audit, disqualifier checklist, roster, chain map, tool
      scorecard, team standard, 30-day plan) plus a short glossary, all
      reference material, no `[KEY-INSIGHT]`/`[PULLQUOTE]` by design.
      844 words but 8pp standalone: worksheets are meant to be
      low-word-density, real blank space, not padding. Found and fixed a
      real pipeline bug while building this: pandoc's default 72-column
      heuristic picks non-wrapping table columns for tables whose header
      row is short even when a body cell's text is long, which overflowed
      the page margin (both here and in chapter 12's identical table).
      Fixed by passing `--columns=40` to every pandoc chapter conversion
      in `books/pipeline/build.py`, forcing consistent wrapped/proportional
      table columns; re-verified every table-bearing chapter in the book
      (01, 08, 11, 12, 15) still renders correctly after the change.
- [x] 16 Measuring What Delegation Actually Saves You — new chapter,
      inserted before the templates appendix. One `[KEY-INSIGHT]` (METR's
      2025 RCT on developers self-reporting AI made them faster while
      measured 19% slower), a worked example (Renaldo measuring two tasks
      and firing the one that only felt efficient), and a two-week
      time-log worksheet. 1,160 words, 5pp standalone. Rendered pages
      checked. Note: chapter ordering fix — book.yaml list order (not the
      `id` field) controls displayed chapter order, so "15 Templates and
      Worksheets" was repositioned to the end of the `chapters:` list
      without a file rename; see the comment left in book.yaml.
- [x] 17 Common Failure Patterns Across Task Types — new chapter.
      Synthesizes the book's own examples into five patterns by task
      shape (writing/drafting, categorization/triage, scheduling,
      research/summarization, chains), a new organizing lens rather than
      new anecdotes. One `[KEY-INSIGHT]` (IBM's 2026 ErrorMap/ErrorAtlas
      taxonomy across 73 models, on omission/misinterpretation being as
      common as fabrication). 1,078 words, 5pp standalone. Rendered pages
      checked.
- [x] 18 Revisiting a Fired Task — new chapter. Pays off chapter seven's
      promise that firing isn't permanent: a calendar-based, six-month
      revisit habit, a real fresh trial rather than a memory check, the
      expectation that most revisits confirm the original firing, and a
      worked example (Ingrid, a coverage-term task fired then genuinely
      revived a year later). No new `[KEY-INSIGHT]` box; leans on chapter
      nine's already-cited METR capability-growth research for its
      rationale instead of citation fatigue. 956 words, 4pp standalone.
      Rendered pages checked.
- [x] 19 Six Businesses, One Method — new chapter. Six fast vignettes
      (boutique clothing, HVAC contractor, independent bookstore,
      residential real estate, yoga studio, paralegal support) each
      showing a genuine first task and its real, narrow seam, proving the
      method isn't specific to the deeper examples used elsewhere. One
      `[KEY-INSIGHT]` (OECD's Dec 2025 SME AI-adoption-by-sector data).
      1,073 words, 4pp standalone. Rendered pages checked.
- [x] 20 Not All AI Tools Are the Same Kind of Tool — new chapter.
      Distinguishes three shapes of AI tool (general chat assistant,
      narrow purpose-built tool, action-taking agent) and how briefing,
      checking, and firing apply differently to each, especially agents
      needing a pre-action checkpoint rather than a post-draft one. A
      worked example (Odalys running all three shapes across different
      tasks). No new `[KEY-INSIGHT]`; this chapter reorganizes and
      extends the method itself rather than resting on a new external
      claim. 1,022 words, 4pp standalone. Rendered pages checked.
- [x] 21 What Changes When the Task Involves Money — new chapter. Why
      financial tasks carry a fundamentally different risk (money already
      moved, not just time to fix), raw arithmetic as a structural weak
      point, reconciliation against an independent source instead of
      internal-consistency spot-checking, and a stricter reading of
      chapter seven's disqualifiers. One `[KEY-INSIGHT]` (Dziri et al.
      2023's GPT-4 multiplication-accuracy findings, honestly hedged as
      dated but structurally still relevant), a worked example (Felix's
      furniture-quoting task and the underpriced quote reconciliation
      caught). 1,008 words, 4pp standalone. Rendered pages checked. This
      is the last new substantive chapter before the templates appendix.
- [x] 22 The Cost of Never Trying — new chapter. Names the risk the
      book's own caution can create if it's the only lesson taken: using
      chapter seven's disqualification logic (which governs whether to
      keep running a task you've tried) as an excuse to never run chapter
      three's cheap trial in the first place. One `[KEY-INSIGHT]` (reused
      JPMorganChase Institute report, a different specific stat: new-
      business AI adoption cohorts reaching 10% in 6 months vs. 6+ years
      for 2019-founded firms), a worked example (Yusuf, eighteen months
      of correctly-reasoned deliberation resolved in one afternoon). 949
      words, 4pp standalone. Rendered pages checked.
- [x] 23 Conclusion: The Manager You're Becoming — new chapter, a genuine
      capstone the book lacked (chapter 10 closed the original 10-chapter
      arc tactically; this closes the now much longer book thematically).
      Returns to chapter one's two opening people, names the single
      orientation underneath all twenty-two chapters, and states plainly
      what the book asked the reader to give up (a "set and forget" tool,
      a category-level verdict on AI) and what actually measures
      progress. No `[KEY-INSIGHT]`; a synthesis chapter, not a new claim.
      1,065 words, 4pp standalone. Rendered pages checked. Sits between
      chapter 22 and the templates appendix.
- [x] 24 Explaining This to Clients and Customers — new chapter, placed
      before the conclusion. External-facing disclosure, distinct from
      chapter thirteen's internal team disclosure: the "would a
      reasonable person feel misled" line, why routine reviewed
      communication doesn't need a disclosure but a testimonial or
      firsthand account attributed to a specific person does. One
      `[KEY-INSIGHT]` (the FTC's AI enforcement policy and its 2024 fake-
      review rule). 885 words, 4pp standalone. Rendered pages checked.
      Chapter order is now ...22, 24, 23 (conclusion), 15 (templates,
      last); ids don't need to match position, see the book.yaml note.
- [x] 15 Templates and Worksheets — expanded with four more templates
      matching the new chapters (revisit tracker for ch18, agent
      pre-action checkpoint for ch20, financial reconciliation checklist
      for ch21, disclosure decision for ch24) plus two glossary entries
      (reconciliation, revisit). 844 -> 1,145 words, 8 -> 10pp standalone.
      Genuine low-word-density reference growth, not padding; also
      improves cohesion between the new chapters and the appendix.
      Rendered pages checked, no overflow issues.
- [x] Chapters 17 and 19 — added closing "Try this" exercises
      (previously the only two substantive chapters without one).
      170pp after this pass. Rendered pages checked.
- [x] Cross-reference audit and fix, all chapters — every "Where this
      goes next" and internal chapter citation from chapter 14 onward
      pointed at the manuscript file's `id` rather than the book's real
      rendered chapter number, which diverge once chapter 15 (Templates)
      moved to the end of `book.yaml`'s list. Recomputed the correct
      rendered number for every forward/backward reference (14, 15, 16,
      17, 18, 19, 20, 21, 22, 23) including the parenthetical chapter
      tags and glossary entries inside chapter 15 itself, and fixed all
      of them. This was a real, previously-shipped defect, not new
      content; worth flagging to the human author as something to spot-
      check on the full read-through.
- [x] Chapters 20, 21, 22, 24 — added closing "Try this" exercises,
      matching every other substantive chapter. 176pp after this pass.
      Rendered pages checked.
- [x] Second worked examples for chapters 16, 18, 20, 21, 22 (which had
      shipped with only one, unlike chapters 1-13) and a first worked
      example for chapter 24 (which had none): Soo-ah (ch16, the
      opposite-direction measurement case to Renaldo's), Odalys's
      relationship-dependent task that correctly keeps failing its
      revisit (ch18), Odalys's agent near-miss that set her reorder
      threshold (ch20), Farrah's judgment-call reimbursement task (ch21,
      the disqualifier-1 case the chapter's stricter reading promised but
      hadn't shown), Malik's opposite failure to Yusuf's, skipping the
      trial rather than never starting it (ch22), and Wanda's client-
      testimonial disclosure decision (ch24). 176pp, no page-count change
      from this pass alone (the exercises above already claimed the
      gained pages; this pass is pure density, not padding). Rendered
      pages checked. Two typos added to `ALLOW` (malik's, renaldo's,
      soo), one UK spelling slip (cancelled -> canceled) fixed.
- [x] Notes and Sources back-matter appendix — new
      `books/ai-employee/back-matter/notes_and_sources.md`, registered in
      `book.yaml`'s `back_matter` list ahead of acknowledgments/about-the-
      author. Collects all 27 `[KEY-INSIGHT]` citations from every
      chapter, grouped by chapter with a one-sentence recap and the full
      citation, following the same pattern already established in
      `books/stop-guessing/back-matter/notes_and_sources.md`. Genuine
      nonfiction back matter a real published book in this category
      would carry, not padding: a reader who wants to verify or chase a
      claim now has one place to find it. **185pp — inside the [180,
      240] target range.**
      Building this surfaced a real, previously-latent bug in the shared
      `pandoc_backmatter()` in `books/pipeline/build.py`: a back-matter
      `\chapter*` doesn't advance memoir's chapter counter or call
      `\chaptermark`, so any `##` heading inside a back-matter file was
      numbering its sections off whatever real chapter preceded it (a
      stray "24.17 Chapter 1: ..."), and the recto running head kept
      showing the previous real chapter's title straight through the
      whole appendix instead of "Notes and Sources". Fixed both: back-
      matter headings now render unnumbered (`\section*`/`\subsection*`),
      and `\chaptermark` is called explicitly after `\chapter*`. Shared
      file also used by `stop-guessing`'s four appendices and its own
      Notes and Sources page, so this fix benefits that book too — worth
      flagging if that session's already-rendered PDF needs a rebuild to
      pick it up. Also added a `notes_and_sources` entry to `build.py`'s
      back-matter `titles` dict so the chapter heading reads "Notes and
      Sources" rather than Python's `.title()` default "Notes And
      Sources".
- [x] Full rebuild + EPUB rebuild + `qc.py --release` at the new target.
      **185 pages, inside [180, 240].** Gutter confirmed locked at 0.5in
      (the 151-300pp band) against the real, final page count, `qc.py
      --release` reports the band correctly with no stale-gutter failure.
      `qc.py` (both plain and `--release`) reports only the sign-off gate,
      no warnings. EPUB builds cleanly (436 KB). This closes the author's
      mid-run directive: the book grew from 69pp/10 chapters to
      185pp/24 chapters plus a Notes and Sources appendix, entirely
      through genuine, non-redundant substance — new chapters, new
      worked examples, new citations, worksheet appendices, and a
      sources appendix, never restated prose or inflated padding.

### Sizing math behind the plan

Pre-expansion: 10 chapters, 15,166 words, real full-build page count 69pp
(word-count estimator undercounts real pages by roughly 1.45x once
`[PULLQUOTE]`/`[KEY-INSIGHT]`/`[TAKEAWAYS]` box whitespace and chapter-opener
spacing are counted, per `book.py`'s plain word/320wpp estimator vs. the
actual rendered PDF). To land inside [180, 240]pp real, targeting roughly
42,000-50,000 total words across 13 chapters: existing chapters roughly
double to 2,500-3,500 words each with real added substance, the two new
narrative chapters (11, 12) at roughly 3,500-4,500 words each, chapter 13
lighter on prose (worksheet format) but still a real page count from
layout. Check actual word/page count after each chapter and adjust the
remaining ones rather than front-loading a rigid per-chapter quota.

## Status — full editorial pass complete (187pp, print-ready apart from sign-off)

Per the author's editorial directive: a full structural edit, line edit,
citation re-verification, and release build, with the manuscript now
reduced to a single remaining author action (read and sign off). Full
detail in "The editorial pass" section below; short version:

- Read all 24 chapters plus front and back matter in rendered order.
  Fixed a real continuity defect: chapter 9 and chapter 10 both still
  called chapter 10 "the final chapter"/"this book", leftover framing
  from before the expansion added 14 more chapters after it. Chapter 10
  now gets its own "Where this goes next" transition into chapter 11.
- Re-audited every `chapter <word>` cross-reference across the whole
  manuscript against the actual rendered chapter numbers (the id-vs-
  list-order mapping documented below). All clean; no further
  mislabeled references found beyond the ones already fixed in the
  prior expansion pass.
- Confirmed zero `[AUTHOR-INPUT]` markers exist anywhere in the
  manuscript, `book.yaml`, or back matter. Item 3 of the editorial
  directive (resolve every remaining `[AUTHOR-INPUT]` the sanctioned
  way) needed no action: there was nothing left blocking.
- Live re-verified all 27 `[KEY-INSIGHT]` citations (two parallel
  research passes, one per half of the book, plus direct follow-up
  searches on anything flagged). Found and corrected six real issues:
  - **Ch. 11 (& the matching Notes and Sources entry)**: the
    JPMorganChase "1.7% in 2019" figure was actually the *female-owned
    firms* subgroup baseline, silently blended with what read as a
    topline "17.7% by 2025" figure. Rewrote using the report's real,
    verifiable numbers: male-owned firms 2%→19.7%, female-owned
    1.7%→17.2%, and employer vs. non-employer firms 26.1% vs. 15.3% by
    2025 (a gap that widened since 2023, not the vaguer "meaningfully
    higher" the original claimed).
  - **Ch. 17 (& Notes and Sources)**: the ErrorMap/ErrorAtlas citation
    said "21 datasets and 73 models," which was the arXiv v1 figure;
    the paper has since been revised and the live arXiv link now shows
    35 datasets and 83 models. Updated both to match what a reader
    checking the citation today will actually see.
  - **Ch. 7 (& Notes and Sources)**: the Zillow KEY-INSIGHT dated its
    whole citation "November 2021," but the $881M full-year loss figure
    wasn't reported until Zillow's Q4 earnings release in February
    2022. Split the citation to date each figure correctly.
  - **Ch. 2 (& Notes and Sources)**: the BRIDGE benchmark claim's
    specific "95.8% of models improved, two-thirds by over 20%" figures
    could not be independently confirmed against the primary paper or
    any secondary coverage found live. Replaced with two directly
    confirmed data points instead (Gemini-1.5-Pro +27%, DeepSeek-R1
    +16%, few-shot vs. zero-shot), and softened the surrounding prose's
    "held across ninety-five different models" claim to match.
  - **Ch. 3**: softened "significantly higher on every measured
    competency" to "across the measured competencies" — the underlying
    study's exact per-competency breakdown wasn't independently
    confirmable, "significantly higher overall" was.
  - **Ch. 9 (& Notes and Sources)**: softened Boehm's "order of
    magnitude at each stage" to the source's actual range (roughly 4x
    to 100x depending on project size) rather than implying a clean,
    uniform 10x.
  - Everything else (21 of 27 citations) checked out as accurately
    cited on live re-verification, no changes needed.
- One real, previously-latent pipeline bug found and fixed in
  `books/pipeline/build_epub.py`, shared across every book using this
  pipeline: `build_master_html()` and `back_matter_html()` both
  hand-rolled an `<h1>{title}</h1>` in front of each chapter/back-matter
  file's own pandoc-converted HTML, but every one of those files already
  opens with its own `# Title` markdown heading that pandoc converts to
  an `<h1>` on its own. With `--epub-chapter-level=1`, that meant every
  single chapter and back-matter section produced two `<h1>`s and
  therefore two entries in the EPUB's nav/TOC (confirmed: the built
  EPUB had 52 nav entries for a 27-section book, with inconsistent
  title casing and apostrophe escaping between the two duplicate
  copies). Removed the redundant hand-rolled heading in both functions;
  rebuilt EPUB now has exactly 27 correctly-titled, non-duplicated nav
  entries. This fix applies to every book built with this pipeline, not
  just this one.
- Full release build: **187 pages**, inside the [180, 240] target.
  `qc.py --release` clean apart from the sign-off gate. Gutter confirmed
  locked at 0.5in (151-300pp band) against the real page count. All
  fonts embedded (`pdffonts` confirms 3 embedded/subset TeX Gyre Schola
  faces, no external font references). EPUB rebuilds cleanly (both
  before and after the nav-duplication fix). Rendered spreads visually
  inspected: title page, copyright page, table of contents, every page
  touched by a citation rewrite, both new chapter-10/chapter-9
  cross-reference fixes, and the Notes and Sources appendix.
- Interior PDF committed to `books/ai-employee/proofs/ai-employee.pdf`,
  a deliberate, author-requested exception to the never-commit-`build/`
  rule, so the author can read it directly on GitHub without running
  the pipeline locally. `build/` itself remains gitignored and
  untouched by this exception.

## What's left for the human author

Reduced to a single blocking action plus three genuinely author-only
housekeeping items; everything else the editorial pass could resolve
has been resolved.

- **Sign-off (the one blocking item)**: read
  `books/ai-employee/proofs/ai-employee.pdf` end to end and set
  `verified: true` in `book.yaml` once every claim and every anecdote
  is one you can personally defend. Not something this or any session
  should do on the author's behalf; it is the signature that keeps the
  KDP AI-assisted declaration true.
- **Byline**: `book.yaml`'s `author:` field is still the literal
  placeholder `"Your Name"`. Left untouched per the editorial
  directive; replace it with the real author name before publishing
  (it flows into the copyright page, title page, and EPUB metadata
  automatically on the next build).
- **Back matter**: `book.yaml` lists `acknowledgments` and
  `about_the_author` in `back_matter` alongside the new
  `notes_and_sources` (now written and shipped). Neither
  `acknowledgments.md` nor `about_the_author.md` exists yet
  (`build.py`/`build_epub.py` both skip a missing back-matter file
  silently rather than failing, which is why the book still builds
  clean without them). These need the real author's own bio and
  acknowledgments; not written here for the same reason
  `[AUTHOR-INPUT]` markers are never invented.
- **KDP dashboard questionnaire**: at upload, KDP will ask directly
  whether the book is AI-generated or AI-assisted. Per
  `books/CLAUDE.md` §1 this is AI-assisted (author direction, outline,
  and required sign-off review, not autonomous generation) — answer
  accordingly; the copyright page's disclosure line already says this
  in the book itself.
- **ISBN**: the copyright page currently reads "ISBN: [assigned at KDP
  publishing step]" (the class's own default placeholder), correct for
  where this manuscript is in the pipeline.
- **Cover**: out of scope for this pipeline per `books/CLAUDE.md` §6, a
  separate step once page count is locked (it now is, at 187pp).

## The core device

Every chapter should cash out the same central metaphor: an AI tool doing
a delegated task is a fast, eager, occasionally overconfident new hire who
has read everything and has zero judgment about your specific situation.
That's the whole book. Each chapter is one piece of ordinary people
management, applied to that hire: writing the job description, running a
trial, checking work without redoing it, knowing its specific tells,
giving feedback that sticks, and knowing what never to hand off. Reach for
management vocabulary the reader already owns before reaching for AI
vocabulary they don't.

## Chapter map (see "Revised outline" above for the current, full version)

| Chapter | Core idea |
| --- | --- |
| 01 The Delegation Problem | Vending-machine trust vs. management trust; why both over- and under-trusting AI come from the same mistake |
| 02 Writing the Job Description | A prompt is a job description: context, constraints, examples, what "done" looks like |
| 03 The Trial Task | How to pick the first task: small, recurring, low-stakes, easy to check |
| 04 Checking the Work Without Redoing It | Spot-checking technique; the trap of blind acceptance vs. redoing everything yourself |
| 05 Learning Its Failure Modes | Every task/tool pair has characteristic failures; build a specific mental performance review, not a generic AI-limitations list |
| 06 Feedback That Actually Sticks | Saved instructions, system prompts, memory features, correcting standing instructions instead of restarting from scratch |
| 07 When to Fire It | The disqualification checklist: judgment calls, relationship-dependent tasks, error costs too high, error rate that never comes down |
| 08 Your Second Hire, and Your Third | Scaling to several delegated tasks without losing track of your own systems |
| 09 The Team of One | Chaining simple steps together (research, then draft, then format) without turning into a coding book |
| 10 A 30-Day Delegation Plan | Week-by-week plan from zero to a small working portfolio; closing checklist |
| 11 Four Delegations, Worked in Full | New: two full, extended case studies running the whole method start to finish |
| 12 Objections and Edge Cases | New: FAQ-style chapter, real pushback argued honestly |
| 13 Templates and Worksheets | New: reference appendix, the book's templates as fillable pages |

## Things to hold onto while writing the rest

- Tool-agnostic on purpose. Never anchor an example to one specific app's
  UI, that's exactly the content that goes stale first and dates the book
  within a year.
- `[AUTHOR-INPUT: ...]` markers want a specific delegated task that went
  right or wrong for the real author, not a generic anecdote. One or two
  per chapter, load-bearing ones only.
- Keep the register different from stop-guessing: shorter sentences,
  broader audience, less jargon tolerance. A reader here has not opted
  into "PM vocabulary" the way the stop-guessing reader has.
