# The Accountability Gap

The demo went well. That's usually where this story starts.

Somebody on your team, or a vendor, or you yourself, put together a working example: an AI feature that drafts responses, or triages tickets, or summarizes a document, or approves something small automatically. You ran it a few times in the meeting. It looked sharp. Leadership nodded. A launch date got written down.

Then the feature shipped, and a few weeks later a case came back that made you flinch a little: a summary that quietly dropped the one sentence that mattered, a draft that sounded confident about something false, an approval that technically followed the rules and still felt wrong. Somebody asked you, directly, whether this was a one-off or a pattern. And you realized, standing in that meeting, that you didn't actually know. You had a demo. You didn't have an answer.

That gap, between being accountable for a feature and being able to say with any real confidence whether it works, is what this book is about closing. Not by making you an engineer. Not by teaching you to read model architecture diagrams. By giving you the specific, learnable habit of turning "it seems to work" into a number you built, checked, and would stake your name on.

If you manage, spec, or evaluate any product with an AI component in it, that gap is currently yours whether you asked for it or not. This chapter explains exactly where it comes from, because the fix only makes sense once the cause is precise.

## The tool you already have doesn't apply here

Every product manager already owns a method for deciding whether a feature works: acceptance criteria. You write down what "done" means before the work starts, engineering builds to that definition, QA checks the definition holds, and you ship once it does. It's a good method. It has worked for as long as software has shipped in cycles governed by test cases.

It has one assumption baked so deep into it that nobody usually has to say it out loud: **given the same input, the system produces the same output.** Click the button, the same thing happens, every time. Submit the form, the same validation runs, every time. That assumption is what makes a test case meaningful at all. Write the test once, run it forever, trust the result.

An AI feature breaks that assumption on purpose, as a direct consequence of how it works, not as a bug that better engineering will eventually fix. Ask a large language model the same question twice and you can get two different, individually reasonable-sounding answers. This isn't inconsistency in the pejorative sense. It's the mechanism doing exactly what it's built to do: at each step, the model isn't looking up a fixed answer, it's sampling from a distribution of plausible next words, weighted by how likely each one is given everything that came before. Turn that dial toward more randomness and you get more variety, useful for anything that benefits from not sounding the same way twice. Turn it toward less and the outputs converge, though rarely to bit-for-bit identical. Either way, "the same input produces the same output" is no longer true, and it was never going to become true with a better prompt or a newer model. It's the wrong test for what you're holding.

This is the actual reason your existing acceptance-criteria habit stops working the moment an AI component enters the feature. Not because you're bad at your job. Because the tool you're using was built for a category of software that doesn't behave this way, and nobody handed you the replacement.

## What this actually looks like on a Tuesday

Abstract mechanism is easy to nod along to and easy to forget by the next meeting. Here is the same problem in a shape you'll recognize.

Say your team ships a feature that drafts a reply to an inbound support ticket, and a human reviews the draft before it sends. In the demo, someone typed in a clean, well-written ticket, the draft came back accurate and well-organized, and everyone in the room was satisfied. That's a single sample from a distribution, treated as if it were the whole distribution. It's the equivalent of testing a new checkout flow once, with a test credit card, on a fast connection, and calling it launch-ready.

Now picture the ticket that actually arrives at 4:50 p.m. on a Friday: three run-on sentences, a typo in the order number, an attached screenshot that the system can't read, and a customer who mentions two different issues in the same message and only cares about one of them. The same feature, run against that input, might handle it gracefully. It might also confidently draft a reply to the wrong issue, state the wrong order number as fact, or invent a policy detail that sounds exactly as fluent as the correct ones from the demo. Nothing about the system changed between the demo and the Friday ticket. The input changed, and because the underlying mechanism is probabilistic rather than fixed, a harder or stranger input doesn't just risk a worse answer, it risks a *differently shaped failure* than anything the demo showed you, one nobody wrote a test case for because nobody could have predicted its exact shape in advance.

