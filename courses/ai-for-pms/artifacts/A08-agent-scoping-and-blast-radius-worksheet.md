# A08 · Agent Scoping and Blast-Radius Worksheet

Part of *AI Product Skills for PMs & Analysts*. Delivered in lecture 6.8, the
workshop, and built from lectures 6.1 to 6.7. Use it to scope one proposed
agent before anyone builds it, so that the people who would build it, approve
it and be woken by it can see exactly what it may do and who stops it.

---

## 1. How to use this

1. **Pick one real automation idea.** Something you have genuinely considered
   handing to an agent. The refund case this section keeps returning to is a
   fine choice if nothing else comes to mind.
2. **Set a twenty-minute timer.** The bar is complete, not perfect: every
   question answered with something. Where the honest answer is a guess, label
   it a guess so it never reads as more certain than it is.
3. **Work down in order.** Suggested pacing: 4 minutes on section 1, 4 on
   sections 2 and 3, 4 on sections 4 and 5, 5 on section 6, 3 on section 7.
4. **Spend your care on section 6.** Sort every action, not just the one that
   worried you. It is the section most likely to be quietly incomplete.
5. **Compute section 3, do not estimate it.** Count the real steps, pick a
   per-step accuracy you can defend, and write down the number even if it makes
   you wince. That is the worksheet doing its job before launch instead of in an
   incident review.
6. **Say what the system must do, not how to build it.** No tool name, no
   framework, no model. This document sets the scope and where a human stays
   involved. The build stays an engineering decision.
7. **Send it to the person who would build it.** Ask which row they would
   challenge first. It is usually section 6.

## 2. The worksheet

| Section | What it must contain | From |
| --- | --- | --- |
| 1. What it is | The workflow test: could a human specify every branch in advance | 6.1 |
| 2. Tools it touches | Every function it can call, split into read and write | 6.2 |
| 3. Chain length and reliability | Steps, per-step accuracy, the whole-chain number | 6.3 |
| 4. Design pattern | Plan then execute, retries, idempotent actions | 6.4 |
| 5. One agent or several | The specific thing one agent would fail to do | 6.5 |
| 6. Blast radius | Every action sorted into one of four rows, with named approvers | 6.6 |
| 7. Disqualification check | Four signals, run with real numbers | 6.7 |

**Agent scoping worksheet: [automation idea]**

| | |
| --- | --- |
| Proposal | |
| Owner (a name) | |
| Engineer who would build it (a name) | |
| Status and date | Draft, in review or approved, and the date |
| Linked documents | The PRD (A01), the rubric (A05), the golden set (A02), and any RAG design doc (A06) |

### 1. What it is

*From lecture 6.1. An agent observes, decides its next action, acts through a
tool, observes the result and decides again, until it judges the task done. A
fixed sequence with a model writing text at one step is a workflow, not an
agent.*

| Prompt | Your answer |
| --- | --- |
| The task, in one sentence | |
| The workflow test: could a human specify every path in advance? If yes, build a workflow. | Yes / no, and why |
| An input its designer might not anticipate, and what the agent would do with it | |
| One concrete decision point where it could plausibly go wrong | |

### 2. Tools it touches

*From lecture 6.2. A tool connection is a permission grant, not a feature
toggle. Ask what it can write, not just what it can read.*

| Tool or function | Reads or writes | What exactly it can change | Who approved the access (a name) |
| --- | --- | --- | --- |
| | | | |
| | | | |
| | | | |
| | | | |

### 3. Chain length and reliability

*From lecture 6.3. The whole-chain success rate is roughly the per-step accuracy
raised to the number of unchecked steps. It falls faster than intuition
expects.*

| Prompt | Your answer |
| --- | --- |
| Steps in the chain, counted (list them) | |
| Per-step accuracy you can defend, and its source: measured or assumed | |
| Whole-chain number: per-step accuracy raised to the number of steps | |
| Where checkpoints could cut the chain (a human or a rule verifies output) | |
| The whole-chain number with those checkpoints in place | |
| The bar it has to clear, and who set it (a name) | |

Reference, from lecture 6.3 (whole-chain success, per-step accuracy down the
side):

