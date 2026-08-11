# Growth automations

Paste-ready prompts implementing `docs/06-growth-engine.md` §4. Every job ends
at a review queue, never at a publish button. See that doc for the schedule,
the channel strategy, and the list of things deliberately not automated.

## Layout

```
growth/
  prompts/     One prompt file per job. The contract each job runs against.
  queue/       Job output awaiting human review. Gitignored.
  data/        Inputs you drop in (KDP report exports, pasted reviews). Gitignored.
  facts.yaml   Registry of decay-prone claims per lecture (freshness sentinel).
```

## Running a job

**Local cron + Claude Code CLI:**

```cron
# Mon 07:00 repurpose, daily 08:00 mine questions, Fri 16:00 freshness
0 7 * * 1  cd ~/udemy && claude -p "$(cat growth/prompts/repurpose-lecture.md)"
0 8 * * *  cd ~/udemy && claude -p "$(cat growth/prompts/question-miner.md)"
0 16 * * 5 cd ~/udemy && claude -p "$(cat growth/prompts/freshness-sentinel.md)"
```

**Claude Cowork / Claude Code web:** create a scheduled session (a routine)
per job whose prompt is "Follow growth/prompts/<job>.md in the udemy repo."
Use Cowork with a browser for the engagement digest: it can read the Udemy
instructor dashboard the way you would.

## The rule

Nothing in `queue/` goes public without a human reading it. The queue is
organised by ISO week (`queue/2026-W33/…`); delete a week's folder once
processed. If a job's output ever feels safe to skip reviewing, tighten the
prompt instead of skipping the review.
