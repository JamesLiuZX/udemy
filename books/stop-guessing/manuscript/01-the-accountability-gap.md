# The Accountability Gap

The demo lasted four minutes, and everyone in the room loved it.

Someone typed a real support ticket into the box, a straightforward one: a customer asking where a delayed order had gotten to. The feature drafted a reply in about two seconds. Warm, accurate, on brand. Someone else tried a messier ticket, one with a typo in it, and the draft still came back clean. Heads nodded around the table. Your VP said, out loud, "okay, I'm sold," and by the end of the week a launch date was sitting on the roadmap.

Six weeks later, one ticket did not go well. Nothing dramatic: no outage, no press. Just a customer reply that went out sounding perfectly confident about something that wasn't true, caught only because the customer happened to write back confused. Somebody asked you, in the next leadership sync, whether that was a one-off or a pattern. You opened your mouth to answer and realized you didn't have one. You had a four-minute demo from six weeks ago. You didn't have an answer for right now.

That gap, between being accountable for a feature and being able to say with any real confidence whether it works, is what this book is about closing. Not by making you an engineer. Not by teaching you to read model architecture diagrams. By giving you the specific, learnable habit of turning "it seems to work" into a number you built, checked, and would stake your name on.

If you manage, spec, or evaluate any product with an AI component in it, that gap is currently yours whether you asked for it or not. This chapter explains exactly where it comes from, because the fix only makes sense once the cause is precise.

## The tool you already have doesn't apply here

Every product manager already owns a method for deciding whether a feature works: acceptance criteria. Write down what "done" means before the work starts. Engineering builds to that definition. QA checks it holds. You ship once it does. It's a good method, and it has worked for as long as software has shipped in cycles governed by test cases.

It has one assumption buried so deep inside it that nobody usually says it out loud: **given the same input, the system produces the same output.** Click the button, the same thing happens, every time. Submit the form, the same validation runs, every time. That assumption is what makes a test case meaningful at all. Write the test once, run it forever, trust the result.

An AI feature breaks that assumption on purpose, as a direct consequence of how it works, not as a bug that better engineering will eventually fix. Ask a large language model the same question twice and you can get two different, individually reasonable answers. This isn't inconsistency in the pejorative sense. It's the mechanism doing exactly what it's built to do: at each step, the model isn't looking up a fixed answer, it's sampling from a distribution of plausible next words, weighted by how likely each one is given everything that came before. Turn that dial toward more randomness and you get more variety, useful for anything that benefits from not sounding the same way twice. Turn it toward less and the outputs converge, though rarely to bit-for-bit identical. Either way, "the same input produces the same output" stops being true, and it was never going to become true with a better prompt or a newer model. It's the wrong test for what you're holding.

That's the actual reason your acceptance-criteria habit stopped working the moment this feature entered your roadmap. Not because you're bad at your job. Because the tool you were trained to use was built for a category of software that doesn't behave this way, and nobody handed you the replacement.

## The ticket that broke the pattern

Here's the ticket from six weeks in, in full, because the abstract version of this story is easy to nod along to and easy to forget by the next meeting.

It landed at 4:50 p.m. on a Friday. Three run-on sentences, a typo in the order number, a screenshot the system couldn't read, and a customer who mentioned two different issues in the same message and only actually cared about one of them. Nothing like the two clean tickets from the demo. The feature drafted a reply anyway, because that's what it does with every input, and this time the draft stated the wrong order number as settled fact, in the same warm, confident voice it used for everything else. No hedge. No flag. It read exactly as trustworthy as the version that had impressed the room six weeks earlier.

Nothing about the system changed between the demo and that Friday ticket. The input changed, and because the underlying mechanism is probabilistic rather than fixed, a harder or stranger input doesn't just risk a worse answer. It risks a *differently shaped* failure than anything the demo showed, one nobody wrote a test case for because nobody could have predicted its exact shape in advance.

[PULLQUOTE: A demo shows you one point in the distribution. It cannot show you the tail, and the tail is where the expensive failures live.]

This is the specific reason a single successful demo is close to worthless as evidence, and most launch decisions still get made on exactly that evidence. Your own VP said "I'm sold" after two tickets. Two tickets was never enough to be sold on. It was enough to be intrigued by, which is a different, much smaller thing.

The Friday ticket above is a composite, built to be recognizable rather than to name names. What happened to Air Canada wasn't. In February 2024, a Canadian tribunal ordered the airline to honor a bereavement discount its own support chatbot had invented on the spot, a policy that didn't exist, stated in the same confident tone the airline's real policy would have used. Air Canada argued in its defense that the chatbot was responsible for its own words, separately from the airline itself. The tribunal did not find that argument persuasive.

[KEY-INSIGHT: A Canadian small claims tribunal ordered Air Canada to pay damages after its customer service chatbot invented a bereavement fare refund policy that did not exist and stated it as fact. The airline argued it wasn't liable for its own chatbot's words; the tribunal disagreed, ruling a company is responsible for all information on its website, "whether it comes from a static page or a chatbot." || Source: Civil Resolution Tribunal of British Columbia, Moffatt v. Air Canada, 2024 BCCRT 149 (Feb. 14, 2024).]