This is the specific reason a single successful demo is close to worthless as evidence, and it's worth sitting with, because most launch decisions are still made on exactly that evidence. A demo shows you one point in the distribution. It cannot show you the tail, and the tail is where the expensive failures live.

## What replaces a test case

The replacement isn't a better test case. It's a different kind of claim entirely: an **evaluation threshold**, measured against a representative set of real cases, with a number attached that you check before every launch and every meaningful change.

Concretely, instead of writing "the summary correctly identifies the customer's request," which sounds like an acceptance criterion but can't actually be checked by running the system once, you write something closer to: "on a set of fifty real support tickets, chosen to include the hard and ambiguous ones, the summary preserves every deadline and dollar amount at least 95% of the time, and a human reviewer would call the summary usable without editing at least 90% of the time." That's not a vaguer standard than a normal acceptance criterion. It's a more honest one, because it's built for something that varies, instead of pretending it doesn't.

Everything in this book is really one long argument for that single move: replace a claim that assumes consistency with a claim that measures it. The chapters ahead walk through exactly how to build the set of cases, how to score them without fooling yourself, what the resulting number actually costs to produce and maintain, how to size the risk if the number turns out to be wrong, and how to say all of this out loud to a room that would rather hear "it's pretty much ready."

The difference is more concrete than it sounds. Here's the same status update, said two ways, about the same feature, on the same day:

| What gets said | What the listener can actually check |
| --- | --- |
| "It's pretty much ready, the team's happy with it" | Nothing. There is no fact in this sentence. |
| "94% pass on a fifty-case set weighted toward the hard tickets, fails on multi-issue messages specifically, fix scoped for next sprint" | Everything. The number, the failure category, and the plan are each independently verifiable. |

Notice the second version isn't longer to say once the work behind it exists; it just moves the work earlier, from a scramble after a customer complains to a deliberate exercise before anyone outside the team sees the feature. That's the actual trade this book is asking you to make: a few focused hours building a measurement, in exchange for never again having to answer "does this work" with a shrug wearing a confident tone of voice.

## A five-minute experiment worth running on your own team

Before any of the framework, it's worth seeing the actual size of the problem with your own eyes, because most people underestimate it until they do.

Take one real, finished piece of output from an AI feature you already have, something a colleague hasn't seen. A drafted email, a support summary, a generated report section. Show it to three or four colleagues separately, with no discussion between them, and ask each one to rate it from one to ten on whether it's good enough to ship as-is. Don't tell them what "good enough" means. Let them decide.

The scores will not agree. Not roughly agree, disagree by a wide margin, on the same piece of text, evaluated by people whose judgment you trust individually. Run this exercise inside a team for the first time and the most common reaction isn't "the AI output was bad," it's a quiet unease about how much of the team's current confidence in "it seems fine" was ever actually shared confidence at all, as opposed to four different private definitions of fine that happened to sound like agreement in a meeting.

[AUTHOR-INPUT: the specific story of a feature you personally shipped, reviewed, or inherited where two reasonable people scored the same output very differently, and what that disagreement actually cost, in time, in a delayed launch, or in a decision made on a number that turned out not to mean what everyone assumed]

That disagreement is not a character flaw in your colleagues, and it isn't fixable by finding smarter reviewers. It's what happens whenever a group of people are asked to judge something the same way without ever having written down what "the same way" means. A rubric fixes exactly this, and chapter five is entirely about how to build one that two people can actually apply the same way, consistently, on the second try and the fiftieth.

## Why this isn't a skills problem

It's worth being direct about something before going further, because the alternative reading of this chapter is a demoralizing one: that you should already know how to do this, and not knowing is a gap in you specifically.

It isn't. The methods this book teaches didn't exist in most product management curricula, bootcamps, or certifications until very recently, and most of the people currently shipping AI features taught themselves under deadline pressure, usually after something went wrong in production first. If your instinct, faced with an AI feature, was to reach for the same acceptance-criteria habit that has served you for years, that instinct was reasonable. It was also wrong for this specific job, the way a completely competent carpenter's instincts would be wrong the first time they were handed a job that required plumbing. The skill transfers partly. The rest has to be learned as its own thing.

