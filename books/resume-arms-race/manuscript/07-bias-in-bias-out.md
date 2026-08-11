# Bias In, Bias Out

A colleague asked Marcus a question he didn't have a ready answer for: "Does our screen let older candidates through at the same rate as everyone else?" Nobody had built the ATS to discriminate by age on purpose. But one of its filters auto-advanced candidates whose most recent degree was within the last eight years, a rule someone had set years earlier as a rough proxy for "current on modern tools," and Marcus realized, turning it over, that a rule keyed to how recently you graduated is also, structurally, a rule keyed to how old you probably are. Nobody had to intend that for it to be true.

That distinction, between what a rule intends and what a rule does, is the entire chapter, and it's worth stating as plainly as the law itself states it before going any further: **this chapter is not legal advice.** Nothing in it should substitute for your own employment counsel's review of your actual screening process in your actual jurisdiction. What follows is the shape of the exposure, in plain language, so you know what to bring to that conversation and why it matters more than it might feel like it does from inside a busy req.

## Intent isn't the test

Most people's instinct about discrimination is that it requires someone deciding, consciously, to treat a group worse. That instinct describes one legal theory, disparate treatment, and misses the one that actually governs most automated and semi-automated screening: disparate impact. Under U.S. federal law (Title VII of the Civil Rights Act of 1964, the framework most relevant here), a facially neutral criterion, one that never mentions a protected characteristic at all, can still create liability if it disproportionately screens out people based on race, sex, age, national origin, religion, or another protected characteristic, regardless of whether anyone meant it to. The graduation-year filter Marcus found is a textbook example: it never asks anyone's age, and it doesn't need to, to functionally operate as an age filter.

[KEY-INSIGHT: In 2023, the EEOC reached its first-ever settlement over AI-driven hiring discrimination. iTutorGroup had configured its application software to automatically reject female applicants aged 55 or older and male applicants aged 60 or older, screening out more than 200 qualified applicants on that basis alone. One rejected applicant discovered the pattern by resubmitting an otherwise identical application with a different birth date and receiving an interview offer. The company paid $365,000 and agreed to ongoing anti-discrimination monitoring. || Source: U.S. Equal Employment Opportunity Commission, "iTutorGroup to Pay $365,000 to Settle EEOC Discriminatory Hiring Suit," EEOC press release, Aug. 9, 2023 (EEOC v. iTutorGroup, Inc., E.D.N.Y.).]

Notice what made this case provable: someone could directly demonstrate the same application, changed on one variable, produced a different result. Most real-world screening bias is far less visible than that, which is exactly why disparate impact doesn't require a smoking gun of intent. It requires a pattern in the outcomes, and a pattern is something you can actually go looking for before a regulator, or a rejected candidate's attorney, goes looking for it first.

[PULLQUOTE: The graduation-year filter Marcus found is a textbook example: it never asks anyone's age, and it doesn't need to, to functionally operate as an age filter.]

## The rule of thumb worth knowing

The EEOC's own technical guidance (issued in 2023, addressing how Title VII applies specifically to algorithmic and AI-driven selection tools) points to a widely used, if informal, screening heuristic: the four-fifths rule. If the selection rate for any group is less than four-fifths, 80%, of the rate for the group with the highest selection rate, that's treated as a warning sign worth investigating, not automatic proof of illegal discrimination, but a signal that the criterion producing that gap needs to be justified as genuinely necessary for the job, not just convenient.

Run the arithmetic on something as simple as your own screen: if 50% of applicants from one group clear an automated cutoff and only 30% of applicants from another group do, that's a selection-rate ratio of 30/50, 60%, well under the 80% threshold. That gap doesn't prove the cutoff is illegal. It proves the cutoff is the kind of thing you want to be able to explain, with a real, job-related justification, before anyone else asks you to.

Federal guidance in this specific area has been unstable. The EEOC's 2023 technical assistance document on AI in hiring was later withdrawn amid a change in federal enforcement priorities, and by the time you're reading this, the guidance landscape may have shifted again in either direction. What hasn't changed, and can't be undone by any single administration's guidance document, is Title VII itself and the disparate-impact case law built on it over decades; a guidance document's removal changes what help you get finding the exposure, not whether the exposure exists. **Verify the current state of federal and state guidance before relying on any of this**, the same discipline this book's KDP publishing pipeline applies to its own compliance claims.

## Jurisdictions are moving faster than federal guidance

The clearest example of jurisdiction-specific regulation, and the one with the most concrete, checkable requirements as of this writing, is local rather than federal.

