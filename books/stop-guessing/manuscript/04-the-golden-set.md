# The Golden Set

The spec was finished, and it was a good one: on a set of fifty real cases, the assistant had to state no fact that contradicted the help center at least 96% of the time, and a human reviewer had to rate the answer usable without a single correction at least 88% of the time. Everyone in the room signed off on it. Nobody in that room said which fifty cases.

So the fifty got chosen the way they usually do. Whoever owned the number had a Thursday deadline and a ticket database sitting right there, so they opened it, sorted by most recent, and copied the top fifty rows into a spreadsheet. Every case in it was a real ticket. Nothing invented, nothing cherry-picked, which felt like plenty of rigor for a first pass. The whole thing took less than half an hour.

The assistant scored 96.4% against that set on the first run. Somebody put the number in the launch deck. It shipped.

Two months later, a customer wrote in disputing a charge on an order that had, in fact, already been partly refunded the week before. The assistant drafted a reply stating the full original amount as owed, in the same clean, confident voice it used for every other ticket, because nothing in its fifty cases had ever shown it what a partial-refund dispute looked like. A reviewer caught it before it went out and asked the obvious question: how does something like this get past a 96% pass rate?

The honest answer was worse than a bug. The case that broke it was never in the fifty at all. Sorting by "most recent" and grabbing the top rows feels like sampling, and technically it is, the same way a photo snapped in the last ten seconds before a phone dies is technically a photo of your day. It shows you whatever happened to be in frame during those ten seconds, weighted entirely by whatever was busiest on the one Thursday afternoon someone happened to look. A partial-refund dispute didn't need to be rare in general to be completely absent from fifty rows pulled on one particular day. It just needed to not be that Thursday's problem.

This is the specific way a golden set fails, and it is a different failure than a sloppy rubric or a careless reviewer. The set can be built entirely from real cases and scored by a genuinely careful rubric, and still tell you almost nothing about your real failure rate, because the fifty cases inside it were never chosen. They were only ever whatever happened to be closest to hand.

That matters more than it might seem, because a golden set isn't one artifact among many. It's the one everything else in an evaluation practice gets checked against: a rubric gets calibrated on it, a cost model gets priced against its pass rate, and the go or no-go conversation two days before launch usually starts, and often ends, with its number. Build the fifty badly and every number downstream of it is wrong in exactly the same quiet way, just harder to trace back to its source.

## Average is the trap

Here is why "sort by most recent" fails so reliably, and why the failure stays invisible right up until it happens to you. It comes down to one piece of arithmetic that almost nobody runs before building a first golden set.

Say a partial-refund dispute, the exact shape of case that slipped through above, actually shows up in one real ticket out of every twenty-five: about 4% of total volume. Not rare. The kind of thing your support team would tell you they see most weeks, if you asked them.

Sample fifty cases completely at random from that traffic, and on average you would expect about two of them to be a partial-refund dispute. Two sounds like enough. It is enough, on average. But "on average" is doing an enormous amount of quiet work in that sentence, and averages are precisely the number that hides a gap like this one. Work out the actual odds instead of the average, and there is a little better than a one-in-eight chance that your fifty cases contain zero partial-refund disputes. Not underrepresented. Zero. Ship on that set and you would see a healthy pass rate sitting on top of a blind spot exactly the size of one case in twenty-five, entirely outside anything your instrument could catch.

The arithmetic is nothing more exotic than multiplying 0.96, the odds that any single random case is not that failure mode, by itself fifty times. It falls slower than instinct expects, and that gap between instinct and arithmetic is the entire problem:

| How often a failure mode occurs | Expected count in 50 random cases | Chance those 50 contain zero |
| --- | --- | --- |
| 1 in 10 | 5 | under 1 in 100 |
| 1 in 25 | 2 | a little better than 1 in 8 |
| 1 in 50 | 1 | more than 1 in 3 |

The middle row is the one that should worry you, not the bottom one. A failure that hits one user in fifty is rare enough that most people already brace for missing it sometimes. A failure that hits one user in twenty-five feels common enough that fifty cases should catch it comfortably, and that feeling is exactly what the arithmetic will not back up. The distance between what a sample size feels sufficient for and what it is actually sufficient for is where a golden set quietly stops being an instrument and starts being a reassurance.

If you already have a golden set sitting somewhere, this is worth doing today, not after you finish the chapter: write down your worst known failure mode, estimate honestly how often it actually occurs in production, and run that number through the same arithmetic. If the chance of zero comes back anywhere near a coin flip, you do not have a coverage problem waiting to happen. You already have one, and it has been sitting inside a passing score.

