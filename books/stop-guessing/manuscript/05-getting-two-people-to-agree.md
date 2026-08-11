# Getting Two People to Agree

Two reviewers sat down with the same fifteen tickets from the new golden set and the same six-question rubric from the spec, and scored them independently, no discussion first. When they compared sheets afterward, they agreed on nine cases out of fifteen. Sixty percent. Not the number anyone wanted to see attached to an instrument they'd just spent an afternoon building.

They didn't panic and they didn't blame each other, which is its own small discipline. They read through the six disagreements together, out loud, one at a time. Five of the six traced back to a single question: "does the summary invent anything." One reviewer had been flagging any paraphrase at all as invention, on the theory that rewording is technically adding words the customer never wrote. The other only flagged claims with no basis in the ticket whatsoever. Same three words on the page, two entirely different tests running behind them, and neither reviewer was being careless.

They reworded the question to something narrower: every claim in the summary is traceable to a specific line in the ticket. Ran the same fifteen cases again. Fourteen of fifteen agreed. One bad question had been responsible for nearly the entire gap, and it took one sentence, not a new rubric, to close it.

## What makes a question rubric-grade

Most rubric questions fail the same way, and they fail while sounding perfectly reasonable. Read these side by side and notice which column you'd actually trust to produce the same verdict twice.

| Sounds like a rubric question | Actually is one |
| --- | --- |
| "Is the tone appropriate?" | "Are all dates and deadlines from the original preserved?" |
| "Is the summary good?" | "Is every claim traceable to a specific line in the ticket?" |
| "Did it handle the request well?" | "Could an agent act on this without reopening the original?" |

Every entry in the left column has a subject and sounds specific. Every one of them still depends on taste: appropriate to whom, good by what standard. The right column asks something a reader could screenshot and circle. A date is either preserved or it isn't. A claim either traces back to the ticket or it doesn't. That's the actual test for whether a question belongs in a rubric: could two people who disagree about almost everything else still land on the same answer, because the answer is sitting right there in the text rather than in their judgment about it. If answering it takes taste, the question isn't finished yet.

## The calibration loop, and why it isn't optional

The scene that opened this chapter is the whole method, and it's shorter than most teams expect once they've done it once. Two reviewers score the same fifteen cases independently, without discussing them beforehand, because discussing them first is what makes the exercise worthless: two people who talk it over first will converge on an interpretation together and never find out the rubric couldn't produce that convergence on its own. Compare case by case, not just the final percentage. Wherever the scores agree, move on. Wherever they don't, stop and reread that exact question together. Nine times out of ten, the wording let two reasonable people take two different readings of the same three words.

Reword the one question causing the disagreement. Only that one. Run the same fifteen cases again. Somewhere around eighty-five percent agreement, freeze the rubric and move on. Fall short, and loop again. Most rubrics need one or two passes through this loop before they hold. Almost none need ten, and if yours does, the question that keeps failing probably needs to be split into two narrower ones rather than reworded a sixth time.

