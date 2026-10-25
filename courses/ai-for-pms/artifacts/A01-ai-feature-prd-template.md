# A01 · AI Feature PRD Template

Part of *AI Product Skills for PMs & Analysts*. Delivered in lecture 3.7 and
used again in the workshop, lecture 3.8. Use it to spec one AI feature so that
engineering can build it, QA can fail a build against it, and a launch review
can hold you to it.

---

## 1. How to use this

1. **Pick a feature you are close to.** The messier and more real, the better.
   A hypothetical feature, or one so simple it carries no real risk, makes this
   easy and teaches you almost nothing, because the hard sections have nothing
   to grip.
2. **Write the acceptance criteria first**, even roughly, before you touch
   anything else. It is the section every other section has to support. A weak
   threshold makes the dataset, the rubric and the failure taxonomy easy to
   skip. A real one forces the rest of the document to hold up.
3. **Then work down the template in order.** A complete first draft takes about
   twenty minutes: 3 on problem and archetype, 5 on acceptance criteria, 4 on
   the dataset and rubric, 4 on the failure taxonomy and degradation path, and 4
   on human in the loop and ownership. That is a pace, not a deadline.
4. **Commit to the dataset and the rubric here. Do not paste them here.** The
   PRD is the contract and they are the deliverables. Write down what each must
   satisfy, and link to where it lives.
5. **If one section stalls the draft, write a dated TBD and keep moving**, for
   example "TBD, owner assigned by Friday". Add it to the open gaps list at the
   end of the template. A named gap costs you nothing but honesty. A blank
   section stops the whole draft.
6. **Keep your usual PRD.** The problem statement, user stories, rollout plan,
   success metrics and anything else that does not depend on the output being
   probabilistic stay exactly as you write them today. This template adds to
   your PRD. It does not replace it.
7. **Run the honest test before anyone else reads it.** It follows the worked
   example. Then give the draft to one real colleague and ask what they would
   push back on.

## 2. The template

Copy everything from "PRD: [feature name]" down to the open gaps list into your
own document, and replace each prompt with your answer. The "From" column below
is a map back to the lecture that teaches the full method. A section that feels
thinner than it should is a reason to reopen that lecture, not a sign you are
bad at this.

| Section | What it must contain | From |
| --- | --- | --- |
| 1. Problem and archetype | What it does, which of the seven archetypes | Course Section 1 |
| 2. Acceptance criteria | The four-part threshold sentence | 3.2 |
| 3. Golden dataset | Size floor, coverage, source, owner, deadline | 3.3 |
| 4. Rubric | Where it lives, pass/fail mapping, calibration proof | 3.4 |
| 5. Failure taxonomy | At least three distinct, named failure types | 3.5 |
| 6. Degradation path | Disclaim, escalate, or decline, and when each applies | 3.5 |
| 7. Human in the loop | Which pattern, matched to blast radius | 3.6 |
| 8. Ownership and review | Who updates the rubric and dataset, how often | 3.3, 3.4 |

**PRD: [feature name]**

| | |
| --- | --- |
| Feature | |
| PRD owner (a name) | |
| Status and date | Draft, in review or approved, and the date |
| Linked documents | Golden dataset, rubric, and any other document this PRD depends on (links) |

### 1. Problem and archetype

*From Course Section 1 (lectures 1.6 and 1.7). This is close to what any decent
PRD already has, so it is the fastest section to write. Do not skip naming the
archetype.*

| Prompt | Your answer |
| --- | --- |
| Objective: whose time or money does this save, and under what condition? A line that could describe any feature is not a PRD line yet. | |
| What the feature does, in one sentence | |
| Archetype: Summarise, Extract, Classify, Draft, Search, Answer or Act. If the feature is several, list each piece separately. | |
| In scope | |
| Out of scope (the non-goals). Name the cases a looser version would never think of. | |
| Expected volume (uses per month), marked measured or projected, with its source | |
| Blast radius: if one output is wrong, can it be undone, and what does it cost? | |

