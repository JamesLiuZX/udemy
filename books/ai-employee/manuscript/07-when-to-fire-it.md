# When to Fire It

Renata owns a small bakery, and for most of a year, AI wrote the first draft of her replies to online reviews. It was good at it. A three-star review about a slow pickup line got a warm, specific, on-brand reply in fifteen seconds instead of the ten minutes Renata used to spend hunting for the right tone. She built the failure-mode list chapter five recommends, found the one seam worth watching (it occasionally over-promised a specific future fix, "we've already fixed our staffing for weekends," when nothing had actually changed), fed that correction back as a standing instruction the way chapter six describes, and watched the seam close. For ordinary reviews, the system worked exactly the way the rest of this book says it should.

Then a review came in alleging a customer had gotten sick after eating one of her cakes. AI drafted a reply that was warm, specific, and apologized in a way that read, to Renata's eye, uncomfortably close to admitting fault for a foodborne illness claim she had no actual evidence was even true. She caught it, rewrote it herself, and updated her standing instructions to flag anything mentioning illness for a fully human reply. Two months later, a different version of the same problem slipped through: a review about a customer's "stomach issues after the cupcakes," phrased just differently enough that the flag didn't catch it, and the draft apologized again in a way she had to unwind.

Renata didn't fix this one. She stopped delegating it. Every review that isn't a potential liability claim still goes through AI first. Every review that touches illness, injury, or anything resembling a legal claim goes straight to her, no draft, no AI step at all. That's not a failure of the system this book has been building. It's the system working correctly, because part of managing anything, a person or a tool, is knowing which jobs never make it past week one no matter how good the candidate looks on the easy tasks.

## Four reasons to stop, not one

"It's not working" isn't specific enough to act on, the same way "it makes mistakes" wasn't specific enough back in chapter five. There are four genuinely different reasons a task belongs on the list of things you stop delegating, and they call for different responses, not one blanket rule of thumb.

**It's a judgment call, not a pattern.** Some tasks don't have a rule you could write down even in principle, because the right answer depends on weighing specifics that change every time: how upset is this customer actually, is this the kind of thing that becomes a bigger problem if handled wrong, does this particular relationship warrant bending a policy that would otherwise hold. Renata's illness-adjacent reviews are exactly this. No standing instruction, however carefully worded, replaces a judgment that has to be made fresh each time.

**It's relationship-dependent.** Some tasks draw on a history the tool structurally cannot have: what this specific client said last year, what this specific vendor already knows about your situation, the unwritten context a long relationship carries. AI can draft in your voice. It cannot remember that this particular customer had a bad experience two years ago that makes an ordinary apology land wrong for them specifically.

**A single error costs more than every success combined.** Most delegated tasks fail cheap: a slightly generic reply, an extra thirty seconds to fix. A handful fail expensive: a false liability admission that a lawyer later has to unwind, a client relationship damaged badly enough that no number of good replies elsewhere makes up for it. When the downside of one bad output outweighs the upside of a hundred good ones, the math doesn't care how rarely the bad one happens.

