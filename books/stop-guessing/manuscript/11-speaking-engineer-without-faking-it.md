# Speaking Engineer Without Faking It

The architecture review for the support-reply assistant's next version had been running for twenty minutes when an engineer said the sentence that ends most rooms like this one: "Honestly, I think we should just fine-tune it on the current policy docs." Three people nodded before the sentence had finished landing. Fine-tuning sounded serious, expensive in a way that signaled commitment, and nobody in the room wanted to be the person who asked a question that revealed they didn't know what a fine-tune actually was.

One PM in that room had spent time with exactly the material this chapter covers. She didn't nod. She asked one question: "How often do the policy docs change?" The engineer paused. "Monthly, sometimes more." She asked a second question: "So we'd be retraining monthly to keep it current?" The room went quiet in a different way than it had gone quiet for the original proposal, the quiet of a plan that had just met a fact it hadn't accounted for. Ten minutes later the team had switched to retrieving the current policy document at answer time instead of baking it into the model, and the fix that replaced days of retraining took an afternoon.

Nothing about that exchange required the PM to write code, train a model, or understand a loss function. It required two questions, asked from genuine understanding of what a fine-tune actually changes and what it costs to be wrong about. That's the entire premise of this chapter: technical credibility in a room like that one isn't a costume you put on. It's a small, learnable vocabulary, backed by just enough real understanding that you can survive the follow-up question. This chapter gives you both, in the order that room actually needed them.

## Four moves, tried in the right order

Every AI feature decision that isn't "should we use AI at all," the question chapter two already answered, eventually becomes one of four moves: write a better prompt, retrieve the right information, let the system take actions, or change the model itself. Three questions, asked in that order, tell you which one you actually need, and the order is the entire point.

Ask first whether the feature needs facts outside what the model already knows, or facts that change over time. If yes, you need retrieval: pulling the current, correct information into the answer at the moment it's asked, rather than hoping the model already knows it. If the facts are fine as they are, ask whether the feature needs multiple steps, or the ability to take an action instead of just producing text: looking something up, then deciding whether to escalate, then acting on that decision. If yes, you need an agent, chapter seven's entire subject. Only if both of those are no do you reach the third question: has a well-written prompt actually failed in real testing, not "might it fail" but actually failed. If it has, a fine-tune, retraining the model itself on your own examples, might earn its cost. If prompting hasn't been seriously tried yet, the honest answer is still prompt.

The reason the order matters isn't abstract. These four moves don't cost the same to be wrong about, and the cost climbs by roughly an order of magnitude at each step.

| Move | What it changes | Cost to try again if you're wrong |
| --- | --- | --- |
| Prompt | The instructions sent with each request | Seconds, edit the text |
| Retrieve | What information gets pulled in | Minutes, swap what's indexed |
| Act | What the system is allowed to do | Hours, new integration code |
| Fine-tune | The model's own weights | Days, a full retrain and re-evaluation |

The policy-docs proposal from this chapter's opening scene collapsed the moment it hit the first question honestly. Monthly-changing facts are exactly what retrieval exists for. A fine-tune baked into today's policy would already be wrong again in four weeks, and every correction after that means another training run, not a five-minute document edit. The team wasn't wrong to want the assistant to know current policy. They were wrong about which of the four moves actually gets you there.

[PULLQUOTE: The expensive option almost never turns out to be the one you needed first. It earns its cost only after the cheaper three have genuinely failed, not because it sounded more serious in the room.]

A second worked example shows the same tree pointed at a different feature. A team building an internal tool to answer employee questions about expense policy considered building a custom-trained model specifically for HR questions, reasoning that a dedicated model would feel more authoritative than a general one wearing a prompt. Run that instinct through the same three questions. Does it need facts outside training data or facts that change? Expense limits and approval thresholds change every fiscal year, so yes, stop there. That's retrieval again, not a fine-tune, and for the identical reason as the first example: information that changes on a schedule belongs in a document the system reads at answer time, not baked into weights that only update when someone deliberately retrains them.