Disqualification check (lecture 1.7). One yes is enough to stop and rethink. A
yes is a punch list, not a verdict.

| Question | Yes or no |
| --- | --- |
| Is a wrong answer severe and irreversible, with no human check first? | |
| Does this need to be correct every time, not just usually right? | |
| Can you neither ground it in facts nor verify it afterwards? | |
| Is the volume too low to justify a golden set at all? | |
| Would a simple rule already solve this, reliably, today? | |

### 2. Acceptance criteria

*From lecture 3.2. Write this section first. It is the one place where vague
text fails exactly like the untestable line from lecture 3.1.*

| Part | Your answer |
| --- | --- |
| What you test against (the golden dataset, by name and size) | |
| What counts as good (the rubric, and the score that passes) | |
| The pass rate required (a percentage, not "most") | |
| The hard floor (what must never happen, even once) | |

Your sentence, in one line:

> On the [N]-case [name] golden set, at least [X]% of [outputs] score
> [pass mark] on the [name] rubric, with zero [outputs] scoring [floor].

You can name the floor as a failure instead of a score, for example "with zero
wrongful approvals". Either way it must be something a rater can point at.

| Prompt | Your answer |
| --- | --- |
| Signed off before the first eval run (lecture 4.9): by whom, and on what date | |

- **Decide the floor first, then the headline percentage.** Deciding what you
  will never tolerate is the clearer conversation, and it makes the second
  number easier to agree on.
- **Name the archetype, then set the bar it earns.** A summariser and an
  action-taking agent do not earn the same benefit of the doubt. Do not copy a
  number from this course or from anyone else's template. Copy the habit.
- **Set it where you would actually hold the line.** A threshold should be
  specific enough to lose an argument against. "100%, no exceptions" is not
  rigour: a probabilistic system essentially never hits 100%, and an impossible
  bar only moves the argument to launch day.
- **If the honest threshold would need to sit above 99% to be responsible**,
  that is the disqualification check telling you the feature as scoped may not
  be the one to ship. Do not negotiate that number down.

> **Not this:** "The AI should respond helpfully and accurately to customer
> questions." Every word feels reasonable and none of it is testable. It is a
> hope with a checkbox next to it.

### 3. Golden dataset

*From lecture 3.3. Built in full in lecture 4.2 and artifact A02. This section
is the commitment to the dataset, not the dataset.*

| Question | Your answer |
| --- | --- |
| How many cases, at minimum? A floor stops "a few examples" counting as done. | |
| What must it cover, not just include? Common path, known failure modes, edge cases and adversarial inputs. Note any you have no data for yet. | |
| Where does the data come from? Real tickets, transcripts or logs. If real data does not exist yet, say so plainly here. | |
| Who owns it (a name), and by when? | |
| When is it frozen, and where is it versioned? Give a date before launch and a location. | |
| Link to the dataset | |

If the feature retrieves from documents, also list which sources are in and
which are out. That is a scope decision, not an engineering call (lecture 5.2).

> **Not this:** "Engineering will define an appropriate test set before launch."
> Nobody owns it, dated it, or wrote down what it has to cover.
>
> **Write this:** "A 50-case golden set, covering common path, known failures,
> edge cases, and adversarial inputs. Owned by [name]. Frozen two weeks before
> launch, versioned in [location]."

### 4. Rubric

*From lecture 3.4. Built in full in lecture 4.3 and artifact A05. This section
points at the rubric and proves it works. It does not contain the rubric.*

| Question | Your answer |
| --- | --- |
| Where does the written rubric live, and which version is current? | |
| How do scores map to pass or fail? Write the pass mark before any case is scored. | |
| Has it been calibrated? Two independent reviewers, 15 cases, agreement of at least 85% (13 or more of the 15). Give the result and the date, or a dated gap. | |
| Who resolves a disagreement? | Disagreements are resolved by rewording the question, not by escalation. |
| Who can edit it, and how are edits logged? An edit to the rubric is worth a note, a date and a reason. | |