[PULLQUOTE: Low agreement is not a careless-reviewer problem. It's an ambiguous-question problem, and the fix is one sentence, not a better reviewer.]

The instinct worth unlearning here is blaming the person. When two reviewers disagree, the natural first reaction is to suspect the other one misread the ticket. Almost always, both of them read it correctly, and the question simply allowed two correct readings to point in different directions. That reframe, question over reviewer, is most of what makes this loop work, because it tells you exactly where to spend the next ten minutes instead of spending them relitigating someone's judgment.

One caution worth stating plainly: don't brief your colleague on what you meant before they score. That defeats the entire test. A rubric has to survive being read cold, because cold is exactly how it gets used every time after this one.

## Handing the scoring to a machine

Everything above costs real hours. Reading transcripts, arguing over wording, running the loop twice, that's an afternoon per rubric. The obvious next move is to hand your calibrated rubric and your fifty cases to a language model and let it score all of them in under a minute, for a fraction of a cent each. For most teams, that's eventually the right call. It's also worth being honest about what you just did: you handed judgment to a system built from the same kind of technology you're trying to evaluate, and asked it to grade its own kind of homework.

That's not disqualifying. It's a reason to check, not a reason to trust on sight. An LLM judge doesn't fail randomly. It fails in a short list of specific, measured ways, the same two showing up across most published research on the topic: it tends to prefer longer answers regardless of whether the extra length adds anything, and when comparing two answers side by side, it shows a real preference for whichever one it reads first, a bias that shrinks but does not vanish when you swap the order and rerun.

[KEY-INSIGHT: In the 2023 study that introduced LLM-as-judge evaluation at scale, GPT-4 agreed with expert human judges on non-tie verdicts about 85% of the time on the MT-Bench benchmark, close to the roughly 81% agreement rate measured between two human judges scoring the same cases. The same study still found GPT-4 vulnerable to a "repetitive list" attack designed purely to make an answer sound longer without adding information: GPT-4 wrongly preferred the padded answer on 8.7% of trials, the best result of any model judge tested and still not zero. || Source: Lianmin Zheng et al., "Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena," NeurIPS 2023 (arXiv:2306.05685).]

Notice what that number actually says. The strongest judge model in a serious, widely cited study, one whose overall agreement with humans nearly matched how much two humans agree with each other, still fell for a padding attack that added no information roughly one time in eleven. Weaker judge models did worse. The models in that study are several generations old now, and newer judges score better on both counts; the reason it's still the study worth knowing is that the two biases it named, length and position, are exactly the ones later research keeps finding in whatever the current generation is. If the best result on record still isn't zero, "the model seemed to score things reasonably in the cases I glanced at" was never going to be an adequate validation step on its own.

The fix is the same calibration loop from earlier in this chapter, run once more with a different second reviewer. Score fifteen cases yourself, using your calibrated rubric. Have the model score the identical fifteen, without seeing your verdicts. Compare. Clear roughly the same eighty-five percent agreement, and you've earned the right to let it score the other thirty-five cases, and every release after this one. Fall short, and sort the disagreements by word count before diagnosing anything cleverer; if they cluster at the long end, you've found the bias the research already told you to expect.

One more cost worth naming here specifically: a validated judge doesn't stay validated. The provider updates the underlying model on a schedule you don't control and usually aren't told about, and a judge that agreed with you in March can quietly disagree by June without a single word of your rubric changing. Treat "validated" as a claim with a date on it, not a permanent fact. "Ninety-two percent, validated against a human rubric on the third of March" survives a hard question in a review meeting. A bare "ninety-two percent" invites one.

## How much of a swing is real

Once you're scoring buckets of five, fifteen, or fifty cases release after release, a new problem shows up: the number moves between releases even when nothing about the feature actually changed. Small samples swing, in both directions, purely from which cases happened to land in this particular batch, and the only fix is knowing roughly how much swing is ordinary noise before you react to it.

| Cases in the bucket | Swing that could easily be noise alone |
| --- | --- |
| 5 | Up to about 45 points, either direction |
| 15 | Up to about 25 points |
| 50 | Up to about 14 points |
| 100+ | Up to about 10 points |

At five cases, a swing of up to roughly forty-five points in either direction sits comfortably inside what pure luck can produce on its own. That covers most of the scale; at five cases, almost nothing is provably real yet. At fifty, the size most buckets in a golden set actually sit at, noise alone rarely moves the number more than about fourteen points, which is exactly why a four-point shift on your aggregate pass rate deserves a shrug rather than a launch review. At a hundred or more, ordinary wobble narrows to about ten points, which is roughly where your largest, common-path bucket will eventually sit if the golden set keeps growing.

This cuts in an uncomfortable direction for the smallest bucket you built in chapter four. Five adversarial cases moving from five-out-of-five to two-out-of-five is a sixty-point swing, sitting right at the edge of what five cases can even measure. That's a genuinely honest, genuinely unsatisfying answer: you cannot prove that drop is real, and you cannot dismiss it as noise either, because both of those claims overreach what five data points can support. The responsible move is neither panic nor relaxation. It's collecting more adversarial cases, fifteen or twenty, before anyone in the room gets to have an opinion with real confidence behind it.

## Don't fool yourself after the numbers are already real

Every technique in this chapter protects the number itself. None of it protects the moment a person looks at that number and decides what to do about it, and that moment is where teams who did everything else correctly still quietly talk themselves into shipping something the number told them not to.

It happens two ways, almost always. A case fails, and someone notices out loud that it's "not really representative," and it quietly disappears before the next run, not through any single dishonest decision but through a dozen reasonable-sounding small ones. Or the threshold moves to meet the result: the plan said ninety percent, the number comes back eighty-seven, and in the room, eighty-seven starts sounding close enough, just this once, given the deadline.

You will hear a version of this sentence, probably from someone reasonable, under real pressure, not trying to deceive anyone: "eighty-seven's close enough to ninety, right?" That's what makes it dangerous. It doesn't sound like cheating. It sounds like judgment, like reading the room. And it's the exact moment where an afternoon of rigorous calibration work gets quietly overruled by a feeling nobody voted on.

The fix borrows a term from clinical trials, which solved this exact problem before product teams had to: pre-registration. Write the pass threshold down, get one other person to see it, and timestamp it, before the eval runs and before anyone has seen a score. Now the conversation in the room isn't "is eighty-seven close enough." It's "we wrote ninety, here's why, do we still believe that," which is a different and much more honest conversation to be having with a deadline in the room.

Clinical trials didn't adopt pre-registration as an abstract best practice. They adopted it after a specific, well-documented failure of exactly this discipline, worth knowing because it shows what "not really representative" and "close enough" look like at a much higher stakes table than a launch review. A 1990s trial of the antidepressant paroxetine in adolescents, run by GlaxoSmithKline and known afterward as Study 329, specified two primary outcome measures and seven secondary ones in its protocol before the trial began, the equivalent of a pre-registered threshold. When the results came in, the drug missed every single one of those nine pre-specified outcomes. It did not beat placebo on any of them. The published paper, appearing in a respected journal in 2001, reported four different, more favorable measures that had never been named in the original protocol, and concluded the drug was "generally well tolerated and effective" for adolescent depression.

[KEY-INSIGHT: GlaxoSmithKline's Study 329, a 1990s clinical trial of paroxetine in adolescents, pre-specified two primary and seven secondary outcome measures in its protocol. The drug failed to outperform placebo on any of the nine pre-specified outcomes. The paper as published in 2001 instead reported four new, more favorable outcome measures that had not been named in the original protocol, and concluded the drug was "generally well tolerated and effective," a conclusion later reanalyses found the pre-registered data did not support. || Source: Le Noury et al., "Restoring Study 329: efficacy and harms of paroxetine and imipramine in treatment of major depression in adolescence," BMJ, 2015.]

That's the goalpost move this chapter has been warning about, played out with a drug prescribed to real teenagers rather than a feature launch: not one dishonest number, but nine failed outcomes quietly set aside in favor of whichever measures, found after the fact, told the story the sponsor needed. The fix that followed, years later, was regulatory: clinical trial registries now require the primary outcome to be declared publicly before a trial starts, precisely so a sponsor can't do after the fact what Study 329's authors did. A pre-registered eval threshold is the same fix, borrowed early, before your own version of this story needs a regulator to force it.

Sometimes the disciplined answer really is: don't ship. That costs a date occasionally, and it's supposed to. A threshold that bends every time it's inconvenient was never a threshold. It was decoration, and every number you report after that stops being one anyone has real reason to trust without rechecking it themselves.

## Run the loop this week

Pick the rubric you trust least, the one you built fastest or have never actually tested against a second reviewer. Find a colleague, hand them fifteen real cases and the rubric with no briefing, and score the same fifteen yourself, separately, today. Compare tonight or tomorrow, not next sprint.

Before you look at the disagreements, write down what percentage you'd consider acceptable, and why. That single sentence, written before you see the number, is the entire pre-registration habit this chapter asks for, practiced on something small enough to cost you an afternoon instead of a launch.

[TAKEAWAYS]

- Low agreement between two reviewers is almost never a careless-reviewer problem. It's an ambiguous-question problem, and the fix is usually one reworded sentence.
- Run the calibration loop, score fifteen cases independently, compare, reword the one question causing most disagreement, before trusting any rubric with a launch decision.
- An LLM judge can validate against the same loop, but even the strongest published results still show real length and position bias. Treat "validated" as dated, not permanent.
- A pass-rate swing at five or fifteen cases is often just noise. Check the bucket size before reacting to the number.
- Write your threshold down before you see the score. The room will always find a reason a near-miss is close enough; a pre-registered number is what keeps that conversation honest.

[/TAKEAWAYS]

## Where this goes next

Chapter six turns from whether a feature is good enough to what it actually costs to run at the volume you're planning to run it at, because a feature that clears every threshold in this chapter can still lose money in a way nobody notices until the first real invoice arrives.
