# The Golden Set

The message landed in the team channel on a Tuesday, three days after the new spec from chapter three got signed off: "need the eval set by Thursday, can someone pull 50 examples?"

Nobody owned that ask specifically, so an engineer did the obvious thing. She opened the ticket database, sorted by most recent, and copied the top fifty rows into a spreadsheet. By Thursday afternoon the golden set existed, the feature scored ninety-one percent against it, and the number went into the launch deck without anyone feeling like they'd cut a corner. Fifty was the number the spec asked for. Fifty was what got delivered.

Four months later, the company changed its refund policy. Customers who'd been charged twice for an annual plan could now get an automatic same-day refund instead of a two-week manual review, and the support queue filled up with a kind of ticket that had barely existed back in that Tuesday-to-Thursday sprint: short, urgent, mentioning a bank dispute already in motion. The feature had never seen more than one or two of those in training, because there had barely been one or two of those in the world when the fifty examples got pulled. It handled them the way it handled everything else: fluent, confident, and wrong about which policy applied. Nothing in the ninety-one percent had lied. It simply hadn't been asked.

## Fifty is a coverage decision, not a sample size

This is the mistake almost every golden set makes on its first attempt, and it's worth naming precisely, because it doesn't look like a mistake while it's happening. Sorting by date and grabbing the top fifty feels rigorous. So does asking an engineer for "a representative sample," which sounds careful and, underneath, usually just means random with extra syllables. Both produce a real number. Neither produces an instrument that can tell you what you actually need to know.

The question a golden set has to answer isn't how many cases. It's which cases, chosen on purpose, would actually catch this feature failing before a real customer does. That's a coverage decision, and coverage doesn't happen by accident. A pile of the fifty most recent tickets is a photograph of whatever was already common last Tuesday. It says nothing about the failure mode that shows up twice a month, and even less about the one that hasn't happened yet.

The size of the problem is easy to underestimate until you do the arithmetic. Picture a failure mode that hits one real customer in twenty-five, about four percent, common enough to show up in the support queue most weeks. Draw fifty cases completely at random and you'd expect to see it roughly twice on average. Average is the trap: work out the actual odds, and there's better than a one-in-eight chance that a random fifty contains exactly zero examples of it. Not underrepresented. Absent. Ship on that golden set and you'd score in the low nineties, feel confident, and carry a blind spot the width of one customer in twenty-five sitting entirely outside anything you measured. A biased sample fails louder than that. A genuinely random one just fails quietly, which is worse, because nothing about the number you're looking at tells you it happened.

