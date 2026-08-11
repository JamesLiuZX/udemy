# The Spec Nobody Can Argue With

Picture the meeting that happens two days before almost every AI feature launch. Someone asks if it's ready. Someone else says it feels ready. A third person, usually the most senior voice in the room, says it looks good to them and the launch proceeds. Nobody in that room is being careless. They're doing the only thing the document in front of them allows, because the spec they wrote described what the feature should do, not what "done" actually means, and a description of behavior can't settle an argument the way a threshold can.

This is the most common gap in AI feature specs, and it's almost never intentional. A normal product spec for deterministic software gets away with describing behavior, because behavior and correctness are the same question when a system does the same thing every time. "The button submits the form" is both a description and a testable claim. For an AI feature, the same style of sentence, "the assistant answers customer questions accurately," describes intent without being testable at all. Nobody can look at that sentence and say whether the feature is done, only whether it sounds like the right idea.

## What the tribunal actually required

Go back to the Air Canada chatbot from chapter one, because the legal ruling names, almost accidentally, exactly the standard this chapter is trying to help you meet. The tribunal didn't require Air Canada to have a perfect chatbot. It required the company to have taken reasonable care that the information it gave customers was accurate, and found that it hadn't, because nothing in Air Canada's process caught a chatbot answer that directly contradicted the airline's own written policy before that answer reached a customer.

[KEY-INSIGHT: The Moffatt v. Air Canada ruling turned on whether the airline took reasonable care to ensure the information its chatbot gave customers was accurate. The tribunal found it hadn't: nothing in Air Canada's process checked the chatbot's answers against the airline's actual, documented policy before those answers reached a customer. || Source: Civil Resolution Tribunal of British Columbia, Moffatt v. Air Canada, 2024 BCCRT 149 (Feb. 14, 2024).]

"Reasonable care" is a legal standard, but it maps directly onto a product practice: a documented threshold, checked before launch, against a representative set of real cases. That's not a compliance nicety layered on top of good product work. For an AI feature, it's close to the definition of good product work, the same document that protects a launch decision internally is the document that would demonstrate reasonable care externally if it were ever questioned.

## The two-part spec

A spec that can actually settle the two-days-before-launch argument has two parts, and most AI feature specs today have only the first.

**Part one, the familiar part:** what the feature does, who it's for, what it looks like. This is the part every PM already knows how to write, and it doesn't change much from how you'd spec a deterministic feature.

**Part two, the part that's usually missing:** the evaluation threshold. A specific, numeric, checkable claim, in the same format every time: "on a set of N real cases, chosen to include the hard ones, the feature achieves [specific outcome] at least [percentage] of the time, and fails in [specific way] no more than [percentage] of the time." This is the sentence that turns "should answer accurately" into something a person can actually check by running the golden set and reading the number.

[PULLQUOTE: A description of behavior can't settle an argument the way a threshold can. "Should answer accurately" isn't a testable claim. A number is.]

## What this looks like written down

Here's the same acceptance criterion, written the old way and the new way, for a feature that answers customer questions from a knowledge base:

| The old way | The new way |
| --- | --- |
| "The assistant should answer customer questions accurately using our help center content." | "On a 50-case set covering the 10 most common ticket categories plus 15 known edge cases, the assistant states no fact that contradicts the help center at least 96% of the time, and a human reviewer rates the answer as usable without correction at least 88% of the time." |

The old version reads fine in a document and settles nothing in a room. The new version is longer, and it's also the only one of the two that a skeptical engineer, a nervous legal reviewer, or a tribunal, could actually check against evidence rather than against a feeling in the room two days before launch.

## A second industry learns the same lesson

Air Canada shows what happens when a threshold is missing from a single customer-facing answer. Rite Aid shows what happens when the same gap sits underneath an entire program, running for years, across hundreds of stores, before anyone outside the company found out.

Rite Aid deployed facial recognition technology in hundreds of its US stores to flag shoppers it believed were likely shoplifters, comparing customers against a watchlist in real time. In December 2023 the Federal Trade Commission announced a settlement banning Rite Aid from using facial recognition for surveillance for five years. The FTC's complaint didn't turn on whether facial recognition can work. It turned on what Rite Aid had never actually checked: the agency found the company had never tested the technology's accuracy before rolling it out, never enforced the image-quality standards the system needed to function reliably, and never adequately trained the employees acting on its alerts. The result, according to the FTC, was a program that disproportionately misidentified women and people of color as shoplifters, sometimes leading staff to search or eject a real customer over a match nobody had verified was reliable in the first place. The five-year ban ended up outliving the chain itself: Rite Aid went through a second bankruptcy and closed its last stores in 2025.

