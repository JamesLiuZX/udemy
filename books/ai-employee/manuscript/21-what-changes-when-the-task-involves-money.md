# What Changes When the Task Involves Money

The quote read cleanly, confident totals, no visible seams, and it was nearly thirty percent below Felix's real cost on a custom piece that would have taken his workshop a week to build. The tool had applied a labor multiplier to the wrong dimension. Nothing about the finished number looked wrong; wrong arithmetic almost never does. He caught it only because he'd stopped reading quotes for plausibility and started recalculating them.

Every task category this book has covered so far shares an assumption worth making explicit now: that a wrong output, caught late, costs time to fix and maybe some embarrassment. A task involving money directly, an invoice, a reimbursement calculation, a price quote, a payroll adjustment, breaks that assumption in a specific way. The cost of a wrong output isn't measured in time anymore. It's measured in dollars that already moved, and money that's moved is meaningfully harder to walk back than a sentence that's been sent.

## Why arithmetic specifically deserves extra suspicion

Writing tasks fail by inventing a plausible detail. Money tasks can fail the same way and also fail at something more basic: getting the actual arithmetic wrong, a structural weak spot in how these systems work, not a training gap that quietly resolves as models improve in other ways.

[KEY-INSIGHT: A widely cited 2023 study tested GPT-4 on multiplying numbers of increasing length and found accuracy on three-digit multiplication at 59% when asked directly, dropping to 4% for four-digit multiplication and 0% for five-digit multiplication, evidence that raw arithmetic reliability degrades sharply and predictably as a calculation gets longer, a structural pattern tied to how these models process text rather than a simple knowledge gap. Individual models have improved since, especially ones that can invoke an actual calculator or run code rather than compute purely from learned patterns, but the underlying caution the finding points to, verify a calculation, don't just trust that it reads correctly, still holds regardless of which specific model you're using. || Source: Dziri, N., et al., "Faith and Fate: Limits of Transformers on Compositionality," Advances in Neural Information Processing Systems 36, 2023 (originally arXiv:2305.18654).]

A wrong number in a piece of prose is often invisible on a casual read, and this is exactly where chapter four's "checking without redoing it" needs a specific amendment for anything involving money: the seam for a financial task isn't a topic or a category the way it was for Maria's expense line items. It's every individual number, and every one of them needs to trace back to a source you can independently verify, not just look plausible against the numbers around it.

## Reconciliation, not spot-checking

The general spot-check method from chapter four, find the seam, check it completely, sample the rest lightly, still applies, but a financial task needs a specific version of "checking completely": reconciliation, verifying a total against an independent source that didn't come from the same process that produced the number you're checking. A quoted price should trace back to your actual price list, not to whether it sounds reasonable. A reimbursement total should trace back to the actual submitted receipts, added independently, not to whether the tool's math looks internally consistent. Internal consistency is not the same thing as correctness, and a plausible-looking total that's wrong in a way that's internally consistent is exactly the failure that's hardest to catch by reading alone.

