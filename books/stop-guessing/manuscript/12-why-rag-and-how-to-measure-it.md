# Why RAG, and How to Measure It

A mid-sized company built an internal assistant to answer employee questions about benefits, and version one was a capable model given a paragraph describing the company. It sailed through every demo. Then a real employee asked how many vacation days she'd get after five years, and the assistant answered instantly, confidently, and completely wrong: a tidy, plausible tiered schedule that had never appeared in any document the company owned. A manager approved a request based on that number before anyone caught the mistake.

Nothing about that answer read as a guess. It had the same tone, the same structure, the same confidence a correct answer would have had. That's the specific danger this book named back in chapter one: a wrong answer that looks exactly like a right one. The fix the team reached for changed exactly one thing about the assistant, and understanding what that one thing was is the entire reason this chapter exists.

## An access problem, not a reasoning problem

The team's second version didn't retrain the model, didn't write a cleverer prompt, and didn't switch to a bigger one. It gave the assistant the actual policy document at the moment it answered, so instead of reasoning from what vacation policies generally look like, it read the real number off the real page and said that instead. Same model, same question, same day. The only thing that moved was whether the fact the answer depended on was actually present when the model needed it.

That's retrieval-augmented generation, RAG for short, and it's worth being precise about what it does and doesn't fix, because the term gets reached for as a general-purpose upgrade and it solves exactly one kind of failure. A missing-fact failure is a case where the right answer exists somewhere, in a document, a database, a policy page, and the model simply didn't have it in front of it. Retrieval fixes that completely, because it hands over the actual source instead of asking the model to guess convincingly. A reasoning failure is different: the model had the right information and still drew the wrong conclusion from it, miscounted, misread a qualifier, or contradicted itself. Handing a reasoning failure more documents doesn't touch the problem, the same way handing a calculator more digits doesn't fix a formula that was wrong to begin with. Before proposing RAG for any specific complaint, find one concrete wrong answer and diagnose which failure it actually was. Only one of the two is retrieval's job.

