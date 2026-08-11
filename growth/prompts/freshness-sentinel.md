# Job: freshness sentinel (weekly)

You are running inside the udemy repo. AI facts decay fast, and a confidently
wrong price or model name in a lecture is the fastest bad review in this
genre. Find what has decayed. Do not edit lectures; report only.

## The registry

`growth/facts.yaml` lists decay-prone claims, one entry per claim:

```yaml
- lecture: "7.1"
  claim: "GPT-4o input pricing $2.50 per million tokens"
  source: "https://openai.com/api/pricing"
  checked: "2026-08-11"
```

If the file does not exist yet, create it by scanning all lecture narration
and slides for: model names, per-token or per-seat prices, context window
sizes, rate limits, "as of <date>" statements, product names that version
(then still do the check below on what you found).

## The check

1. For each entry, fetch the source page and compare the claim.
2. Classify: `current`, `changed` (say what it is now, quote the page),
   `page-moved` (find the successor page if obvious), or `unverifiable`.
3. Also skim the providers' pricing/model pages for *new* facts that
   contradict any lecture even if unregistered (new flagship model names are
   the classic one).

## Output

Write `growth/queue/<iso-week>/freshness-report.md`:

- A table: lecture, claim, status, what changed, suggested fix wording.
- A verdict line per affected lecture: `re-verify` (claim changed materially:
  the lecture's `verified: true` is now stale and the instructor must re-sign
  after the fix) or `cosmetic` (wording drift only).
- Update `checked:` dates in `growth/facts.yaml` for everything you checked,
  and add entries for new decay-prone claims you noticed.

Lectures listed as fastest-decaying in `docs/03-launch-playbook.md` §6
(1.4, 2.6, 7.1, 7.4) get checked even if their registry entries look fresh.
