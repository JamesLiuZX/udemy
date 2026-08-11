# Metrics That Survive Production

The quarterly review opened with a chart everyone in the room liked: messages per session on the refund agent, up twenty percent over the previous month. Someone called it out as the headline of the update. Heads nodded, the way they'd nodded at a four-minute demo back in chapter one, and the meeting was ready to move to the next slide.

One person didn't move on. "Up twenty percent could mean people are getting real value and coming back for more. It could also mean the agent is getting it wrong on the first try often enough that people are retyping the same request three different ways before it lands. Which one is it?" Nobody in the room had a second number to answer with. The rising line was the only evidence anyone had brought, and a rising line, on its own, cannot tell delight from friction. Both look identical in a raw usage count.

## Why engagement alone lies about a probabilistic feature

Most product metrics were built on an assumption that held for years: a feature does the same thing every time it's used, so more usage reliably means more value. That assumption is exactly what chapter one spent its opening pages dismantling for a probabilistic feature, and it fails engagement metrics in a specific, costly way. An AI feature can generate more usage precisely because it's failing, every retry counting as another data point in a chart that leadership reads as success.

This doesn't make engagement a useless number. It means engagement alone was never built to answer the question that actually matters: is this feature good, or is it merely being used. For a deterministic feature those two questions collapse into one. For a feature that behaves differently every time it runs, they can point in opposite directions, and only a second metric, checked deliberately, tells you which one you're looking at.

## Three metrics built for this

| Metric | What it actually measures | Why it survives |
| --- | --- | --- |
| Adoption | Of everyone who could use it, who actually does | Distinguishes real reach from a loud minority |
| Acceptance | How often a suggestion is kept, not edited or discarded | A direct quality signal, from production, not a golden set |
| Deflection | How often the feature resolves a need without a human | Ties usage directly to the cost it was built to justify |

Adoption replaces a raw usage count, which a small group of power users can inflate while everyone else quietly ignores the feature. The denominator is the part teams skip most often, and skipping it is usually what makes an adoption number flattering rather than honest: ten thousand people using a feature this month means something completely different depending on whether ten thousand or two hundred thousand people had it available to them at all.

Acceptance is the metric this chapter leans on hardest, because it's the closest thing to a live, continuous version of chapter four's golden set, except scored by every real user instead of fifty chosen cases. Every time someone keeps a drafted reply exactly as written, or rewrites three of its five sentences, that's a quality signal arriving for free, at a scale no offline evaluation could ever reach.

Deflection matters most for the exact shape of feature this book keeps returning to: a support assistant handling a request that used to need a person. It's the metric that connects directly back to chapter six's unit economics, because a feature that deflects real volume is one actually earning its cost, not one people poke at out of curiosity. For the refund agent, deflection says exactly what the engagement chart couldn't: of the refund requests that reached it, how many closed without a human touching the case at all. That's the number the cost model and the risk register were both quietly building toward, the one that finally says whether the automation earned its keep.

