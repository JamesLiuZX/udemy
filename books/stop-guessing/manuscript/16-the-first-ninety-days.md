# The First Ninety Days

An idea landed on the desk in the first week of the new role, the way an idea always does: a customer request forwarded with "can we just do this with AI," three lines long, sounding entirely plausible in the room. Everyone wanted an answer by Friday. Nobody wanted to spend a quarter of engineering time finding out the answer was no.

That tension is the actual shape of the job this book has been preparing you for, and it doesn't wait for you to feel ready. This chapter is the part that turns fifteen chapters of method into something you can run on a real Tuesday: a five-day process for a new idea, and a ninety-day shape for a new role, both built entirely from tools this book already gave you.

## The discovery sprint: five days, five questions you already have

Most AI feature ideas should die in a sprint. Very few should die in production, and the gap between those two sentences is the entire argument for running one before committing real engineering time. The sprint isn't new material. It's five questions from earlier chapters, asked in a specific order, against a real idea, under a real deadline, with an exit built into every single day.

Day one is chapter two's seven shapes and disqualification checklist, asked of the actual idea on the desk: does AI even fit this problem, in this shape. An idea that fails here on a shape mismatch doesn't earn four more days confirming what day one already answered. Most ideas that don't survive a sprint don't survive past day two.

Day two is chapter seven's blast radius question, asked earlier than that chapter first raised it: can this be undone, and what does it cost if it's wrong. An idea that survives day one but carries a genuinely high blast radius isn't automatically disqualified. It needs that answer written down honestly before day three's effort is worth spending.

Day three is chapter four's coverage test, asked under a deadline instead of over a careful afternoon: can anyone on the team sketch even a rough golden set, cases they could plausibly score, deliberately including the hard ones, not just the obvious ones. If nobody can, that's not a paperwork gap. It's a sign nobody has actually agreed what "correct" means for this feature yet, and building anything before that's settled means building toward an undefined target. An idea that only produces confident cases for the easy, common inputs and goes quiet on the genuinely ambiguous ones is telling you something real, and it's exactly the fuzziness that would otherwise have shown up as a disputed pass rate months later, discovered far earlier and far cheaper here.

Day four doesn't need chapter six's full cost model, built properly with real measured token counts. It needs the rough version: an honest order-of-magnitude guess at cost per use, multiplied by a realistic volume estimate. That back-of-envelope number has killed more bad ideas by Friday than a polished model ever will, because a number that's clearly too high doesn't need more precision to make its point.

Day five isn't a fresh judgment call. It's an honest summary of the first four. Go, if all four questions cleared. No, stated plainly, if any one of them didn't. Or a narrower version, the option most sprints under-use: the same idea, scoped down to the slice that actually clears every question, instead of either the full original pitch or nothing at all.

[KEY-INSIGHT: A July 2025 report from MIT's Project NANDA reviewed more than 300 publicly disclosed enterprise generative AI initiatives and surveyed and interviewed leaders across industries. It found that 95% of organizations piloting generative AI saw no measurable return on the investment, despite an estimated $30-40 billion in enterprise spending on the category, with the small successful minority concentrated in narrow back-office automation rather than the sales and marketing tools that received most of the budget. The report was preliminary and its methodology contested, and its headline number should be read as a directional finding rather than a precise one; Gartner's independent accounting for the same period, that more than half of generative AI projects were abandoned after proof of concept, points the same direction. || Source: MIT Project NANDA, "The GenAI Divide: State of AI in Business 2025," July 2025; Gartner, "Why 50% of GenAI Projects Fail," 2026.]

That gap, ninety-five percent of real spending producing no measurable return, is what a missing discovery sprint looks like at industry scale. Most of that spend wasn't wasted on ideas that were clearly bad from the start. It was spent finding out slowly and expensively what a five-day sprint, run honestly, tends to find out by Wednesday.

## A sprint that only ever says yes isn't running the process

A sprint that always ends in "let's build it" isn't evaluating anything. It's performing evaluation on top of a decision that was already made before day one started, and everyone on a team usually knows it within a sprint or two, which quietly kills trust in every future sprint's yes as well. Track this the way chapter nine asked you to track any real metric: count sprints run against sprints that ended in yes, and watch that ratio over time. A ratio sitting near a hundred percent yes is the single clearest sign a sprint has stopped doing its actual job, whatever any individual sprint looked like from the inside.

