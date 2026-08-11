# Where RAG Breaks in Production

The support-reply assistant's retrieval scorecard had cleared every number in chapter twelve's table: hit rate above ninety percent, average rank near the top, precision comfortably past the threshold. Three weeks after launch, a customer wrote in furious about a refund the assistant had described as "already processed, see ticket 4471," except the customer's actual ticket was 5,102, and 4471 had been closed and resolved eight months earlier for a different customer entirely. Support pulled the transcript and found the assistant hadn't hallucinated a ticket number out of nowhere. It had genuinely retrieved ticket 4471, alongside the real one, because both tickets described a similar-sounding issue and the old, resolved one had never been removed from the index. Reading both at once, the model blended them into a single, confident, wrong answer.

Nobody had touched the pipeline since launch. The scorecard from three weeks earlier was still, technically, accurate. What had changed was the corpus underneath it, and that gap between a system that passed its test and a system that's still passing it in production is what this chapter is about.

## Six specific ways a passing system still breaks

A RAG system that scored well in chapter twelve's testing embarrasses you in production in one of six specific ways, and naming which one you're looking at is what turns "the bot is being weird" into a bug someone can actually fix. Most of these have nothing to do with the model at all, which is worth saying plainly, because a room's default instinct when something goes wrong is to blame the visible part.

| Failure | What it looks like | Fix lives in |
| --- | --- | --- |
| Stale index | Confidently cites a policy that changed last month | A re-index schedule, later in this chapter |
| Permission leakage | Surfaces content the asker shouldn't see | Access filtering, later in this chapter |
| Chunking damage | A retrieved fragment nobody could actually use | Chunking strategy, chapter twelve |
| Context overflow | Retrieved chunks and history together get silently trimmed | Trim history first, not the retrieved facts |
| Near-duplicate confusion | An old and a current version both retrieved, blended together | Remove the superseded copy before it competes |
| Silent failure | Nothing relevant exists, and the model answers anyway | A written degradation path, chapter three |

Two of these, staleness and permissions, are large enough to earn their own section further in this chapter. The other four are worth sitting with now, because each one is easy to misdiagnose as the model simply being unreliable when the actual cause sits earlier in the pipeline.

Context overflow deserves a second look, because the obvious fix is backwards. When retrieved chunks and conversation history together exceed what the model can hold, something has to get cut, and most systems default to trimming whichever content arrived last, which is usually the retrieval results. That's exactly wrong. History is often padding by the time it's five turns old, restating things already said. The retrieved chunks are the actual facts the answer depends on. Trim history first, and treat cutting into retrieval as the last resort, not the default.

Silent failure is the one worth the most attention of the four, because it produces the most convincing wrong answers of anything on this list. A model asked a question with nothing relevant in its retrieved context doesn't usually say so. It answers anyway, fluently, drawing on the same general pattern-matching that produced the vacation-policy story back in chapter twelve, and nothing about the output signals that retrieval came back empty. That gap is exactly what a written degradation path exists to close: a rule, decided in advance and specified in the PRD, that a query with no strong retrieval match gets an honest "I don't have information on that" instead of a confident guess dressed up as fact.

## The failure that hides behind a passing scorecard

Ticket 4471's return is worth naming formally, because near-duplicate confusion happens whenever two versions of similar content both sit in the index, both look relevant to the same query, and both get retrieved together. Neither individual chunk is technically wrong. The model, holding both at once with nothing telling it which one is current, produces something blended and false. It isn't a reasoning failure in the sense chapter twelve defined one. It's an index that was never cleaned of a document it had already superseded.

This connects directly back to chapter twelve's honest caveat about oversized chunks: an embedding covering more than one idea matches worse than a focused one. Two near-duplicate chunks retrieved side by side do something similar to the model's reasoning, not to its embeddings. It's now holding two versions of the truth simultaneously, with nothing in the prompt to say which one is current, and it resolves that tension the same way it resolves any gap in its information: fluently, and often wrong.

