# B08 · The Results Scorecard (Winner / Loser / Noise)

Part of *AI UGC Video Ads*. Built in lecture 8.5, the Section 8 workshop, from
lectures 8.1 to 8.4. The companion file is `B08-results-scorecard.xlsx`: an empty
workbook that applies the decision tree from lecture 8.2 and the iterate-or-new-angle
rules from lecture 8.4 to one ad set per row. Nothing in it is pre-filled.

Use it on the test you built in B07 and the ads you cleared in B05. If you have no
live data yet, score the last account you ran taste-only, before this course, using
whatever numbers you can recall or reconstruct, and say in the row that they are
reconstructed.

---

## 1. How to use this

1. **Name the objective and its metric before you look at any result** (section 2).
   A great click-through rate on the wrong objective is not a good result. It is an
   answer to a question you were not asking.
2. **Set the top block first** (CAC ceiling, kill spend, the frequency at which you
   treat a winner as tiring), copying the first two from your testing worksheet (B07).
   Decide the third now, not while looking at a tired ad.
3. **Score one ad set per row,** about fifteen minutes each:

| Step | Time | What "done" looks like |
| --- | --- | --- |
| Name the objective and the metric | 3 min | Written down before you look at results |
| Run the three-question tree | 5 min | An honest verdict, including noise if that is what it is |
| Check frequency, if it is a winner | 2 min | A real number, not a guess |
| Decide the next action | 5 min | Keep running, refresh or retire, with a reason |

4. **Expect noise and losers.** Most ad sets in a real test land in the noise bucket or
   the loser bucket, not winner. That is the accurate result, not a disappointing one.
   The workbook flags a sheet where every ad set is a winner.
5. **Write every verdict back to the asset library (B06)** with its date.

**Scorecard: [product / test]**

| | |
| --- | --- |
| Product | |
| Owner (a name) | |
| Test and date range | |
| Testing worksheet (B07) version | |
| Where the numbers come from (platform, export date) | |

## 2. Step 1: the right metric for the objective (lecture 8.1)

Different questions need different answers. Read each ad set against the objective you
set before the test, not the one that happens to look flattering now.

| Objective | The real question | The metric that answers it |
| --- | --- | --- |
| Cold awareness | Does the hook actually stop the scroll? | Thumb-stop rate, hook retention |
| Consideration | Does the offer earn a real look? | Click-through rate, landing page engagement |
| Conversion | Does the whole funnel actually sell? | Cost per purchase, against your CAC ceiling |

A vanity metric moving in the right direction feels like good news. Check it against
the objective first. The same ad can be read against awareness when shown to a cold
audience and against conversion when shown to a warmer one.

## 3. Step 2: the three-question tree (lecture 8.2)

Every result sorts into exactly three buckets. Most people only use two. The third,
noise, is the one that protects you.

```text
1. Cleared the kill rule with real margin?       No  -> Loser
2. Beats the CAC ceiling by a swap-proof gap?    Yes -> Winner
3. Sample small enough that the swap test flips  Yes -> Noise: keep running
   the result?                                   No  -> Loser
```

Only one path ends at Winner. The questions are yours to answer, from your numbers:

| Question | How to answer it honestly |
| --- | --- |
| Cleared the kill rule with real margin | Spend past your kill figure with the key signal present, and not just barely (B07, section 3) |
| Beats the CAC ceiling by a swap-proof gap | Cost per order is under the ceiling, and swapping one or two results would not change the story (B07, section 4) |
| Sample small enough that the swap test flips it | Single-digit orders are a hint, not a verdict. If one or two orders the other way would reverse the call, it is noise |

The workbook applies the tree to your three Yes or No answers. It cannot judge them
for you. It shows spend, orders and cost per order beside them so you can.

## 4. Step 3: fatigue, if it is a winner (lecture 8.3)

A winner does not fail. It wears out. A tired winner and a loser that never worked can
look identical on a dashboard and need different responses.

| Signal | Never-worked loser | Fatigued winner |
| --- | --- | --- |
| History | Never cleared the kill rule | Genuinely won, per the tree |
| Frequency | Usually still low | Climbing, often past 3 or more |
| The fix | Kill it | Refresh the creative, keep the angle |

Fatigue is predictable, not sudden. Watch frequency on every winner, not just its
performance. By the time click-through alone shows a problem, you have already paid
tired-ad prices for days. The frequency at which you act is your decision, written in
the top block. The "past 3" in the lecture is an observation from its example, not a
rule for your account. Your own watchlist and refresh cadence is B09.

## 5. Step 4: iterate or new angle (lecture 8.4)

"Make something new" hides two different jobs. A refresh reuses what worked. A new
angle starts over from the map.

| Situation | What it means | The move |
| --- | --- | --- |
| Never cleared the kill rule | The angle itself never landed | New angle, never a refresh |
| Winner, tired for the first time | The cut wore out, the angle did not | Refresh: same angle, new cut |
| Refreshed once already, tired again quickly | The whole angle is wearing out | New angle, retire this one |

Two patterns across cycles:

| Pattern | What you see | The call |
| --- | --- | --- |
| A: the angle still has life | The refreshed cut recovers close to the original's performance and runs a comparable healthy stretch | Refresh again |
| B: the angle is spent | The refreshed cut never fully recovers, or tires in a fraction of the first cut's runtime | Retire the angle and go back to the map |

A refresh is cheap, which quietly biases you toward refreshing even when the data says
Pattern B. Easy is not the same as correct. The workbook's "Next action" column follows
this table from the answers you give.

## 6. The workbook

| Column group | What it does |
| --- | --- |
| Top block | CAC ceiling and kill spend from B07, and your fatigue frequency |
| Objective and metric | A dropdown, then the metric that answers it |
| Spend, orders, signal, cost per order | The evidence beside your judgement |
| The three Yes or No answers | The tree's inputs. You answer them |
| Verdict | Winner, Noise: keep running, or Loser, from the tree |
| Frequency, refreshed before, pattern | Only for winners |
| Next action | Keep running, refresh, refresh again, retire, or new angle, with a reason you write |
| Tally and four checks | Winners, noise and losers; and checks that the objective was named, the ceiling and kill rule set, every winner checked for fatigue, and not everything called a winner |

## 7. Honest test

- Was the objective written down before you read the numbers?
- Did every Yes come with evidence, and would one or two swapped orders change it?
- How many ad sets did you call winners? If most, how hard did you apply the swap test?
- Did any winner have no frequency checked?
- Is any "refresh" really a Pattern B angle that is cheaper to cut again?
- Is every verdict written back to the asset library?

## 8. Open gaps

| Section | What is missing | Owner and date |
| --- | --- | --- |
| | | |