Say the honest caveat this tree earns on its own: most real features need more than one box at once, and the tree isn't asking you to pick a single answer. A support agent that looks up an account and then processes a refund is doing retrieval to find the account and taking an action to process the refund, both together. The tree's job is to make sure every box that genuinely applies gets named, not to force a single winner.

## The vocabulary that separates a demo from production: latency and throughput

A second gap shows up less often in a planning meeting and more often the first week after launch: a feature that felt instant in every demo starts feeling slow the moment real users show up at the same time. That gap has a name, and it's worth having the vocabulary before the first busy Monday finds it for you.

Latency is how long one request takes, start to finish. Throughput is how many requests the whole system can handle at once. They sound like the same conversation about speed. They aren't, and the fix for one can quietly make the other worse: a common way to raise throughput is batching several requests together before processing them, which is good for total capacity and can mean any single request in that batch waits slightly longer before its turn comes.

The vocabulary that actually matters here is p95, and it's worth understanding precisely why an engineer will resist giving you a plain average. Picture a hundred requests to a feature. Most land in under a second. A handful, one or two in a hundred, take four or eight seconds. Averaged across all hundred, those slow ones nearly disappear from the number. They don't disappear from the person who waited eight seconds. P95 is the response time slower than ninety-five percent of requests: the number that describes what an unlucky user actually experiences, not what a typical one does.

[KEY-INSIGHT: A 2013 Communications of the ACM paper by Google engineers Jeffrey Dean and Luiz Andre Barroso, "The Tail at Scale," showed how badly rare slow responses compound once a system depends on many components. If a single server has only a 1-in-10,000 chance of a request taking longer than one second, a service built from 2,000 such servers running in parallel will see almost one in five user-facing requests exceed one second, because the user is waiting on whichever component happens to be the slow one that time. || Source: Jeffrey Dean and Luiz Andre Barroso, "The Tail at Scale," Communications of the ACM, Vol. 56, No. 2, February 2013, pp. 74-80.]

Read that math against any AI feature built from more than one call: a retrieval step, then a model call, then maybe a second model call to check the first one's output. Each individual step can have a very low chance of running slow and the whole chain still ends up feeling slow to a meaningful share of real users, for the same reason a service built from thousands of servers does. This is exactly why "the average was fine in the demo" is one of the least reassuring sentences in a launch review. A demo run by one person, alone, at a quiet moment, has none of the queuing and contention that real concurrent traffic creates. Ask for p95 under realistic concurrent load specifically. A number measured with nobody else in the system is closer to marketing than to a promise.

## Reading a benchmark table the way an engineer already does

A vendor announces a new model with a benchmark score, or a competitor comparison, and the natural reading is "this model is better." Chapter fourteen, the objections chapter, tells the specific story of a benchmark number that didn't survive contact with the real, publicly released model. The habit worth building now is the one that catches that gap before you've committed to anything: a benchmark score is a real measurement of how a model performs on a fixed set of questions someone else wrote, not a measurement of how it'll perform on your task, with your data, in your product.