[PULLQUOTE: A pile of the fifty most recent cases is a photograph of what was already common. It says nothing about the failure that hasn't happened yet.]

## The four buckets

The fix isn't a bigger pile. It's a deliberate split, decided before anyone starts pulling examples, so the fifty cases end up covering four different jobs instead of one job done fifty times.

| Bucket | Count | Proves |
| --- | --- | --- |
| Common path | 20 | The everyday case doesn't quietly regress |
| Known failure modes | 15 | The bugs you already found stay fixed |
| Edge cases | 10 | Unusual but real inputs don't break it |
| Adversarial | 5 | Someone trying to break it, on purpose, can't |

Twenty common-path cases cover the ordinary request your customers hit constantly. It's tempting to treat this bucket as the boring one and skimp on it in favor of more interesting failure modes, which is exactly backward: skip it and you can pass the golden set while quietly regressing the thing that matters most, because nothing in your fifty was even pointed at it.

Fifteen are known failure modes: the specific ways you've already watched this exact feature break, in production, with a real customer on the other end. The double-charge ticket that lost the refund deadline belongs here, if that's the incident your team lived through. Every case in this bucket is a bug you are refusing to let back in unnoticed, which is a different and stronger claim than "the feature usually works."

Ten are edge cases: real, unusual inputs that genuinely happen, just rarely. A request in a second language. A ticket with almost no content in it. A field a customer left blank. Rare does not mean safe to ignore; it's exactly where a probabilistic system tends to get strange, because strange inputs are underrepresented in whatever data taught it to be fluent in the first place.

Five are adversarial: someone deliberately trying to make the feature misbehave, whether that's a customer trying to talk a refund bot into an unauthorized payout or a prompt engineered to extract instructions the feature was never supposed to reveal. Small bucket, disproportionate cost if it's empty, because an attacker only needs one gap and you need all of them closed.

[KEY-INSIGHT: Amazon built an internal AI hiring tool that was trained and scored on roughly ten years of resumes submitted to the company, a set dominated by men because of the tech industry's own existing gender skew. The tool taught itself to downgrade any resume containing the word "women's" and to penalize graduates of two all-women's colleges, a pattern the very data used to build and check it was structurally unable to surface, because that data carried the same skew. Amazon scrapped the project in 2017 once engineers couldn't confirm the bias had actually been removed. || Source: Jeffrey Dastin, "Amazon scraps secret AI recruiting tool that showed bias against women," Reuters, Oct. 10, 2018.]

Notice what actually failed there. It wasn't a bug in the model in the narrow sense; the system was accurately reflecting the data it was shown. The blind spot was a property of the data's composition, invisible from inside the data itself, exactly the shape of problem an empty bucket produces. A team that had deliberately asked "what does our evaluation set look like split by gender of applicant" would have found the gap before a candidate did. Nobody asked, because the pile of resumes felt representative the same way the top fifty most recent tickets felt representative: it was what was already there.

## An entire industry's benchmark had the same blind spot

Amazon's hiring tool shows the failure inside one company's own evaluation set. The next case shows the same failure sitting inside the benchmarks an entire industry used to grade itself, which is a more uncomfortable finding precisely because nobody involved thought they were cutting a corner.

In 2018, researchers Joy Buolamwini and Timnit Gebru published a study called Gender Shades, testing three commercial facial-analysis systems, built by IBM, Microsoft, and a company called Face++, on how accurately each one classified a face's gender. All three vendors reported strong overall accuracy, in the high nineties, the kind of number that would close a launch review without a second question. Buolamwini and Gebru built their own evaluation set instead of trusting the vendors' reported numbers, deliberately balanced across skin tone and gender rather than pulled from whatever images were already easiest to source, and ran all three systems against it. The overall accuracy numbers had been true and almost meaningless at the same time: error rates for lighter-skinned men sat under one percent, while error rates for darker-skinned women climbed as high as 34.7 percent on the worst-performing system, an error more than forty times larger, invisible inside every vendor's own headline number.

[KEY-INSIGHT: The 2018 Gender Shades study by Joy Buolamwini and Timnit Gebru tested three commercial facial-analysis systems (IBM, Microsoft, Face++) on gender classification accuracy across a newly built, deliberately balanced evaluation set. All three systems showed error rates under 1% for lighter-skinned men, while error rates for darker-skinned women reached as high as 34.7% on the worst-performing system, a disparity invisible in any vendor's previously reported overall accuracy figure. || Source: Joy Buolamwini and Timnit Gebru, "Gender Shades: Intersectional Accuracy Disparities in Commercial Gender Classification," Proceedings of Machine Learning Research, 2018.]

Read that gap the way this chapter has taught you to read any golden set: not as a story about three careless companies, but as a story about what an evaluation set inherits from wherever its images came from. The standard face datasets these systems were graded against for years were themselves skewed toward lighter-skinned subjects, the same "whatever was already easiest to source" failure as sorting a ticket database by date and grabbing the top fifty. Three separate engineering teams, at three separate companies, all cleared the same distorted bar, because none of them had ever been handed a bucket labeled "darker-skinned women" and asked whether it was actually full. The fix Buolamwini and Gebru demonstrated wasn't a better model. It was a deliberately rebalanced evaluation set, the industry-scale version of this chapter's four buckets, applied to a benchmark instead of one company's ticket queue.

## How you actually build one

Start from real production logs or real pilot transcripts, never invented examples. An invented case only ever tests the failure you already imagined, which is precisely the blind spot a golden set exists to find instead of confirm.

Filter that raw traffic into rough candidates for each of the four buckets, then have a human, whoever actually owns this feature, read every candidate and tag it: common path, known failure, edge case, or adversarial, with one line on why. This is the step teams try to skip, and it's the one that makes the other three mean anything at all. A spreadsheet of fifty untagged transcripts is not a golden set. It's a pile with a number attached.

Curate down to fifty, dropping near-duplicates that would quietly let one pattern count three times. Then freeze it, and version it the way you'd version code: a date, a change log, one named owner who approves edits. A golden set that's editable on a whim by whoever's frustrated with this week's score stops being an instrument and goes back to being an opinion, just a more expensive one wearing a spreadsheet.

## Why this step doesn't get cheaper

Be straight about the actual cost, because it's the part every roadmap quietly underestimates. A script can pull five hundred raw candidates out of a support log in about a minute. Turning five hundred candidates into fifty that mean something takes real hours: reading transcripts, arguing where common path ends and edge case begins, noticing that the adversarial bucket is nearly empty because nobody has seriously tried to attack this feature yet.

That step does not compress, and it cannot be delegated to the model you're trying to evaluate. Budget an actual afternoon for it, not the twenty minutes it looks like in a planning meeting. Teams that skip straight to building the scoring rubric, which is the more visible, more demo-able piece of work, end up with a nicely engineered instrument pointed at fifty cases that don't prove much of anything. The rubric was never the hard part. Choosing what the fifty cases have to cover was, and it stays the hard part every time the set gets refreshed.

## What fifty cases still can't tell you

Say the limit of this chapter plainly, because a golden set that scores well can be quietly wrong in a way no amount of careful bucketing fixes: a golden set is a photograph, correct for the exact moment it was frozen, and production keeps moving after the shutter closes. Add a new policy, a new customer segment, a new integration, and the world your fifty cases describe stops being the world your feature actually operates in, without a single line of the golden set changing and without the score moving even slightly. That gap has a name, golden-set drift, and it has exactly one cause: production changed and your fifty cases didn't.

This isn't an argument against building the set. It's the reason the set alone was never going to be enough, and why chapter nine comes back to this exact problem once the feature is live and drift becomes something you can actually watch for instead of discover from a complaint. A golden set answers "did we break anything we already knew to check." It cannot answer "has the world changed since we checked," and treating a good offline score as permission to stop watching is the single most common way a well-built golden set still lets a real failure through.

## Count your own buckets

Pull up the golden set behind whichever feature you're most confident in, the one you'd point to first if someone asked whether your evaluation practice actually works. Count how many of its cases genuinely fall into each of the four buckets, honestly, not by how you remember building it.

Most people running this for the first time find the same shape of gap this chapter has now shown you twice: a common-path bucket that's really twenty near-duplicates of the same easy case, an adversarial bucket with one or two token entries nobody seriously tried to break, or a dimension, like Gender Shades found for skin tone, that was never sorted into a bucket at all because nobody thought to ask whether it needed one. Write down whatever gap you find as a specific, named finding, the same discipline this book asks of every other measurement. An empty bucket you've now counted is a todo. An empty bucket nobody ever counted is the blind spot the next Friday ticket walks straight into.

[TAKEAWAYS]

- A golden set is a coverage decision, not a sample size. Fifty cases chosen at random can miss an entire real failure mode, silently, more than one time in eight.
- Split deliberately across four buckets: common path, known failure modes, edge cases, adversarial. An empty bucket is a finding, not a filing problem.
- Build from real production traffic, never invented examples, and budget real hours for a human to read and tag every candidate. That step doesn't compress and can't be delegated to the system being evaluated.
- A golden set is a photograph, not a live feed. It cannot see the world changing after it's frozen, which is why it's necessary and not sufficient on its own.

[/TAKEAWAYS]

## Where this goes next

Chapter five puts a rubric underneath these fifty cases, so that scoring one of them means the same thing no matter who's holding the pen. A perfectly built golden set still produces five different opinions from five different reviewers if nobody has agreed in writing what "good" means, which turns out to be a more common failure than a badly built golden set is.
