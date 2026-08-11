# Job: KDP telemetry (weekly)

You are running inside the udemy repo. Read the KDP report exports the user
dropped into `growth/data/` (KDP dashboard exports: orders, KENP reads, and
any rank/review notes they pasted) and turn them into one honest page.

If `growth/data/` has nothing newer than the last report, write a one-line
report saying so and stop. Never estimate sales you cannot see, and never
scrape Amazon; the inputs are the user's own exports only.

## Produce `growth/queue/<iso-week>/kdp-report.md`

1. **Trend table, one row per published title** (the portfolio ships
   sequentially, so early on this is one row): units by format, KENP reads,
   revenue, and (if provided) best rank and review count: this week, last
   week, 4-week average.
2. **Review velocity:** new ratings this week and the ratio of ratings to
   estimated sales. Below roughly 1 rating per 40 sales, flag that the
   back-matter ask may be weak or mispositioned.
3. **Signal reading, honestly hedged:** what moved, the most plausible cause
   from what actually happened this week (a promo, a post, a price change:
   check the queue folders for what shipped), and what is noise. Rank moves
   without a cause are usually noise; say so rather than inventing stories.
4. **One recommended action** for next week, chosen from: price ladder step
   (per `docs/05-kdp-playbook.md` §5), a Select promo day, an ads bid/keyword
   change, a back-matter tweak, or nothing ("hold" is a valid recommendation
   and often the right one).

## Boundaries

- No review-generation tactics beyond the honest asks defined in the playbook.
- If the data suggests the book itself has a quality problem (review text
  recurring on one complaint), say that plainly. The fix is a revision, and
  KDP allows uploading one; that beats any promo.
