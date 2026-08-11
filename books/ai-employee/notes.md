# Status and chapter map

Not part of the build. Working notes for continuing this manuscript across
sessions, same pattern as books/stop-guessing/notes.md.

## Status — manuscript complete, release-gate clean

- All 10 chapters are written, built, and visually inspected (rendered
  pages checked for every chapter, not just compiled). None of the 10
  chapters use `[AUTHOR-INPUT: ...]`; every chapter's load-bearing evidence
  is a `[KEY-INSIGHT: claim || source]` instead, each one independently
  verified against a live web search at writing time, consistent with the
  repo's stated default for this book (`books/CLAUDE.md` §1,
  `books/docs/02-research-and-sourcing.md`). There is nothing blocking on
  `[AUTHOR-INPUT]` anywhere in the manuscript right now.
- Full build (`python3 books/pipeline/build.py --book ai-employee`): 69
  pages. EPUB build (`build_epub.py`): succeeds, 347 KB. Front matter,
  table of contents, and a chapter opener spread were all visually
  spot-checked in the full assembled PDF (not just the per-chapter
  `--only` renders) — running heads, recto chapter starts, and TOC page
  numbers all check out.
- `qc.py --book ai-employee --release`: **1 fail, 0 warn** — the single
  fail is `verified: false`, which is correct and must stay that way until
  the real author reads the whole thing and signs off. That is the only
  thing standing between this manuscript and being release-ready.
- `target_pages` was rebased from the initial guess of [120, 170] (the
  same placeholder stop-guessing started with) down to **[65, 90]**, once
  the real full-build page count (69pp, all 10 chapters, no back matter
  yet) was known. Same reasoning stop-guessing used: padding chapters to
  hit a number that was only ever a guess would violate the no-padding
  discipline the video course holds, so the target moved to match real,
  unpadded density instead. 69pp sits inside the 24-150 gutter band
  (0.375in) with room to spare even if back matter adds a few pages.
- Toolchain note: this session's environment had neither `pandoc`, a LaTeX
  toolchain, nor `hunspell` installed at the start. All were installed via
  `apt-get` (pandoc; texlive-xetex + texlive-latex-recommended +
  texlive-latex-extra + texlive-fonts-recommended + latexmk; hunspell +
  hunspell-en-us) before the first build. `qc.py`'s spellcheck silently
  no-ops when `hunspell` isn't on PATH, so any prior "qc.py clean" report
  for chapters 01-03 may not have actually run the spellcheck step. Once
  hunspell was installed, spellcheck flagged real words/names not in its
  en_US list (character names Priya/Renata, and words like "onboarding",
  "foodborne", "salesy", "disqualifiers"); these were added to `ALLOW` in
  `books/pipeline/qc.py`, the sanctioned extension point per that file's
  own comment, not worked around.

## What's left for the human author

- **Sign-off**: read the full manuscript and set `verified: true` in
  `book.yaml` yourself. Not something this session can or should do.
- **No `[AUTHOR-INPUT]` markers exist** to fill in — every chapter reached
  for `[KEY-INSIGHT]` instead, per the repo's stated preference. If a
  genuinely strong personal story exists for a specific moment in any
  chapter (chapter one's "vending machine" opener, or chapter seven's
  bakery scene, are both natural spots), swapping in a real
  `[AUTHOR-INPUT: ...]` is still an option, just not a requirement.
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

## Chapter map

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
