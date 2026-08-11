# Field Notes: Three Worked Case Studies

Every chapter so far has taught one piece of the method against the same recurring feature: a support-reply assistant that grew into a refund agent. That repetition was deliberate, the same case followed long enough to show how the pieces connect. It also leaves an honest gap. Seeing one feature evaluated end to end doesn't prove the method travels to a feature that looks nothing like it.

This chapter closes that gap with three compressed but complete field notes, each running the method against a feature type this book hasn't touched: a document-extraction tool, a sales-lead predictor, and an internal coding agent. None of the three is a real company's product. Each one is built the way a real feature actually gets scoped, walking through the same questions in the same order, so you can watch the whole method run start to finish before running it yourself.

## Case one: the invoice-extraction assistant

A finance team wants an AI feature that reads incoming vendor invoices, PDFs and scanned images alike, and extracts the vendor name, invoice total, due date, and line items into the accounting system, replacing a slow manual entry step.

**Shape.** This is chapter two's extractor shape, and it's worth naming the specific failure mode that shape carries: inventing or dropping a field silently, with no visible hedge, exactly the risk chapter two's Whisper example showed for medical transcripts. Here the analogous danger is a wrong total or a wrong bank routing detail entering the accounting system stated as clean fact.

**Disqualification check.** A single wrong extraction is recoverable, an overpayment can usually be clawed back, so this clears chapter two's checklist on that count. It fails a different way if the feature is scoped to auto-approve payment without review: that combination, an irreversible-feeling wire transfer triggered by an unverified extraction, is exactly the shape of blast radius chapter seven warns against.

[KEY-INSIGHT: In early 2024, an employee at the engineering firm Arup was tricked into making 15 separate wire transfers totaling $25 million after joining a video call in which every other participant, including the company's CFO, was an AI-generated deepfake built from public video and audio of real executives. The employee's initial skepticism about the request was overcome once the video call appeared to confirm it. || Source: CNN, "Arup revealed as victim of $25 million deepfake scam involving Hong Kong employee," May 16, 2024.]

That incident didn't involve an invoice-extraction tool, and it's exactly why it belongs here: it shows what happens when a finance process trusts a plausible-looking confirmation instead of a structural check. An extraction tool that looks confident is the same category of plausible confirmation. The fix is identical to chapter seven's blast radius table: extraction feeds a human review step for anything above a set dollar threshold or below a confidence floor, and payment execution is a separate, gated action, never triggered by the extraction step directly.

**Spec.** On a 50-invoice golden set stratified by vendor format, the assistant extracts vendor name and total correctly at least 98% of the time, and flags rather than guesses whenever line-item confidence falls below a set threshold, measured against chapter three's two-part template.

**Golden set.** Common path: standard machine-printed invoices from repeat vendors. Known failure modes: multi-page invoices where the total sits on a different page than the line items. Edge cases: scanned, handwritten, or multi-currency invoices. Adversarial: a PDF with hidden or altered text designed to change the extracted routing details, the direct extraction-shape analogue of chapter eight's prompt-injection category.

**Verdict.** Ships, scoped to extraction and flagging only. No extraction result triggers a payment without a named human approver, and the adversarial bucket gets revisited every quarter as new manipulation techniques surface.

## Case two: the lead-scoring predictor

A sales team wants a model that scores every inbound lead from one to a hundred, predicting likelihood to convert, so reps spend their limited time on the leads most likely to close.

**Shape.** Chapter two's predictor shape, the same family as the Zillow story: an estimate, aggregated across many individual guesses, where a systematic skew in one direction is more dangerous than any single wrong score.

**Disqualification check.** No single wrong score is unrecoverable, a rep just spends an hour on a cold lead, which clears the first question easily. The harder question is chapter eight's bias category: the model learns "likely to convert" from years of the sales team's own past outcomes, and if that history quietly reflects which leads reps happened to prioritize rather than which leads were actually strongest, the model will confidently reproduce that same pattern going forward, the same mechanism that broke Amazon's hiring tool in chapter four, aimed at a sales pipeline instead of a stack of resumes.

**Spec.** On a golden set of 50 historical leads with known, verified outcomes, leads scored in the top twenty percent convert at a rate at least three times the overall baseline, re-measured every quarter rather than validated once and left alone, because chapter four's golden-set drift risk is especially sharp here: a shift in the market, a new competitor, a changed pricing page, can all move what "likely to convert" actually means without a single line of the model changing.

**Golden set and bias check.** Split the historical leads by source, industry, and company size before scoring, the same segmented-pass-rate discipline chapter eight applied to phrasing style. If leads from one industry or region convert well in practice but the model systematically underscores them, that's a finding worth surfacing before the score starts shaping which territories get attention and, eventually, which reps get credited for results.

