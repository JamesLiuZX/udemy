# Seven Shapes

In November 2021, Zillow shut down an entire division and laid off a quarter of its workforce because of a forecasting error.

The division was Zillow Offers, the company's iBuying business: an algorithm estimated what a home would sell for, Zillow bought it directly from the owner at a price derived from that estimate, made light repairs, and resold it. The model had worked well enough in stable markets. Then the pandemic housing boom hit, prices moved faster and more unevenly than the model's training data had ever seen, and the algorithm kept confidently producing numbers that were, in aggregate, wrong in one direction. Zillow ended up owning thousands of homes it had overpaid for, unable to resell them without a loss. The company took a write-down of just over four hundred million dollars for the year and closed the business.

This wasn't a story about a bad model. Zillow employed genuinely skilled data scientists, and the model performed reasonably by the standards it was tested against. It's a story about a shape mismatch: a forecasting problem, in a domain with sudden regime change and enormous per-error cost, wired directly into automatic purchase decisions with no human check absorbing the tail risk. The lesson isn't "don't use AI to estimate home prices." Real estate sites still do that, usefully, every day. The lesson is that the same underlying capability, price estimation, is safe in one shape and dangerous in another, and the shape is a decision you make, not a fact about the technology.

## Why "should we use AI here" is the wrong first question

Most teams walk into an AI feature decision asking one binary question: should we use AI for this, yes or no. That question doesn't have a stable answer, because it skips the step that actually determines the risk: what shape is this feature, and does that shape match how much confidence the situation actually requires.

The same underlying model, the same API call even, behaves completely differently depending on the shape it's wired into. A price estimate shown to a homeowner as "here's a ballpark, get a real appraisal" is informational. The identical estimate wired directly into an automatic purchase offer is a financial commitment made by a probabilistic guess. Same capability. Different shape. Different amount of damage a wrong answer can do.

## Seven shapes, and what breaks in each

These aren't the only way to categorize AI features, but they cover the overwhelming majority of what shows up on a real product roadmap, and each one fails in its own specific way.

**Classifier.** Sorts an input into one of a known set of categories: routing a support ticket, flagging spam, tagging a document by type. Fails by misclassifying, usually recoverably, since a wrong category is often just a wrong queue, not a wrong fact stated to anyone.

**Extractor.** Pulls structured data out of unstructured input: parsing an invoice, reading a resume into fields. Fails by inventing or dropping a field silently, which is more dangerous than misclassifying because the output looks like clean structured data, no visible hedge, even when a number was hallucinated.

**Generator.** Produces new text or content: drafts, summaries, replies. Fails by stating something false in the same fluent voice as something true, which chapter one already covered in detail.

**Retriever, grounded in your own data.** Answers a question using a specific knowledge base rather than general training: a support bot pulling from your docs, a policy lookup tool. Fails when it retrieves the wrong passage, or the right passage but reads it wrong, and states the result with the same confidence either way.

**Recommender.** Ranks or surfaces options among many: search results, product suggestions, prioritized leads. Fails quietly, by degrading average quality rather than producing one dramatic wrong answer, which makes it the hardest of the seven to notice failing without a real measurement in place.

**Predictor.** Estimates a future numeric or categorical outcome: churn risk, fraud likelihood, a home's future sale price. Fails by being confidently wrong at scale in a correlated way, the Zillow shape exactly, where every individual estimate can look reasonable and the aggregate exposure is still catastrophic if the underlying market shifts in one direction all at once.

**Agent.** Takes multi-step, tool-using action with reduced human review between steps: rebooking a flight, executing a refund, modifying a database record. Fails by compounding: each step's error rate multiplies against every other step's, and unlike the other six shapes, the agent can act on its own mistake before a human ever sees it. Chapter seven covers this shape in far more depth, because the math involved deserves its own chapter.

[KEY-INSIGHT: Zillow's home-buying algorithm, Zestimate-derived and wired directly into automatic purchase offers, was cited by the company's own leadership as the direct cause of the 2021 shutdown of its Zillow Offers division: a predictor shape, in a market with sudden regime change, with no human check absorbing the tail risk before a purchase was committed. || Source: Zillow Group, Inc. Form 10-K, FY2021; company statements on the Zillow Offers wind-down, November 2021.]

## The disqualification checklist

Before evaluating how well an AI feature performs, ask whether it should exist in its proposed shape at all. Any yes below is a reason to change the shape, not necessarily to abandon the feature.

[PULLQUOTE: The lesson from Zillow isn't "don't use AI to estimate prices." It's that the same capability is informational in one shape and a financial commitment in another, and the shape is a decision you make.]

- **Is a single error unrecoverable, financially or otherwise, once it happens?** If yes, put a human checkpoint between the model's output and the action it triggers, the exact checkpoint Zillow's automatic-offer shape removed.
- **Does the situation actually require deterministic, identical behavior?** Billing calculations, regulatory filings, anything where "the same input produces the same output" is a hard requirement rather than a nice-to-have, is a poor fit for a probabilistic system, full stop, regardless of shape.
- **Can you verify output at the volume you'll actually operate at?** A shape you can spot-check at ten cases a day but not at ten thousand needs a cheaper verification method built in before it ships, not after.
- **Does a simple rule already solve this reliably?** A keyword filter that already catches ninety-eight percent of spam doesn't need a model wrapped around it; save the probabilistic complexity for the genuinely ambiguous remainder.
- **Is this fundamentally a forecast, in a domain with real regime change?** Weather, markets, and anything downstream of collective human behavior shifting suddenly is the hardest category to model reliably, and the category where confident wrongness is most expensive, exactly the Zillow shape.

## Why this isn't about being anti-AI

None of this is an argument for caution as a general posture, and it's worth being clear about that, because "when in doubt, don't" is not actually the lesson here. Zillow's own core business, the search and valuation tool that made Zestimate a household name in the first place, still runs a similar underlying model today, informationally, without an automatic purchase attached to it, and it's one of the most-used real estate tools in the world. The model didn't get safer. The shape did.

The skill this chapter is teaching isn't caution. It's precision about where the actual risk in a feature lives, so you can put your energy into the one or two shape decisions that matter instead of treating every AI feature as equally dangerous or equally safe.

[TAKEAWAYS]

- Ask what shape a feature takes before asking whether to use AI at all. The same capability is safe or dangerous depending on the shape, not the model.
- The seven shapes: classifier, extractor, generator, retriever, recommender, predictor, agent. Each fails in its own specific way, worth knowing before you ship it.
- Zillow's failure wasn't a bad model. It was a predictor shape, in a volatile market, wired directly into an unrecoverable financial action with no human checkpoint.
- The disqualification checklist changes the shape of a feature, not necessarily the decision to build it. Most yes answers point to "add a human checkpoint," not "cancel the project."

[/TAKEAWAYS]

## Where this goes next

Chapter three turns a feature that survived this checklist into an actual written spec, the document that turns "we think this works" into acceptance thresholds engineering can build against. Everything from here forward assumes you already know which of the seven shapes you're building, because the spec, the golden set, and the risk register in the chapters ahead all depend on it.
