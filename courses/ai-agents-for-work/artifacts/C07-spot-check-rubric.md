# Spot-Check Rubric

*From AI Agents for Your Job. Use once an agent has moved from Trial to the Review rung (Section 1.2) — the checks that keep running after trust is granted, not before.*

## Sampling rule

Check a fixed share of runs, not a vibe. A reasonable starting point:

| Agent's volume | Sample |
| --- | --- |
| Daily | One run a week, chosen at random, not the easiest-looking one |
| Weekly | Every run, until you have twelve logged with no failure |
| On demand | One in five, or after any change to the prompt |

## The five questions, every sampled run

1. **Facts**: does every fact in the output actually appear in the source data? Nothing invented?
2. **Scope**: did the agent stay inside the scope from its job description?
3. **Ceiling**: was the ceiling respected? No action it wasn't allowed to take?
4. **Tone**, where relevant: would you be comfortable if a client or your director saw exactly this?
5. **Drift**: does this look different from how the agent behaved a month ago, for no reason you can name?

## Scoring

- **Pass**: all five, no notes needed
- **Watch**: passes, but something is worth a second look next time (name it)
- **Fail**: any invented fact, scope breach, or ceiling breach, regardless of how minor it looks

## What a Fail actually means

One Fail does not mean the agent is broken. It means:

1. Log exactly what went wrong and why, in plain language
2. Move the agent back to Trial for that specific failure mode until you understand the cause
3. Do not quietly patch the prompt and move on without re-testing against the case that failed

## The habit this rubric protects

Spot checks do not stop once trust is earned. They get less frequent. An agent you have not checked in two months is not an agent you trust, it is an agent you have stopped watching. Those are different things, and the difference is where Section 8's incident happened.

---
*Part of the AI Agents for Your Job artifact set. C08, the guardrails worksheet, is the next layer: what an agent can never do, regardless of what a spot check catches after the fact.*
