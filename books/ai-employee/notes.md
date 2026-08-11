# Status and chapter map

Not part of the build. Working notes for continuing this manuscript across
sessions, same pattern as books/stop-guessing/notes.md.

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

## What's left for the human author

- **Sign-off**: read the full manuscript and set `verified: true` in
  `book.yaml` yourself. Not something this session can or should do.
- **No `[AUTHOR-INPUT]` markers exist** to fill in — every chapter reached
  for `[KEY-INSIGHT]` instead, per the repo's stated preference. If a
  genuinely strong personal story exists for a specific moment in any
  chapter, swapping in a real `[AUTHOR-INPUT: ...]` is still an option,
  just not a requirement.
- **Back matter**: `book.yaml` lists `acknowledgments` and
  `about_the_author` in `back_matter`, but neither
  `books/ai-employee/back-matter/*.md` file exists yet (`build.py` skips a
  missing back-matter file silently rather than failing). These need the
  real author's own bio and acknowledgments; not written here for the same
  reason `[AUTHOR-INPUT]` markers aren't invented.
- **ISBN**: the copyright page currently reads "ISBN: [assigned at KDP
  publishing step]" (the class's own default placeholder), correct for
  where this manuscript is in the pipeline.
- **Cover**: out of scope for this pipeline per `books/CLAUDE.md` §6, a
  separate step once page count is locked.

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
