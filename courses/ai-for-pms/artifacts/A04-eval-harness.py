"""A04 · Eval harness in Python. Part of AI Product Skills for PMs & Analysts.

Reads the Scores tab of A03, exported as CSV, and prints the pass rate for each
bucket. Usage:  python3 A04-eval-harness.py golden_set_scores.csv [--min 0.9]
"""
import csv, sys
from collections import defaultdict

rubric = ["q1", "q2", "q3", "q4", "q5", "q6"]
path = next((a for a in sys.argv[1:] if not a.startswith("--")), "golden_set_scores.csv")
floor = float(sys.argv[sys.argv.index("--min") + 1]) if "--min" in sys.argv else None
totals, passes, bad = defaultdict(int), defaultdict(int), []

with open(path, newline="", encoding="utf-8-sig") as f:
    reader = csv.DictReader(f)
    reader.fieldnames = [h.strip().lower() for h in reader.fieldnames]
    missing = [c for c in ["bucket"] + rubric if c not in reader.fieldnames]
    if missing:
        sys.exit(f"Missing column(s): {missing}. Found: {reader.fieldnames}")
    for line, row in enumerate(reader, start=2):
        bucket = (row["bucket"] or "").strip().capitalize()   # sheet matching ignores case
        scores = [(row[q] or "").strip() for q in rubric]
        if not bucket and not any(scores):
            continue                                  # an empty row in the sheet
        if not bucket or any(s not in ("0", "1") for s in scores):
            bad.append(line)                          # never guess; report it
            continue
        totals[bucket] += 1
        if all(s == "1" for s in scores):
            passes[bucket] += 1

for bucket in sorted(totals):
    rate = passes[bucket] / totals[bucket]
    print(f"{bucket:20s} {passes[bucket]}/{totals[bucket]}  {rate:.0%}")
if bad:
    sys.exit(f"Rows not counted (blank bucket or a score that is not 0 or 1): lines {bad}")
if floor is not None and any(passes[b] / totals[b] < floor for b in totals):
    sys.exit(f"A bucket is below the {floor:.0%} floor.")