[PULLQUOTE: A normal feature breaks when someone changes the code. A RAG system can break when someone on a completely different team uploads a revised document and forgets to remove the old one, six months after the launch review closed the file.]

Say the honest caveat this whole chapter has been building toward: passing a retrieval scorecard once isn't permanent. A corpus keeps changing even when the code never does, accumulating duplicates and drifting out of date in ways a launch-day scorecard structurally cannot see coming, because it measured a snapshot that stopped being current the moment someone else's document upload made it stale. This is the argument for treating retrieval quality the way chapter four treats a golden set: something re-checked on a real schedule, not verified once at launch and filed away as finished. A specification that names a retrieval threshold and never revisits it has quietly assumed the world holds still. Production keeps proving that it doesn't.

## The two failures that actually kill enterprise rollouts

Chunking and retrieval quality get most of a RAG project's attention, and they're not usually what stalls a real enterprise deployment. What stalls it is discovering, often late and often in a security review nobody scheduled for this reason, that a document carries information retrieval never checked in the first place: who's allowed to see it, and whether it's still true. Both problems share one root cause. An embedding represents what a piece of text means. It has no opinion on access, and no opinion on the calendar.

Both failures hide easily in a pilot, for the same reason: a pilot usually runs with one tester who has full access to everything, on a corpus that was indexed yesterday. Neither failure has anywhere to surface under those conditions. Both show up the moment a pilot becomes a real rollout: many users with genuinely different access levels, a corpus that's now months old and still growing.

| Reality | The naive assumption | What's actually needed |
| --- | --- | --- |
| Permissions | Anyone who can query can see everything indexed | Filtered by the asker's real access, checked live |
| Permissions | Access is fixed at the moment of indexing | A promotion or an offboarding must propagate immediately |
| Freshness | The index reflects the current document | The index is a snapshot from whenever it was last built |
| Freshness | An outdated version is harmless if it's still there | It competes on equal footing with the current one |

The permission rows matter because a real organization's documents were never written at one flat access level. General HR policy. Restricted compensation bands. A leadership-only strategy memo. Index all three into one shared pool and point a single retrieval system at it, and the system has no way to know it's supposed to treat those three differently unless someone explicitly built that filtering in, checked against the asker's real, current permissions, not the permissions that existed the day the document was indexed.

[KEY-INSIGHT: Starting around January 21, 2026, Microsoft 365 customers reported that Copilot Chat could read and summarize emails sitting in their own Sent Items and Drafts folders even when those emails carried confidentiality labels and data-loss-prevention policies specifically meant to keep them out of an AI system's context. Microsoft confirmed the bug, tracked internally as CW1226324, attributing it to a code issue that let labeled items be picked up by Copilot despite the label being set. Microsoft stated the bug did not expose data to a different, unauthorized person, only to the AI reading past a label-based restriction inside each user's own mailbox, and began rolling out a fix in February 2026. || Source: TechCrunch, "Microsoft says Office bug exposed customers' confidential emails to Copilot AI," February 18, 2026; BleepingComputer, "Microsoft says bug causes Copilot to summarize confidential emails," February 2026.]

Read that incident precisely, because the nuance is the point. Microsoft's own statement is careful to say nobody else gained access to anyone's private mail. What broke was narrower and just as instructive: a boundary that existed on the content itself, a confidentiality label, a DLP policy, the exact kind of access rule this chapter's table describes, sat there unread by a system built to summarize meaning, not to check restrictions. Retrieval doesn't automatically respect a label any more than it automatically respects a role, a team, or an org chart, unless someone explicitly builds that check into the pipeline and tests it the way chapter twelve taught you to test hit rate and precision. A confidentiality label is metadata. An embedding is meaning. Nothing connects the two unless a person wires that connection in on purpose.

A second version of this same gap shows up in a legal setting, at smaller scale but higher stakes per incident: a law firm's internal document search, built to help associates find precedent quickly across the firm's matter files, indexed everything into one searchable pool before anyone asked whether an associate on one client's matter should be able to retrieve a filing from a different, unrelated client's confidential matter. The two clients happened to be direct competitors. The search worked exactly as designed, which was the actual problem: nothing in the system understood that finding the right document and being allowed to see it were two different questions.