[PULLQUOTE: An engagement number alone can't distinguish delight from friction, because both look identical in a raw usage count.]

## Read them together, not alone

Notice that both readings of the twenty percent rise start from the identical chart. The only difference is whether anyone checked a second metric before deciding what the first one meant. A user delighted with a first answer doesn't ask a second time. A user fighting the feature generates exactly the retries that inflate engagement while acceptance quietly drops in the background, unwatched, because product tends to have the engagement dashboard by default and acceptance has to be deliberately added by someone who specifically asked for it.

Pair them, the same discipline chapter six asked of a margin number sitting next to an engagement number on the same page. Two metrics moving together tell a real story. One metric alone is a single data point dressed up as an answer.

A high acceptance rate isn't automatically the reassuring opposite either, and it's worth being honest about the direction this can fail in too. A suggestion accepted without being read produces the exact same acceptance event as one read carefully and judged genuinely good. A low-stakes feature nobody scrutinizes closely is especially prone to this, and a high acceptance number there is weaker evidence than the identical number on a feature people actually check before keeping. Pair acceptance with a downstream signal where you can get one: did the accepted draft go out unedited, or did it quietly get undone five minutes later.

[KEY-INSIGHT: Klarna's OpenAI-powered customer service assistant, launched in February 2024, handled roughly two-thirds of the company's customer service chats within a month, a deflection number the company publicized as equivalent to 700 full-time agents. In May 2025, CEO Sebastian Siemiatkowski told Bloomberg that cost had been "a too predominant evaluation factor" in organizing the change, with the result that "what you end up having is lower quality," and announced Klarna was rehiring human agents for a hybrid model. || Source: Bloomberg interview with Sebastian Siemiatkowski, reported May 2025 (via Forbes, "Klarna Reverses AI Push, Says Customers Prefer Human Support," May 18, 2025).]

Read that against this chapter's own table and the mechanism is precise, not vague. Deflection told a genuinely true story: the assistant really was resolving a large share of chats without a human. It just wasn't the only story, and nobody was reading a quality signal next to it with enough weight to catch the gap before customers did and a CEO had to say so publicly. A single strong metric, celebrated without a second one to check it against, is exactly how a real company arrived at exactly this chapter's warning, at a scale far larger than a quarterly review.

## A single metric, celebrated for years, before anyone checked underneath it

This trap isn't unique to AI features, and it's worth seeing it at a scale that has nothing to do with software at all, because the mechanism is identical: a headline number gets celebrated, repeatedly, without anyone checking a second number that would have told a different story.

For years, Wells Fargo publicly touted its "cross-sell ratio," the average number of financial products each customer held, as proof of the bank's success, with an internal goal of eight products per customer. Investors and analysts read the rising ratio the way the leadership team in this chapter's opening scene read a rising engagement chart: as unambiguous evidence the strategy was working. It wasn't checked against a second number until regulators did the checking instead. Employees under intense pressure to hit the cross-sell target had opened roughly 1.5 million bank accounts and roughly 565,000 credit card accounts that customers never authorized or, in many cases, never knew existed.

[KEY-INSIGHT: Wells Fargo publicly promoted its "cross-sell ratio," the average number of financial products per customer, as evidence of its Community Bank's success between 2011 and 2016, with an internal target of eight products per customer. Regulators later found that employees, under pressure to hit that target, had opened approximately 1.5 million unauthorized bank accounts and roughly 565,000 unauthorized credit card accounts. The Consumer Financial Protection Bureau and other regulators fined Wells Fargo a combined $185 million in 2016. || Source: Consumer Financial Protection Bureau, "CFPB Fines Wells Fargo $100 Million for Widespread Illegal Practice of Secretly Opening Unauthorized Accounts," press release, September 8, 2016.]

The cross-sell ratio wasn't a lying number, in the narrow sense. Every one of those accounts really did exist and really did count. That's exactly what makes the parallel worth sitting with: a metric can be completely accurate and still tell a false story, because nobody paired it with the second number, complaint volume, unauthorized-account reports, anything that would have shown the ratio was being hit the wrong way. An engagement chart moving the right direction deserves exactly the same skepticism before anyone treats it as the whole story.

## Instrument before, not after

None of the three metrics above exist unless something captures them at the only moment they can be captured: when a suggestion first appears on screen. A deterministic feature can afford to instrument late, because the button does the same thing in month three that it did in month one, so a metric added later can still be reasoned about honestly for the months before it. An AI feature can't. The exact prompt version and model behind a specific answer exists for one moment, and if nothing recorded it, that moment is gone for good. Add acceptance tracking three months after launch and the real cost isn't three months of a missing number. It's the permanent inability to know what those three months of real usage actually looked like.

The fix is a small, deliberate event schema, not a broad logging effort. Four events, one shared identifier running through all of them: a "shown" event capturing the request ID, prompt version, model, and timestamp; an "outcome" event recording accept, edit, or reject against that same request ID; an "escalation" event recording whether a human took over; and a "feedback" event capturing any explicit signal a user bothers to give. Tie all four to the same identifier chapter six's cost model already needed for tracing spend, and any outcome becomes traceable back to the exact version that produced it. Ship a prompt change with that thread intact, and acceptance before and after the change is two clean numbers you can compare directly, instead of a room full of people guessing whether the new version "feels" better.

Capture exactly enough to compute these three metrics, not a data lake nobody ever queries. Whatever gets logged about a request is data now subject to the same questions chapter eight already asked about personal data: log the request ID and the outcome, and think hard before logging the full text of every request by default just because it seemed useful at the time.

## The dashboard leadership actually reads

A team operating a feature day to day genuinely needs many panels: latency by percentile, cost by model, error rate by endpoint, every diagnostic signal earlier chapters taught you to watch. That dashboard does its job by being comprehensive.

Hand that same dashboard to a leadership review and it fails, not because the numbers are wrong, but because comprehensive and decision-ready are different qualities. Leadership isn't operating the feature. They're deciding whether to fund it, expand it, or pull it back, and that decision needs three or four numbers, not fifteen. The instinct under pressure is to show more, because more feels more honest. It's usually the opposite: more panels just give the room more places to find whatever story it already believed walking in. A leadership view built from this chapter's three metrics, plus one cost or margin figure, forces a discipline that fifteen panels never will, because someone has to decide in advance which numbers actually matter enough to survive the cut.

Refresh cadence matters more than it looks like it should. A dashboard refreshing every minute doesn't help a monthly decision; it just adds noise between the meetings that actually matter, so match the refresh rate to the decision cycle, not to whatever the infrastructure happens to support. The two dashboards, the team's and leadership's, can share one source of truth without sharing a screen: the same instrumentation feeds both, one queried in full diagnostic detail, the other rolled up to a handful of numbers built for the person actually looking at them.

Say the honest caveat plainly, because the pressure on a leadership dashboard runs in one direction: make it look good, quietly drop the panel that doesn't. A dashboard that only ever shows good news has stopped reporting and started performing, the same trap chapter eight named for a stale risk register. A trustworthy version has to be allowed to show a bad number, with a sentence next to it about what's being done, because the version that only ever shows green gets believed right up until the quarter it can't hide the real number any longer, and every green quarter before that one loses its credibility retroactively the moment it happens.

## Find your unpaired metric

Pick the one number about an AI feature you report most often, the one that would headline your own version of the quarterly review this chapter opened with. Ask honestly: what second number would have to move the wrong way for that first number to actually be bad news, and do you currently have it.

If the answer is no, that's this chapter's finding, worth fixing before the next report goes out rather than after someone in the room asks the question this chapter's opening scene did. Most headline metrics already have an obvious pairing, acceptance next to engagement, complaint volume next to a sales ratio, a quality signal next to deflection. The fix is rarely building something new. It's usually putting a number you already have on the same page as the one everyone already watches.

[TAKEAWAYS]

- Engagement alone can't distinguish delight from friction on a probabilistic feature. Rising usage can mean the feature is working, or it can mean users are retrying a broken first answer.
- Track adoption, acceptance, and deflection together. Each catches a story the other two miss, and none of the three is trustworthy read alone, including acceptance, which can hide unread rubber-stamping.
- Instrument before launch, not after. A shared request ID across shown, outcome, escalation, and feedback events is what makes any outcome traceable back to the version that produced it, and that thread can't be reconstructed retroactively.
- Build a separate leadership dashboard: three to five numbers, refreshed on the decision's own cadence, and honest enough to show a bad one. A dashboard that never shows bad news has stopped informing anyone.

[/TAKEAWAYS]

## Where this goes next

Chapter ten turns to the conversation these numbers actually get used in: how to say all of this out loud, calibrated, to a stakeholder who wants certainty this book has already spent nine chapters explaining you don't have.