There's a second, quieter reason this isn't a personal failing, and it's worth naming because it changes how you should feel walking into your next AI feature review. Every stakeholder in that room, the engineer, the designer, your own manager, is very likely operating from the same borrowed acceptance-criteria instinct you are, unless they've specifically had to build an evaluation practice before. Nobody in that room is quietly holding the answer you feel like you're missing. The room's collective confidence in "it seems fine" is usually an average of several people's individually unexamined intuition, not a shared, checked fact, which is exactly what the five-minute experiment two sections back demonstrates the moment you actually run it on a real team. Realizing that the room doesn't secretly know something you don't is, for most people, the single most useful reframe in this entire chapter.

None of this is an argument for lowering the bar, either. It's the opposite: once you notice that the room's confidence was never actually shared, the honest move is to build the thing that would make it shared, a real number everyone can look at, rather than staying quiet because everyone else seems calm.

> A sentence that gestures at how profoundly AI is changing everything, without committing to a single fact a reader could check, is the sentence a book like this one is tempted to write next. Distrust it on sight, here or anywhere else. The rest of this book tries hard never to say anything that isn't checkable.

## What this book will not do

Say this plainly, because a business book that only ever tells you where its method works is not one you should trust with a launch decision.

This book will not turn you into a machine learning engineer, and it isn't trying to. You will not learn how to train a model, tune its weights, or debug why a specific token got picked over another. That's a different job, done by different people, and pretending otherwise would make this book worse at the one thing it's actually for.

It also won't help much if your organization already has a mature evaluation practice, dedicated ML engineers building golden sets as part of their normal workflow, and a product function that already speaks fluently in pass rates and confidence intervals. If that's you, this book mostly confirms what you already do, with maybe one or two sharper framings along the way. It's written for the much larger group standing where the opening scene of this chapter started: accountable, present in the room, and one honest step away from being able to say something better than "it seems to work."

And it will not remove the discomfort of the five-minute experiment two sections back. Learning to measure disagreement doesn't make disagreement disappear. It makes it visible, arguable, and fixable, which is a real improvement over invisible and quietly costing you a launch, but it is not the same thing as everyone suddenly agreeing.

## Where this goes next

Chapter two gives you a map: seven distinct shapes an AI feature can take, from a simple classifier to a multi-step autonomous agent, and a clear-eyed answer to the one question that comes before any evaluation work at all, whether AI is even the right tool for what you're building. Some of the best decisions in this book are decisions not to build something. That one comes first for a reason.

From there, the chapters build in the order the actual job asks the questions. Chapters three and four turn a feature idea into a written spec and a real set of test cases, the foundation everything else stands on. Five gets a second reviewer scoring those cases the same way you would, so "we checked it" means more than one person's opinion. Six and seven price the feature and size the risk of anything that acts semi-autonomously, both questions finance and legal will eventually ask whether or not you've prepared an answer. Eight builds a register for what could go wrong before someone in a compliance review finds it for you. Nine covers the specific numbers worth watching once the feature is live, because the evaluation work doesn't end at launch, it just changes what it's measuring. Ten is about saying all of this out loud, calibrated, to a stakeholder who wants certainty you don't actually have and shouldn't pretend to. Eleven turns the whole method into a repeatable habit for a new role or a new quarter. Twelve, the last chapter, is an honest accounting of where every method in this book stops working, because a book that never says so isn't one you should trust with a real launch decision.

None of that is abstract theory waiting to be applied later. Each chapter ends with something to actually do this week, on a feature you already own, because the entire premise of this book is that the gap from the opening scene closes through practice, not through finishing the table of contents.

Everything after this chapter, the golden set, the rubric, the cost model, the risk register, the metrics that hold up after launch, builds on the single idea it exists to plant: you are not being asked to eliminate uncertainty. You are being asked to measure it, honestly, in a form specific enough that the next hard question in the room has a real answer instead of a shrug dressed up as confidence.
