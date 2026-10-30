# A04 · Eval Harness (Python)

Part of *AI Product Skills for PMs & Analysts*. Read line by line in lecture
4.7. The file is `A04-eval-harness.py`. It does the same arithmetic as the A03
spreadsheet, so a computer can run it without you. It uses only what ships with
Python 3, so there is nothing to install.

---

## 1. How to use this

1. In the A03 spreadsheet, export the **Scores** tab as CSV
   (File, Download, CSV in Google Sheets; Save As, CSV in Excel).
2. Put the CSV and `A04-eval-harness.py` in one folder.
3. Run: `python3 A04-eval-harness.py golden_set_scores.csv`
4. You get one line per bucket: passed over scored, and the pass rate.
5. **Check it against the spreadsheet.** The Dashboard tab and this output must
   agree for every bucket. Two independent workings of the same arithmetic
   agreeing is the test. If they do not, trust neither until you find out why.

Optional floor, for the automated check described in the lecture: add
`--min 0.9` and the script exits with an error if any bucket's pass rate is
below 90%. That non-zero exit is what lets a build pipeline block a change. Wiring
it into a pipeline is a job for an engineer, about five minutes of their time.

## 2. What the script does

- Reads the CSV and lower-cases the column headers, so `Q1` and `q1`, `Bucket`
  and `bucket` all work.
- Counts, for each bucket, the cases scored and the cases where all six rubric
  questions are 1. That is the same rule as the spreadsheet's Overall column.
- Skips rows that are completely empty (the A03 sheet exports spare rows).
- Treats bucket names the way the spreadsheet does, ignoring capital letters.
- Prints the same layout as lecture 4.7.

## 3. How it differs from the lecture's short version

Lecture 4.7 shows the core of the script. This file has that core plus the
guards below, because the lecture itself warns that a script which trusts its
input will crash or silently miscount.

| Guard | What it prevents |
| --- | --- |
| Header names are normalised | A `KeyError` on `Bucket` versus `bucket` |
| Empty rows are skipped | A crash on the spare rows in an exported sheet |
| A blank bucket or a score other than 0 or 1 is reported by line number and the script exits with an error | A case silently dropped from a bucket, or a "yes" counted as something |
| Missing columns stop the script and list what was found | A confusing traceback |
| `--min` floor | Nothing blocks a change, when you want it to |

A row that is reported is not counted. Fix the CSV and run again. The script
does not guess.

## 4. Limits

- It scores nothing. Every 1 and 0 comes from your rubric and your validated
  judge, as with the spreadsheet.
- It reads a CSV, so it is only as good as the export. Check the header row
  before you suspect the script.
- A bucket with a handful of cases moves a lot on one score. Read the
  `passed/scored` counts next to the percentage.

## 5. Where this fits

A02 is the golden set, A05 the rubric, A03 adds up the scores in a spreadsheet,
and this script adds them up without anyone opening a file. The next lecture
asks whether a change in a pass rate is real or noise.
