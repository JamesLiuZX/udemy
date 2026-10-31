# A10 · Model Selection Scorecard

Part of *AI Product Skills for PMs & Analysts*. Built in lecture 7.4. The
companion file is `A10-model-selection-scorecard.xlsx`. It opens in Excel,
Google Sheets and LibreOffice, uses no macros, and is empty: no model, score,
price or latency is filled in for you. Use it to choose a model from your own
evidence instead of a leaderboard.

---

## 1. How to use this

1. **Write the quality floor first, in writing, before any cost number goes in
   the sheet.** It is the pass rate on your golden set that the feature has to
   clear, taken from the acceptance criteria in the PRD (A01). Write it even if
   it feels obvious. An "obvious" threshold has a way of drifting once a cheap,
   fast option is sitting in the same table looking tempting.
2. **Run each candidate through the same golden set** (A02), under identical
   conditions: the same prompt, the same cases, the same rubric (A05) and the
   same judge, whether that judge is a person or a calibrated LLM judge. Change
   any of those between rows and the pass rate column becomes unrelated numbers
   that happen to share a table. The sheet asks you to confirm this for each row.
3. **Enter, per candidate:** the pass rate, the cost per call (from the model in
   A09), and the p95 latency in seconds, measured, not quoted.
4. **Read the sheet in this order.** The column "Clears the floor?" removes any
   model below the floor first. Cost and latency ranks are then worked out only
   among the models that remain. A model that fails the floor is not a cheaper,
   slower version of an acceptable answer. It is a model that fails the
   threshold.
5. **Argue the real trade-off among what is left**, and write the reasoning
   down next to the choice. "We picked flagship" cannot be defended or revisited.
   "We picked flagship because the failure cost outweighs four times the spend"
   can.
6. **Put a recheck date on it** and rerun it then (section 4).

## 2. Using the workbook

1. Make a copy of `A10-model-selection-scorecard.xlsx`.
2. At the top, fill the feature, the date, the recheck date, the quality floor
   and where it came from, the golden set and rubric versions, the judge, and
   the cost unit.
3. In the candidates table (room for six), enter the model, the version and
   date you tested, the pass rate, cost, p95 latency, and Yes or No for
   identical conditions.
4. "Clears the floor?", the cost rank and the latency rank calculate. A failing
   model shows "No: out" in red and gets no rank.
5. The six checks should read OK before you show the sheet to anyone: floor
   written, at least two candidates scored, cost and latency present for every
   scored candidate, identical conditions confirmed, at least one candidate
   clears the floor, and a recheck date set.
6. Fill in the decision block at the bottom: the chosen model, what you gave up
   and why it is worth it, who decided, and when.

If nothing clears the floor, the sheet says so. That is a finding about the
feature or the prompt, not a reason to lower the floor.

## 3. Worked example, from lecture 7.4

An example of how to read the table, not data to reuse. Suppose the feature's
floor is 85%.

| Model | Pass rate (your golden set) | Cost per call | p95 latency |
| --- | --- | --- | --- |
| Flagship | 94% | 8 cents | 3.2s |
| Mid-tier | 89% | 2 cents | 1.4s |
| Budget | 71% | Half a cent | 0.6s |

The budget model is out before its price or speed matter. Among the two that
remain, the decision is five points of pass rate against four times the cost and
double the latency. A feature where a wrong answer is expensive (see the blast
radius sort in A08) leans toward paying for the five points. A feature where
speed is the product experience, and both models clear the floor comfortably,
leans the other way. The scorecard makes that a visible choice. It does not make
it for you.

## 4. Limits

- **It goes stale.** Providers update pricing and ship models constantly. The
  mid-tier option that won this quarter may be beaten next month. Rerun it on the
  recheck date. Keep the golden set reusable so a rerun takes an afternoon and
  not a fresh round of choosing cases.
- **Three dimensions only.** It does not cover caching, batching or routing
  (lecture 7.3), or whether the feature still makes money per user at the winning
  model's price (lecture 7.5, the margin trap). A model can win this scorecard
  and the feature can still lose money.
- **Latency detail comes later.** p95 is a single column here. Perceived speed
  and latency budgets are lecture 7.6.
- **Your numbers are only as good as your golden set.** A fifty-case set with an
  empty bucket will flatter every row equally. Check A02's open gaps first.
- **Benchmarks are not a substitute.** If you only have a benchmark number for
  one candidate and an impression for another, that is the gap this scorecard
  exists to close.

## 5. Where this fits

A02 supplies the cases, A05 the rubric, and A09 the cost per call. This sheet
puts the three on one page for every candidate, ahead of the decision in the
unit-economics workshop (lecture 7.7).