## The same mechanism, a completely different feature

It's tempting to file the Air Canada story under "customer service chatbots," a narrow category, and assume the lesson doesn't reach whatever you're actually building. It reaches further than that, because the failure was never about customer service. It was about a probabilistic system answering a question it hadn't seen phrased quite that way before, confidently, in a register indistinguishable from the answers it got right.

New York City learned the same lesson at a much larger scale. In October 2023 the city launched MyCity, an official chatbot meant to help small business owners navigate licensing, labor, and housing regulations, a use case with nothing in common with an airline's bereavement policy on paper: different agency, different feature, different underlying question entirely. Within months, reporters testing the bot found it confidently telling business owners things that were flatly illegal under New York law: that they could take workers' tips, that landlords could refuse tenants paying with housing vouchers, that a restaurant could simply refuse cash. None of these answers looked uncertain. Each one used the same even, official tone as the questions the bot answered correctly, because the mechanism generating both was identical: a distribution of plausible-sounding next words, with nothing in the architecture flagging which outputs happened to be true.

[KEY-INSIGHT: New York City's official MyCity chatbot, built to help small business owners navigate city regulations, was found in March 2024 to be telling business owners that employers could legally keep workers' tips, that landlords could reject tenants paying with housing vouchers, and that restaurants could refuse cash payment, all illegal under New York City law and stated as confident fact. The city's own mayor acknowledged the chatbot's answers were "wrong in some areas" but initially kept it live regardless, and by mid-2025 the tool was reported to be costing the city roughly half a million dollars a year while still giving unreliable guidance. || Source: "NYC's AI Chatbot Tells Businesses to Break the Law," The Markup, March 29, 2024.]

Notice what the two stories share, because it's the entire argument of this chapter, not a coincidence of two badly built products. Both systems had almost certainly been demoed successfully before launch. Both produced answers that were fluent, well formatted, and indistinguishable in tone from a correct one. And both failures were specific to a question nobody happened to test before the system met a real person who needed the true answer, not a plausible one. A support-reply assistant and a municipal regulatory chatbot could not be less alike as products. The mechanism that broke them was exactly the same mechanism, which is why this chapter's lesson doesn't narrow to whichever feature you happen to own.

## What replaces a test case

The replacement isn't a better test case. It's a different kind of claim entirely: an **evaluation threshold**, measured against a representative set of real cases, with a number attached that you check before every launch and every meaningful change.

Concretely, instead of writing "the draft correctly identifies the customer's issue," which sounds like an acceptance criterion but can't actually be checked by running the system once, you write something closer to this: on a set of fifty real tickets, chosen to include the hard and ambiguous ones, the draft states no fact about an order that isn't verified at least 98% of the time, and a human reviewer would send it with no edits at least 90% of the time. That's not a vaguer standard than a normal acceptance criterion. It's a more honest one, because it's built for something that varies instead of pretending it doesn't.

The difference is more concrete than it sounds. Here's the same status update, said two ways, about the same feature, on the same day:

| What gets said | What the listener can actually check |
| --- | --- |
| "It's pretty much ready, the team's happy with it" | Nothing. There is no fact in this sentence. |
| "94% pass on a fifty-case set weighted toward the hard tickets, fails on multi-issue messages specifically, fix scoped for next sprint" | Everything. The number, the failure category, and the plan are each independently verifiable. |

Notice the second version isn't longer to say once the work behind it exists. It just moves the work earlier, from a scramble after a customer complains to a deliberate exercise before anyone outside the team sees the feature. That's the actual trade this book is asking you to make: a few focused hours building a measurement, in exchange for never again having to answer "does this work" with a shrug wearing a confident tone of voice.

## A five-minute experiment worth running on your own team

Before any of the framework, it's worth seeing the actual size of the problem with your own eyes, because most people underestimate it until they do.

Take one real, finished piece of output from an AI feature you already have, something a colleague hasn't seen. Show it to three or four colleagues separately, with no discussion between them, and ask each one to rate it from one to ten on whether it's good enough to ship as is. Don't tell them what "good enough" means. Let them decide.

The scores will not agree. Not roughly agree: disagree by a wide margin, on the same piece of text, from people whose judgment you trust individually. Run this exercise inside a team for the first time and the most common reaction isn't "the AI output was bad." It's a quiet unease about how much of the team's current confidence in "it seems fine" was ever actually shared confidence at all, as opposed to four different private definitions of fine that happened to sound like agreement in a meeting.

That disagreement is not a character flaw in your colleagues, and it isn't fixable by finding smarter reviewers. It's what happens whenever a group of people are asked to judge something the same way without ever having written down what "the same way" means. A rubric fixes exactly this, and chapter five is entirely about building one that two people can actually apply the same way, consistently, on the second try and the fiftieth.

## Why this isn't a skills problem

