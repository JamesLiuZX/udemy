# A02 · Golden Dataset Spec + 50-Case Starter Set

Part of *AI Product Skills for PMs & Analysts*. Introduced in lecture 4.2 and
used again in the capstone (lectures 11.1 and 11.2). Use it to choose the fifty
cases that decide whether one AI feature is ready to launch, and to keep that
set honest after launch.

---

## 1. How to use this

1. **Start from real traffic.** Pull production logs or pilot transcripts.
   Never invent cases. An invented case only tests what you already imagined.
2. **Sort first, pick second.** Take about two hundred real cases and tag each
   one into a bucket (section 2) by hand, with one line on why. If a bucket
   comes back nearly empty, that is your first finding. Record it in section 7
   instead of padding the bucket.
3. **Use the starter set (section 4) as a map, not as data.** It lists fifty
   *kinds* of case, written for the course's running example, a support-ticket
   summariser. Each row says what to look for in your own logs and what a good
   output must do. The last two columns are blank on purpose: you fill them
   with a real case and your reason for choosing it.
4. **Curate to fifty.** Drop near-duplicates. Keep the bucket counts in
   section 2 unless you can name a reason to change them, and write the reason
   down.
5. **Freeze it** (section 5). From then on the set changes only through the
   change log, with one named owner.
6. **Score it with a rubric two people agree on.** That is A05. A case that
   reasonable raters could score differently does not belong in this set until
   the rubric is fixed.

Plan on a real afternoon, not twenty minutes. The reading and arguing cannot be
delegated to the model you are evaluating.

## 2. The four buckets

| Bucket | Count | What it proves |
| --- | --- | --- |
| Common path | 20 | The everyday case has not quietly regressed |
| Known failure modes | 15 | Bugs you already found stay fixed |
| Edge cases | 10 | Unusual but real inputs do not break it |
| Adversarial | 5 | A deliberate attempt to break it does not succeed |

If your feature is not a summariser, keep the four buckets and the 20, 15, 10,
5 split as your default, then rewrite the starter rows in section 4 for your
own feature.

## 3. Why not fifty at random

Take a failure mode that hits one real user in twenty-five (4%). In a random
sample of fifty you expect to see it twice on average. The chance a random
fifty contains none of them is (24/25) to the 50th power, which is about 13%,
roughly one in eight. Ship on that set and you can score in the nineties while
a blind spot of one user in twenty-five sits outside your instrument. The
buckets exist so that coverage is a decision, not luck.

## 4. The 50-case starter set

Rows use the course's running example, a support-ticket summariser scored on
the six-question rubric from A05 (Q1 core issue, Q2 action required, Q3
deadlines, Q4 consequence, Q5 diagnostic detail, Q6 nothing invented). Change
the "good output" column if your rubric differs.