[PULLQUOTE: Internal consistency is not the same thing as correctness, and a plausible-looking total that's wrong in a way that's internally consistent is exactly the failure that's hardest to catch by reading alone.]

## Where the disqualifiers get stricter

Chapter seven's four disqualifiers don't change for financial tasks. How conservatively you apply them should. A judgment call embedded in a financial task, whether a borderline expense counts as reimbursable, deserves the same "keep it human" treatment chapter seven gave Renata's illness-adjacent reviews, for the same reason: no standing instruction reliably replaces judgment on an ambiguous case, and getting it wrong here has a dollar figure attached, not just an awkward email. The third disqualifier, a single error costing more than every success combined, is close to a default yes for anything moving money in any real volume, the same logic chapter seven's Zillow example showed at a much larger scale: a systemic pricing error repeated across enough transactions can erase the value of every transaction that went right.

## A quoting task, checked the right way

Felix runs a small custom furniture workshop and delegated the first pass of price quotes to prospective clients, combining a materials cost lookup with a labor estimate based on the piece's described dimensions. His first version trusted the tool's arithmetic directly, materials cost times quantity, plus a labor multiplier, and it read cleanly every time, confident totals with no visible seams. The actual reconciliation, checking each quote's total by recalculating it independently against his real price sheet rather than reading whether it looked right, caught a real error in the fourth quote he checked: a labor multiplier applied to the wrong dimension, off by enough to have quoted a customer nearly 30% below his real cost on a piece that would have taken a week to build.

Felix didn't fire the task. He added the one check that actually mattered: every quote now gets its final total independently recalculated from the same three numbers, materials, dimensions, labor rate, before it goes out, a task that takes ninety seconds and would have caught the underpriced quote before it ever reached a customer. The drafting still saves him real time. The arithmetic just never gets trusted on its own say-so anymore.

What changed between Felix's two versions is the difference between chapter four's spot-check and a real reconciliation:

| | Spot-check (chapter four) | Reconciliation (money tasks) |
| --- | --- | --- |
| The seam | A topic, a category, a vendor | Every individual number |
| The standard | Reads plausibly, matches the pattern | Traces to an independent source |
| The check | Sample the seam, skim the rest | Recalculate the total from source figures |
| Time cost | Minutes per batch | Ninety seconds per quote, every quote |

## The judgment call inside a financial task

Not every seam in a financial task is arithmetic, and it's worth naming the judgment-call version this chapter's stricter disqualifier reading was built for. Farrah, whose nonprofit trial appeared earlier in this book, also delegated a first pass of expense reimbursement decisions for staff travel: was a given receipt within policy, did it need a manager's second signature, did a borderline category, a working meal that was arguably also a social one, count as reimbursable at all. The arithmetic on any single reimbursement was trivial, adding a few line items correctly. The actual risk lived entirely in the borderline calls, and those calls depended on institutional context no receipt line item could supply: which donor-restricted funds a given trip's expenses could legitimately draw against, and which staff member's history of borderline claims warranted a closer look this time.

Farrah applied this chapter's stricter reading of chapter seven's first disqualifier and kept every borderline reimbursement decision human, letting the tool handle only the mechanical parts: pulling receipt totals, checking basic policy thresholds, flagging anything ambiguous for her review rather than guessing at it. The volume made this cheap to sustain, most reimbursements weren't borderline at all, so the human review queue stayed short even with every genuinely ambiguous case routed there by design. The distinction that mattered wasn't between arithmetic and judgment in the abstract. It was noticing, task by task, which parts of a single financial process were which, and refusing to let a tool's confidence on the easy ninety percent obscure a judgment call sitting in the other ten.

## Try this: reconcile one number

Pick one financial task, or one delegated task with a financial number embedded in it, that you currently trust without checking. Recalculate its most recent output independently, from source, the way Felix recalculated his quotes.

________________________________________________________________

Did the number hold up? If it didn't, that's real evidence for a standing instruction or a stricter checkpoint. If it did, you've earned a lighter, faster reconciliation habit for that task going forward, not zero checking.

[TAKEAWAYS]

- A wrong output in a financial task costs money that's already moved, not just time to fix, a fundamentally different risk profile than most tasks in this book.
- Raw arithmetic is a specific, structural weak point, not just another category of possible error. Verify a calculation against an independent source; don't trust that it reads correctly.
- The seam for a financial task is every individual number, not a topic or category. Reconcile against a source that didn't come from the same process that produced the number, not against whether the total looks internally consistent.
- Apply chapter seven's disqualifiers more conservatively for anything touching money. The third one, a single error outweighing every success, is close to a default yes for any financial task run at real volume.

[/TAKEAWAYS]

## Where this goes next

Chapter twenty-one names a risk this book's own caution can create if it's the only lesson taken from it: using careful evaluation as a permanent excuse to never actually try.