[KEY-INSIGHT: New York City's Local Law 144, in effect since 2023, requires any employer using an "automated employment decision tool" to substantially assist or replace human decision-making in hiring to obtain an independent bias audit of that tool every year, publish a summary of the results, and notify candidates at least ten business days before the tool is used, with the option to request an alternative process. Penalties run up to $1,500 per violation per day, and the legal obligation sits with the employer using the tool, not the vendor who built it. || Source: New York City Local Law 144 of 2021 (effective Jan. 1, 2023; enforcement began July 5, 2023), NYC Department of Consumer and Worker Protection.]

That last point is worth repeating on its own: the obligation sits with you, the employer, not with the company that sold you the screening software. A vendor's marketing claim that its tool is "bias-free" or "audited" is not a substitute for your own compliance under a law like this one, and treating a vendor's assurance as sufficient due diligence is one of the more common, avoidable mistakes companies make in this specific area. Other U.S. states and cities have moved on similar territory (Illinois has separate rules specific to AI use in video interviews, and Colorado passed a broader AI Act touching high-risk automated decisions including employment), and internationally, the EU's AI Act classifies employment-related AI systems as "high-risk," triggering its own separate compliance regime. This book doesn't attempt a full jurisdiction-by-jurisdiction survey, which would be out of date before it printed; the point is structural, not a checklist: if you're using any tool that scores, ranks, or filters candidates, assume there is a real, specific, possibly local regulatory regime that applies to it, and find out which one, with counsel, rather than assuming a general awareness of Title VII covers everything.

## Marcus runs his own check

Once Marcus understood the four-fifths rule, he didn't need special tooling to apply a rough version of it himself. His ATS already reported pass-through rates by req; he pulled the graduation-year filter's pass rate for candidates with degrees older than eight years against candidates with more recent ones, using the visible proxy of years since graduation printed on the resume itself, not any protected characteristic directly. The ratio came out under 50%, well below the 80% threshold, for a filter that had never been re-examined since someone set it up years earlier for reasons nobody currently at the company could fully reconstruct.

| Group | Applicants | Passed | Pass rate |
| --- | --- | --- | --- |
| Degree within 8 years | 210 | 105 | 50% |
| Degree older than 8 years | 60 | 18 | 30% |

Ratio: 30 ÷ 50 = 60%, below the 80% threshold.

He didn't have the authority to declare the filter illegal or to unilaterally decide it was fine. What he did have, and used, was the ability to bring a specific, quantified finding to his head of talent acquisition and to legal counsel, instead of a vague worry, which turned an abstract discomfort into a concrete decision someone with the actual authority to make it could actually make.

Legal's first question back to him was one he hadn't fully prepared for: was the eight-year cutoff actually necessary for the role, or just a convenient number someone had picked. He didn't have a confident answer on the spot, and said so rather than guessing, which turned out to be the right call. It took a short conversation with the hiring manager to establish that nothing about the role genuinely required currency with tools from the last eight years specifically; the real requirement, comfort with a small number of named systems, was something chapter six's task-word rewrite could name directly instead of leaving it to a proxy. The four-fifths number opened the conversation. The actual fix came from asking what the filter was supposed to measure in the first place, and discovering nobody could answer that precisely either.

## Sana's version, without the same data access

Sana doesn't have access to her client companies' full applicant pools or their internal pass-through data; she only sees the candidates she personally submits and whether they advance. What she can, and does, track is her own referral pattern over time: whether candidates she submits from certain backgrounds advance to a client interview at a noticeably different rate than others, holding the role and her own assessment of fit roughly constant. It's a much rougher signal than Marcus's, but it serves a real purpose: if her own submissions show a persistent gap, that's worth raising with the client directly, both because it may point to something in their screen worth their own scrutiny and because continuing to submit into a pattern she's noticed without naming it is its own kind of exposure for her, professionally and potentially legally, depending on her role in the process.

## What this chapter will not do

This chapter will not tell you whether any specific practice at your company is or isn't illegal; that determination depends on facts this book can't see and law this book can't practice, and anyone telling you otherwise from inside a book chapter should not be trusted on the point. It will not attempt a comprehensive survey of every U.S. state or international jurisdiction's rules either, both because that list is moving and because a stale legal survey is worse than no survey, since it invites false confidence in guidance that's already out of date.

What it will say plainly, one more time: intent is not the test that matters most here. A rule nobody built to discriminate can still discriminate in its effects, and the only way to know is to look at the outcomes directly, the way Marcus did with a spreadsheet he already had access to.

## Try this: run a four-fifths check on one filter

Pick one automated or semi-automated cutoff in your current screening process, a keyword requirement, a degree filter, a years-of-experience threshold, anything that advances some candidates and rejects others before a human reads their full application. Using whatever data you can legitimately access, calculate the pass-through rate for at least two comparable groups the filter affects.

If any group's rate falls under 80% of the highest group's rate, don't conclude anything on your own. Bring the specific number to whoever owns that filter and, if your organization has one, to legal counsel, framed as a question: is this filter actually necessary for the job, and can we justify it if asked. That question, asked early and specifically, is the entire difference between finding this yourself and having it found for you.

[TAKEAWAYS]

- Disparate impact doesn't require intent. A facially neutral rule (a graduation-year cutoff, a keyword filter) can still create real legal exposure if it disproportionately screens out a protected group, regardless of why it was originally built.
- The four-fifths rule (a group's selection rate below 80% of the highest group's rate) is a widely used warning-sign heuristic, not a verdict, but a real one worth checking yourself before someone else does.
- Regulation in this space is real, specific, and jurisdiction-dependent (NYC's Local Law 144 bias-audit requirement is the clearest current example), and it sits with the employer using a tool, not the vendor who built it. Verify current federal and state guidance before relying on any of this.
- None of this is legal advice. It's a map of where the exposure lives, so the conversation with your own counsel starts from a specific, quantified concern instead of a vague one.

[/TAKEAWAYS]

## Where this goes next

Chapter eight builds the other half of this same discipline forward: not just finding where a screen might be creating exposure, but building a documented, defensible process from the start, the kind you could actually walk a regulator or a rejected candidate's lawyer through without flinching.