And the ticket example above was the generous version of the problem: a genuinely random draw. Real golden sets are almost never built from one clean random sample. They get built from whichever transcripts were open in a tab, a sample biased before anyone even starts counting, tilted toward whatever recent traffic happened to look like on the one day someone went looking for it.

This is not only a small-numbers problem that disappears once a set gets bigger or a team gets more careful. It has happened before, at real, audited scale, on a very different kind of feature, and the underlying mechanism was identical: a test set nobody had deliberately built to include the case that mattered.

[KEY-INSIGHT: A 2018 audit of three commercial gender-classification systems, Microsoft, IBM, and Face++, found error rates no worse than 0.8% for lighter-skinned men and as high as 34.7% for darker-skinned women on the identical task. Two of the field's standard benchmarks for testing this kind of system turned out to be 79.6% and 86.2% light-skinned respectively. The systems were not failing a hard case. Nobody had built a test that included one. || Source: Joy Buolamwini and Timnit Gebru, "Gender Shades: Intersectional Accuracy Disparities in Commercial Gender Classification," Proceedings of Machine Learning Research, vol. 81 (2018), pp. 77-91.]

The fix is not a bigger random sample, although a bigger one does help some (look again at how much more slowly the bottom row's odds improve than instinct expects). The fix is refusing to leave coverage to chance in the first place.

## The four buckets

Once random, even careful random, stops looking sufficient, the question changes. It stops being how many cases you need and becomes which fifty, chosen on purpose, would actually catch this feature failing in the ways it is likely to fail.

A useful starting split, worth adapting to your own feature rather than applying as a fixed formula, is four buckets.

**The common path.** The ordinary, everyday case your users hit constantly: the boring ticket, the boring question, the bulk of your real volume. It is tempting to shortchange this bucket, since it is the least interesting fifty rows to sit and read. Skip it and you can pass your golden set while quietly regressing the exact thing most users experience most of the time, because nothing in your fifty was ever measuring it.

**Known failure modes.** Every specific way you have already watched this feature break. In the case above, a partial-refund dispute now has a permanent seat in the set. Every row here is a bug you are refusing to let back in unnoticed.

**Edge cases.** Real, unusual inputs that happen rarely but do happen: a ticket in a second language, a required field left blank, an order number pasted in with a typo. Rare does not mean irrelevant. It is often exactly where an AI feature turns strange in a way a person would not.

**Adversarial.** Someone deliberately trying to break the feature or bend it into doing something it should not: a message engineered to extract a policy the company never published, a request dressed up as routine while asking for something it has no business handing over. Most teams build this bucket last, if they build it at all, and it is usually the one that turns up the most uncomfortable finding.

A common split that works as a starting point, not a rule, is roughly twenty common-path cases, fifteen known failure modes, ten edge cases, and five adversarial. Adjust the proportions to what you are actually building: a feature with real regulatory exposure probably wants more than five adversarial cases; a purely informational feature, with no action attached to a wrong answer, can often get away with fewer.

The building itself is not glamorous, and treating it as an afterthought is exactly how it stops happening. Start from real production logs or real pilot transcripts, never invented examples: an invented example only ever tests the failure you already imagined, which defeats the entire point of building the set at all. Filter that raw traffic into rough candidates for each bucket, then have an actual person, you or whoever owns the feature, read every candidate and tag it: which bucket, and one line explaining why. That tagging step is the one people try to compress or skip, and it is the one that makes the other three mean anything. A script can pull five hundred raw candidates out of a database in about a minute. Turning them into fifty that mean something takes a real afternoon of reading transcripts and arguing over where the common path ends and an edge case begins. That step does not compress, and it cannot be delegated to the model you are trying to evaluate, for roughly the same reason a student cannot be trusted to grade the exam they just wrote.

Once you have your fifty, drop the near-duplicates and freeze the set: a version number, a date, one named owner who approves any change to it, the same discipline you would apply to a piece of code. A golden set that is editable on a whim, by whoever is unhappy with today's score, stops being an instrument and goes back to being an opinion. Just a more expensive one to produce.

## The photograph problem

Freezing the set is the right move, and it creates a new problem on a delay: a golden set, however well built, is a photograph. It is exactly right about the day you took it, and it says nothing at all about the day after that.

Picture the set above, six months on. This time it was built properly: twenty common-path cases, fifteen known failure modes including that partial-refund dispute, ten edge cases, five adversarial, each one read and tagged by a real person, frozen, versioned. It scores 91%, release after release, and the team has come to trust that number the way you would trust a smoke alarm that has never once gone off.

Then, in month seven, the company changes its refund policy: refunds now settle in three business days instead of ten. Nothing about the feature changed. Nothing about the golden set changed. But partial-refund disputes, the exact case deliberately built into the known-failure-modes bucket back in month one, go from an occasional ticket to a meaningful slice of a normal week, because a faster refund creates far more windows where a customer emails before their statement has caught up with reality.

Pull ten real tickets this week, chosen at random, not curated, and score them on the identical six-question rubric the golden set uses. The golden set still says 91%. The ten live tickets come back wider and lower: a couple of twos, a one, an average well under what the frozen set promised. Nothing about the rubric broke. Nothing about how the set was built was careless. Production moved and the photograph did not, which is the entire mechanism behind a gap like this. It has exactly one cause: the world changed, and the fifty cases did not.

[PULLQUOTE: A golden set, however well built, is a photograph. It is exactly right about the day you took it, and it says nothing at all about the day after that.]

Call this golden-set drift, because it deserves its own name rather than getting blamed on "the model got worse" or "the rubric's too strict," which is what it usually gets blamed on in a room where nobody has connected the dip to a policy change from five months back. The model did not get worse. The rubric did not get stricter. The set simply stopped being a photograph of the world it was now being asked to judge.

This is also why freezing and versioning the set earlier in this chapter was not bureaucracy for its own sake. A set that gets quietly hand-edited whenever someone dislikes a score cannot be observed going stale, because there is no fixed photograph left to compare against. Versioning is what makes drift visible at all, instead of just quietly, permanently wrong.

The fix costs about twenty minutes a release, which is cheap next to every alternative to knowing. Once a release, pull a small handful of transcripts you did not choose and did not curate, and score them on the rubric you already have. Getting two different people to apply that rubric the same way is its own skill, and it is where this book goes next. For now, treat the comparison itself as the whole exercise: if the number roughly matches the golden set's score, the photograph is still current, and you can stop worrying for another cycle. If it does not, that is not a reason to panic, and it is not a reason to distrust the rubric either. It is the earliest possible warning that the set needs a rebuild, arriving weeks before a support escalation would have delivered the same news with your name already attached to the launch decision.

## Where this doesn't reach

None of this works, at least not in the form described here, before a feature has any real usage to draw from. The four buckets assume a population of actual production traffic, or at minimum a genuine pilot with real users, to sort into common path, known failures, edge cases, and adversarial attempts. A brand-new feature, days from its first user, has no such population yet. The honest move there is to build a provisional set from the closest real proxy available (a pilot cohort, a closely related existing feature's transcripts, a small group of real target users trying deliberately to break something) and to treat its score as provisional too: a launch gate, not a settled fact, due for a full rebuild the moment enough real traffic exists to replace it with something better.

The other place this chapter's structure strains is a feature where a single case is not one input and one output but a whole chain of actions: an agent booking a flight, adjusting a refund, and updating three systems in sequence. There, fifty end-to-end transcripts test fifty specific paths through a tree with far more paths than that, and "coverage" stops meaning what it means for one reply to one ticket. That shape gets its own chapter, and its own harder math, later in this book. For a feature that takes one input and produces one output, which is still most of what actually ships, four deliberate buckets and a regular drift check are the right tool, and a sufficient one.

## Where this goes next

This chapter leaned on an "identical rubric" without fully earning the phrase: the same six questions, scored the same way, whoever happens to be holding the pen. That is a harder problem than it sounds, in the same way "should answer accurately" sounded simple right up until chapter three took it apart. Two careful, competent people looking at the same transcript routinely land on different scores, for reasons that have nothing to do with how good either of them is at their job.

Chapter five is about closing that gap: building a rubric specific enough that two reviewers actually apply it the same way, on the second case and the fiftieth, and proving they did rather than just hoping so. That is what turns a golden set from one person's carefully organized opinion into a shared instrument the whole room can trust.

[TAKEAWAYS]

- A golden set is a coverage decision, not a sample-size decision. Fifty cases chosen on purpose beat five hundred chosen by convenience.
- Random sampling silently misses real failure modes. A problem that hits one user in twenty-five has a little better than a one-in-eight chance of appearing zero times in a random fifty.
- Build from four deliberate buckets: common path, known failure modes, edge cases, and adversarial, using real transcripts only and a person who reads and tags every one.
- Freeze and version the set once it exists, then check it against a handful of uncurated live cases every release. A frozen set still drifts as production changes underneath it.
- This structure assumes real usage to draw from. A feature with no traffic yet, or one whose "case" is a whole chain of actions rather than one exchange, needs a different approach.

[/TAKEAWAYS]