[KEY-INSIGHT: The FTC's December 2023 settlement with Rite Aid, the agency's first algorithmic-unfairness enforcement action, banned Rite Aid from using facial recognition for surveillance for five years. The FTC's complaint centered on Rite Aid's failure to test the technology's accuracy before deployment, its failure to enforce image-quality standards the system needed to function, and its failure to adequately train staff acting on its alerts, resulting in a pattern of false matches that disproportionately flagged women and people of color. || Source: Federal Trade Commission, "Rite Aid Banned from Using AI Facial Recognition After FTC Says Retailer Deployed Technology without Reasonable Safeguards," press release, December 19, 2023.]

Notice that every failure the FTC cited is a missing threshold from this chapter's own two-part spec, just written in the language of a regulatory complaint instead of a product document. "Never tested the technology's accuracy" is the absence of an evaluation threshold. "Never enforced image-quality standards" is the absence of the input conditions a threshold has to specify to mean anything. A spec for that program, written the way this chapter argues for, would have forced someone to write a sentence like "on a representative set of real store footage, including low light and partial-face angles, the system correctly matches a watchlisted individual at least N% of the time, and falsely flags an uninvolved customer no more than M% of the time," and then to actually check it before the cameras went live in a single store, let alone hundreds. Nobody has to guess what would have happened next if that number had come back bad. That's the entire value of writing it down before launch instead of after a five-year ban.

## Why this isn't extra process for its own sake

If two numeric thresholds sound like bureaucracy layered onto a spec that used to be one paragraph, it's worth being direct about why that reading is backwards. The old one-paragraph spec didn't actually avoid the work. It deferred it, from a deliberate exercise before launch to a reactive scramble after the first customer complaint, the exact trade chapter one's status-update comparison already walked through. The threshold isn't new work invented by this chapter. It's the same work, moved earlier, where it's cheaper and where it protects the launch decision instead of only explaining it after the fact.

## What this chapter will not do

This chapter will not give you one universal threshold number to copy into every spec. Ninety-six percent is right for some features and dangerously low for others; chapter eight is entirely about sizing a threshold to the actual cost of the failure it's guarding against, not picking a number that sounds rigorous.

It also won't turn spec-writing into a solo activity you do at your desk and hand down. A threshold that only you believe in doesn't survive the same room that used to accept "should answer accurately" on faith. Getting a second person to actually apply your threshold the same way you would, consistently, is a separate skill, and it's the entire subject of chapter five.

## Write the sentence, not the paragraph

Take one AI feature you own, shipped or planned, and find its current spec. Find the sentence that describes what "done" means. Read it back and ask honestly: could a skeptical engineer, using only that sentence, determine whether the feature is ready without asking you a follow-up question.

If the answer is no, rewrite it using this chapter's exact template: on a set of N real cases, chosen to include the hard ones, the feature achieves [specific outcome] at least [percentage] of the time, and fails in [specific way] no more than [percentage] of the time. Don't worry yet about whether the percentages are right. Chapter four covers building the case set that number gets measured against, and chapter eight covers sizing the threshold itself to the actual cost of being wrong. For now, the exercise is narrower and cheaper: notice how many specs on your own roadmap are still, honestly, the old way, one paragraph that sounds like a decision and settles nothing.

[TAKEAWAYS]

- A spec that only describes behavior can't settle whether an AI feature is done. Only a spec with a checkable threshold can.
- The two-part spec: what the feature does (the familiar part), and a specific numeric evaluation threshold checked against a representative case set (the part usually missing).
- "Reasonable care," the actual legal standard that decided the Air Canada case, maps directly onto this practice. A documented threshold, checked before launch, is what reasonable care looks like for a probabilistic feature.
- Writing the threshold doesn't create new work. It moves work that was always going to happen, from a reactive scramble after a complaint to a deliberate check before launch.

[/TAKEAWAYS]

## Where this goes next

Chapter four is about building the actual set of cases a threshold gets checked against, the golden set, because a threshold is only as trustworthy as the fifty cases it's measured on, and building that set well is its own specific skill with its own specific failure modes.
