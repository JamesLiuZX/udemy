# Status and chapter map

Not part of the build. Working notes for continuing this manuscript across
sessions, same pattern as books/stop-guessing/notes.md.

## Status — expansion in progress (author directive, mid-run)

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

### Revised outline

Chapters 01-10 keep their numbers and core argument; each is being
expanded in place (see "Expansion plan per chapter" below), not replaced.
Three new chapters are being added after them:

| Chapter | Addition |
| --- | --- |
| 11 Four Delegations, Worked in Full | New. Two extended, deep case studies (not the same small worked examples used inline elsewhere) that each run the *entire* method start to finish on one real business, showing how brief, trial, spot-check, failure-mode list, standing instruction, disqualifiers, roster, and chaining actually interact in one continuous story rather than one skill at a time. |
| 12 Objections and Edge Cases | New. FAQ-style chapter, real pushback argued honestly: "I don't have time to write a five-part brief," "the tool changed and broke my failure-mode list," "what about regulated work," "what if I don't trust AI at all," and similar. Each answer names the objection's real merit before answering it, consistent with "name the limit of the advice" already governing the rest of the book. |
| 13 Templates and Worksheets | New. Reference appendix, not narrative: the five-part brief template, the failure-mode list template, the roster template from chapter eight, the four-disqualifier worksheet from chapter seven, and a blank 30-day calendar page, laid out as literal fillable pages. No `[KEY-INSIGHT]`/`[PULLQUOTE]`/`[TAKEAWAYS]` expected here; it's reference material, not argument. |

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
- [ ] 06 Feedback That Actually Sticks
- [ ] 07 When to Fire It
- [ ] 08 Your Second Hire, and Your Third
- [ ] 09 The Team of One
- [ ] 10 A 30-Day Delegation Plan
- [ ] 11 Four Delegations, Worked in Full (new)
- [ ] 12 Objections and Edge Cases (new)
- [ ] 13 Templates and Worksheets (new)
- [ ] Full rebuild + EPUB rebuild + `qc.py --release` at the new target,
      gutter confirmed at 0.5in against the real page count.

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
