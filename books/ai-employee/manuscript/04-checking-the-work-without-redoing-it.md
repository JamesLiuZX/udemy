# Checking the Work Without Redoing It

Maria runs the books for a nine-person landscaping company, and every quarter she hands AI a batch of three hundred and forty expense line items to categorize: fuel, equipment, payroll, materials, the usual buckets. The first quarter she tried it, she opened all three hundred and forty afterward and checked every single one against the receipt. It took her longer than categorizing them herself would have. She closed the spreadsheet that night having proven the AI could do the task and having saved exactly zero minutes doing it.

The second quarter, still stinging from how long the first one took, she skimmed the categories, saw nothing wrong in the first twenty rows, and filed the whole batch. In May, her accountant flagged eleven items posted as "equipment" that were actually gas station fuel purchases, the two categories AI kept confusing because the same vendor sold both from the same till. Eleven misclassified line items pushed her quarterly numbers off by enough that the accountant had to redo the depreciation schedule.

Both quarters failed for opposite-looking reasons. Both failed the same way: Maria never found the one thing actually worth checking. Quarter one, she checked everything and found nothing, because she wasn't checking for anything in particular, just re-verifying at random. Quarter two, she checked nothing and missed the one recurring error that was hiding in plain sight the whole time, repeating in a predictable pattern she'd have caught in about ninety seconds if she'd known to look for it.

## The false choice

Redoing everything and checking nothing feel like opposites, but they share a hidden assumption: that checking AI's work means either reading all of it or reading none of it. That assumption is wrong, and it's the reason both of Maria's quarters failed. The actual skill is neither. It's knowing where errors are likely to cluster, and checking there, hard, while skipping the rest with real confidence instead of nervous half-attention.

This is not a new skill invented for AI. It's how a good editor reads a junior writer's fifth draft, not the first: not word by word from the top, but straight to the places a piece like this usually goes wrong, the transition, the ending, the one claim that needs a source. It's how an experienced nurse checks a new hire's medication chart: not every single entry with equal weight, but the high-risk drugs and the unusual dosages first. Redoing everything is what you do for someone you've never worked with and have no data on. Checking nothing is what you do for someone you've decided, on no real evidence, to trust completely. Spot-checking with a target is what you do for someone whose specific failure pattern you already know, which is exactly the position chapter three's trial task is supposed to leave you in.

[PULLQUOTE: Redoing everything and checking nothing feel like opposites. They share the same hidden assumption: that checking means all of it or none of it.]

## Why the smart middle actually works

It sounds like it should be riskier than reading everything. It measurably isn't, and the reason is one of the oldest, most counterintuitive findings in how humans review other people's work: reviewing everything makes you worse at reviewing, not better, because attention isn't a flat resource you spend evenly across three hundred and forty rows. It's a resource that runs out, and a reviewer's error-catch rate drops the longer a review session runs, exactly the failure Maria hit in quarter one without knowing to name it. A tired reviewer skimming row three hundred catches less than an alert reviewer targeting the twelve rows most likely to be wrong.

[KEY-INSIGHT: In one of the earliest and most cited studies of sustained attention, radar operators watched an unmarked clock hand jump forward at irregular intervals over a two-hour session and had to report each jump. Their detection rate dropped ten to fifteen percent within the first half hour alone, and kept declining, more gradually, for the rest of the session. The task never changed. The watchers did. || Source: Mackworth, N.H., "The Breakdown of Vigilance during Prolonged Visual Search," Quarterly Journal of Experimental Psychology, 1, 1948, pp. 6-21.]

That drop happened in the first thirty minutes, not the third hour, which is the detail worth sitting with. Maria's three hundred and forty rows would have taken her well past that thirty-minute mark, which means her attention was already degrading before she was even a third of the way through quarter one's "check everything" pass. The rows she was most likely to miss weren't randomly distributed either. They were disproportionately the ones near the end, exactly where a real error was actually sitting.

That's the case for targeting instead of reading everything. The case against reading nothing is less about attention and more about a specific, well-documented trap: once something arrives dressed as a finished answer, people stop checking it against other evidence they already have sitting right in front of them, even when that evidence directly contradicts it.

[KEY-INSIGHT: In a flight-simulator study, pilots using an automated electronic checklist were told to shut down an engine after a fire warning, even though other cockpit instruments contradicted the alert. Seventy-five percent of pilots followed the automated recommendation anyway. A control group doing the identical task with a traditional paper checklist, no automated recommendation to defer to, made the same wrong call only twenty-five percent of the time. || Source: Mosier, K.L., Palmer, E.A., & Degani, A., "Electronic Checklists: Implications for Decision Making," Proceedings of the Human Factors Society 36th Annual Meeting, 1992, pp. 7-11.]

Notice what actually produced the gap. It wasn't that the automated group had worse instruments or less information available to them. They had the exact same contradicting instrument readings sitting in the exact same cockpit. The automation's recommendation just made them stop looking at it. That is precisely what happened to Maria in quarter two: the categorized spreadsheet looked finished, so she stopped cross-checking it against the one thing that would have caught the error, the vendor names she already had in the same file.

## Building an actual spot-check

Here's the method that would have caught Maria's error in about two minutes instead of missing it for two months.

**Find the seam, not the middle.** Errors don't scatter evenly across a batch. They cluster where the task is genuinely ambiguous: two categories that overlap, an edge case the brief didn't cover, a format the tool hasn't seen much of. Before you check anything, ask where this specific task could plausibly go wrong, the way Maria's fuel-versus-equipment vendor was always going to be the seam the moment she thought about it for ten seconds.

