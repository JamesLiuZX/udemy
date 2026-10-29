# A03 · Eval Harness (Spreadsheet)

Part of *AI Product Skills for PMs & Analysts*. Built in lecture 4.6. The file
is `A03-eval-harness-spreadsheet.xlsx`. It opens in Excel, Google Sheets and
LibreOffice, uses no macros and no add-ins, and is empty: it contains no
scores. Use it to turn rubric scores into a live pass rate for each bucket of
your golden set.

---

## 1. How to use this

1. **Make a copy of the file.** Keep the original blank so you can start again.
2. **Scores tab.** One row per case. Type the case ID, pick the bucket from the
   dropdown, then enter 1 (pass) or 0 (fail) for each of the six rubric
   questions, Q1 to Q6. The dropdowns refuse anything else.
3. **Overall (column I)** calculates itself: 1 only if all six questions
   passed, otherwise 0. There is no partial credit, because the rubric is pass
   or fail. A row with some scores missing shows "incomplete" rather than a
   number.
4. **Dashboard tab** reads the Scores tab. For each bucket it shows the number
   of cases scored, how many passed, and the pass rate, plus the all-cases line.
5. **Read the checks (Dashboard B11 to B13).** The first two should read OK
   before you trust any number. The third just compares cases scored with the
   fifty planned.
6. **To see why a bucket dropped,** filter the Scores tab to Overall = 0 and
   one bucket. Those are the cases to go and read.

## 2. The two formulas doing the work

```text
Scores tab, column I (Overall), row 2:
=IF(COUNT(C2:H2)=0,"",IF(COUNT(C2:H2)<6,"incomplete",IF(SUM(C2:H2)=6,1,0)))

Dashboard tab, pass rate for one bucket (E4 is Common path):
=IF(C4=0,"",AVERAGEIF(Scores!$B$2:$B$111,A4,Scores!$I$2:$I$111))
```

The Overall formula is lecture 4.6's `=IF(SUM(C2:H2)=6,1,0)` wrapped so that a
half-scored row is flagged instead of silently counting as a fail. The pass
rate is the lecture's average-if. Because Overall is only ones and zeros, the
average is the pass rate. The same formula serves all four buckets: only the
bucket name changes.

## 3. The failure it is built to catch

A case with a bucket the sheet does not recognise, for example "Comon path",
drops out of every bucket average and nothing errors. Two guards are in the
file. The bucket column is a dropdown, so a typo cannot be typed. And check B11
compares the cases that have a score with the cases the four buckets counted;
if they differ it turns red and says so. Pasting values over the dropdown skips
the first guard, which is why the second exists.

Spreadsheet matching ignores capital letters, so "Common Path" and "Common
path" count as the same bucket. A misspelling or a stray space is what drops a
case.

## 4. Check it before you trust it

Build your fifteen calibration cases from A05 into the Scores tab first. You
already hand-scored them twice, so you know the answer. If the Dashboard's pass
rate matches your hand tally, the sheet is right. If it does not, trust the
hand tally and look for the typo.

## 5. Limits

- It does not score anything. A human, or a judge you have validated, enters
  every 1 and 0. Past a few hundred rows, formulas that scan whole columns slow
  down. The formulas read rows 2 to 111, so up to 110 cases work as shipped.
- The "Target cases" column holds the 20, 15, 10, 5 split from A02. Change it if
  you changed your plan.
- Percent pass rates on five or ten cases move a lot with a single score. Read
  the counts next to the percentages.

## 6. Where this fits

A02 is the golden set, A05 is the rubric that scores it, and this sheet adds up
the scores. The Python version, A04, produces the same numbers from a CSV
export of the Scores tab, so you can run the check in CI later.
