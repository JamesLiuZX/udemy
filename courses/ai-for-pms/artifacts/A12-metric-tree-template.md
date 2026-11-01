# A12 · The Metric Tree Template

Part of *AI Product Skills for PMs & Analysts*. Delivered in lecture 9.6, the
workshop, and built from lectures 9.1 to 9.5. Use it to put one chosen North
Star metric and its supporting metrics for a live AI feature onto one page, with
every number either real or honestly marked unmeasured.

---

## 1. How to use this

1. **Pick the feature you are closest to,** the one whose numbers you would
   recognise on sight. Set a twenty-minute timer.
2. **Choose the North Star deliberately** (section 3), for what this feature
   actually does. Write down why it is this number and not another.
3. **Fill the tree** (section 4): adoption, acceptance, deflection and a cost
   number, each with a written definition, a current value, and a label: measured
   or unmeasured. "Unmeasured" is a valid entry. A guess wearing the shape of a
   number is not.
4. **Check your instrumentation** (section 5), your last A/B test (section 6), one
   feedback loop (section 7) and your leadership dashboard (section 8).
5. **Finish with the honest test** (section 9). A tree with one honest gap is
   worth more than one with five numbers nobody checked.
6. **Send it to whoever owns your next leadership update.**

Suggested pacing: minutes 0 to 4 on sections 3 and 4, 4 to 8 on section 5, 8 to
12 on section 6, 12 to 16 on section 7, 16 to 20 on section 8.

## 2. The shape

```text
                 North Star (chosen on purpose)
               /        |            |           \
        Adoption   Acceptance    Deflection   Cost per resolution
```

Lecture 9.6's diagram draws the example tree with deflection rate as the North
Star and three branches under it: adoption, acceptance, and cost per resolution.
Your North Star may be any one of the four; the other three sit beneath it. The
four together are what the lecture calls a complete metric tree.

| Metric | What it measures | Why it survives (lecture 9.1) |
| --- | --- | --- |
| Adoption | Of everyone who could use the feature, who actually does | Separates real reach from a loud minority |
| Acceptance | How often a suggestion is kept, not edited or discarded | A direct proxy for quality, from production, not from a golden set |
| Deflection | How often the feature resolves a need without a human | Ties usage directly to the cost the feature was built to justify |
| Cost number | What it costs per resolution (or per unit your feature delivers) | Keeps usage honest against spend (see the model in A09) |

Read the three behaviour metrics together. Each one catches a story the other
two miss. Engagement alone can rise while acceptance falls, which means more
retries, not more value. A high acceptance rate is not automatically good news
either: users rubber-stamping a low-effort suggestion looks identical to genuine
quality in the data.

## 3. The North Star

| Prompt | Your answer |
| --- | --- |
| Feature | |
| What this feature is for, in one sentence | |
| Your North Star metric | |
| Why this number and not a different one | |
| Who defends this number in a leadership meeting (a name) | |
| Would you trust it enough to defend it live? If not, what would change your mind | |

## 4. The tree

For every metric write the definition first, so that two people would compute
the same number: what counts in the numerator, what counts in the denominator,
over what period.

| Metric | Definition (numerator, denominator, period) | Current value | Measured or unmeasured | Source | Owner (a name) | Trend, and since when |
| --- | --- | --- | --- | --- | --- | --- |
| North Star: | | | | | | |
| Adoption | | | | | | |
| Acceptance | | | | | | |
| Deflection | | | | | | |
| Cost number | | | | | | |

| Prompt | Your answer |
| --- | --- |
| Engagement trend and acceptance trend side by side: do they move together? If they move in opposite directions, that is the finding, not a coincidence to explain away. | |
| Could high acceptance here mean rubber-stamping rather than quality? How would you tell? | |
| Any branch marked unmeasured: what does it take to measure it, and who does it | |

## 5. Instrumentation check (lecture 9.2)

The moment a suggestion appears on screen is the only moment you will ever know
exactly what it was. Whatever happened before you started logging cannot be
analysed afterwards. Capture exactly enough to compute the three behaviour
metrics, not a data lake nobody queries.

| Event | What it must capture | Do you log it today? | Same request_id as the others? |
| --- | --- | --- | --- |
| Shown | request_id, prompt version, model, timestamp | | |
| Outcome | accept, edit or reject | | |
| Escalation | whether a human took over | | |
| Feedback | any explicit signal given | | |

| Prompt | Your answer |
| --- | --- |
| Pick one request from last week. Was it accepted, edited or rejected, and which prompt version produced it? Could you answer? | |
| Does a request_id actually connect your shown and outcome events? | |
| Does what you log respect the data questions from your risk register (A11, block 2)? | |
| The gap, and when logging will start | |

## 6. A/B test check (lecture 9.3)

A standard A/B calculator assumes both variants behave identically every time
they run. An AI feature does not.

| Check | Your last (or next) test |
| --- | --- |
| Randomised by user, not by request: a user stays in one arm for the whole test | |
| Prompt version pinned for both arms until the test formally ends | |
| Model version pinned, or any change recorded | |
| Sample size sized larger than the calculator says, to absorb the model's own output variance. State the margin and why. | |
| Results traced to a known, fixed configuration | |
| Finding | |

Underpowering the test costs you whichever way it falls.

## 7. One closed feedback loop (lecture 9.4)

More usage generates more data. That data improves the feature only if a
specific person closes the loop on purpose. Nothing in the loop except usage
happens automatically.

```text
Usage -> Signal (accept, edit, reject) -> Sampled for review
      -> Golden set row or prompt fix -> Improved feature -> Usage
```

| Prompt | Your answer |
| --- | --- |
| Five rejected outputs from the last week. Did any of them become a golden set case (A02) or a fix? | |
| The person who samples rejected cases, by name | |
| The cadence (weekly, on a real calendar) | |
| One real case you turned into a fix or a golden set row, and what changed | |
| Is any part of the feature allowed to retrain itself automatically from unfiltered user input? If yes, that is the injection risk (A11, block 1) aimed at your training data | |

## 8. The leadership dashboard (lecture 9.5)

The dashboard your team operates with and the dashboard leadership needs are two
different documents. This one supports a single decision.

| Prompt | Your answer |
| --- | --- |
| The decision this dashboard supports | |
| Panels today (count). If more than five, which three actually drove the decision in the room? | |
| The three to five numbers: adoption, acceptance, deflection and one cost number | |
| Refresh cadence, matched to how often the decision could change | |
| Has it ever shown a genuinely bad number? If never, ask whether it has stopped reporting and started performing | |

## 9. Honest test

- Can you defend the North Star live, and say why it is not a different number?
- Is every value real, or honestly marked unmeasured?
- Does every metric have a written definition two people would compute the same
  way?
- Did you attempt the instrumentation check on a real request, or only read it?
- Is anything on the tree there because it looks complete?

## 10. Open gaps

| Section | What is missing | Owner and date |
| --- | --- | --- |
| | | |

## 11. Where this fits

This tree closes the loop with the rest of the course. The golden set (A02) and
rubric (A05) measure quality before launch, the scorecard (A07) and eval harness
(A03, A04) keep measuring it, the unit-economics model (A09) supplies the cost
number, the risk register (A11) holds what could go wrong, and this tree is how
you report what is happening now.
