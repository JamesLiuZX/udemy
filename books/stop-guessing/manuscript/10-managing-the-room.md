# Managing the Room

The roadmap review had one slide left when someone asked the question every PM eventually gets asked: "When does the contract-review assistant ship, and how good will it be?" The honest answer was that nobody had built the eval yet. The answer that actually came out was "Q3, ninety-five percent accurate." It felt like confidence in the room. It was two guesses, stacked on top of each other, wearing a single number nobody had earned yet.

Nothing in that sentence was a lie in the ordinary sense. Nobody in the room was trying to deceive anyone. It was optimism, stated with more precision than the evidence behind it could support, which is a specific and avoidable failure mode, not a personality flaw. This chapter is about the two places that failure shows up most often: the stakeholder conversation happening today, and the roadmap document that outlives it.

## Translate the hedge

A stakeholder's expectations rarely come from your golden set. They come from a keynote demo, a competitor's launch post, or a headline about a frontier model, none of which mention the failure category your own eval work already found. The job isn't to dampen their enthusiasm. It's to replace an expectation built on marketing with one built on evidence you already have sitting in a spreadsheet.

| Instead of | Say |
| --- | --- |
| "It's pretty much ready" | "94% on our golden set, fails on this named category" |
| "The model's really good now" | "Cleared the quality floor, here's the model we picked and why" |
| "It should be fine" | "Blast radius is bounded, here's the named approver" |

Read the right column as a direct export of chapters already written, not new language to invent under pressure in the room. A pass rate from chapter five, a scorecard decision from chapter six, a blast radius sort from chapter seven, each one already exists before the stakeholder conversation starts. What every right-column sentence has that the left column lacks is something a listener could check later. "Ninety-four percent, fails on this category" is a claim reality can prove wrong, which is exactly what makes it trustworthy now. "It's pretty much ready" can't be checked against anything, so it never earns or loses credibility. It just gets forgotten until something breaks, and then it gets remembered for the wrong reason.

Notice, too, that the right column is shorter to say once the number is actually in hand, not longer. The specificity isn't extra work in the room. It's work already done, back when the golden set and the scorecard got built, and the room is just the place it finally pays off.

## The demo that costs you later

What gets put in front of a stakeholder matters as much as what gets said about it. A demo built from three hand-picked, all-clean cases never touches the known failure category, and trust breaks the first time the stakeholder hits it themselves, on their own, unprepared. A demo that includes one clean success and one real boundary case from the golden set names the limitation before anyone finds it alone, and trust survives the first real failure because it was already expected.

The difference shows up later, not in the room that day. A stakeholder who's never seen the feature fail treats the first failure as a broken promise. A stakeholder who's already seen a named limitation, on your terms, in a controlled setting, treats the identical failure as an expected edge case. Same failure, completely different outcome, decided entirely by what was shown weeks earlier.

Choosing that boundary case honestly is harder than it sounds, because the instinct before an important meeting pulls hard toward the safest possible showing. Resist it specifically here. The whole value of naming a limitation before someone else finds it is lost if the limitation shown is a trivial one nobody would have hit anyway. Pick the case that actually worries you, not a token weakness chosen for how harmless it looks next to the good ones.

[PULLQUOTE: A stakeholder who's already seen a named limitation treats the first real failure as an expected edge case. A stakeholder who hasn't treats it as a broken promise.]

## Don't overcorrect into sandbagging

Sandbagging every estimate is its own failure, not a safe default, and it's worth naming because the instinct after being burned once swings hard toward maximum caution. If every estimate is quietly padded three times over, a stakeholder learns to mentally discount everything said, which means the one estimate that really is at risk stops landing too. The goal was never pessimism. It was calibration: a number that's right about as often as it claims to be, not padded in either direction.

Watch for the specific symptom of overcorrection: a stakeholder starts routinely double-checking numbers already checked, or quietly building their own buffer on top of an existing one. That's not caution on their part. It's the market price of a track record that's stopped being informative, and it costs exactly as much to earn back as trust lost the other way. A track record with zero misses in either direction isn't a sign of skill. It's usually a sign of padding thick enough to hide the real variance underneath it.