[PULLQUOTE: When the downside of one bad output outweighs the upside of a hundred good ones, the math doesn't care how rarely the bad one happens.]

**The error rate genuinely never comes down.** This is the one chapter five and six's whole method is built to prevent, which is exactly why it's worth naming as its own category: sometimes you do everything right, find the real seam, write the specific correction, save it properly, and the pattern still doesn't close. That's real information. It means the task is harder than a standing instruction can fix, not that you haven't tried hard enough yet.

## When you did everything right anyway

Renata's story shows a judgment-call task getting caught quickly, within two attempts. It's worth seeing the fourth criterion, the one where the error rate simply never converges, play out on a task where nothing about the process was rushed.

Teodora is a financial advisor with a small independent practice, and she spent two full months trying to delegate the first draft of her quarterly portfolio rebalancing notes, the short explanation she sends each client about why their allocation shifted. She followed the method exactly. A real five-part brief. A trial run across eight different client accounts before trusting anything. A spot-check targeted at the seam she found, explanations involving a client's bond allocation, where the tool kept describing interest-rate risk in a way that was technically defensible but not quite how she'd actually explain it. She wrote a standing instruction. She revised it twice more as new bond-related misses turned up. By week eight, the bond-allocation seam still hadn't closed. It had just changed shape three times.

That is real information, not a personal failure. Teodora didn't do anything wrong across those two months, and lowering her standards to declare it "good enough" would have meant sending clients a technically-defensible-but-slightly-off explanation of their own money, the exact kind of task where "mostly right" isn't actually a passing grade. She fired the task for bond-heavy accounts specifically, kept it for the simpler equity-only rebalancing notes where the seam had, in fact, closed cleanly by week three, and went back to writing the bond explanations herself. Two months of real, rigorous effort produced a precise, narrow answer instead of a vague one, which is exactly what the effort was for.

## A public version of the same lesson

The same four reasons show up at a much bigger scale in one of the more visible AI retreats of the last few years. In 2021, McDonald's began testing AI voice ordering at its drive-thrus with IBM, eventually running it at over a hundred U.S. locations. It got a specific, if embarrassing, kind of famous: viral videos of the system adding bacon to a customer's ice cream order, tacking on nine sweet teas nobody asked for, or continuing to add chicken nuggets to an order after the customer repeatedly asked it to stop.

[KEY-INSIGHT: After roughly two years of testing automated AI order-taking at drive-thrus in partnership with IBM, McDonald's ended the pilot in June 2024 and began removing the technology from participating restaurants. No official error rate was ever published, but the decision followed a sustained, widely documented pattern of order mistakes, background noise and accents confusing the system, corrections being ignored, adjacent lanes' orders getting mixed together, that repeated across viral videos over an extended period rather than resolving as the system was tuned. || Source: "McDonald's to end AI drive-thru test with IBM," CNBC, June 17, 2024; "McDonald's is ending its drive-thru AI test," Restaurant Business, June 2024.]

Notice which of the four reasons was actually operating. It wasn't a single catastrophically expensive error the way a false liability admission would be for Renata's bakery. It was the fourth reason on its own: two years is a long runway for a large company with real engineering resources to close a gap, and the pattern of errors didn't close. McDonald's didn't say voice ordering can never work. The company kept the door open to trying a different vendor. What ended was this specific attempt, on the evidence that this specific tool, on this specific task, wasn't converging toward reliable, and continuing to run it in production was costing more in trust and cleanup than it was saving in labor.

A different large-company retreat shows the third criterion instead, a single category of error large enough to outweigh everything else.

[KEY-INSIGHT: Zillow ran a home-buying business that used its automated pricing algorithm to make cash offers on houses directly, and in 2021 stopped letting its own pricing experts override the algorithm's estimates. When home values shifted faster than the algorithm adjusted for, Zillow wrote down its housing inventory by as much as $569 million, the home-flipping division lost roughly $881 million for the year, and the company shut the business down entirely and cut 25% of its workforce. || Source: "Zillow Shuts Down Home-Flipping Business After Racking Up Losses," Bloomberg, November 2, 2021; "Zillow to Lay Off 25% of Its Workforce and Shutter House-Flipping Service," CBS News, November 2021.]

That decision to stop letting human pricing experts override the algorithm is the detail worth sitting with. It wasn't that the algorithm was always wrong. It was that removing the human check meant nothing caught the moments it was wrong, at exactly the scale where one bad pricing pattern, repeated across thousands of homes, could outweigh every accurate valuation that came before it. A false liability admission on one bakery review and an overpriced home bought at scale are wildly different in size. The underlying math is the same one from earlier in this chapter: when a single category of error is expensive enough, no volume of good outcomes elsewhere buys it back.

## What firing actually looks like

Firing a task doesn't have to mean abandoning the tool. Renata still delegates the large majority of her review replies. She fired one narrow slice of one task, illness-adjacent complaints, not the whole review-reply system, and that narrowness is the point. The disqualification checklist above is a checklist for a specific task, not a verdict on AI in general, the same distinction chapter five drew between a tool's reputation and a single task's failure pattern. A task that fails one of the four criteria gets pulled. Everything else keeps running exactly as it was.

It's worth being honest about the piece that stings: pulling a task you've already invested in, briefed carefully, spot-checked, and corrected, feels like a loss in a way that never delegating it in the first place wouldn't have. It isn't one. The trial from chapter three, the checking from chapter four, and the correction from chapter six all did their job here. They're what generated the evidence that this specific task belongs on the list. A trial that ends in "don't delegate this one" is a successful trial, not a wasted one, the same way a probationary period that correctly identifies a bad fit before the stakes get higher is the process working, not the process failing.

## What this chapter will not do

This will not tell you these four criteria are permanent verdicts on a task. The tool that mishandles illness-adjacent reviews today might handle them fine after a real improvement to the underlying model, the same kind of change chapter six flagged as something to watch for, not assume away. Revisit a fired task occasionally, with a fresh small trial, the same way you'd reconsider a role you'd previously decided a given hire wasn't suited for, rather than treating the original decision as fixed forever.

It also won't tell you every hard task fails all four criteria at once, or that you need all four to justify pulling something. One is enough. A task can be perfectly low-stakes and still belong on the list if it's genuinely a judgment call with no learnable pattern underneath it, the same way a task can have learnable patterns and still belong on the list if a single miss is expensive enough.

## Try this: run the disqualification checklist

Pick a task you're currently delegating, ideally one that's been running long enough to have a real failure-mode list behind it. Answer honestly:

| Question | Yes / No |
| --- | --- |
| Does any part of this depend on a judgment call with no learnable rule underneath it? | |
| Does it depend on relationship history the tool structurally can't have? | |
| Would a single miss cost more than every good result combined? | |
| Has the error rate genuinely failed to close, after a real trial, a real spot-check, and a real correction? | |

A single yes is enough to pull that task, or that slice of it, the way Renata pulled illness-adjacent reviews without touching the rest. All four no's is real, earned evidence the task is safe to keep running as is, not a guess.

[TAKEAWAYS]

- A task belongs on the "stop delegating this" list for one of four distinct reasons: it's a judgment call with no fixed rule underneath it, it depends on relationship history the tool can't have, one error costs more than every success combined, or the error rate genuinely never comes down despite real effort.
- One of the four is enough. You don't need all of them to justify pulling a task.
- Firing a task usually means narrowing scope, not abandoning the tool. Pull the specific slice that fails, keep delegating everything that doesn't.
- A trial that correctly identifies a task you shouldn't delegate is a successful trial, not a wasted one. It did exactly what chapters three, four, and six exist to make possible.

[/TAKEAWAYS]

## Where this goes next

Everything so far has been about managing one delegated task well. Chapter eight is about what changes, and what doesn't, once you're doing this for several tasks at once instead of one.