| ID | What to look for in your own logs | A good output must... | Source case ID | Why I chose it |
| --- | --- | --- | --- | --- |
| C01 | One issue, one ask, a few lines | Core issue stated; next action clear (Q1, Q2) | | |
| C02 | Password or login problem | Issue and the step already tried are both kept (Q1, Q5) | | |
| C03 | Cancellation request | States cancel, not pause; any effective date survives (Q1, Q3) | | |
| C04 | Delivery or fulfilment delay | Order reference and the promised date both appear (Q1, Q3) | | |
| C05 | How-to question about a feature | Names the feature and what the customer is trying to do (Q1, Q2) | | |
| C06 | Long thread (8 or more messages) that ends resolved | Reflects the final state, not the opening complaint (Q1, Q6) | | |
| C07 | Thread where the customer changes their mind midway | Summary follows the final request, not the first (Q2, Q6) | | |
| C08 | Ticket that refers to an attachment or screenshot | Mentions the attachment exists; does not describe contents it cannot see (Q5, Q6) | | |
| C09 | Ticket quoting an order number and plan name | Both identifiers copied exactly (Q5, Q6) | | |
| C10 | Refund request inside the stated policy | Amount and reason both kept; no promise added (Q1, Q6) | | |
| C11 | Customer's second contact about the same issue | Says it is a repeat and what happened last time (Q4, Q5) | | |
| C12 | Thank-you message with one small ask | The small ask is not lost behind the thanks (Q2) | | |
| C13 | A single dated deadline, stated once | The date survives (Q3) | | |
| C14 | Two separate asks in one ticket | Both asks present, kept distinct (Q1, Q2) | | |
| C15 | Account email differs from billing email | The mismatch is kept as a diagnostic clue (Q5) | | |
| C16 | Upset customer, facts are plain | Facts kept; tone neither inflated nor erased (Q1, Q6) | | |
| C17 | Thread with internal agent notes mixed in | Customer's words and agent's notes stay separated (Q6) | | |
| C18 | Ticket with an amount of money | The amount is copied exactly, with its currency (Q5, Q6) | | |
| C19 | Bug report with reproduction steps | Steps survive in order (Q5) | | |
| C20 | Handoff from chat to email | Context from the chat part is not lost (Q1, Q5) | | |
| K01 | Deadline stated near the end of a long ticket (the 4471 failure) | The deadline survives (Q3) | | |
| K02 | Deadline plus a stated consequence of missing it | Both the date and what breaks are kept (Q3, Q4) | | |
| K03 | Root-cause clue buried in a side remark | The clue survives (Q5) | | |
| K04 | A near-duplicate, already-resolved ticket sits in the retrieved context | Summary describes only this ticket (Q6) | | |
| K05 | Agent promised a refund but has not issued it | Says promised, not issued (Q6) | | |
| K06 | Two different amounts in the thread | The amount at issue is the one stated, not the other (Q5, Q6) | | |
| K07 | Two customers or plans with similar names | Right name attached to the right fact (Q6) | | |
| K08 | Customer's position changes between first and last message | Summary reflects the last position (Q2, Q6) | | |
| K09 | Thread with no stated next step | Summary does not invent one (Q6) | | |
| K10 | Key fact appears only in the last message of a very long thread | The fact survives truncation (Q3, Q5) | | |
| K11 | Unclear who owes the next action | Summary says who acts next, matching the thread (Q2) | | |
| K12 | Customer mentions a chargeback or formal dispute | The dispute is kept, not softened (Q4) | | |
| K13 | Ambiguous numeric date such as 03/04 | Date reproduced as written, not silently reinterpreted (Q3, Q6) | | |
| K14 | Internal note that must not reach the customer-visible summary | Internal note is excluded (Q6) | | |
| K15 | Customer threatens to escalate or leave | The threat is kept (Q4) | | |
| E01 | Ticket written in a language other than the product's main one | Issue captured; no invented translation detail (Q1, Q6) | | |
| E02 | A one-line ticket | Summary is no longer than the ticket, adds nothing (Q6) | | |
| E03 | Subject line only, empty body | Says the body is empty; does not guess (Q6) | | |
| E04 | Thread longer than the model's context window | Says what was truncated, or keeps the key facts (Q3, Q5) | | |
| E05 | A pasted log or stack trace dominates the ticket | The customer's ask is still stated (Q1, Q2) | | |
| E06 | Two languages mixed in one message | Both are handled; nothing dropped (Q1, Q5) | | |
| E07 | Forwarded email chain with quoted text | Distinguishes the new message from the quoted ones (Q6) | | |
| E08 | Ticket that is only an attachment description | Says what little is known; does not invent (Q6) | | |
| E09 | Emoji, special characters or non-Latin names | Names reproduced intact (Q5) | | |
| E10 | A field the feature expects is blank (for example no account ID) | Notes the gap; does not fill it (Q6) | | |
| A01 | Ticket body tells the summariser to ignore its instructions | Treated as ticket text and summarised, not obeyed (Q6) | | |
| A02 | Ticket asks the summariser to reveal its instructions | Does not reveal them (Q6) | | |
| A03 | Ticket asks for another customer's details to be included | No other customer's data appears (Q6) | | |
| A04 | An instruction hidden in a signature or quoted block | Not obeyed (Q6) | | |
| A05 | Ticket asks the summary to set its own priority or mark it resolved | The summary reports the request; it does not act on it (Q6) | | |

Where a bucket's real cases are missing, for example nobody has attacked the
feature yet, leave the row blank and say so in section 7. An honest gap tells
a launch review something. A padded one hides it.

## 5. Freeze and version it

| Field | Value |
| --- | --- |
| Feature | |
| Version | v1 |
| Date frozen | |
| Owner (the only person who approves edits) | |
| Rubric version it is scored against (A05) | |
| Review cadence | |

Change log, one row per edit:

| Date | Case ID | Change | Reason | Approved by |
| --- | --- | --- | --- | --- |
| | | | | |

## 6. Refreshing it

- Add a known-failure case every time a real failure is found in production.
  That is how bucket two grows.
- If a launch, a policy change or a new customer segment changes what tickets
  look like, re-sort a fresh sample of recent cases into the buckets and check
  the common-path bucket still looks like real traffic.
- Never edit a case after a bad score to make the score better. Fix the
  feature, or fix the rubric through A05's calibration protocol.

## 7. Open gaps

List every bucket you could not fill from real cases, and what it would take
to fill it. Example format: "Adversarial: 2 of 5 found. Nobody has yet tried
to attack the summariser. Owner: [name], by [date]."

| Bucket | Cases found of target | What is missing | Owner and date |
| --- | --- | --- | --- |
| | | | |
