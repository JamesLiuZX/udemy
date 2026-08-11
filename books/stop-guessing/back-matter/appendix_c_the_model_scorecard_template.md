# Appendix C: The Model Scorecard Template

Chapter six's rule for reading this scorecard: check the pass-rate column first, alone, against the threshold chapter three's spec actually set. A model that fails the quality floor is disqualified before its price or its speed enter the conversation at all. Only compare cost and latency between models that already clear the bar.

## The template

Score every candidate model against the identical golden set, the identical rubric, under identical conditions. Change any of those between rows and the pass-rate column stops being a comparison and becomes unrelated numbers sharing a table.

| Model | Pass rate | Meets floor? | Cost/call | p95 latency | Notes |
| --- | --- | --- | --- | --- | --- |
| | | | | | |
| | | | | | |
| | | | | | |

- **Pass rate**: from your own golden set and rubric, chapters four and five, never a vendor's published benchmark alone.
- **Meets quality floor?**: yes or no, checked against the threshold in your spec, before anything else on this row is allowed to matter.
- **Cost per call**: measured against your golden set's real token counts, chapter six's discipline, not a demo conversation.
- **p95 latency**: under realistic concurrent load, chapter eleven's standard, never a quiet single-user test.
- **Notes**: anything that would change the recommendation, a stated training cutoff, a known weak category, a contamination concern from chapter eleven's benchmark-reading section.

## Worked example: three candidates scored

Adapted from chapter six's own table, for the support-reply assistant.

| Model | Pass rate | Meets floor (85%)? | Cost/call | p95 latency | Notes |
| --- | --- | --- | --- | --- | --- |
| Flagship | 94% | Yes | 8 cents | 3.2s | Justified by refund-agent failure cost |
| Mid-tier | 89% | Yes | 2 cents | 1.4s | Best pick, quarter of flagship's cost |
| Budget | 71% | **No** | Half a cent | 0.6s | Disqualified; price, speed moot |

Read the budget row the way chapter six insists on reading it: seventy-one percent isn't a cheaper, faster version of an acceptable answer. It's a model that fails the threshold, and no saving on the other two columns changes that fact. The real decision left standing, once budget is out, is whether flagship's extra five points of pass rate justify four times mid-tier's cost and more than double its latency, a trade-off with no universal answer, only a reasoned one written down next to the choice.

## Before you call this comparison done

- Every candidate scored against the identical golden set and rubric, not different samples
- The quality floor applied first, before cost or latency entered the comparison
- Token counts and costs measured from real golden-set cases, not a demo conversation
- Latency measured as p95 under realistic concurrent load, not a single quiet test
- The final choice written down with its reasoning, not just the model name, so it can be revisited intelligently later
- A re-check date set, since a model that wins this comparison today can be superseded within months
