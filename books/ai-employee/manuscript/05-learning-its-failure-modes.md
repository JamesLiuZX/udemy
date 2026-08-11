# Learning Its Failure Modes

Devon runs a one-person consulting practice, and he uses the same AI tool for two completely different jobs. Every Monday, it drafts the first pass of a client proposal: scope, timeline, a few comparable case numbers pulled from his own past projects. Every day, it also manages his calendar, moving meetings around when a client asks to reschedule.

Three weeks in, the calendar assistant double-booked a client call against a dentist appointment because the client had written "3pm EST" and Devon's calendar was set to Pacific, and the tool quietly assumed the times matched. Devon caught it the morning of, rescheduled the dentist, and walked away from the whole experience with one flat conclusion: this thing makes careless mistakes, so it should be watched constantly. For the next month, he read every proposal draft as if it might contain the same kind of careless error the calendar had.

It never did. The proposal drafts had a completely different problem, one he only found by accident three months in, when a client emailed asking where a "40% average time savings" figure in his proposal had come from. Devon didn't recognize the number. He hadn't written it, and neither had any of his past project reports. The tool had invented a plausible-sounding statistic to fill a gap in a case study section, the same fluent, confident voice it used for the numbers that were real. That failure had nothing to do with timezones, and the timezone failure had nothing to do with invented statistics. Two tasks, same tool, two completely unrelated ways of going wrong, and Devon had spent a month watching for the wrong one on the wrong job.

## The mistake hiding inside "AI makes mistakes"

"AI makes mistakes" is true and almost useless, the same way "employees sometimes underperform" is true and tells you nothing about which employee, on which task, in which specific way. Devon's error wasn't carelessness. It was treating the tool as one thing with one failure pattern, when what he actually had was two separate task and tool pairings, each with its own specific, learnable, largely predictable way of going wrong. The calendar task fails on ambiguous timezone notation. The proposal task fails by inventing specific numbers to fill a gap in a narrative. Neither pattern predicts the other, and averaging them into one vague caution, "watch out, it makes mistakes," is worse than useless because it spends your limited attention on the wrong signal on any given task.

[PULLQUOTE: "AI makes mistakes" is true and almost useless. It tells you nothing about which task, on which tool, in which specific way.]

The same pattern shows up at a much larger scale in one of the more rigorous studies to actually measure this. Researchers at Stanford tested several AI legal research tools, all marketed on the same premise: built specifically to avoid the hallucinated case citations that had already embarrassed lawyers in court. If "AI hallucinates" were a fact about AI in general rather than about specific task and tool pairs, you'd expect these tools to fail at roughly similar rates on roughly similar tasks. They didn't.

[KEY-INSIGHT: Testing several AI-powered legal research tools built specifically to reduce hallucinated citations, researchers found Lexis+ AI produced incorrect or unsupported answers on more than 17% of test queries, while Westlaw's AI-Assisted Research product did so on roughly 33%, nearly twice the rate, on the same category of legal research task. A third tool, Thomson Reuters's Ask Practical Law AI, showed a different failure mode almost entirely: incomplete rather than fabricated answers, on more than 60% of queries. || Source: Magesh, V., Surani, F., Dahl, M., Suzgun, M., Manning, C.D., & Ho, D.E., "Hallucination-Free? Assessing the Reliability of Leading AI Legal Research Tools," Journal of Empirical Legal Studies, 2025 (originally released as a Stanford RegLab/HAI working paper, 2024).]

Same broad task, three specifically built tools, three different failure rates, and one of the three failing in a genuinely different way than the other two, incompleteness instead of invention. A user who walked away from testing Lexis+ AI with a general rule about "AI legal research tools" would carry an unearned, wrong assumption straight into Ask Practical Law AI, where the measured risk, at least as of that study, wasn't confident fabrication at all, it was a confident-sounding answer that's simply missing half of what a complete one would include. The specific rates will have moved since; the variance between tools is the durable finding. The lesson isn't specific to lawyers. It's the same lesson Devon learned the expensive way: the unit that has a failure mode is the task and the tool together, not the tool alone and never "AI" as a category.

## The other half of the same matrix

Devon's story shows one tool, two tasks, two unrelated failure patterns. It's worth seeing the mirror case too: one task, two tools, because the unit that matters is the pairing, and a pairing has two axes, not one.

Simone runs marketing for a regional gym chain and tested two different AI writing tools on the identical task, the weekly member newsletter, before picking one to use going forward. Both tools got the structure right: a workout tip, a member spotlight, a class schedule reminder. Where they differed was specific and consistent. The first tool, run five times, twice quietly changed a class time in the schedule reminder to a plausible-sounding but wrong hour, the kind of error that's invisible unless you already know the real schedule. The second tool never touched the schedule, not once across five runs, but it repeatedly invented a specific member's name and a specific compliment for the spotlight section when Simone's brief didn't supply one, a fabrication problem the first tool never showed.

