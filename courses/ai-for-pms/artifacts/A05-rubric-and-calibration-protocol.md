# A05 · Evaluation Rubric Template + Inter-Rater Calibration Protocol

Part of *AI Product Skills for PMs & Analysts*. Introduced in lecture 0.4,
taught in full in lecture 4.3. Use it to define what "good" means for one AI
feature, in a form two different people score the same way.

---

## 1. How to use this

1. Write your questions **before** you look at any output. Questions written
   after peeking will, without your meaning to, be questions the output
   happens to pass.
2. Aim for **six** questions. Fewer than four and you miss the failure that
   matters; more than eight and reviewers stop reading carefully.
3. Every question must be **binary** (pass or fail, no scales),
   **observable** (checking it means pointing at evidence in the input or
   output, not consulting your feelings), and about **one property** (if a
   question contains "and", split it).
4. Score by answering the questions in order. The total is "questions
   passed, out of six". Do not average, do not weight, do not round up.

## 2. The rubric template

Fill in one row per question. The example rows in section 3 show the level
of specificity to aim for.

| # | Question (binary, observable, one property) | What earns a PASS | Evidence to point at |
| --- | --- | --- | --- |
| 1 | | | |
| 2 | | | |
| 3 | | | |
| 4 | | | |
| 5 | | | |
| 6 | | | |

Scoring record, one row per output scored:

| Output ID | Q1 | Q2 | Q3 | Q4 | Q5 | Q6 | Total /6 | Rater | Date |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| | | | | | | | | | |

## 3. Worked example: the support-ticket summariser

The rubric used on ticket #4471 in lecture 0.4, for a summary a support
agent should be able to act on without opening the original ticket:

| # | Question | What earns a PASS |
| --- | --- | --- |
| 1 | Core issue captured | The billing problem is stated |
| 2 | Action required is clear | The agent knows what to do next |
| 3 | Deadlines preserved | Any date or time pressure survives |
| 4 | Consequence preserved | What breaks if ignored is kept |
| 5 | Diagnostic detail kept | Clues to root cause survive |
| 6 | Nothing invented | No claim absent from the ticket |

The AI summary in that lecture scored 3 of 6: it captured the issue and the
action, invented nothing, and dropped the deadline, the consequence, and the
mismatched-email clue. Note that the three failures were exactly the three
details an agent needed to resolve the ticket without reopening it.

## 4. Question quality checklist

Run every draft question past these before you calibrate:

- [ ] Can it be answered pass or fail, with no "sort of"?
- [ ] Could a colleague point at the exact evidence for their answer?
- [ ] Does it test one property only (no "and", no "or")?
- [ ] Would two honest people find the same evidence?
- [ ] Is it about the output, not about the rater's taste?

Vague words are the usual defect. "Professional", "clear", "appropriate" and
"accurate overall" each dissolve into two or three observable checks when
you ask what you would actually point at. Do the dissolving on paper, in the
rubric, not in each rater's head.

## 5. The calibration protocol

A rubric is not done when it is written. It is done when two people score
alike with it. One pass of this loop takes about an hour: roughly twenty
minutes to score fifteen cases, then the discussion, which takes longer than
the scoring did. That conversation is where the rubric actually gets better.

1. **Pick fifteen real cases** from your own golden set, spanning good to bad.
2. **Two people score all fifteen independently.** No discussion first, and do
   not brief your colleague on what you meant by any question. The rubric has
   to survive being read cold, because cold is how it will be used once it is
   real.
3. **Compare case by case**, not just the final percentage. Two columns in a
   spreadsheet is the whole tool: your verdicts next to theirs, row by row. A
   case counts as an agreement when both of you reach the same verdict on it
   (pass or fail against your pass mark).
4. **Where you disagree, stop and read that question again, together.** Nearly
   always both of you read it correctly and the wording allowed two correct
   readings. Reword the question, never your colleague's judgement, and reword
   only the question that caused the disagreement.
5. **Run the same fifteen cases again** with the reworded question and compare
   again.

**The bar to clear:** agreement above 85%, which is 13 or more of the 15 cases.
Clear it and you freeze the rubric and score all fifty. Fall short and you loop
again. Most rubrics need one or two passes through this loop.

**One caution:** percent agreement can flatter you. If more than about 90% of
outputs pass (or fewer than about 10%), two raters scoring almost at random
would still agree most of the time, by chance alone. In that case ask a data
analyst for Cohen's kappa, which corrects for chance. With a pass rate anywhere
in the middle, roughly 30% to 70%, plain agreement is honest enough on its own.

## 6. Calibration comparison sheet

One row per case. Fill the last three columns only on the rows where you
disagreed, then run the same fifteen cases again after rewording.

| Case | Rater A verdict | Rater B verdict | Agree? | Question that caused it | Ambiguity found | Rewritten as |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | | | | | | |
| 2 | | | | | | |
| 3 | | | | | | |
| 4 | | | | | | |
| 5 | | | | | | |
| 6 | | | | | | |
| 7 | | | | | | |
| 8 | | | | | | |
| 9 | | | | | | |
| 10 | | | | | | |
| 11 | | | | | | |
| 12 | | | | | | |
| 13 | | | | | | |
| 14 | | | | | | |
| 15 | | | | | | |

Agreement = cases agreed on, out of 15. Pass 1: ____ of 15. Pass 2: ____ of 15.

## 7. Where this fits

A calibrated rubric is the atom of everything in Section 4. Run it across
fifty inputs instead of one and you have a golden set (lecture 4.2, artifact
A02). Turn "questions passed" into a pass rate across those fifty and you
have an eval (lectures 4.6 and 4.7). Put a threshold on that pass rate and
you have an acceptance criterion you can put in a spec (Section 3).
