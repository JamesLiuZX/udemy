# B07 · Testing Architecture + Kill Criteria Worksheet

Part of *AI UGC Video Ads*. Built in lecture 7.5, the Section 7 workshop, from
lectures 7.1 to 7.4. The companion file is
`B07-testing-architecture-and-kill-criteria.xlsx`: an empty workbook with a Plan
tab that works out your margin, CAC ceiling, budgets and kill rule, and an Ad sets
tab that flags a kill when your own rule is hit. Nothing in it is pre-filled.

Use it on the batch that cleared pre-flight (B05). Nothing here is generated fresh.

---

## 1. How to use this

1. **Decide every number before any result exists.** The worst time to decide when to
   kill an ad set is while you are watching it underperform. Each number below is
   set now, in writing, with its source.
2. **Use your own numbers.** Yours will not match anyone else's, and they should not.
   A testing architecture that fits your actual margin is the only kind worth
   building. Copying another account's budget or kill figure onto yours without
   working out your own margin is the same mistake as copying someone else's claim
   without checking it.
3. **Work in this order,** and expect the whole run to take longer than the
   timings if your costs are scattered:

| Step | Time | What "done" looks like |
| --- | --- | --- |
| Confirm your contribution margin | 10 min | A real number, worked out, not estimated |
| Set the CAC ceiling and the kill rule | 5 min | Both written down, from your own maths |
| Build one ad set per cleared angle | 20 min | Same audience, same placement, only the creative changes |
| Set the daily budget per ad set | 5 min | A total you can actually sustain across every ad set combined |

4. **Open the workbook,** fill the yellow cells on the Plan tab, read the five checks,
   then list your ad sets on the Ad sets tab.

**Test: [product name]**

| | |
| --- | --- |
| Product | |
| Owner (a name) | |
| Batch (B03 and B04 versions, and the B05 clearance date) | |
| Ad platform and account | |
| Date this plan was written | |

## 2. The structure: isolate the variable (lecture 7.1)

An ad account is the instrument that tells you which angle wins. Structured wrong, it
burns budget and tells you nothing.

| Setup | What is being compared | What you learn |
| --- | --- | --- |
| One ad set with several creatives mixed in | Whichever the algorithm happens to favour early | Almost nothing about the angles |
| One ad set per angle, same budget, same audience | Angle against angle, cleanly | Which angle actually performs, isolated from everything else |

```text
CAMPAIGN: [product, first test]
  Ad set 1: [angle]    Budget: X
  Ad set 2: [angle]    Budget: X
  Ad set 3: [angle]    Budget: X
  ...
Same audience, same placement, same budget in every ad set.
Only the creative angle changes.
```

Isolating angles this cleanly costs some delivery efficiency in the short term. You
are deliberately trading a little of that for an answer you can trust.

| Structure check | Your answer |
| --- | --- |
| Number of ad sets (one per cleared angle) | |
| The audience, identical in every ad set | |
| The placement, identical in every ad set | |
| The one thing that differs (the angle), and nothing else | |
| Ad filenames, from the naming standard (B06) | |

## 3. The numbers (lectures 7.2 and 7.5)

The five decisions, in the order the workbook asks them:

| # | Decision | How to work it out | Your number | Source |
| --- | --- | --- | --- | --- |
| 1 | Contribution margin per order | Order value minus product and fulfilment cost, minus other per-order costs (payment fees, shipping, returns) | | |
| 2 | CAC ceiling | Your margin multiplied by a share you choose. The course uses roughly 70% of margin as its rule. State the share you use and why | | |
| 3 | Ad sets and daily budget per ad set | Enough spend per ad set to reach a real signal without overcommitting. Total across all ad sets must be sustainable | | |
| 4 | Kill rule | About two days of one ad set's daily budget, with none of your key signal | | |
| 5 | The key signal | A behaviour, not a softer metric. Lecture 7.2 uses add-to-cart because it is someone doing something. Pick the one that fits what you sell | | |

Why a hard kill rule: without one, the decision becomes "give it one more day, the
algorithm is still learning", spend continues, and nothing is learned. With one, the
call is made and the budget moves to an ad set that is showing signal. Write the rule
here and do not renegotiate it during the test.

The ratio matters more than any specific figure. The course's own example kills at
about two days' spend with zero of the key signal. Your figures come from your
margin, not from the example.

## 4. Reading small numbers honestly (lecture 7.4)

The kill rule protects your budget. These three questions protect you from fooling
yourself with what is left. No formula changes how much data a small budget can
produce, and this worksheet does not pretend one does.

```text
BEFORE CALLING A WINNER, ASK:
1. How many conversions does the leading ad set actually have?
   Single digits: treat the lead as a hint, not a verdict.
2. Would swapping one or two results change the story?
   If yes, the result is fragile, not real.
3. Has this ad set cleared the kill rule with room to spare,
   not just barely?
```

Three conversions to one is not a result. It is two coin flips landing the same way.
The workbook's status column says "Hint, not a verdict" for any ad set with fewer than
ten orders, and "Enough orders to read" above that. The ten comes from the lecture's
"single digits" wording. It is a prompt to ask the three questions, not a statistical
test.

| For each ad set you think is winning | Your answer |
| --- | --- |
| Orders so far | |
| Would one or two results swapped change the story? | |
| Cleared the kill rule with room to spare? | |
| Decision (and who makes it) | |

## 5. The Ad sets tab

One row per ad set: the angle (B01), the ad file (B06), spend so far, key signal
count and orders. The tab then shows:

| Column | What it does |
| --- | --- |
| Cost per order | Spend divided by orders, once there is an order |
| Against the CAC ceiling | Under or over the ceiling you set |
| Status | KILL when spend has reached your kill figure with zero of your key signal; otherwise Running, a hint, or enough orders to read |

Record each decision with its date, and write it back to the asset library (B06).
Every winner, loser or noise call goes into that record.

## 6. Honest test

- Is every number from your own margin, with its source written next to it?
- Was the kill rule fixed before any result existed?
- Is the daily total something you can sustain for the whole test?
- Is it one angle per ad set, with everything else identical?
- Did you call anything a winner on single-digit orders?
- Did the ad being tested clear pre-flight (B05)?

## 7. Open gaps

| Section | What is missing | Owner and date |
| --- | --- | --- |
| | | |