> **Not this:** "Reviewed by a subject matter expert for quality." Whoever is
> free on Tuesday is the whole rubric.
>
> **Write this:** "Scored against the six-question accuracy rubric (attached),
> calibrated to at least 85% agreement between two independent reviewers before
> use."

### 5. Failure taxonomy

*From lecture 3.5. A single pass rate lumps these together, and they are not
the same event. List at least three distinct types, each with a response.*

| Failure type | Starter note (lecture 3.5) | What it looks like in your feature | What the system does when it happens |
| --- | --- | --- | --- |
| Confidently wrong | A false fact, stated as true. Must never reach the user unchecked. | | |
| Right content, wrong format | Breaks the parser. A silent failure downstream, not a visible one. | | |
| Times out or errors | No answer at all. Needs a retry or a fallback, not a hang. | | |
| Over-cautious refusal | Declines something safe. Annoying, rarely dangerous. | | |
| Partially right | Some facts correct, one is not. The hardest to catch. | | |
| (your own) | | | |

Delete the rows that do not apply and add your own. Most features have three or
four realistic failure types, not a dozen. Picture the worst thing the feature
has done, or could plausibly do, and ask which row it belongs in. The hard
floor from your acceptance criteria names the most dangerous row.

For that row, finish this sentence: "When this happens, the system
______________." If you cannot finish it yet, that is this week's real work,
not a detail to leave for later.

### 6. Degradation path

*From lecture 3.5. The alternative to a degradation path is not safety. It is a
confident guess with nothing behind it.*

Something has to check an output before it reaches anyone: a confidence score,
a guardrail, or a rule that catches the shape of a known failure. When the
check fails, the feature makes one of three honest moves:

- **Disclaim:** say plainly that the feature is not sure.
- **Escalate:** hand the case to a human.
- **Decline:** refuse the request outright.

Fill in one row per check:

| The check | What it catches | Move: disclaim, escalate or decline | Why this move fits the blast radius |
| --- | --- | --- | --- |
| | | | |
| | | | |
| | | | |

Choose by archetype and blast radius, not by whichever was easiest to build. A
drafting tool can usually just disclaim and let the human who reviews it
decide. A feature about to act on someone's behalf has no draft step left to
catch a bad guess, so escalating or declining is often the only responsible
choice.

Degradation is not free. A guardrail set too sensitive spends half its time
saying "I'm not sure" about things the feature knew, or sends easy cases to a
human who now has more work than the feature saved. Give the rate its own
threshold, the same way the pass rate has one.

| Prompt | Your answer |
| --- | --- |
| Maximum degradation rate: the share of requests allowed to take this path, and what it is measured on | |

### 7. Human in the loop

*From lecture 3.6. "We'll have a human in the loop" is not a design until it
says when, reviewing what, and before or after the action. Tick one pattern.*

| Chosen | Pattern | The human is involved | Right for |
| --- | --- | --- | --- |
| [ ] | Pre-approval | Before every single action | Irreversible, high blast radius |
| [ ] | Draft-then-review | Before every output ships | Anything reaching a user directly |
| [ ] | Sampled audit | After the fact, on a percentage | Reversible, high volume, low stakes each |
| [ ] | Escalate on uncertainty | Only when the guardrail flags it | Once that guardrail is actually trustworthy |
| [ ] | Monitor only | After the fact, in aggregate | Lowest-stakes, fully reversible tools |

| Question | Your answer |
| --- | --- |
| Why does this pattern fit the blast radius? Reversible or not, and the cost if wrong. | |
| Who is the reviewer, and what exactly do they see? | |
| Volume limit per reviewer, as a number. A queue with no stated limit grows until it breaks. | |
| How will you stop the check turning into a rubber stamp? Rotate reviewers, lower the volume, or narrow pre-approval to the high-stakes cases and sample the rest. | |
| What evidence would let you move to a lighter pattern, and who decides? | |