It's worth being direct about something before going further, because the alternative reading of this chapter is a demoralizing one: that you should already know how to do this, and not knowing is a gap in you specifically.

It isn't. The methods this book teaches didn't exist in most product management curricula, bootcamps, or certifications until very recently, and most people currently shipping AI features taught themselves under deadline pressure, usually after a Friday-afternoon ticket of their own. If your instinct, faced with an AI feature, was to reach for the acceptance-criteria habit that has served you for years, that instinct was reasonable. It was also wrong for this specific job, the way a genuinely skilled carpenter's instincts would be wrong the first time they were handed a job that required plumbing. The skill transfers partly. The rest has to be learned as its own thing.

There's a second, quieter reason this isn't a personal failing. Every stakeholder in that leadership sync, the engineer, the designer, your own manager, was very likely operating from the same borrowed instinct you were, unless they'd specifically had to build an evaluation practice before. Nobody in that room secretly knew the answer you felt like you were missing. The room's confidence after the demo was an average of several people's unexamined intuition, not a shared, checked fact, which is exactly what the five-minute experiment above demonstrates the moment you actually run it. Realizing the room doesn't secretly know something you don't is, for most people, the single most useful reframe in this chapter.

None of this argues for lowering the bar. It argues the opposite. Once you notice the room's confidence was never actually shared, the honest move is to build the thing that would make it shared: a real number everyone can look at, instead of staying quiet because everyone else seems calm.

A sentence that gestures at how profoundly AI is changing everything, without committing to a single fact a reader could check, is the sentence a book like this one is tempted to write next. Distrust it on sight, here or anywhere else. The rest of this book tries hard never to say anything that isn't checkable.

## What this book will not do

Say this plainly, because a business book that only ever tells you where its method works is not one you should trust with a launch decision.

This book will not turn you into a machine learning engineer, and it isn't trying to. You will not learn how to train a model, tune its weights, or debug why a specific token got picked over another. That's a different job, done by different people, and pretending otherwise would make this book worse at the one thing it's actually for.

It also won't help much if your organization already has a mature evaluation practice: dedicated ML engineers building golden sets as part of their normal workflow, a product function that already speaks fluently in pass rates and confidence intervals. If that's you, this book mostly confirms what you already do, with maybe one or two sharper framings along the way. It's written for the much larger group standing where the opening scene of this chapter started: accountable, present in the room, one honest step away from being able to say something better than "it seems to work."

And it will not remove the discomfort of the five-minute experiment. Learning to measure disagreement doesn't make disagreement disappear. It makes it visible, arguable, fixable, which is a real improvement over invisible and quietly costing you a launch. It is not the same thing as everyone suddenly agreeing.

## Where this goes next

Chapter two gives you a map: seven distinct shapes an AI feature can take, from a simple classifier to a multi-step autonomous agent, and a clear-eyed answer to the one question that comes before any evaluation work at all, whether AI is even the right tool for what you're building. Some of the best decisions in this book are decisions not to build something. That one comes first for a reason.

From there, the chapters build in the order the actual job asks the questions. Chapters three and four turn a feature idea into a written spec and a real set of test cases, the foundation everything else stands on. Five gets a second reviewer scoring those cases the same way you would, so "we checked it" means more than one person's opinion. Six and seven price the feature and size the risk of anything that acts semi-autonomously, both questions finance and legal will eventually ask whether or not you've prepared an answer. Eight builds a register for what could go wrong before someone in a compliance review finds it for you. Nine covers the specific numbers worth watching once the feature is live, because the evaluation work doesn't end at launch, it just changes what it's measuring. Ten is about saying all of this out loud, calibrated, to a stakeholder who wants certainty you don't actually have and shouldn't pretend to. Eleven and twelve teach you to hold your own in a room full of engineers: the vocabulary and judgment calls that separate a credible question from a bluff, then the specific case of retrieval, the single most common way an AI feature reaches outside its own model. Thirteen is where that retrieval system actually breaks in production, and how to catch it before a customer does. Fourteen answers the specific objections you'll actually hear once you start saying calibrated numbers out loud, the ones a chapter of theory doesn't fully prepare you for. Fifteen walks the entire method through three complete worked cases in domains this book hasn't touched yet, so you see it run start to finish before being asked to run it yourself. Sixteen turns all of it into a repeatable habit for a new role or a new quarter. Seventeen, the last chapter, is an honest accounting of where every method in this book stops working, because a book that never says so isn't one you should trust with a real launch decision.

None of that is abstract theory waiting to be applied later. Each chapter ends with something to actually do this week, on a feature you already own, because the entire premise of this book is that the gap from the opening scene closes through practice, not through finishing the table of contents.

[TAKEAWAYS]

- A demo is one sample from a distribution, not proof the distribution is safe. Never launch on demo evidence alone.
- If a status update contains no number a listener could independently check, it isn't a status update.
- Disagreement between reviewers isn't a people problem. It's what happens before anyone writes down what "good" means.
- This gap isn't a personal skills failure. Almost nobody in the room has been taught this yet, including whoever seems most confident.

[/TAKEAWAYS]
