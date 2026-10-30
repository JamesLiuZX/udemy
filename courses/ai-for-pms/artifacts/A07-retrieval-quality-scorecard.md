# A07 · Retrieval Quality Scorecard

Part of *AI Product Skills for PMs & Analysts*. Taught in lecture 5.4. The
companion file is `A07-retrieval-quality-scorecard.xlsx`, an empty workbook that
does the arithmetic. Use this page to understand the three measures and to score
your first ten queries by hand. Use the workbook once the hand tally has taught
you what "relevant" means for your own content.

---

## 1. How to use this

1. **Write ten real questions**, from real traffic if you have it. For each one,
   write down the document that holds the right answer **before** you run
   anything. If you look at the results first, you will find reasons the first
   thing that came back was fine.
2. **Fix k**, the number of chunks your feature keeps and hands to the model
   (for example the top 5). Use the same k for every query.
3. **Run each question through retrieval only.** Do not score the final answer
   here.
4. **For each query, record three facts** in the table in section 3:
   - the **rank** of the first chunk from the right document (1 is the top
     result), or blank if none of the kept chunks came from it;
   - the **number of kept chunks that were relevant**, meaning a chunk that
     helps answer the question, out of k;
   - a note on anything odd.
5. **Work out the three measures** (section 2), then read the misses first.
6. **Score the final answers separately** against the rubric (A05). Retrieval
   can be perfect and the answer still wrong, because the right chunk can be
   misread. Run this scorecard first: if retrieval is failing, scoring the
   answers will not tell you where to intervene.

## 2. The three measures

| Plain question | Technical name | How to work it out | What it catches |
| --- | --- | --- | --- |
| Did we find it at all? | Hit rate (recall at k) | Queries where the right document appeared anywhere in the k kept chunks, divided by queries scored | A document that exists but never surfaces |
| How high did it rank? | Mean reciprocal rank | For each query, 1 divided by the rank (1, 1/2, 1/3 and so on), and 0 for a miss; then the average | The right chunk buried near the cutoff |
| How much of what we got was useful? | Precision at k | For each query, relevant chunks kept divided by k; then the average | Noise diluting the context the model reads |

Also worth recording, because it is easy to read: the **average rank when
found**. It ignores the misses, so read it next to the hit rate and never alone.

A rank of 9 when you keep only 5 is a miss. Count it as one.

## 3. Hand-scoring table

| # | Query | Known correct source | Rank of first correct chunk (blank if none) | Relevant chunks among the k kept | Notes |
| --- | --- | --- | --- | --- | --- |
| 1 | | | | | |
| 2 | | | | | |
| 3 | | | | | |
| 4 | | | | | |
| 5 | | | | | |
| 6 | | | | | |
| 7 | | | | | |
| 8 | | | | | |
| 9 | | | | | |
| 10 | | | | | |

k used for every query: ____

| Measure | Your result |
| --- | --- |
| Hit rate: found ____ of ____ queries | |
| Average rank when found | |
| Mean reciprocal rank | |
| Mean precision | |
| Misses (queries where the source was not found) | |

## 4. Reading it

- **Read the misses first.** A rank problem is something the existing pipeline
  can improve. A pure miss usually points upstream: to chunking (lecture 5.3),
  or to the document never having been ingested at all.
- **Compare the three measures, not just the first.** A high hit rate with a
  low average precision means the right chunk is in the results, buried in
  noise. A good precision with a low hit rate means what comes back is clean but
  the right document is often absent.
- **A first scorecard is usually less flattering than the demo.** Five queries
  that all worked were never a measurement.
- **Ten queries is a start.** One query changes the hit rate by ten points. Use
  the scorecard to learn what "relevant" means for your content, then grow the
  set, using the golden set rules from A02.

## 5. Using the workbook

1. Make a copy of `A07-retrieval-quality-scorecard.xlsx`.
2. On the **Queries** tab, enter the query, the known source, k, the rank (leave
   blank for a miss) and the relevant-chunk count. The other columns calculate.
3. The **Summary** tab shows the four numbers and four checks. All four checks
   should read OK before you trust a number: they catch a rank larger than k, a
   relevant count larger than k, a scored query with no relevant count, and a
   found source with no relevant chunk.
4. The workbook has room for 30 queries. It scores nothing for you: every rank
   and every relevant count is your judgement.

Do the first ten by hand, then enter them in the workbook and check that the
Summary matches your hand tally. If it does not, trust the hand tally and look
for the typo.

## 6. Where this fits

This scorecard is the retrieval row in the RAG design doc (A06, section 4,
Retrieval targets). The targets you write there are the numbers you check here.
It sits beside the rubric (A05) and the golden set (A02): those measure the
answer, this measures what the answer was built from.