[KEY-INSIGHT: Two independent 2024 studies found widespread contamination in public LLM benchmarks. An open-source contamination report estimated that 29.1% of test items on MMLU, at the time one of the most cited public benchmarks of model knowledge, had leaked into models' training data. A Yale-led study presented at NAACL took a different route to the same conclusion: it masked one of the answer options in benchmark questions and asked models to reproduce the missing option verbatim, which ChatGPT and GPT-4 managed 52% and 57% of the time respectively, far above what working it out from the question alone should produce. || Source: Yucheng Li et al., "An Open-Source Data Contamination Report for Large Language Models," Findings of EMNLP 2024; Chunyuan Deng et al., "Investigating Data Contamination in Modern Benchmarks for Large Language Models," Proceedings of NAACL 2024.]

A model scoring well on a benchmark it may have partly memorized isn't lying to you, exactly. It's answering a slightly different question than the one the headline percentage implies. The industry's response to that finding is worth knowing too: contaminated benchmarks get retired and replaced with fresher, harder ones on a cycle of a year or two, which means the specific benchmark names in any vendor deck will keep changing. The habit of asking what's actually inside the test set is the part that transfers. Two habits catch most of what matters here. First, check whether anything resembling your actual task type is represented in the benchmark at all: most general-purpose benchmarks lean heavily on math, code, and trivia because those are cheap to grade automatically, and a feature that summarizes support tickets or drafts marketing copy may have nothing in common with what was actually tested. Second, treat a public benchmark as a floor, not a ceiling: a model that scores poorly across the board is probably genuinely weak, but a model that scores well tells you it probably isn't broken, not that it's good at your specific task. Chapter four's golden set is what actually answers that second question, and no benchmark table replaces it.

## The phrases themselves, and the caveat that keeps them honest

Everything in this chapter compresses into a short list of things worth saying out loud in a technical conversation, each one signaling that you understand what's behind it. None of these are magic words. They work because you now know the mechanism each one points at, and the first follow-up question will find the gap immediately if you don't.

| Say this | It signals |
| --- | --- |
| "Is this retrieval, or the model itself?" | You separate what it knows from what it looked up |
| "Did we prompt this, or fine-tune it?" | You know these are not interchangeable fixes |
| "What's the p95, not the average?" | You know the average hides the tail |
| "Does that hold under real concurrent load?" | You know a quiet demo isn't production |
| "Is that benchmark representative of our task?" | You've read past the leaderboard |
| "What's our pass rate on the golden set?" | You expect a real eval, not a vibe |
| "What's the blast radius if this is wrong?" | You've run chapter seven's math before shipping |
| "What would make us turn this off?" | You have an exit plan, not just a launch plan |

Say the honest caveat this list earns on its own: these phrases only work if you can survive the follow-up question they invite. Ask "what's our p95" and freeze when someone actually answers with a number, and you've signaled the opposite of what you intended, more clearly than if you'd said nothing at all. This chapter's whole premise, without faking it, is not decoration. Use a phrase because six sections of real understanding sit behind it, not instead of building that understanding. A borrowed question with nothing behind it is worse than an honest "I don't know yet, walk me through it," because the room can tell the difference and remembers which one they heard.

## What this doesn't fix

None of this makes you able to debug the code, tune the model, or replace the engineer who actually builds the thing. That was never the goal, and a PM who starts using this vocabulary to argue technical decisions past the people who own the implementation has misused it. The point of a sharp question is to make sure the right conversation happens, with the right people, before a decision ships, not to win the conversation yourself. If you find yourself asking "what's our p95" as a way to prove a point rather than to actually learn the number, you've turned a genuine question into exactly the performance this chapter warned against.

## Try this before your next technical conversation

Pick a real proposal on your team that reached for the most serious-sounding option first, a fine-tune, a rebuild, a switch to a bigger model, and run it backward through the three questions: does it need facts, does it need actions, has a simpler option actually failed real testing. Most of the time it stops at the first or second question, and the fix was cheaper than the one that got proposed.

Then pick three phrases from this chapter's table, not all eight, the ones that fit a conversation you can already see coming this week. Say each one out loud once and imagine the honest follow-up. If you can answer it, you're ready to use it for real.

[TAKEAWAYS]

- Four moves exist for improving an AI feature: prompt, retrieve, act, or fine-tune, tried in that order because the cost of being wrong climbs roughly tenfold at each step.
- Latency and throughput are different measurements, and the fix for one can make the other worse. Ask for p95 under real concurrent load, never a quiet demo's average.
- A benchmark score measures performance on someone else's fixed test set, sometimes one the model has partly seen before. It's a floor, not a ceiling, and your own golden set is what actually answers whether a model is good at your task.
- A sharp technical question only works if you can survive the answer. Use these phrases because you understand what's behind them, not as a substitute for that understanding.
- This vocabulary earns you a seat in the conversation. It doesn't make you the engineer, and using it to overrule the people who actually build the feature misuses exactly what it was for.

[/TAKEAWAYS]

## Where this goes next

Chapter twelve takes the single most common box from this chapter's decision tree, retrieval, and opens it up properly: why it exists, what it actually does step by step, and the specific numbers that tell you whether it's working.