**Check the seam completely, not a sample of it.** If fuel-versus-equipment is the risk, look at every single line item that touches that vendor, not a random ten percent of the whole batch. A random sample across three hundred and forty rows might easily miss all eleven fuel misclassifications by chance. A targeted check of the twenty rows from that one vendor catches every one of them, in a fraction of the time reading all three hundred and forty would take.

**Sample the rest lightly, for a different kind of confidence.** Once the known seam is checked, a quick scan of ten or fifteen rows from elsewhere in the batch isn't there to catch a specific error. It's there to catch a pattern you didn't anticipate, the seam you didn't know to look for yet. Light, not exhaustive: you're listening for a surprise, not auditing for certainty.

**Write down what you found, every time.** The seam changes as the tool's failure pattern shifts, and chapter five is built entirely around noticing that shift instead of checking the same seam forever out of habit after it's stopped being the real risk.

## A second seam, a different kind of task

The seam isn't always a mixed-up category. Sometimes it's a missed word.

James manages maintenance requests for a 140-unit apartment complex, and AI triages incoming tenant messages into "urgent" and "routine" before they hit his queue. The failure mode Maria dealt with was a mix-up between two similar buckets. James's is different: the tool occasionally files a message as routine when it technically mentions a repair category that's usually minor, but does so in a sentence that also mentions water. "Routine: kitchen faucet handle is loose" and "Routine: kitchen faucet is leaking under the sink" look almost identical to a keyword-matching glance, and only one of them is a "call a plumber today" problem, not a "get to it next week" one.

Reading every message defeated the point of automating triage at all, a hundred and forty units generate a lot of routine noise. Trusting the routine bucket completely meant a leak sat in the queue for four days once, and the tenant below reported a ceiling stain before anyone caught it. The seam, once James named it, was narrow and specific: any message in the routine bucket that also contains "water," "leak," "drip," or "wet," regardless of what category it got filed under. He checks every one of those completely, several a week, and skims the rest of the routine bucket lightly for anything that reads urgent on a plain read despite its label. The fix wasn't reading more messages. It was reading the right four words.

## What this is actually trading off

Maria's quarter of expensive learning, compressed to one glance:

| Strategy | Time cost | What it caught | Why |
| --- | --- | --- | --- |
| Check all 340 rows | Longer than doing it herself | Nothing new | Attention decays long before row 340 |
| Check nothing | Minutes | Missed 11 misfiled items for two months | Finished-looking output stopped the question |
| Check the seam (about 20 rows, one vendor) | About two minutes | All 11 | Errors cluster where categories overlap |

A full check trades time for a false sense of thoroughness, since a tired reviewer three hundred rows in isn't actually thorough no matter how carefully they started. No check at all trades time for real risk, the kind that shows up two months later as a redone depreciation schedule. A targeted spot-check trades neither. It costs a few minutes instead of an afternoon, and it catches the errors that were actually going to happen instead of the errors a random sample might or might not stumble onto.

That trade only works, though, because it depends on already knowing roughly where a task tends to break, which is knowledge you don't have on day one. The first few times you run any new delegated task, before you've built up that picture, check more broadly than this chapter recommends, closer to the trial-run discipline from chapter three than to a narrow, confident seam-check. Spot-checking a seam you haven't actually identified yet isn't efficient. It's just a full check's carelessness wearing a smarter-sounding name.

## What this chapter will not do

This will not tell you a spot-check replaces sign-off on anything that actually matters. A quarterly filing, a client-facing document, anything where being wrong is expensive or slow to unwind, still gets a full read by a human before it goes anywhere, the same way a hospital doesn't spot-check the medication chart for a patient in the ICU. Spot-checking is the right tool for volume, recurring, individually low-stakes work, which describes most delegated tasks but not all of them.

It also won't pretend the seam stays fixed forever. The vendor that kept confusing fuel and equipment might get cleanly resolved next quarter and a completely different seam opens up somewhere else. A spot-check habit that never updates which seam it's checking is just quarter two's mistake again, dressed up as a system.

## Try this: name your seam

Pick a task you're already delegating and haven't formally spot-checked yet. Answer these before your next batch comes in:

- Where is this task genuinely ambiguous, two categories that overlap, an edge case, a format the tool rarely sees?
- What's the narrowest, most specific version of that seam you can name, a vendor, a keyword, a field, not just "sometimes it's wrong"?
- How will you check that seam completely, not sample it, the next time this task runs?
- What does a light, five-minute scan of everything else actually look like, and what are you listening for when you do it?

Write the answers down somewhere you'll actually see again. That's the whole of chapter five's failure-mode list, started a chapter early.

[TAKEAWAYS]

- Checking AI's work isn't a choice between reading everything and reading nothing. Both extremes fail the same way: neither one is actually checking for the errors that are actually likely.
- Find the seam where this specific task tends to break, check it completely, then sample the rest lightly for surprises.
- Automation doesn't just risk being wrong. It risks making you stop checking evidence you already have sitting in front of you, even when that evidence contradicts it.
- A spot-check only works once you know where a task tends to break. Before that, check broadly, closer to a trial run than a targeted spot-check.

[/TAKEAWAYS]

## Where this goes next

Chapter five turns "where this task tends to break" from a one-time discovery into an ongoing habit: building a real, specific picture of a task's failure modes instead of relearning the same seam by accident every few months.