Most features start on draft-then-review while everyone is still learning how
they fail, and earn their way down to sampled audit or escalation once the pass
rate and the failure taxonomy have proven it out. Escalate on uncertainty is
the most efficient pattern and the easiest to pick too early: a model can be
confidently wrong, and a confident wrong answer sails straight past a check
built to catch uncertainty. If a wrong output is expensive or irreversible and
your pattern is anything short of pre-approval, write down why.

> **Not this:** "Don't worry, we'll have a human in the loop."

### 8. Ownership and review

*From lectures 3.3 and 3.4. Unowned work is nobody's job until launch week.*

| Item | Who updates it (a name) | How often, and what forces an update | Where changes are logged |
| --- | --- | --- | --- |
| Golden dataset | | | |
| Rubric | | | |
| Threshold and floor | | | |
| This PRD | | | |

What forces an update: a change to the prompt or the model, which means
re-running the eval, and production changing under a frozen set (golden-set
drift, lecture 4.1). A cheap check once a release: pull ten transcripts you did
not choose, score them on the same rubric, and compare with your golden-set
pass rate. If the live number misses it, the set has drifted.

An edit to the rubric or to the threshold is worth a note, a date and a reason.
A rubric that quietly changes between releases makes every pass-rate comparison
meaningless.

| Prompt | Your answer |
| --- | --- |
| Launch review: who signs off, and when | |

### Your usual PRD sections, unchanged

User stories, rollout plan, and the success metrics this feature promises to
move. Keep them as you always have. They are not repeated here because nothing
about them changes when the output is probabilistic.

### Open gaps

Anything you could not answer yet goes here with an owner and a date, so that
nothing is skipped in silence. An unanswered question is honest. A vague
sentence pretending to answer it is not.

| Section | What is missing | Owner | Date |
| --- | --- | --- | --- |
| | | | |
| | | | |

## 3. Worked example: the support-ticket summariser

The PRD for the summariser used throughout the course, the one behind ticket
#4471 in lecture 0.4. The quoted sentences are the ones taught in lectures 3.2
to 3.4. Square brackets mark answers only your own team can give: a name, a
date, a location, a measured number. Never fill those with a guess.

| Section | What the summariser's PRD says |
| --- | --- |
| 1. Problem and archetype | Objective: give a support agent a summary they can act on without opening the original ticket. Archetype: summarise. Drafting the reply, routing the ticket and acting on the account are separate archetypes, each with its own copy of this template. Out of scope: replying to the customer, closing the ticket, any change to the account. Volume: [tickets per month, measured on the channel it serves]. |
| 2. Acceptance criteria | "On the 50-case support golden set, at least 90% of responses score 4 or 5 on the accuracy rubric, with zero responses scoring 1." Signed off by [name] on [date], before the first eval run. |
| 3. Golden dataset | "A 50-case golden set, covering common path, known failures, edge cases, and adversarial inputs. Owned by [name]. Frozen two weeks before launch, versioned in [location]." Source: real tickets from the desk's own history, not invented examples. Ticket #4471 goes in as a known failure. |
| 4. Rubric | "Scored against the six-question accuracy rubric (attached), calibrated to at least 85% agreement between two independent reviewers before use." The six questions: core issue captured, action required is clear, deadlines preserved, consequence preserved, diagnostic detail kept, nothing invented. A score of 4 or 5 passes, and the mapping is written into the rubric before any case is scored. A 1 is the floor: a claim stated as fact that is not in the ticket. Disagreements are resolved by rewording the question, not by escalation. Calibration result: [__] of 15 on [date]. |
| 5. Failure taxonomy | Confidently wrong: a claim in the summary that is not in the ticket, which is the hard floor. Drops a critical detail: the failure in ticket #4471, where the deadline, the consequence and the email mismatch were lost. Times out or errors: no summary at all. Over-cautious refusal: declines to summarise a ticket that is safe to summarise. |
| 6. Degradation path | Check: a rule that flags any ticket whose text contains a date the summary leaves out, the shape of the 4471 failure. Move: disclaim. The summary carries a visible note that it may be incomplete, with the original ticket beside it, because the agent reading it is already the human who decides. On a timeout or error, show the original ticket rather than a blank panel. Maximum degradation rate: [__]% of tickets. |
| 7. Human in the loop | Draft-then-review at launch: the agent reads the summary next to the original ticket. Move to sampled audit only once the pass rate and the failure taxonomy have proven it out, with [name] deciding. Volume limit: [number] summaries per agent per day. |
| 8. Ownership and review | Golden set owned by [name], rubric owned by [name], and every edit to either, or to the threshold, logged with a note, a date and a reason. Once a release, score ten uncurated recent tickets on the same rubric and compare with the golden-set pass rate. |

