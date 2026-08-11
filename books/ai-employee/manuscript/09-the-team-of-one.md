# The Team of One

Ola runs a small nonprofit, and every quarter she sends a fundraising appeal letter to past donors. The letter needs three things done in order: research this quarter's giving trends so the appeal opens with something current, draft the actual appeal around that research, and format the result for a mail merge that personalizes each letter with the donor's name and last gift amount. She used to do all three herself, slowly. Then she tried handing the whole chain to AI in one long request: research this, then write the letter from it, then format it for merge, all in a single pass.

The letter that came back read beautifully. It opened with a specific-sounding claim about a rise in monthly giving among donors under forty, built the whole emotional appeal around that trend, and merged cleanly into three hundred personalized copies. Ola almost sent it. She caught the problem only because a board member happened to ask where the under-forty statistic came from, and when Ola went looking, she couldn't find it anywhere in the research step's own notes. It had drifted in somewhere between research and draft, a plausible-sounding elaboration on a much vaguer real trend, and by the time it reached the formatted, personalized, ready-to-mail version, it looked exactly as authoritative as everything true around it.

Nothing about any single step had failed the way Devon's proposal drafts failed back in chapter five, with one obvious invented number sitting in an obvious gap. Each step had done a plausible job of building on what the step before it produced, which was exactly the problem: the third step trusted the second step's output completely, the second step trusted the first step's output completely, and nobody, human or otherwise, ever looked at the seam between any two of them.

## Why a chain is riskier than its steps

A single delegated task fails or it doesn't, and chapter four's spot-check catches most of what matters. A chain of tasks, each one feeding the next, doesn't just add up that risk. It compounds it, the same way a machine built from several components in sequence is only as reliable as all of them working at once, not just the best one or the average one.

[KEY-INSIGHT: Research on how AI systems perform on tasks of different lengths and complexity has found a consistent pattern: reliability drops sharply as a task requires more sequential steps or more time to complete, even as overall model capability improves year over year. One widely cited 2025 study measuring this found that leading models could complete short, simple tasks reliably but their real-world success rate fell off sharply as task length and step count grew, a gap the researchers found has been closing over time but was still substantial as of the study. || Source: METR (Model Evaluation and Threat Research), Kwa, T., et al., "Measuring AI Ability to Complete Long Tasks," arXiv:2503.14499, March 2025.]

Think about what that means arithmetically, not just intuitively. If a single step is right nine times out of ten, that's a good rate for a delegated task, well above what chapter four's spot-check discipline needs to catch the rest cheaply. Chain three steps like that together with nobody checking in between, and the chance all three land correctly isn't ninety percent anymore. It's closer to seventy. Chain five, and it's closer to sixty. The steps didn't get worse. The chain did, purely from length, and the finished, formatted output at the end gives you no visual hint of which step the actual error crept in on, the same way Ola's mail-merged letter looked identically polished whether the underlying claim was true or invented.

