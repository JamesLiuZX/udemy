# Not All AI Tools Are the Same Kind of Tool

The order was eleven times larger than anything Odalys would have chosen herself, placed automatically, through a supplier she trusted, before she saw a single line of it. Nothing tripped the boundary she'd written, because the boundary was watching for the wrong thing. What made that mistake possible wasn't a worse model or a lazier check. It was a different kind of tool: one that acts, instead of one that drafts, and she'd been supervising it like the kind she already knew.

This book has talked about "AI" and "the tool" as if they were one kind of thing, on purpose, because the management skill underneath delegation is the same regardless of which specific product you're using. That simplification has done real work for nine chapters. It's time to complicate it slightly, because "AI tool" actually spans at least three genuinely different kinds of software, and knowing which kind you're delegating to changes exactly how a few pieces of this method apply. Odalys's near-miss, told in full below, is what the difference costs when it goes unnoticed.

## Three shapes, one underlying skill

**A general-purpose chat assistant.** This is the shape most of this book's examples assume by default: you type a request, it responds, the conversation holds context for as long as the session lasts and, if the tool supports it, a saved standing instruction beyond that. Chapters two through seven map onto this shape almost exactly as written. The brief, the trial, the spot-check, and the standing instruction all assume a back-and-forth conversation, because that's what this shape actually is.

**A narrow, purpose-built tool.** Software built for one specific job, categorizing expenses, drafting a specific document type, transcribing a call, rather than a general conversational assistant you redirect at whatever task comes up. These tools often have less flexible briefing (you may be filling in a form rather than writing a paragraph of context) and, often, a narrower and more predictable failure pattern precisely because they do less. The trial-and-spot-check discipline from chapters three and four still applies completely. What usually differs is chapter two's brief: a purpose-built tool may not have room for all five parts as free text, and the equivalent of "the situation" and "what it can't know" might live in configuration settings rather than a written paragraph.

**An agent or automation that takes multiple actions on its own.** The most consequential shape to get right, and the one chapter nine's chaining advice was written for directly: a system that doesn't just draft an answer but actually does things, sends an email, updates a record, moves money, across multiple steps without necessarily stopping to show you each one. Chapter nine's checkpoint discipline isn't optional caution for this shape, it's close to the whole ballgame. An agent that completes five real-world actions before you see any output has already spent whatever your checkpoint would have caught, by the time you're looking at anything at all.

[PULLQUOTE: An agent that completes five real-world actions before you see any output has already spent whatever your checkpoint would have caught, by the time you're looking at anything at all.]

## Where the shape changes the method, specifically

**Briefing.** A chat assistant takes a written brief close to chapter two's literal five paragraphs. A purpose-built tool often takes the same five pieces of information spread across settings, templates, and configuration rather than prose, worth translating deliberately rather than assuming the tool "just knows" what a five-part brief would have said. An agent needs the brief to include an explicit boundary on what it's allowed to do without stopping, not just what a good output looks like, since the brief here is governing actions, not only words.

**Checking.** A chat assistant's output sits still until you read it, which is what makes chapter four's spot-check straightforward: nothing happens until you act. A narrow tool's output usually behaves the same way. An agent's output can already be irreversible by the time you see it, an email sent, a record changed, which means the checkpoint has to happen before the action, not after the draft, a meaningfully stricter version of chapter four's discipline than a chat assistant ever required.

**Firing.** Chapter seven's four disqualifiers apply to all three shapes, but the third one, a single error costing more than every success combined, deserves extra weight for an agent specifically. A chat assistant's worst realistic failure is a bad draft you catch before sending. An agent's worst realistic failure can be an action already taken, which changes the actual math behind that disqualifier even when the underlying task looks similarly low-stakes on paper.

## A concrete comparison

Odalys runs a small subscription box business and uses all three shapes for different tasks, which makes her setup a clean illustration. A general chat assistant drafts customer support replies, chapter four's ordinary spot-check discipline, read the draft, check the seam, send it. A narrow, purpose-built tool categorizes returned items by reason code from a dropdown-style interface, and her "brief" for it is really just a one-time configuration of which reason codes map to which categories, checked once at setup and revisited only when she adds a new code. An automation reorders low-stock items from her primary supplier automatically once inventory crosses a threshold, and for that one, alone among her three tools, she requires a checkpoint before the action fires, not after: any reorder over five hundred dollars pauses for her approval before the order actually goes out, because an agent's mistake here isn't a bad draft to fix, it's money already spent on inventory she might not have wanted.

The three shapes, side by side, in Odalys's own operation:

| | Chat assistant | Purpose-built tool | Agent |
| --- | --- | --- | --- |
| Her example | Support reply drafts | Return reason-code categorizer | Auto-reorder automation |
| Where the brief lives | Written five-part prose | Configuration and settings | Allowed-action boundary, dollar threshold |
| When the checkpoint happens | After the draft, before sending | At setup, and when codes change | Before the action fires |
| Worst realistic failure | A bad draft you catch | A miscategorized batch | Money already spent |

## The near-miss that set the threshold

Odalys didn't pick five hundred dollars out of caution alone. Her first version of the reorder automation had no dollar threshold at all, only a blanket rule requiring approval for any order touching a new supplier she hadn't used before, a boundary that felt reasonable when she wrote it and turned out to miss the actual risk entirely. A seasonal spike in one product's sales pushed its reorder quantity well above her normal order size, triggered automatically through her existing, already-approved supplier, and placed a genuine order eleven times larger than she'd have chosen herself, all before she saw a single line of it. Nothing about that order used a new supplier. Nothing tripped her original boundary. The mistake wasn't in the supplier relationship at all, it was in a quantity that had quietly drifted past what "routine" meant for that product.

She caught it within the hour, canceled what the supplier's own return window still allowed, and rewrote the checkpoint around what had actually gone wrong rather than what she'd originally guessed would: a dollar threshold on the order's total value, not a rule about which supplier it used. The lesson generalizes past inventory: a pre-action checkpoint is only as good as the boundary it's actually watching, and the boundary worth setting is rarely obvious until something slips through the one you guessed at first.

## Try this: name your own three shapes

List every AI tool you or your team currently uses, or are seriously considering. For each one, write which of the three shapes it is: a general chat assistant, a narrow purpose-built tool, or an agent that takes real actions on its own.

________________________________________________________________

For any tool you marked as an agent, write down what it can currently do without a human pausing to approve it first. If you can't answer that precisely, that's the seam to close before delegating anything further to it.

[TAKEAWAYS]

- "AI tool" spans at least three genuinely different shapes: a general chat assistant, a narrow purpose-built tool, and an agent that takes real actions on its own. The underlying management skill is the same across all three; a few specifics of how it applies aren't.
- A purpose-built tool's brief often lives in configuration and settings rather than prose. Translate chapter two's five parts deliberately rather than assuming the tool already knows them.
- An agent's checkpoint has to happen before an irreversible action, not after a draft, a stricter version of chapter four's discipline than a chat assistant requires.
- The third disqualifier from chapter seven, a single error costing more than every success combined, deserves extra weight for any agent that can act without a pause, because its worst failure is usually an action already taken, not a draft you catch in time.

[/TAKEAWAYS]

## Where this goes next

Chapter twenty looks at a category of task this book has mostly sidestepped until now on purpose: anything involving money directly, where the ordinary stakes of a delegated task go up by an order of magnitude.
