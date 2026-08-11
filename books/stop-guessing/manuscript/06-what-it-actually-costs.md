# What It Actually Costs

"What does this actually cost us?" The question came from finance, in the quarterly budget review, aimed at the support-reply feature that had cleared its threshold two months earlier and was now running in production. The answer felt easy: "About four cents a conversation." A few heads nodded. Four cents sounded like nothing, and it wasn't a lie.

Finance asked a second question, quieter, the kind that only lands if you've priced something before: "Four cents times how many conversations, though?" Nobody in the room had that number ready. The feature had passed every quality bar in chapters four and five. Nobody had ever multiplied its per-conversation cost out to what the company was actually spending on it, and the meeting adjourned with a follow-up action item that should have existed before launch, not two months after.

## Three multiplications, not one

This is the mistake almost every team makes with a new AI feature, and it's an easy one to miss, because the first number, the per-conversation cost, is the one you get for free. You run the feature, you check the bill, you feel reassured, and you stop there. The two multiplications that actually matter to anyone who owns a budget only happen if somebody deliberately does them.

| Level | Calculation | Result |
| --- | --- | --- |
| Per conversation | (8,000 in-tokens x 3/M) + (1,200 out-tokens x 15/M) | $0.042 |
| Per user, per month | $0.042 x 4 conversations | $0.168 |
| All users, per month | $0.168 x 50,000 active users | $8,400 |

Walk down that table the way the actual budget conversation walks down it, because each row answers a different question. The first row answers "does this work economically at all," and four cents sounds fine. The second answers "is this a rounding error for one person," and seventeen cents a month still sounds fine. The third row answers the question that was actually being asked in that meeting, what this costs the company, and eight thousand four hundred dollars a month is the number that gets someone's attention in a way the first two never do. Same underlying cost, at three different scales, producing three completely different reactions.

Each multiplier in that table is a real assumption, not an arbitrary round number, and deserves the same scrutiny as the token counts. Four conversations a month is a claim about how often someone actually returns to this feature. Fifty thousand active users is a claim about where the product is today, or realistically headed. Change either one and the bottom row moves by exactly that proportion, which is worth showing live in the room if anyone pushes back on the total.

## Measured, not guessed

The two token counts feeding the first row, eight thousand in and twelve hundred out, can come from two very different places, and only one of them is honest.

The tempting source is a handful of test conversations run by the team that built the feature: naturally shorter and tidier than what real users produce, and the version that happens to make the launch deck look best is the one that tends to survive. The right source is the golden set from chapter four, the same fifty real, deliberately messy cases already sitting in the repository. Run token counts against those instead of against a demo, and the number is whatever it actually is, not whichever number looked good in a rehearsal.

This matters more than it sounds like it should, because the gap between a demo estimate and a real one doesn't stay the same size as it moves through the table. A token count that's thirty percent low at row one is thirty percent low at the total-spend row too, and the total-spend row is the one somebody actually budgets against. A golden set built with the coverage discipline from chapter four has a second advantage here beyond honesty: it's already stratified across common, difficult, and messy cases, so the token counts it produces reflect the genuine mix of short asks and long ones, not whichever single conversation the team happened to rehearse before the meeting.