[PULLQUOTE: A fast, confident no is a successful sprint, not a failed one. The sprint's entire job is finding out fast, before anyone spends real engineering time finding out the expensive way.]

Compare the cost of a week spent on a sprint against the cost of a quarter of engineering discovering the same no, after a date has already been promised to someone. The sprint that produces a confident no on day two is one of the cheapest wins available to a team, and it deserves to be reported that way in the room, not quietly filed away as a project that didn't work out.

## Three milestones for the first ninety days

The same discipline that evaluates a new idea also shapes a new role, and the generic version of a thirty-sixty-ninety plan, learn the product, build relationships, ship a quick win, isn't wrong so much as it's not specific to anything. It says nothing an interviewer couldn't have guessed before you walked in the door. This book has spent fifteen chapters building things more specific than that.

| Window | What it's for | Built from |
| --- | --- | --- |
| Days 1-30 | Audit what's actually true, change nothing yet | Chapter two's shapes, chapter eight's register |
| Days 31-60 | Finish one small, checkable proof | Chapter four's golden set, or one honest register row |
| Days 61-90 | Make the proof outlive you personally working on it | Chapter nine's dashboard, chapter ten's roadmap fix |

Days one to thirty aren't about changing anything. They're about finding out what's actually true, because a new hire has information value long before they have standing to act. Classify every AI-touching feature you can find, shipped or planned, using chapter two's shapes, and check honestly whether any of them has an eval or a risk register row already. Most people doing this for the first time find at least one that has neither, and that finding, stated plainly, is usually the single most useful thing to hand a new manager in week two.

[KEY-INSIGHT: Lou Gerstner spent his first months as IBM's new CEO in 1993 auditing the company rather than announcing a strategy. At a press conference about four months in, he told reporters, "the last thing IBM needs right now is a vision," explaining that his audit had found the company already owned drawers full of vision statements and had accurately predicted most major technology trends; what it lacked was the ability to act on any of them. Gerstner spent the next nine years executing tough, specific, market-driven strategy instead, and IBM's market capitalization grew from roughly $29 billion to $168 billion over that period. || Source: Louis V. Gerstner Jr., public remarks, 1993, as documented in coverage of his tenure including "Louis V. Gerstner, Who Revived a Faltering IBM in the '90s, Dies at 83," reporting his 1993 remarks and IBM's subsequent market-cap growth.]

Notice what Gerstner refused to do, under exactly the pressure this chapter's day-thirty table is built to resist: perform having a plan before the audit had actually finished. The room wanted a vision on day one. He gave them one on nobody's schedule but his audit's, and it was built from what ninety days of actually checking had found, not from what would have sounded confident at a press conference in week two. The specific number that followed, nearly six times the company's market value over nine years, is not proof this always works. It's proof that refusing to perform certainty before you've earned it is a strategy real leaders have bet a company on, not just a caution this book invented for a smaller stage.

Days thirty-one to sixty are where the audit turns into something real. Pick the single gap that matters most, small enough to actually finish inside a month, and fix it visibly: a golden set for the most fragile shipped feature, or the first honest row in a risk register that didn't exist before you arrived. The point isn't the artifact's size. It's that it's finished and checkable, which a proposal never is.

Days sixty-one to ninety are about durability, not a second one-off win. Turn the single proof into something that outlives you personally working on it: a dashboard built on chapter nine's three-metric floor, so the team can see the number without asking you directly, or a roadmap line fixed the way chapter ten describes, so next quarter's commitment isn't another guess. The real test of day ninety is whether a teammate could pick this up and continue it if you left tomorrow.

A day-thirty update built from one named finding, "this feature has no eval," plus one dated commitment, what ships by day sixty and how you'll know, is smaller and less impressive in the room than a deck covering everything learned about the product. Make that trade anyway. The comprehensive version is exactly what makes it unfalsifiable: nobody can check "here's everything I've learned" against anything, six weeks later or ever. A manager who watches one specific, dated commitment land on time starts trusting the next one by default, which compounds faster than any broad survey of impressions ever will.

## The plan is a hypothesis, not a contract

Say the honest caveat plainly, because finishing a plan exactly as written, regardless of what the audit actually finds, is its own failure, not a sign of discipline. This is the sprint-theater point from earlier in this chapter, aimed at a whole quarter instead of a single feature idea. A ninety-day plan followed to the letter no matter what days one to thirty reveal stops being judgment and becomes a performance of having a plan. The entire reason to spend the first thirty days auditing is that the audit might change what the next sixty should be.

If that happens, say so plainly, the same discipline chapter ten asked of replacing a hedge with a real number. "The plan changed because of what I found in week two, here's the new day sixty" is a stronger sentence to bring to a manager than quietly forcing the calendar to match an assumption the audit already disproved.

## Before you call any package finished

Whatever the sprint or the ninety-day plan actually produces, the same closing habit applies: check your own work against specific, checkable criteria before anyone else sees it, not a vague sense of being done.

| Artifact | Passes if |
| --- | --- |
| The spec | The threshold is a number, not a vague goal |
| Golden set | It includes a genuine boundary case and one adversarial case, not only clean ones |
| Rubric | Two people would score the same case the same way |
| Cost model | Every number is labeled measured or still projected |
| Model choice | A quality floor was applied before cost was compared |
| Risk register | All five categories have a real entry, not a placeholder |
| Dashboard or metric | It ties directly to the cost model's payoff claim, not just a chart that exists |

A cost model can pass a shallow version of its own row, every field filled in, while still resting on a volume estimate nobody actually checked. This checklist confirms that something exists and is labeled honestly. It cannot confirm the judgment behind it was correct, and that gap is exactly what a second, independent reader is for, the same discipline chapter five built for a rubric. Run this list against your own work looking for the reason it should fail, not confirming the reasons it should pass. Most people running it honestly for the first time find one or two genuine gaps, most often a golden set with no real boundary case, or a metric with no real connection back to what it's supposed to justify. Fixing either one usually takes under an hour, which is a small price for a package that survives more than a skim.

[TAKEAWAYS]

- Run a five-day discovery sprint on any new AI feature idea, reusing this book's own tools in order: shape fit, blast radius, golden-set coverage, rough cost, then an honest go, no, or narrower.
- A fast, confident no is the sprint succeeding, not failing. Track the ratio of sprints that end in yes; a ratio near one hundred percent means the sprint stopped doing its job.
- Shape a new role's first ninety days around three dated, checkable artifacts, not three status updates: an honest audit, one small finished proof, and one habit that outlives you personally doing it.
- Treat any plan as a hypothesis. If the audit finds something bigger than expected, say so and change the plan, rather than finishing it on schedule for its own sake.
- Before calling any package done, check it against specific criteria, looking for the reason it should fail. A checklist confirms a field is filled in, not that the number in it is right.

[/TAKEAWAYS]

## Where this goes next

Chapter seventeen is the last one, and it's the hardest to write honestly: where every method in this book actually stops working, because a book that never says so isn't one worth trusting with a real launch decision.