## The roadmap that doesn't lie

The same failure that turned one stakeholder answer into two stacked guesses can sit quietly inside an entire roadmap, and it usually gets there through a template rather than a decision. Most roadmap templates have one column for "when" and no column for "validated," inherited from years of features that never needed that second column, because a checkout redesign's scope is knowable in advance in a way that ninety-five percent accuracy on an unbuilt eval simply isn't.

| Feature | Sprint status | Threshold | Date |
| --- | --- | --- | --- |
| Contract-review assistant | Not started | -- | -- |
| Support-reply v2 | Cleared | 94%, named failure category | Q3 |
| Refund agent expansion | In progress | -- | -- |

Read the columns left to right, because it's the actual sequence, not just a table layout. Sprint status comes before threshold, threshold comes before date. A roadmap line with a date in it and nothing in the threshold column is the exact trap from this chapter's opening scene, just formatted differently, and it's worth noticing that an empty threshold cell is an honest state. "In progress, no threshold yet" is incomplete and true. A guessed threshold dressed up as measured is the same hedge from the stakeholder conversation, wearing a spreadsheet instead of a sentence.

This isn't an argument against giving dates at all. The support-reply row above has a real date, because it has a real threshold behind it, sourced from a golden set that actually got scored. The contract-review row doesn't get a date yet, and that's not a weaker roadmap. It's a more honest one, and the difference between the two rows is exactly the difference between a discovery sprint that's happened and one that hasn't.

[KEY-INSIGHT: In 2012, MD Anderson Cancer Center contracted with IBM for what was originally scoped as a six-month, $2.4 million pilot to build an AI system recommending cancer treatments to oncologists. The project ran through four years of contract extensions without ever reaching clinical use at the hospital, and was canceled in 2016 after spending $62 million, according to a University of Texas System audit that also found the project had bypassed standard procurement procedures. || Source: University of Texas System audit, reported in "Big Data Bust: MD Anderson-Watson Project Dies," Medscape, February 2017.]

That gap between a six-month pilot and four years of extensions is what a roadmap looks like when a date gets set before the threshold that should have produced it. Nobody involved set out to spend sixty-two million dollars proving a capability that was never validated. The original commitment simply priced a scope and a timeline for something nobody had measured yet, and every extension after that was the cost of discovering, one contract renewal at a time, how far the real number sat from the promised one.

Adding these two columns to a roadmap template costs nothing beyond the willingness to leave a cell honestly blank. An evidence-first roadmap looks less impressive on a single slide than one full of confident dates, and leadership often wants the date more than they want the honesty behind it. That pressure is real, not imaginary, and it's the same calibration principle from earlier in this chapter, aimed at an entire quarter instead of one conversation: the honest version costs something in the room today, and pays it back the day a date would otherwise have quietly slipped, or a project would have quietly run four years past its original pilot.

[TAKEAWAYS]

- Translate every hedge into the specific, checkable claim already sitting behind it: a pass rate, a scorecard decision, a blast radius sort. The specific version is usually shorter to say, not longer, once the number exists.
- Demo a real boundary case on purpose, not just clean successes. A limitation named before someone finds it survives contact with reality; a limitation discovered alone reads as a broken promise.
- Calibration cuts both ways. Padding every estimate for safety is as uninformative as inflating one, and a stakeholder eventually prices both the same way: by ignoring the number.
- A roadmap needs sprint status and a real threshold before it earns a date. An empty threshold cell is honest. A guessed one dressed up as measured is the same failure the MD Anderson-Watson project ran for four years and sixty-two million dollars before anyone stopped it.

[/TAKEAWAYS]

## Where this goes next

Chapter eleven turns this whole book into a repeatable habit for a new role or a new quarter, because none of it was meant to be applied once and filed away. It works because it's the way you'd approach the next feature, and the one after that, by default.
