# Objections and Pushback

Ten minutes into a lunchtime workshop on evaluation practice, the slides stopped mattering. A director two rows back said what half the room was thinking: "This all sounds right, but we genuinely do not have three days to build a golden set before Thursday." A PM near the front followed with a second one before the first had finished landing: "Our vendor already published a ninety-nine percent accuracy number, why are we redoing their homework?" By the time someone in the back asked whether legal would now need to sign off on every prompt change, the workshop had turned into exactly what this chapter is about: not the framework itself, but the specific sentences a real room says back to it.

None of these objections are unreasonable, and treating them as obstacles to argue past is the wrong instinct. They're the honest cost of a real constraint someone in the room is actually facing, and the previous ten chapters already contain the answer to most of them. This chapter collects the ones that come up most often, and points back to exactly where the answer already lives.

## The quick reference

| The objection | The short answer |
| --- | --- |
| "We don't have time for this" | The five-day discovery sprint (chapter thirteen) and the rough cost check (chapter six) both fit inside a week. The alternative isn't zero time spent, it's the same time spent later, after launch, under worse conditions. |
| "The vendor already tested it" | Their number describes their benchmark, not your feature, your users, or your failure modes. Chapter four's golden set exists because a vendor's number and your risk are two different questions. |
| "Legal will slow everything down" | A risk register (chapter eight) is what makes a legal review fast, because it gives counsel a specific, answerable question instead of an open-ended one. Skipping it doesn't remove the review. It removes your preparation for it. |
| "Our competitors shipped without this" | You don't know what it's costing them yet. Chapter six's margin trap and chapter nine's metrics exist precisely because a shipped feature and a profitable, safe one are not automatically the same feature. |
| "This is overkill for a small feature" | Scale the method, not the discipline. A five-case golden set and a one-line risk register entry are still a real threshold and a real owner. Zero of either is the actual overkill. |
| "Engineering owns testing, not me" | Engineering can test whether the code runs. Only someone who knows what "correct" means for this specific feature can build the threshold that says whether it works. That's chapter three's entire argument. |
| "Nobody on the team knows how to build an eval" | Chapter four's golden set and chapter five's rubric are built from reading real cases and writing down what "good" means, a skill closer to product judgment than to machine learning. |
| "The model will be different next month anyway" | The golden set, the rubric, and the threshold don't expire when the model changes. They're exactly what lets you tell, in an afternoon, whether the new model is actually better instead of just newer. |

## "We don't have time," taken seriously

This is the objection worth the most honesty, because the time pressure is almost never imaginary. Someone really does have a date on a calendar, and the discovery sprint or the golden set really does cost real hours nobody budgeted for.

[KEY-INSIGHT: Gartner predicted in July 2024 that at least 30% of generative AI projects would be abandoned after proof of concept by the end of 2025, citing poor data quality, inadequate risk controls, escalating costs, and unclear business value as the leading causes. || Source: Gartner, "Gartner Predicts 30% of Generative AI Projects Will Be Abandoned After Proof of Concept By End of 2025," press release, July 29, 2024.]

Read that number against the objection, because it reframes what "not having time" is actually costing. Unclear business value is what a cost model from chapter six exists to fix. Inadequate risk controls is chapter eight, named almost word for word. Nobody skipping the discipline this book teaches is saving time in any real sense. They're moving the same hours from a deliberate exercise before launch to a much larger, much less deliberate one after the feature joins the thirty percent that gets quietly abandoned. The honest answer to "we don't have time" isn't "make time anyway." It's "name the smallest version of this that fits the time you actually have," which is exactly what the five-day discovery sprint and a five-case starter golden set are for.

## "The vendor already tested it," taken seriously

A vendor's benchmark number is real, in the narrow sense that someone really measured it. It's also answering a question you didn't ask: how does this model perform on the vendor's chosen test set, not how does it perform on your users, your failure modes, your definition of good enough.

In April 2025, Meta announced that its new Llama 4 Maverick model had climbed to second place on LMArena, a widely watched public benchmark, outperforming several established competitors. Developers who checked more closely found that the version Meta had submitted to the benchmark was a specially tuned "experimental" variant, optimized for the kind of chatty, agreeable responses that score well with human voters, and different from the model Meta actually released for anyone to use. Once the publicly released version was tested directly, it fell from second place to thirty-second.

[KEY-INSIGHT: In April 2025, Meta's Llama 4 Maverick model reached second place on the public LMArena leaderboard. Developers discovered that the version submitted for benchmarking was a specially tuned "experimental" variant optimized for conversational style, distinct from the publicly released model. Once directly tested, the publicly released version of Maverick fell to 32nd place on the same leaderboard. || Source: The Register, "Meta accused of Llama 4 bait-n-switch to juice LMArena rank," April 8, 2025.]

Notice this wasn't a small, rounding-error gap. It was the difference between a top-tier result and a middling one, on the exact model a real user would actually get. Nobody has to assume bad faith to take the lesson: a benchmark number, even a real one, measures the version and the conditions it was measured under, not the version and conditions your feature will actually run in. Chapter four's golden set is how you find out, cheaply, whether your vendor's number and your feature's real behavior are the same claim or two different ones wearing the same percentage.

## "Legal will slow everything down," taken seriously

This objection usually comes from a real, remembered experience: a review that dragged for weeks because nobody could answer counsel's first question precisely. The fix isn't skipping legal. It's giving them something specific enough to answer quickly.

Picture the same request landing in a legal review two different ways. Version one: "We built an AI feature, is it okay to ship." That's not a question counsel can answer in a single pass, because it isn't actually one question, and every follow-up they ask adds another week. Version two: a completed risk register from chapter eight, five rows, each with a named risk, an owner, and a specific mitigation, plus an explicit flag on the one row still open. Counsel can now answer the actual, narrow question in front of them: does this specific mitigation on this specific row meet the bar, not "is AI generally fine." A prepared register doesn't just speed up the review. It's usually the difference between one review and three.

## Prepare your own answers

Pick the objection from this chapter's table that you expect to hear next, specifically, on a real feature you're about to propose. Write out your actual answer, in your own words, before the meeting where you'll need it, not during it.

Most people find this harder than it sounds, because an answer prepared under pressure tends to default to reassurance ("it'll be fine") instead of the specific, checkable claim chapter ten already taught you to give a stakeholder. Write the version with a number in it. If you don't have the number yet, that's today's finding, not a reason to wing the meeting anyway.

[TAKEAWAYS]

- Most objections to this book's method are honest reactions to a real constraint, not resistance to the idea itself. Answer the constraint, not the resistance.
- "We don't have time" is usually true and still doesn't argue for skipping the discipline. It argues for scaling it to the time available, not to zero.
- A vendor's benchmark number answers a different question than yours. Llama 4 Maverick's drop from second to thirty-second place on the same leaderboard is what the gap between "their number" and "your feature" can actually look like.
- A completed risk register speeds up a legal review by giving counsel a specific, answerable question. Skipping it doesn't avoid the review. It removes your preparation for it.

[/TAKEAWAYS]

## Where this goes next

Chapter twelve walks the entire method through three complete worked cases, start to finish, in domains this book hasn't touched yet, so you see every chapter's tools working together on one feature before being asked to run them on your own.
