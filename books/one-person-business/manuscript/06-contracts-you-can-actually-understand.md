# Contracts You Can Actually Understand

The contract landed in Priya's inbox from a new client, a mid-sized agency, eleven pages of the kind of legal language that makes a busy freelancer skim to the signature line and hope. She meant to read it properly that weekend. She read the first two pages twice, understood most of it, hit a paragraph about "work made for hire" and indemnification, and did what she always did with that paragraph: assumed it was standard, and signed.

It probably was standard. That's not really the problem this chapter is about. The problem is that "probably" isn't a great word to build a business relationship on, and Priya had no fast way to turn "probably standard" into "actually checked" without either paying a lawyer to read an eleven-page agency contract for a mid-sized project, or spending an evening she didn't have cross-referencing legal terms on forums of uncertain quality.

## What AI is actually good at here, and it's narrower than it sounds

Before anything else in this chapter: what follows is not legal advice, and no tool, AI or otherwise, changes that. What a language model is genuinely useful for is a first, fast pass that turns dense legal phrasing into plain English you can actually evaluate, and flags the clauses worth a closer look. What it is not reliably useful for is telling you, with confidence, that a contract is safe to sign. Confidence and correctness are different things, and a model will produce the first one whether or not it has the second.

[KEY-INSIGHT: In a controlled 2018 study, an AI contract-review tool was tested against twenty experienced corporate lawyers reviewing the same five real non-disclosure agreements for risk. The AI averaged 94 percent accuracy at spotting the risks planted in the contracts, against an average of 85 percent for the lawyers, and did it in 26 seconds against an average of 92 minutes for the human reviewers. The catch worth naming plainly: the best individual lawyer in the study matched the AI's accuracy exactly, and the study measured NDAs specifically, a narrower and more standardized document than a full services agreement. || Source: LawGeex, in partnership with legal academics from Stanford, Duke, and USC, "Comparing the Performance of Artificial Intelligence to Human Lawyers in the Review of Standard Business Contracts," February 2018.]

Read that result carefully rather than as a headline. It's genuinely striking that an AI system matched or beat experienced lawyers on speed and average accuracy for a narrow, standardized document type. It is not evidence that AI review replaces a lawyer's judgment on a contract that's unusual, high-stakes, or drafted by the other side to favor them, which describes a meaningful share of what actually lands in a freelancer's inbox. Use the speed. Stay honest about the ceiling.

[PULLQUOTE: A model will produce confidence whether or not it has correctness. Those are different things, and only one of them protects you.]

## The three-pass read

Here's the actual workflow, built around what a first pass is good for rather than what it isn't.

**Pass one: plain-English translation.** Paste the contract in and ask for a section-by-section summary in ordinary language, no legal jargon retained. This alone catches most of what Priya was skimming past: not because the original wording was hiding something, but because dense phrasing makes even an unremarkable clause feel unreadable, and unreadable clauses get skipped rather than understood.

**Pass two: the flag list.** Ask specifically for anything that's unusual, one-sided, or worth a question before signing: payment terms that favor the client heavily, IP or ownership language broader than the actual project needs, an indemnification clause that exposes you personally, a termination clause with no notice period. Naming the categories to look for, rather than asking an open "is this okay," produces a far more useful answer, because it forces the model to check specific things instead of offering a general reassurance.

**Pass three: the question list, not the redline.** Turn the flags into plain questions you'd actually ask the client: "This says the deliverables become your exclusive property on payment, but the agreement doesn't define what happens to my source files if you cancel mid-project. Can we add a line covering that?" Sending a short list of specific questions reads as careful, not difficult, and most legitimate clients answer them without friction. A contract that generates real pushback on a reasonable question is itself useful information about that client.

## Marcus's flag list has one category Priya's doesn't

Pass two's flag categories, payment, IP, indemnification, termination, cover most of what a services agreement needs checked. Development contracts routinely carry one more risk that a generically trained flag list can miss unless you name it explicitly: ownership language broad enough to claim code that existed before the project started.

Marcus reuses a personal library of utility functions and boilerplate across nearly every engagement, the accumulated efficiency of three years of similar work, and some client contracts, usually not out of malice but out of a template nobody customized, define "work product" broadly enough to technically claim anything delivered as part of the project, pre-existing code included. His addition to pass two is a fifth flag category specific to his kind of work: does the IP clause distinguish between code written for this project and code Marcus already owned and brought to it. A well-drafted contract does. A copy-pasted one often doesn't, not out of bad faith, just because whoever assembled the client's template never worked with a developer who reuses infrastructure across clients.

The same instinct extends to open-source dependencies. If a project's stack leans on open-source libraries carrying their own licenses, a flag-list pass that asks specifically whether the contract's IP language conflicts with any dependency's license terms catches a problem months before it becomes a hard-to-unwind mess, rather than after a client's own legal team notices it during due diligence on an acquisition.

## What this genuinely saves, and what it doesn't

What this workflow saves is the Sunday evening Priya used to lose to a contract she'd sign anyway, uncertain the whole time whether she'd actually understood it. Fifteen minutes of a structured three-pass read replaces hours of skimming and hoping, and it replaces "probably standard" with an actual list of what's standard and what isn't, in language you can evaluate instead of just accept.

What it doesn't save is the moment a contract is genuinely unusual, high-value, or clearly drafted to favor the other side. A twenty-minute AI-assisted read of an eleven-page standard services agreement is a reasonable use of the tool. The same read on a six-figure exclusivity agreement, or one with a non-compete clause reaching further than feels right, is not a substitute for twenty minutes of an actual lawyer's time, and the cost comparison there favors the lawyer by a wide margin once you weigh what's actually at stake.

[AUTHOR-INPUT: your own story here, a specific clause you almost missed, or almost signed, that a plain-English pass caught, and what you actually did about it]

## The exact prompts

All three passes, worth saving together as a sequence:

> **Pass one:** "Summarize this contract section by section in plain English, no legal jargon retained. Where a section is genuinely ambiguous rather than just densely worded, say so explicitly instead of picking one interpretation silently.
>
> [paste contract]"
>
> **Pass two:** "Review this contract for anything unusual, one-sided, or worth a question before signing, specifically: payment terms that favor the other party heavily, IP or ownership language broader than the project needs, an indemnification clause that exposes me personally, a termination clause with no notice period[, and pre-existing IP or open-source license conflicts, if applicable]. List each flag with the specific clause it comes from."
>
> **Pass three:** "Turn each flag above into one plain, non-confrontational question I could send to the other party."

Pass two's bracketed addition is Marcus's fifth category from earlier in this chapter; adjust the named categories to your own field's specific risks rather than using the four generic ones unmodified. A flag list built from named categories that don't actually match your kind of work misses exactly the risk that matters most to you.

## Why having any real contract matters more than any single clause

Step back from the specific flags for a moment, because the choice this chapter really cares about happens earlier than any clause-by-clause read: whether a written contract exists at all.

[KEY-INSIGHT: A peer-reviewed study analyzing Freelancers Union Independent Worker Survey data found that using a written contract was associated with income roughly 13.7 percent higher than working without one, rising to 21.7 percent higher among the New York respondents specifically studied, even after accounting for the contract not guaranteeing full, on-time payment by itself. || Source: William M. Rodgers, Sara Horowitz, and Gabrielle Wuolo, "The Impact of Client Nonpayment on the Income of Contingent Workers: Evidence from the Freelancers Union Independent Worker Survey," 2014.]

That gap isn't proof a contract magically produces better clients. It's more likely evidence of what a contract represents: a freelancer confident enough in their own value to insist on formal terms tends to also price, negotiate, and select clients more deliberately across the board. Either way, the three-pass read in this chapter only has something to work on if a contract exists in the first place. For any inquiry that doesn't come with one, chapter three's proposal is the document to build the terms into before work starts, not something to add after a dispute makes it necessary.

## What this chapter will not do

This chapter will not tell you which specific clauses are legally enforceable in your jurisdiction, because that genuinely varies by state, country, and the specific facts of a dispute, and getting it wrong with false confidence is worse than not answering at all. It will not tell you a contract is safe. What it gives you is a faster, more honest first read, and a sharper sense of exactly which questions are worth asking a client, or worth taking to an actual lawyer before you sign anything with real money or real risk attached.

[TAKEAWAYS]

- AI contract review is genuinely fast and, on narrow standardized documents like NDAs, competitive with experienced lawyers on accuracy. It is not evidence that it replaces judgment on unusual or high-stakes agreements.
- Run a three-pass read: plain-English translation, a flag list built from named categories (payment, IP, indemnification, termination), then a question list, not a redline.
- Sending specific questions to a client reads as careful, not difficult, and a client's reaction to a reasonable question is itself useful information.
- The line is value and unfamiliarity, not effort. A standard services agreement is a reasonable AI-assisted read. A six-figure or unusual agreement is worth an actual lawyer's twenty minutes.

[/TAKEAWAYS]

## Try this: run the three-pass read on your current contract

Pull up whatever contract governs your most active client relationship right now, even one you signed months ago and never revisited. Run all three passes tonight:

1. **Translate.** Ask for a plain-English, section-by-section summary.
2. **Flag.** Ask specifically about payment terms, IP and ownership, indemnification, and termination notice, plus your own kind of work's specific risk (pre-existing IP and open-source licensing, if you build software; usage rights and revision limits, if you create).
3. **Question.** Turn anything flagged into one plain question. You don't have to send it today. Just write it down.

Most freelancers running this for the first time on a contract they already signed find at least one thing worth a question, not because the contract is bad, but because nobody reads a document this closely the first time, under deadline pressure, with a new client waiting for a signature.

## Where this goes next

Chapter seven turns to the work that's easy to deprioritize precisely because nothing about it feels urgent on any given day: staying visible to future clients without marketing eating the week you don't have to give it.
