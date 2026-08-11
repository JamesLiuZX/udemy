# Status and chapter map

Not part of the build. Working notes for continuing this manuscript across
sessions, same pattern as books/stop-guessing/notes.md.

## Status

- Chapter 01 is written and verified-pending-signoff: built, rendered pages
  visually inspected, `qc.py` clean beyond the `verified: false` and
  `[AUTHOR-INPUT]` gates.
- Chapters 02 through 10 are outlined in `book.yaml` (titles, order) but the
  manuscript files do not exist yet. `build.py --only 01` works today; a
  full `--book ai-employee` build will fail until every listed chapter has
  a real file.
- `target_pages` starts at [120, 170], the same starting estimate used for
  stop-guessing before any chapter existed. Recalibrate against the real
  rendered page count once chapter 01 (or a few chapters) exist, the same
  way stop-guessing's target moved once real density was known. Don't pad
  chapters to hit a number that was only ever a guess.

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