**Metrics.** Deflection doesn't apply here, nothing is being automated away. The metric that matters is closer to chapter nine's acceptance: how often a rep actually acts on a high score versus overriding it, tracked by segment. A high override rate on leads from one particular source is either a model problem or a trust problem, and the two require different fixes.

**Verdict.** Ships as a ranking signal shown alongside the reasoning behind it, not as an automatic filter that hides low-scored leads from reps entirely, and the segmented pass rate gets checked every quarter, not just at launch.

## Case three: the internal coding agent

An engineering team wants an agent that reads an internal bug ticket, writes a code fix, runs the existing test suite, and opens a pull request for a human to review, reducing the time from ticket to draft fix.

**Shape.** This is chapter seven's agent shape without question: the model decides what to do next at each step, from reading the ticket through to opening the PR, not a fixed sequence a person specified in advance.

**Reliability math.** Count the real steps: read the ticket, plan an approach, write the change, run the test suite, open the PR. Five steps. At a still-respectable ninety percent per-step accuracy, chapter seven's table puts the whole chain's success rate at fifty-nine percent, worse than a coin flip landing the intended way, before anyone's even looked at code quality. The test-suite step is the checkpoint that actually matters here: a run that fails tests doesn't proceed to opening a PR at all, which resets the compounding at exactly the point most likely to catch a bad plan before it reaches a human's queue.

**Blast radius.** Opening a pull request against a non-production branch is reversible and low-cost: nobody merges it without a human looking first, so this half of the feature clears chapter seven's top row with no gate needed. Anything beyond that, merging automatically, deploying automatically, touching credentials or production infrastructure, moves straight to the bottom-right combination the same chapter's table reserves for a named, mandatory approval gate. The agent in this case gets no merge access and no deploy credentials at all, on purpose, not as a placeholder for later.

**Risk register.** The prompt-injection row from chapter eight applies directly if the ticket source accepts input from outside the immediate engineering team: a ticket description is untrusted content the moment anyone besides a vetted engineer can file one, and a sentence inside it could try to steer what the agent does next. The fix is the same one chapter eight already gave: the agent's tool access stays fixed regardless of what a ticket's text asks for, so a crafted ticket has nowhere to reach beyond what a legitimate one could.

**Verdict.** Ships scoped narrowly: read-and-propose only, test-gated before any PR opens, no merge or deploy access, tickets restricted to a vetted internal source until the adversarial bucket in its golden set has actually been tested against a crafted one.

## What the three cases have in common

None of these three needed every tool in this book at full strength. The extraction tool leaned hardest on the golden set and the injection risk. The predictor leaned hardest on bias and drift. The agent leaned hardest on the reliability math and blast radius. That's the actual skill this chapter has been demonstrating: not running every chapter's checklist in full on every feature, but recognizing which two or three questions carry the real risk for the specific shape in front of you, and spending your limited hours there.

[PULLQUOTE: Not every chapter's checklist in full on every feature: recognize which two or three questions carry the real risk for the shape in front of you, and spend your limited hours there.]

The three verdicts, side by side, are the compressed version of the whole exercise:

| | Invoice extraction | Lead scoring | Coding agent |
| --- | --- | --- | --- |
| Shape | Extractor | Predictor | Agent |
| The risk that mattered | Silent wrong field | Learned bias, drift | Compounding, blast radius |
| The chapters that carried it | Four, eight | Four, eight, nine | Seven, eight |
| The boundary it shipped with | No payment without a named approver | Signal shown, never a hidden filter | No merge, no deploy, test-gated |

## Write your own field note

Pick a real AI feature you own or are about to propose, and write your own version of one of these three notes: shape, disqualification check, spec, golden set sketch, the one or two risk-register rows that actually worry you, and a verdict.

Keep it to one page. The value of this exercise isn't thoroughness, it's forcing yourself to name which two or three questions matter most for this specific feature, the same judgment call each case study above had to make, before a launch review makes you answer it under pressure instead of on your own schedule.

[TAKEAWAYS]

- The method isn't specific to one feature type. Applied to an extractor, a predictor, and an agent, the same questions surface the real risk each time, even though the answers look completely different.
- Which chapters matter most depends on the shape. An extraction tool's real risk lives in golden-set coverage and injection; a predictor's lives in bias and drift; an agent's lives in reliability math and blast radius.
- A verified confirmation isn't the same as a structural check. The Arup deepfake scam succeeded because a video call felt like verification. A gated approval step doesn't rely on anything feeling convincing.
- Scoping down, not abandoning the idea, is usually the actual verdict. All three cases shipped, each with a specific, named boundary on what the feature was allowed to do without a human.

[/TAKEAWAYS]

## Where this goes next

Chapter sixteen turns from a single feature to a role: the five-day discovery sprint for the next idea that lands on your desk, and the ninety-day shape for making this method a habit rather than a one-time read.