[PULLQUOTE: The chain doesn't fail because a step got worse. It fails because length compounds risk, and a polished final output gives no hint of which step actually broke.]

## The fix is a checkpoint, not a coding project

Here's the part worth saying plainly, because it's easy to assume the fix for a multi-step process is a more sophisticated, more automated pipeline: it isn't, and this book isn't about to turn into one. You do not need to learn to build an autonomous agent, write code, or wire tools together to fix what happened to Ola's letter. You need exactly one thing: a human look at the output of each step before it becomes the input to the next one, the same spot-check discipline from chapter four, just inserted at every seam in the chain instead of only at the very end.

Run the research step. Read it, specifically checking anything that reads like a hard number or a claim you'd want to defend if a board member asked. Only then hand that reviewed research to the drafting step. Read the draft against the research you already checked, watching for exactly the kind of drift Ola missed, a specific claim that sounds like it came from the research but doesn't quite trace back to it. Only then hand the reviewed draft to the formatting step, which is usually the safest of the three because formatting rarely invents new claims, it just arranges existing ones.

Three short reviews, each cheap because each one is checking a single step's output against a single step's input, cost less total time than a full read-through of the finished letter would, and they catch the exact failure a full read-through is worst at catching: an error that's had two more steps to get dressed up in confident, coherent prose by the time anyone actually looks at it.

[KEY-INSIGHT: One of the most widely cited findings in software engineering is that the cost of fixing a defect rises sharply the later it's caught in a multi-stage process, by a factor the classic data puts anywhere from roughly four times to as much as a hundred times, depending on the project: cheap to fix during early requirements work, meaningfully more expensive once it reaches design or coding, and far more expensive again once it's shipped and found in the field. || Source: Boehm, B.W., "Software Engineering Economics," Prentice-Hall, 1981 (data originally presented in Boehm, B.W., "Software Engineering," IEEE Transactions on Computers, C-25(12), 1976).]

That pattern isn't specific to software, and it's exactly why checking at each seam beats checking only at the end. An invented statistic caught in the research step costs Ola thirty seconds to strike out. The same statistic caught after it's built the emotional core of a drafted appeal costs a rewrite. Caught after formatting and mail merge, on three hundred personalized letters, it costs either an awkward recall email or the reputational cost of never catching it at all. The error didn't get more wrong at each stage. It got more expensive to fix, precisely because more work had been built on top of it.

## Knowing where to stop chaining

Not every multi-step process is worth chaining through AI at every stage, and the same instinct from chapter seven's disqualification list applies here at the level of an individual step rather than a whole task. If one step in the chain is a judgment call, research prioritization that depends on knowing which donors the board actually cares about impressing this quarter, for instance, that step might belong to Ola herself, with AI picking back up for the drafting and formatting steps that follow her judgment call rather than trying to replace it.

A three-step chain with a checkpoint at each seam is manageable for almost anyone willing to spend a few extra minutes reading between steps. A seven or eight-step chain, even checked carefully at every seam, starts costing more in review time than it saves in drafting time, the same trade chapter four described for a single task's spot-check, now playing out across an entire process instead of one document. When a chain gets that long, the better fix usually isn't more automation. It's cutting the chain down to the steps that actually benefit from delegation and doing the rest yourself, the same triage chapter seven already taught you to run on a single task.

## When the chain itself is the problem

Sometimes the fix isn't more checkpoints. It's a shorter chain.

Desmond runs a small events company and tried automating his post-event client recap into seven chained steps: pull the attendance numbers, summarize vendor feedback, draft a wins section, draft an improvements section, pull it all into a client-facing narrative, format it against the company template, and generate a follow-up email referencing the recap. He dutifully added a checkpoint at every seam, the way this chapter recommends, and found the review time alone ran to nearly an hour per event, almost as long as writing the whole recap by hand used to take.

The problem wasn't that any single checkpoint was hard. It was that seven steps meant seven checkpoints, and the review time chapter four warned about, the cost of checking, had scaled right along with the chain instead of staying cheap. Desmond cut it to three: pull the raw numbers and feedback in one step, draft the full narrative, wins and improvements together, in a second step from that reviewed data, and format it in a third. Two checkpoints, not six. The seven-step version he'd built wasn't a more thorough process. It was one genuine task wearing the shape of a long chain, several sub-steps that never needed to be separate at all, because chaining had started to feel like the default move rather than a deliberate one.

## What this chapter will not do

This will not tell you every multi-step task is dangerous to delegate, or that chaining is a technique to avoid. Ola's three-step process works well now, with two checkpoints added, and saves her real time every quarter compared to writing the whole letter herself. The danger was never the chain. It was running the whole chain with nobody looking at the seams, mistaking a single polished final output for evidence that every step behind it had gone right.

It also won't pretend a checkpoint at every seam catches everything. A reviewer who's rushed, tired, or checking the wrong thing at a seam can still miss what's actually wrong there, the same limits from chapter four apply here at every joint in the chain, not just at the end. The checkpoint habit lowers the risk a chain compounds silently. It doesn't erase the need for the same real judgment chapters four and five have been building this whole book.

## Try this: map your chain

If you're already running, or considering, a multi-step delegated process, write out the actual steps in order:

| Step | What it produces | Is a checkpoint here worth the time? |
| --- | --- | --- |
| | | |
| | | |
| | | |

Count the steps. Past three or four, ask honestly whether any two adjacent steps are really one task wearing two labels, the way Desmond's wins and improvements sections were. Collapse what collapses cleanly before you add a single checkpoint.

[TAKEAWAYS]

- A chain of delegated steps is riskier than any single step in it. Errors compound across steps the way unreliability compounds across the parts of any sequential system, even when each individual step is fairly reliable on its own.
- A polished, fully formatted final output gives no hint of which step an error actually entered on. By the time you're reading the finished version, an early mistake has had every later step to get dressed up in confident prose.
- The fix is a human checkpoint at every seam, not a more sophisticated automated pipeline. Reading each step's output before it feeds the next step catches drift a single end-to-end review usually misses.
- Not every step belongs to AI. A genuine judgment call inside a chain is a candidate to keep for yourself, the same disqualification logic from chapter seven, applied one step at a time instead of to a whole task.

[/TAKEAWAYS]

## Where this goes next

Chapter ten turns everything from writing a real brief through knowing when to stop chaining into an actual thirty-day plan: what to do in week one, what to add in week two, and how to tell, by the end of the month, that the system has actually taken hold.
