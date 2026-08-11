# Appendix B: The Risk Register Template

Chapter eight's standard for a working row: scored honestly, owned by one named person, given a specific mitigation, and dated for review. A register missing any one of those four is decoration. This appendix is the blank instrument, plus a fully worked example, so the standard is easy to hold your own draft against.

## The five categories

| Category | The question it answers |
| --- | --- |
| Prompt injection | Can content the feature reads be mistaken for an instruction it should follow? |
| Data and privacy | What personal data reaches the model, where does it go after, and can the vendor train on it? |
| Regulatory | Does this feature's use case, not its model, carry a real legal obligation, and does it reach a jurisdiction that imposes one? |
| Bias and fairness | Does the pass rate hold steady across the different people who actually use this, measured, not assumed? |
| Incident response | Is there a quality-specific signal, a named owner, and a tested kill switch for the day prevention wasn't enough? |

## The template

One row per risk. Don't try to fill all five categories in a single sitting; three real, specific rows are worth more than five vague ones.

| Category | Risk (specific, not a topic) | Owner (one name) | Mitigation (a concrete change, or "not yet, due [date]") | Status | Review date |
| --- | --- | --- | --- | --- | --- |
| | | | | | |
| | | | | | |
| | | | | | |
| | | | | | |
| | | | | | |

A risk written as a topic, "prompt injection is a risk we should think about," owned by "the team," isn't a register row yet. A risk written as a specific, checkable sentence, "an uploaded PDF's text can currently reach the system prompt unescaped," owned by one person with a real date, is a row someone can actually close.

## Worked example: five filled rows

Adapted from chapter eight's own worked table, for an internal tool that lets employees search company documents in plain language.

| Category | Risk | Owner | Mitigation | Status | Review date |
| --- | --- | --- | --- | --- | --- |
| Prompt injection | A document with embedded instructions could get the assistant to summarize files outside the requester's own access | J. Okafor | Retrieval step returns text only, no tool access; access control checked before retrieval runs, not after | Mitigated | 2026-03-01 |
| Data and privacy | Search queries are currently logged in full, including anything a user pastes | J. Okafor | Redact query text before logging; retain only query length and result count | Open, due 2026-02-15 | 2026-02-15 |
| Regulatory | Unclear whether this tool's output could be repurposed to help screen internal candidates for promotion, which would move it into a heavier obligation tier | R. Singh | Confirm intended use with legal; add an explicit scope restriction to the product spec if promotion screening is ever proposed | Open, due 2026-02-20 | 2026-02-20 |
| Bias and fairness | Golden set has no cases in languages other than English | R. Singh | Pull 15 non-English queries from real logs; score them separately before the next release | Open, due 2026-02-01 | 2026-02-01 |
| Incident response | No alert exists if answer quality drops; only latency and error rate are currently monitored | R. Singh | Add a weekly sampled-review alert; kill switch exists but has never been tested | Open, due 2026-03-15 | 2026-03-15 |

Notice the status column carries as much weight as the mitigation column. One row here is genuinely closed. Four are open, dated, and owned, which is a materially more honest state than being silently absent from the register altogether. Anyone reviewing this table before launch knows exactly what's covered and what still needs attention, which is the entire reason to write any of it down.

## Before you call this register done

- Every row names a specific, checkable risk, not a topic
- Every row has exactly one owner, a real person, not "the team"
- Every mitigation is a concrete change, or an honest "not yet, due [date]," never a meeting that might happen
- All five categories have a real entry, even if some are still open
- A review date exists on every row, and closed rows get re-checked, not filed away permanently
- The incident-response row names a quality-specific signal and a kill switch that's actually been tested, not just assumed to work