Notice that ticket #4471 appears three times: as a known failure in the dataset,
as the reason behind rubric questions three to five, and as a named row in the
failure taxonomy. That is what a PRD that holds together looks like. One real
failure, traced through every section, instead of eight sections that never
meet.

The example leaves out what stays as you already write it: the user stories,
the rollout plan and the success metrics.

## 4. The honest test

Filling in every section is not the same as filling it in well. A template
completed with vague content fails exactly like the untestable line from
lecture 3.1, just with better formatting. The test is not whether every box has
text in it. It is whether someone could act on that text: run the calibration
check, find the dataset, apply the threshold.

Before anyone else reads it:

- [ ] Could QA fail a build against the acceptance criteria today, using only
      what is written?
- [ ] The threshold has all four parts: dataset, rubric with its pass mark,
      pass rate, and a hard floor. The floor was decided first.
- [ ] No adjective is doing the work. Every noun is something a project tracker
      could hold someone to.
- [ ] The dataset commitment names a size floor, coverage, a source, a named
      owner, a date before launch and a place it is versioned. The cases are
      linked, not pasted.
- [ ] The rubric section points at a document, not a person. It states the
      calibration result or a dated gap, and how disagreements are resolved.
- [ ] The failure taxonomy has at least three distinct types, and the most
      dangerous one has a finished sentence that begins "When this happens, the
      system ...".
- [ ] The degradation path names disclaim, escalate or decline for each
      trigger, and the degradation rate has its own threshold.
- [ ] The human-in-the-loop pattern is one of the five, by name, matched to
      blast radius, with a volume limit given as a number.
- [ ] Every section has content or a dated TBD with an owner. Nothing was
      skipped in silence.
- [ ] One real colleague has read it and told you what they would push back on.

The same gap turns up in the same few sentences. Dissolve them on sight:

| If the PRD says | What it is hiding | Section to fix |
| --- | --- | --- |
| "The AI should respond helpfully and accurately." | No dataset, no rubric, no threshold, no floor | Acceptance criteria |
| "Engineering will define an appropriate test set before launch." | No size, no coverage, no owner, no date | Golden dataset |
| "Reviewed by a subject matter expert for quality." | "Quality" lives in one person's head | Rubric |
| Nothing about what happens when it is wrong | No failure types, no path for uncertainty | Failure taxonomy, degradation path |
| "We'll have a human in the loop." | Which of the five patterns, and matched to what | Human in the loop |

## 5. Where this fits

This PRD is the document the rest of the course plugs into. A02 builds the
golden dataset you committed to (lecture 4.2) and A05 builds the rubric and
proves it calibrated (lecture 4.3). A03 and A04 measure the pass rate against
your threshold (lectures 4.6 and 4.7). If the feature retrieves from documents,
the RAG design doc (A06, lecture 5.7) sits inside this PRD and explains how the
system reaches the threshold. If it takes actions, the agent scoping and
blast-radius worksheet (A08, lecture 6.8) goes with it. A09 prices the volume
you wrote down, A11 maps what could go wrong, and A12 tracks the metrics the
PRD promised to move.

In the capstone (lecture 11.1) this is the first of the six required artifacts,
and the check that matters is that the others agree with it: the golden set's
pass bar matches your threshold, the cost model's volume matches your scope, and
every number in the risk register traces back to your scope.