[PULLQUOTE: A token count that's thirty percent low at the per-conversation row is thirty percent low at the total-spend row too, and the total-spend row is the one someone actually budgets against.]

Be honest, too, about which numbers in this model are measured and which are still guesses. Token counts can be measured precisely once the golden set exists. Conversations per user and total active users are informed estimates before real usage data exists, and they deserve to be labeled as exactly that: a clearly marked estimate, built from the closest real analogue available, not a number dressed up to look more certain than it is. A support-reply feature can reasonably borrow its usage estimate from ticket volume on the channel it's replacing. A feature with no real precedent at all should carry a labeled range, a low case and a high case, rather than one confident-sounding figure that's secretly a guess.

## Choosing a model without lying to yourself

Cost isn't the only number on the table once you're choosing which model to actually run this feature on, and comparing all three columns at once, quality, cost, and speed, is exactly how a team talks itself into the wrong row.

| Model | Pass rate (your golden set) | Cost per call | p95 latency |
| --- | --- | --- | --- |
| Flagship | 94% | 8 cents | 3.2s |
| Mid-tier | 89% | 2 cents | 1.4s |
| Budget | 71% | Half a cent | 0.6s |

Read the pass-rate column first, alone, against whatever floor chapter three's spec actually set for this feature. If that floor is eighty-five percent, the budget model is disqualified before its price or its speed enter the conversation at all. Seventy-one percent isn't a cheaper, faster version of an acceptable answer. It's a model that fails the threshold, and no saving on the other two columns changes that fact.

Notice, too, what makes this table trustworthy in the first place: every pass rate in it comes from the same fifty-case golden set, the same rubric, run once per candidate model under identical conditions, whether the judge doing the scoring is a person or the calibrated LLM-as-judge from chapter five. Change any of those between rows and the pass-rate column stops being a comparison and becomes three unrelated numbers that happen to share a table.

Once the disqualified model is gone, the real decision left standing is whether flagship's five extra points of pass rate justify four times the cost and more than double the latency over mid-tier. There's no universal answer to that trade-off. A feature where a wrong answer is genuinely expensive leans toward paying for the five points. A feature where speed is most of the product experience, with both remaining models already clearing the quality bar comfortably, leans the other way. Write the reasoning down next to the choice, not just the choice itself: "we picked flagship because the failure cost outweighs four times the spend" is a decision someone can revisit intelligently in six months. "We picked flagship" on its own is a decision nobody can argue with or defend, because the reasoning left the room the moment the meeting ended.

## The margin trap

Every dashboard you've ever used for a normal software feature treats more usage as unambiguously good, because serving one more page view costs the company close to nothing. An AI feature breaks that assumption quietly, because every single use carries the real, measurable cost from the model built earlier in this chapter, and that cost scales up exactly as usage does.

| Tier | Conversations/month | Cost | Allocated revenue | Margin |
| --- | --- | --- | --- | --- |
| Light user | 2 | 8 cents | $5.00 | +$4.92 |
| Heavy user | 40 | $1.68 | $5.00 | +$3.32 |
| Power user | 150 | $6.30 | $5.00 | -$1.30 |

Read the margin column, not the cost column, because the cost column looks harmless at every row: eight cents, a dollar sixty-eight, six dollars thirty, none of it alarming in isolation. Somewhere between forty and a hundred and fifty conversations a month, this feature crosses from genuinely profitable to actively losing money, on the exact users a product team would normally hold up as its retention success story. That crossover is the real finding here. Everything else in the table is the arithmetic that leads up to it.

Two dashboards can look at that same power user and reach opposite verdicts, and neither one is lying. The engagement dashboard sees a hundred and fifty conversations from the most active user in the segment and flags a win. The margin model sees $6.30 in real cost against $5.00 of allocated revenue and flags a $1.30 monthly loss, growing with every additional conversation. Both are reading the identical user honestly. The trap survives precisely because those two numbers usually live on two different dashboards, owned by two different teams, that rarely sit on the same page.

[KEY-INSIGHT: In June 2025, the AI coding tool Cursor moved its Pro plan away from a flat monthly rate that covered heavy use of frontier AI models toward usage-based credits billed at the underlying API rate, after enough users on expensive frontier models were costing the company more than their flat subscription brought in. The rollout produced unexpectedly large bills for some users and a public backlash over how unclearly the change had been communicated; Cursor's CEO issued a public apology and refunded the disputed charges. || Source: "Cursor apologizes for unclear pricing changes that upset users," TechCrunch, July 7, 2025.]

Notice which part of that story is the actual lesson and which part is a separate, avoidable mistake. The pricing change itself was the correct response to a real crossover: flat-rate revenue meeting a cost that genuinely scales with usage always eventually needs a structural fix, not a hope that usage stays low. The backlash was a communication failure layered on top of a sound economic decision, and it's worth treating those as two different problems with two different fixes. Get the crossover math right early, the way this chapter has walked through, and the pricing change can happen quietly, ahead of the users who'd actually be affected by it, instead of arriving as a surprise on someone's bill.

## This problem predates AI, it just used to be rare

It's worth being clear that the margin trap isn't a new failure mode invented by language models. It's an old one, and AI features are simply the first category of product where almost every single feature carries a real marginal cost, which makes a trap that used to catch one unlucky product a year into something worth checking by default.

Microsoft learned this the hard way in 2016, years before any of this book's subject matter existed, with a much simpler product: cloud storage. Office 365 had offered "unlimited" OneDrive storage to consumer subscribers on a flat monthly fee. Most users stored a modest, genuinely low-cost amount of data. A small number treated "unlimited" as a literal challenge: Microsoft later said some individual accounts exceeded 75 terabytes of storage, more than fourteen thousand times the average user's usage, all under the same flat subscription price as everyone else. Microsoft ended the unlimited tier in 2016 and capped consumer storage at 1TB.

[KEY-INSIGHT: In 2016, Microsoft discontinued unlimited OneDrive cloud storage for Office 365 consumer subscribers after finding that a small number of accounts had stored more than 75 terabytes of data each under a flat monthly fee, more than 14,000 times the average user's usage. Microsoft capped consumer storage at 1TB going forward. || Source: Microsoft OneDrive team announcement, reported by InformationWeek, "Microsoft Kills Unlimited OneDrive Storage, Blames User Abuse," November 2015.]

The shape is identical to Cursor's, a decade earlier and in a completely unrelated product category: a flat price meets a cost that scales with usage, and the heaviest users, the ones a growth dashboard would have celebrated, are the ones quietly losing the company money. What's different for an AI feature is the odds. Cloud storage only crosses into this trap when a genuinely unusual user shows up, fourteen thousand times average, rare enough that most companies never see it. An AI feature's per-use cost is real for every single user, light and heavy alike, which is why this chapter treats the crossover point as something to calculate before launch rather than something to notice after a support ticket from finance.

## Fixing it without punishing success

The tempting wrong conclusion here is that heavy usage is the problem. It isn't. Heavy usage is proof the feature works. The actual problem is a flat-rate structure that was never designed to track a cost that isn't flat, and the fix is pricing or limits that scale with cost the same way the cost itself already scales with usage: a tiered plan, a usage-based add-on past a threshold, or a generous but real cap with a clear upgrade path.

Design that fix before the power-user tier exists in large numbers. Retrofitting pricing onto users who are already used to unlimited use is a far harder, far more public conversation than shipping the structure correctly from the start, and it's the conversation Cursor's users had in public in 2025. Set the cap from your own measured crossover point, not a guess: generous enough that a genuinely typical user never touches it, specific enough that it sits comfortably above the point where this chapter's table turns negative. Then treat the whole model, tokens, usage estimates, and crossover point alike, as something to recheck on a schedule, not a one-time exercise filed away after launch. Prices change, models change, and usage patterns shift as a feature matures; a cost model built once and never revisited is exactly how a feature quietly stops making money without anyone noticing until finance asks the question that opened this chapter.

## Find your own crossover point

Take your heaviest real user on any AI feature you own, an actual account, not a hypothetical average, and run their real usage through this chapter's three-level model. If you can't produce that number within an hour, that's this chapter's finding on its own: cost and usage have never been checked against each other for this feature.

If you can produce it, compare the result against current pricing or limits. A margin that's still positive at your heaviest real user's usage is worth writing down and rechecking next quarter. A margin that's already negative is worth raising this week, in plain terms, before that user's usage pattern becomes normal instead of exceptional.

[TAKEAWAYS]

- Build the cost model three levels deep: per conversation, per user per month, and total monthly spend. Each level answers a different question, and only the last one is the one finance actually asked.
- Measure token counts from your golden set, never from a demo. A biased estimate at row one stays biased by the same proportion all the way to the total.
- Apply the quality floor before comparing cost or speed. A cheap, fast model that fails the threshold isn't a bargain, it's disqualified.
- Watch the margin, not just the cost. An AI feature's most engaged users can be its least profitable ones, invisible to any dashboard that tracks usage without tracking cost on the same page.
- Fix a margin problem with pricing that scales, not by discouraging the usage that proved the feature works. Design the fix before a power-user cohort makes it a public conversation instead of a private one.

[/TAKEAWAYS]

## Where this goes next

Chapter seven turns to a shape of feature this chapter's math doesn't cover on its own: an agent that takes several actions in a row with reduced human review between them, where the real risk isn't the cost of one call, but how fast a small per-step error rate compounds once nobody's checking each step before the next one runs.