[KEY-INSIGHT: In February 2024, Canada's Civil Resolution Tribunal ruled that Air Canada was liable for a negligent misrepresentation made by its website chatbot. A customer, Jake Moffatt, asked the chatbot about bereavement fares after his grandmother's death, and it told him he could book a full-price ticket and claim a bereavement discount retroactively. Air Canada's actual policy required the discount to be requested before travel, not after. The airline argued the chatbot was "a separate legal entity responsible for its own actions"; the tribunal rejected that argument and ordered Air Canada to pay CAD $812.02 in damages. || Source: Civil Resolution Tribunal of British Columbia, Moffatt v. Air Canada, 2024 BCCRT 149, February 14, 2024.]

Read that ruling next to the benefits-assistant story and the parallel is exact. Air Canada's chatbot wasn't malfunctioning in any technical sense. It was answering fluently and confidently from whatever general sense of "bereavement fare policies" it had, because nobody had given it the airline's actual, current bereavement policy document to read from at the moment a customer asked. A tribunal later confirmed, in a way a spreadsheet never could, that the gap between "sounds right" and "is right" has a real cost attached, and that the company on the other end of the chat window owns that cost regardless of which system produced the sentence.

A second, quieter version of the same fix shows up in this book's own recurring example. The support-reply assistant from earlier chapters started as a model answering from general customer-service instinct, and it improved the moment it retrieved the actual, current return policy before answering a question about one. Nothing about the model changed between those two versions. What changed is exactly what changed for the benefits assistant and for Air Canada's chatbot: the fact the answer depended on was present, or it wasn't.

[PULLQUOTE: RAG isn't a smarter version of your feature. It's the same feature, finally given the thing it needed to answer honestly.]

## The pipeline has seven stages, and four of them are yours

Retrieval sounds like a single technical step, and treating it that way is how a PM ends up with no opinion on a decision that was actually theirs to make. A working retrieval system has seven distinct stages, and the pattern worth noticing is which end of that list belongs to product and which belongs to engineering.

| Stage | What happens | Whose call it actually is |
| --- | --- | --- |
| Ingestion | Which documents are even in scope | Product or content owner |
| Chunking | How documents get split into pieces | Product, in detail below |
| Embed and index | Chunks become searchable | Mostly engineering |
| Retrieval | Finding top candidates, filtered by permission | PM sets the cutoff and access rules |
| Re-ranking | An optional second pass that reorders results | PM decides if it earns its latency cost |
| Generation | The model answers using what was retrieved | Mostly engineering |
| Citation | Whether and how a source is shown to the user | Entirely a product decision |

Ingestion is the stage most teams never discuss directly, and it's the highest-leverage one on the list. Every document included is something the system can retrieve and hand to a user. Every document left out is a question the system will now confidently answer wrong instead of well, because nobody ever told it that source existed at all. That's not an engineering detail buried in a config file. It's a scope decision, and it belongs in the dataset section of the same PRD chapter three already taught you to write.

Citation deserves the same weight at the other end of the pipeline. Showing a source next to an answer changes the entire trust relationship a user has with a feature. A cited answer invites someone to check it. An uncited one asks for blind faith, the exact faith the manager in this chapter's opening story extended and shouldn't have had to. Deciding whether and how to cite is a product call with real consequences, not a formatting detail an engineer adds because someone remembered to ask.

Re-ranking is worth naming because it's the stage most PMs have never heard of and will be asked to weigh in on anyway. Initial retrieval is built for speed, scanning a large index fast, which means it's tuned to find roughly the right neighborhood rather than the single best answer. Re-ranking takes that shortlist and runs a slower, more careful pass to reorder it before only the top few results reach the model, trading latency for precision. Say the honest caveat this stage earns: it isn't a free upgrade. It's a real, measurable delay, worth paying for a feature where being wrong in the top result is expensive, and worth skipping for a low-stakes internal tool where nobody will notice the difference. Ask it the same question chapter eleven's latency section already taught you to ask about anything: does this stage earn its cost for this specific feature, or does it just sound like best practice.

## Chunking is a product decision wearing an engineering costume

Ask an engineer for "the chunk size" and you'll get one number back. Real content usually needs several, and picking that number, or numbers, deliberately rather than by tutorial default is a decision that belongs on the product side of the table above, because it depends on knowledge only the product side actually has: what's really in the corpus.

| | Smaller chunks | Larger chunks |
| --- | --- | --- |
| Precision | High, retrieves the exact relevant sentence | Lower, pulls in a whole section |
| Context | Risk of losing the explanation around it | Keeps the full thought intact |
| Cost per query | Lower, fewer tokens retrieved | Higher, more tokens retrieved |
| Failure mode | A sentence with nothing around it to explain it | An answer diluted by irrelevant neighbors |

Neither column is the safe default. A quick factual lookup, a price, a date, a policy number, wants small and precise, because the whole answer is one fact and surrounding paragraphs only add noise. A feature explaining a multi-step process wants larger chunks, because cutting that process into precise, disconnected fragments defeats the point of retrieving it in the first place. The vacation-policy assistant's real fix depended on getting this right: a chunk sized to hold the entire tenure-based schedule together, not split across a boundary that would have handed the model half a table with no header to explain it.

The instinct when chunking feels risky is to make chunks bigger, on the theory that more context is always safer. That instinct backfires in a specific, technical way. An embedding represents what a chunk is about, and cramming three unrelated ideas into one chunk produces an embedding that's a blur of all three, matching none of them as sharply as a focused chunk would have. The safety a bigger chunk seems to buy was never really about size. It was about keeping one coherent idea together, and a chunk scoped to its natural unit, a policy's clause, an FAQ's question-and-answer pair, a table's row with its header, gets there more reliably than simply making everything larger. Most real corpora contain more than one content type, and applying a single chunk-size rule across all of them is usually a decision nobody actually made, just a default nobody thought to question.

## Three numbers that tell you whether retrieval is actually working

The demo for the benefits assistant had five questions, and all five worked, and that's not a measurement, it's five data points that happened to be flattering. Chapter four already taught you why a small, self-selected sample flatters by construction. The same discipline, aimed specifically at retrieval instead of the finished answer, uses three plain questions with real technical names behind them.

| Plain question | Technical name | What it catches |
| --- | --- | --- |
| Did we find it at all? | Hit rate | A document that exists but never surfaces |
| How high did it rank? | Mean reciprocal rank | The right chunk, buried past the cutoff |
| How much of what we got was useful? | Precision | Noise diluting the context |

Score these separately from whether the final answer looked right, and the reason is worth being explicit about. If you only check the finished answer, a retrieval failure and a generation failure produce the identical symptom: a wrong response. You'd know something broke and have no way to know which of the two stages actually did it. Scoring retrieval on its own is what turns "the bot got it wrong" into "the right document was never found" or "it was found and misread," two completely different fixes owed to two completely different teams.

A first honest scorecard tends to look worse than the demo did, and that's the scorecard doing its job. Picture ten test questions, each with a known correct source: eight of ten find that source somewhere in the results, but the average rank when found is third out of five kept, close to falling off the cutoff if anyone tightens it, and only sixty percent of what actually got retrieved on a typical query was relevant, meaning nearly half the context handed to the model was noise it had to read past. The two questions that found nothing at all are the most important row on that scorecard, more important than the ranking numbers, because a pure miss usually traces back to chunking or, worse, to a document ingestion never included in the first place.

Say the honest caveat this scorecard earns and doesn't erase: good retrieval metrics don't guarantee a good answer. The right chunk can be retrieved cleanly and still get misread, summarized wrong, or have a caveat inside it dropped on the way to the final sentence. This scorecard measures only the retrieval half of the feature. Pair it with chapter five's rubric, which measures the half a retrieval scorecard structurally cannot see, and run them in that order: if retrieval itself is failing, no amount of scoring the finished answer tells you where to actually intervene.

## What this doesn't cover yet

Everything in this chapter assumes the retrieval system is stable: the documents don't change underneath it, nobody's permissions determine what they're allowed to see, and the index reflects what's actually true right now. None of those assumptions survive contact with a real production system for very long, and pretending otherwise here would be dishonest about exactly the kind of gap this book keeps insisting on naming. That's deliberately not this chapter's job. It's the next one's.

## Score your own retrieval by hand

Write ten real questions your feature should be able to answer, each with a known correct source document you identify yourself, before you look at what the system actually retrieves. Run all ten through retrieval and score hit rate, rank, and precision honestly, by hand, before building any automated version of this check.

Resist the urge to skip straight to automating it. Scoring ten by hand, once, is what teaches you what "relevant" actually means for your own content, the exact judgment call that otherwise gets made invisibly by whoever writes the automated check later, without ever having done it themselves first.

[TAKEAWAYS]

- RAG fixes a missing-fact failure: the model reasoning fluently without the actual, current document it needed. It does nothing for a reasoning failure, and adding retrieval to a feature that's miscounting or misreading won't touch the real bug.
- The pipeline has seven stages. Ingestion and citation, the two ends, are product decisions with real consequences; the middle is mostly engineering's to build once those calls are made.
- Chunk size is a genuine trade-off, not a default to inherit from a tutorial, and different content types in the same corpus usually need different chunking strategies.
- Score retrieval on three numbers, hit rate, rank, and precision, separately from the finished answer. A clean retrieval scorecard and a good final answer are two different, both necessary, checks.
- Air Canada's chatbot and this chapter's benefits assistant failed the identical way: a fluent, confident answer standing in for a document that was never actually consulted. Retrieval is the fix for exactly that gap, and only that gap.

[/TAKEAWAYS]

## Where this goes next

Chapter thirteen takes a retrieval system that scores well on every metric in this chapter and shows the specific places it still breaks once real production traffic, real permissions, and real time hit it.