Same task, same brief, same five inputs. Two genuinely different failure modes, one per tool. If Simone had tested only the first tool and concluded "AI newsletter tools garble schedule times," she'd have carried that exact wrong caution into the second tool, watching for a schedule error that tool was never going to make while missing the fabricated member quote it actually produced twice. The lesson from Devon's story runs in the other direction here, same conclusion from the opposite angle: neither the task nor the tool alone tells you the failure mode. Only the specific pairing does.

## Building the actual performance review

A real performance review of an employee doesn't say "sometimes makes mistakes." It says what kind, on what kind of work, how often, and under what conditions, because that's the only version of the information that's actually useful for deciding what to double-check next time. Building the same thing for a delegated task takes three ingredients, all of which you already have if you ran the trial from chapter three and the spot-checks from chapter four.

**Collect the misses, not just the total count.** Every time a spot-check catches something wrong, write down what specifically went wrong, not just that something did. "Invented a statistic" and "missed a timezone" are different entries even if you're tempted to file both under "made an error."

**Look for the pattern across misses, not within one.** One invented number could be a fluke. Three invented numbers, all appearing in the same kind of gap, a case study section with a missing data point, is a pattern: this task, with this tool, tends to fabricate specifically when the input has a hole in it. That's the exact thing worth writing down and checking for on every future draft, precisely the "seam" from chapter four, now named instead of rediscovered by accident.

**Separate the pattern from the tool's general reputation.** A tool that's excellent at scheduling and unreliable at invented statistics is not "a good tool" or "a bad tool." It's a tool that's good at one task and needs a specific, targeted check on another. Collapsing that back into a single verdict is exactly the mistake that cost Devon a month of misdirected attention.

Once you've done this for a task a handful of times, you have something closer to an actual personnel file than a vague impression: not "it makes mistakes," but "on proposal drafts specifically, it fabricates a supporting number about one time in five when the input data has a gap, and it has never once gotten a date or a client name wrong." That second sentence tells you exactly where to look next time. The first one never did.

## Why this list should be short

A useful failure-mode list has two or three entries per task, not ten. Once you're tracking ten different ways a task might go wrong, you've stopped building a targeted checklist and started rebuilding the "check everything, trust nothing" habit chapter four already showed doesn't work, just relabeled as diligence. If your list is growing past three or four real, observed patterns, the honest read usually isn't that the tool has that many distinct failure modes. It's that the task itself is too broad, several different jobs wearing one label, and the fix is splitting it into the narrower tasks it's actually made of, not writing a longer checklist for the combined one.

## What this chapter will not do

This will not promise a stable list. The proposal tool that fabricates statistics today might stop doing that after a model update and start doing something else instead, an unannounced version change with real behavioral consequences, exactly the kind of thing this book avoids anchoring examples to for how fast it goes stale. Treat every failure-mode list as current as of your last several checks, not permanent. Revisit it periodically the same way you'd revisit an employee's performance review, not write it once and file it away for good.

It also won't tell you a short, specific failure-mode list makes a task safe to stop watching entirely. It tells you exactly where to keep watching, and exactly where you can now stop watching as hard, which is a meaningfully smaller task than declaring the whole thing solved.

## Try this: start the file

Pick one task you've spot-checked at least a few times already. Write down, in plain language, every specific miss you can actually remember, not a vague sense of "sometimes it's off":

| What went wrong | How often (roughly) | Under what condition |
| --- | --- | --- |
| | | |
| | | |
| | | |

If you land on more than three or four real rows, that's not a failure of the task, it's a sign the task is actually several tasks wearing one name. Note which rows would split cleanly into a separate task of their own, and treat that as a flag for the next time you scope a trial the way chapter three describes, not something to solve today.

[TAKEAWAYS]

- "AI makes mistakes" is true and useless. The real unit of analysis is one task paired with one tool: each pairing has its own specific, learnable failure pattern, and one pairing's pattern rarely predicts another's.
- Even tools built for the identical purpose can fail at different rates and in different ways. Testing one AI legal research tool tells you almost nothing about a different one built for the same job.
- Build a short, specific list from your actual spot-checks: what went wrong, how often, and under what condition, not a generic sense that the tool is "pretty good" or "a little unreliable."
- A failure-mode list with more than three or four real entries usually means the task is actually several tasks stapled together. Split it instead of writing a longer checklist.

[/TAKEAWAYS]

## Where this goes next

Chapter six is what to actually do with a known failure pattern once you have one: feeding it back to the tool in a way that actually sticks, instead of correcting the same mistake fresh every single time it happens.