The freshness rows are the quieter risk of the two, precisely because a stale answer doesn't announce itself. A permission leak at least produces a specific document someone can point to and say plainly, this should never have surfaced. An answer built on a policy that changed three months ago just sounds right. It reads exactly like a current answer would, because nothing about the mechanism generating it distinguishes old truth from current truth. Fixing this isn't exotic: a re-index cadence matched to how often the underlying documents actually change, and a named owner for pulling a superseded document out of the index the moment it's replaced, the same "who owns this" discipline chapter eight's risk register already asked of every other kind of risk in this book.

## When the answer is a live call, not a document

Some content changes faster than any reasonable re-indexing schedule can track, and that's not a harder version of the freshness problem. It's a sign the problem was never a document to retrieve at all. Live inventory counts, today's exchange rate, a support ticket's current status right now, change by the minute in a way no index refresh cycle keeps up with honestly. Forcing content like that into a RAG pipeline anyway produces a system that's stale by design, no matter how tight the re-index schedule gets.

This is worth checking against chapter eleven's decision tree directly, because it revises one of that tree's own answers. "Needs facts that change" pointed toward retrieval. The fuller version of that same test is needs facts that change slower than you can realistically re-index. Past that speed, the honest fix isn't a better pipeline. It's a live tool call at the moment of the question, the agent shape from chapter seven, checking the actual current system instead of a snapshot of it that's already a little bit wrong the moment it's built. Practitioners have a name for retrieval that works this way, an agent deciding at answer time what to look up and where: agentic retrieval. If an engineer says that phrase in a planning meeting, this section is what they're proposing.

## What this chapter doesn't fix

Nothing here makes a retrieval system immune to a determined attacker crafting input specifically to manipulate what gets retrieved or generated. That's chapter eight's prompt-injection territory, a different threat model entirely, aimed at deliberate misuse rather than the ordinary decay this chapter describes. And nothing here replaces the judgment call chapter twelve already named: retrieval can be flawless and the generated answer can still be wrong, because reading the retrieved material correctly is a separate skill from finding it. This chapter closes the gap between a system that passed its test once and a system that keeps deserving that pass. It was never going to close every gap on its own.

## Audit your own index this week

Search your own retrieval corpus for one topic covered by two different documents. If you find one, you've found a live instance of near-duplicate confusion sitting in your own system right now, not a hypothetical one from this chapter.

Then ask the harder, more uncomfortable question: if someone's access were revoked today, how long would their old permissions actually linger in your retrieval system before they're genuinely gone. Minutes, hours, and "whenever the index next rebuilds" are three very different risk profiles wearing the same shrug, and most teams asking this question for the first time don't like the honest answer.

[TAKEAWAYS]

- A retrieval system that scores well once can still degrade in production, because the corpus underneath it keeps changing even when the code never does. Re-check retrieval quality on a schedule, the same discipline chapter four applies to a golden set.
- Near-duplicate confusion, an old and a current document both retrieved and blended, is one of the hardest failures to diagnose from the outside because neither individual chunk was technically wrong.
- Permissions and freshness stall more real deployments than bad chunking does. Both fail because an embedding represents meaning, not access and not the calendar, unless someone explicitly builds that check in.
- Content that changes faster than any reasonable re-index schedule was never a document to retrieve. It needs a live tool call at the moment of the question, not a snapshot trying to keep up with something that changes by the minute.
- The failures in this chapter are ordinary decay, not attack. A prompt-injection defense and a re-index schedule solve two different problems, and a team that only builds one has covered half the actual risk.

[/TAKEAWAYS]

## Where this goes next

Chapter fourteen comes back to the room itself, with the specific pushback lines you'll actually hear once you start naming a threshold, a corpus, or a permission gap out loud instead of letting a demo speak for the whole system.
