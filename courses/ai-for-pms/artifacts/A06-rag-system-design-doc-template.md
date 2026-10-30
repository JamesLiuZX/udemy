# A06 · RAG System Design Doc Template

Part of *AI Product Skills for PMs & Analysts*. Delivered in lecture 5.7 and
used again in the workshop, lecture 5.8. Use it to specify the retrieval system
under one AI feature, in a form an engineer can build from and a reviewer can
push back on.

---

## 1. How to use this

1. **Write section 1 first, and write it as an argument.** It decides whether
   the rest of this document should exist. If you cannot finish it
   convincingly, the document has done its job: this feature may not need
   retrieval, and a better prompt may be the cheaper answer.
2. **Then work down in order.** The order is for the person building from the
   document, not the order the course taught the ideas. Pipeline stages come
   before chunking because you cannot choose a chunk until you know which
   stages exist. Retrieval targets come before failure coverage because you
   need a number to know what counts as a failure.
3. **Use it inside your PRD, not instead of it.** The acceptance criteria in A01
   name the bar the feature must clear. This document is what makes that bar
   reachable.
4. **Commit to numbers and cadences, then mark each as measured or assumed.**
   Do not copy a number from this course or from anyone else's template. Copy
   the habit of writing one down that a reviewer could call too low.
5. **If a section stalls, write a dated TBD with an owner** and add it to the
   open gaps list at the end. A named gap costs nothing but honesty. A blank
   section stops the draft.
6. **Run the disagreement test before anyone else reads it.** For every
   sentence, ask whether a reviewer could reasonably say "that number is too
   low" or "that cadence is too slow". If nobody could, the sentence is still an
   intention.

## 2. The template

Copy everything from "RAG design doc: [feature name]" to the open gaps list into
your own document. The "From" column is a map back to the lecture that teaches
each method.

| Section | What it must contain | From |
| --- | --- | --- |
| 1. Why RAG | Confirms this is a missing-fact problem, not a reasoning problem | 5.1 |
| 2. Pipeline stages | Which of the seven stages are built, and why | 5.2 |
| 3. Chunking strategy | A strategy per content type, not one default | 5.3 |
| 4. Retrieval targets | Hit rate, rank and precision thresholds | 5.4 |
| 5. Failure coverage | Which production failures apply, and the mitigation for each | 5.5 |
| 6. Permissions and freshness | The access model and the re-index cadence | 5.6 |

**RAG design doc: [feature name]**

| | |
| --- | --- |
| Feature | |
| Document owner (a name) | |
| Status and date | Draft, in review or approved, and the date |
| Linked documents | The PRD (A01), the golden dataset (A02), the rubric (A05), the retrieval scorecard, and the list of content sources (links) |

### 1. Why RAG

*From lecture 5.1. Retrieval is the expensive answer on the decision tree from
Section 2, not the default one. Make this section argue for it.*

| Prompt | Your answer |
| --- | --- |
| Find a case where the feature was confidently wrong. Was it missing a fact it should have retrieved, or reasoning badly about facts it had? Only the first is RAG's job. | |
| The missing fact, named: what specifically does the model not know? (Private, proprietary, or changing faster than a training run.) | |
| The document that would have fixed that wrong answer | |
| Why a better prompt would not solve it | |
| Why fine-tuning or a simpler answer would not solve it | |
| The decision | RAG is justified / not justified / not yet known (circle one and say why) |

If the decision is "not justified", stop here and record why. That is a
successful outcome for this document.

### 2. Pipeline stages

*From lecture 5.2. Map the feature against the seven stages. Name the stage
nobody has actually made a decision about.*

| Stage | Built, deferred or out of scope | Decision and reason | Decided by (a name) |
| --- | --- | --- | --- |
| Ingestion: which documents are in scope | | | |
| Chunking | | | |
| Embed and index | | | |
| Retrieval: top-k and the access rules | | | |
| Re-ranking (optional: costs latency) | | | |
| Generation | | | |
| Citation: whether and how sources are shown | | | |

Every optional stage you add costs latency and money for a marginal quality
gain. For any optional stage you keep, write the reason in the table above.

### 3. Chunking strategy

*From lecture 5.3. Real content needs more than one answer. Name the content
types first, then give each its natural unit.*

| Content type | Natural unit (for example a question and answer pair, a clause, a table row with headers repeated) | Chunk boundary and size | Known risk |
| --- | --- | --- | --- |
| | | | |
| | | | |
| | | | |

- A larger chunk is not safer. A chunk covering three ideas produces a blurry
  embedding that matches each of them worse.
- If a content type has no natural unit you can name, record that as an open
  gap instead of applying a default.

### 4. Retrieval targets

*From lecture 5.4. Retrieval quality is scored separately from answer quality.
Five flattering demo queries are not a measurement.*

| Metric | Plain question | Target | Measured or assumed | Where it is scored |
| --- | --- | --- | --- | --- |
| Hit rate at k (k = ?) | Did we find the right source at all? | | | |
| Rank (mean reciprocal rank) | How high did it rank? | | | |
| Precision | How much of what we retrieved was useful? | | | |

| Prompt | Your answer |
| --- | --- |
| Test queries: how many, each with a known correct source document | |
| Who wrote them, and from what real traffic | |
| First measured scorecard, date and link | |
| Answer quality is scored separately against the rubric (A05) | Yes / no |

Good retrieval metrics do not guarantee a good answer. The right chunk can be
retrieved and still be misread, so this scorecard and the rubric from Section 4
are both required.

### 5. Failure coverage

*From lecture 5.5. Six places a RAG system breaks in production. For each one,
say whether it applies and what the mitigation is. "Not applicable" needs a
reason.*

| Failure | Applies? | Mitigation | Owner (a name) |
| --- | --- | --- | --- |
| Stale index: confidently cites a policy that has changed | | | |
| Permission leakage: retrieves a document this user should not see | | | |
| Chunking damage: a fragment nobody could use | | | |
| Context overflow: retrieved chunks plus history silently truncated (trim history before chunks) | | | |
| Near-duplicate confusion: an old and a current version both retrieved | | | |
| Silent failure: nothing relevant exists and the model answers anyway | | | |

| Prompt | Your answer |
| --- | --- |
| The fallback when retrieval returns nothing relevant: disclaim, escalate or decline | |
| Who removes a document once it has been superseded | |
| Rechecked after launch: how often the scorecard is rerun, because the corpus drifts even when the code does not | |

### 6. Permissions and freshness

*From lecture 5.6. These two sink more enterprise pilots than chunking does.*

| Prompt | Your answer |
| --- | --- |
| The access model: whose access decides what a user can retrieve | |
| Where it is checked: at query time against the asker's current access, or at indexing time | |
| How long a permission change takes to reach retrieval, measured | |
| What happens the moment someone's access is revoked | |
| Re-index cadence, and what triggers an unscheduled re-index | |
| How a user can tell how fresh an answer's source is | |
| Content that changes too fast for any index: name it, and say which live system it should call instead | |

Naive retrieval assumes everyone who can ask can see everything indexed, and
that the index matches the current document. Neither survives a real
organisation.

## 3. The honest test

Before anyone else reads the draft:

1. Reread section 1. Could a colleague argue the other side, and would you have an
   answer?
2. Pick any target or cadence you wrote. Could a reviewer call it too low or too
   slow? If not, it is still an intention.
3. For every "Applies? No" in section 5, is there a reason written down?
4. Give the draft to one real colleague and ask what they would push back on.

## 4. Open gaps

| Section | What is missing | Owner and date |
| --- | --- | --- |
| | | |