| Steps | 90% per step | 95% per step | 99% per step |
| --- | --- | --- | --- |
| 1 | 90% | 95% | 99% |
| 3 | 73% | 86% | 97% |
| 5 | 59% | 77% | 95% |
| 7 | 48% | 70% | 93% |
| 10 | 35% | 60% | 90% |

Steps are rarely perfectly independent, so the real number can sit above or
below this table. The direction holds either way: more unchecked steps compound
more risk. Shortening the chain or adding a checkpoint usually moves the number
more than chasing a better per-step score.

### 4. Design pattern

*From lecture 6.4. Most agent demos fail because nobody designed for the third
retry.*

| Prompt | Your answer |
| --- | --- |
| Plan then execute, or step by step? If the plan is shown before anything runs, who or what reviews it? | |
| Retry limit per step, and what happens when it is exhausted (stop and escalate to whom) | |
| For each write action: what happens if it runs twice by accident? | |
| Which write actions need an idempotency check (for example confirm the refund has not already posted) | |
| Where the engineering budget for these patterns goes: the largest blast radius first | |

### 5. One agent or several

*From lecture 6.5. A second agent adds a handoff, and each handoff is a new step
the reliability maths applies to.*

| Prompt | Your answer |
| --- | --- |
| Proposed number of agents | |
| What, specifically, would a single better-scoped agent fail to do? If the honest answer is "nothing specific", use one agent. | |
| Handoffs counted, and added to the chain length in section 3 | |
| Built and run locally first, or heading straight to production? | |

### 6. Blast radius

*From lecture 6.6. Ask what the action can damage and how far, by two
questions: can it be undone, and what does it cost if it cannot. Do not sort a
borderline action into the safer row because that lets you keep moving.*

| Reversible? | Cost if wrong | Verdict |
| --- | --- | --- |
| Yes | Low | Autonomous, no gate needed |
| Yes | High | Autonomous with a spend cap, logged |
| No | Low | Autonomous, flagged for review after |
| No | High | Always needs approval before it happens |

List every action the agent can take, from section 2, and sort each one.

| Action | Reversible? | Cost if wrong (and how you know) | Row | Gate or cap | Named approver (a person, not "the team") |
| --- | --- | --- | --- | --- | --- |
| | | | | | |
| | | | | | |
| | | | | | |
| | | | | | |
| | | | | | |

- Reserve approval gates for the bottom row. Gate everything and you have built
  a slow form, not an agent.
- A guardrail is a mechanism, not a feeling. "We review its work" is not one. A
  named action, a named approver, and an agent that cannot run the action
  without that approval is.
- If more than a couple of actions land in the bottom two rows, that is not a
  failure of the worksheet. It is the scoping finding.

Your scope, in one sentence. Write it so that nobody could mistake it for
"let the agent handle it automatically":

> [Action] up to [limit], [conditions that must hold], capped at [number] per
> [period], escalating anything outside that to [named approver] within [time].

### 7. Disqualification check

*From lecture 6.7. Run it with the numbers from sections 3 and 6, not
impressions. Any one failed row stops the whole proposal.*

| Signal | Why it disqualifies | Pass or fail, with the evidence |
| --- | --- | --- |
| A workflow could specify every path in advance | Pay for autonomy only where branches cannot be predicted | |
| You cannot build a guardrail for its riskiest action | Blast radius with no gate is just blast radius | |
| The reliability maths does not clear your bar, even checkpointed | More steps will not fix what the maths already ruled out | |
| Nobody can meaningfully review its escalations | An escalation path nobody watches is not a safety valve | |

| Prompt | Your answer |
| --- | --- |
| If it fails a row, will a change of scope fix it, or is the idea wrong? | |
| Most proposals fail on scope, not on the idea. What would the smaller, bounded version be? | |

## 3. The honest test

Before anyone else reads it:

1. Is the section 3 number the real one, or the one that would feel better?
2. Does every action in section 6 appear, with a named person against anything
   in the bottom row?
3. Could the engineer build only from this document and know where a human
   stays involved?
4. Is anything written as certain that is really a guess?

## 4. Open gaps

| Section | What is missing | Owner and date |
| --- | --- | --- |
| | | |
