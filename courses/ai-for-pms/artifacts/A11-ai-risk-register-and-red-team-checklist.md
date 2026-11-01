# A11 · AI Risk Register + Red-Team Checklist

Part of *AI Product Skills for PMs & Analysts*. The register is introduced in
lecture 8.1, the five categories are taken in depth in lectures 8.2 to 8.6, and
the checklist is the workshop in lecture 8.7. Use them to record every real risk
to one AI feature, with one named owner and a real review date on each, and to
test the feature against all five categories in about twenty minutes.

This is a working tool for a product owner. It is not legal advice and not a
security audit. Where a row touches law or contracts, the register records the
question and who is answering it. Counsel decides the answer.

---

## 1. How to use this

1. **Start with the red-team checklist (section 4).** Twenty minutes, five
   blocks, one honestly attempted test in each. Every real gap it finds becomes
   a row in the register.
2. **Write the register (section 3) one row per real risk,** using the exact
   input path or failure mode you already suspect for your own feature, not a
   hypothetical one.
3. **Score each row the way lecture 6.6 scored blast radius:** can it be undone,
   and what does it cost if it is wrong (section 2).
4. **Name one person on every row, by name.** Not a team. Not "the business".
5. **Write the mitigation as the change that lowers the blast radius.** "Legal
   will review it" is not a mitigation. It names who worries next, not what
   changes.
6. **Put a real review date on every row,** on a real calendar. A register that
   is reviewed "whenever someone remembers" is a list of worries.
7. **Re-sort when the use case changes,** not only at launch. A new market, a new
   data source or a new tool changes the rows.

## 2. Scoring: reversibility and cost

The same four-row sort as A08 (lecture 6.6).

| Reversible? | Cost if wrong | Verdict | What the mitigation must be |
| --- | --- | --- | --- |
| Yes | Low | Accept and monitor | A named owner and a review date |
| Yes | High | Mitigate; cap the exposure and log | A cap, and a log that makes it traceable |
| No | Low | Mitigate; review after the fact | A flag for review after it happens |
| No | High | Gate it, or do not ship it | An approval before the action, by a named approver |

A row that lands in the bottom row without a gate is not ready to ship.

## 3. The register

**Risk register: [feature name]**

| | |
| --- | --- |
| Feature | |
| Register owner (a name) | |
| Last reviewed | |
| Linked documents | The PRD (A01), the golden set (A02), the agent worksheet (A08) if the feature acts, the RAG design doc (A06) if it retrieves |

One row per risk. Add rows as needed, and mark a row with a closed date when its
mitigation is shipped and tested, rather than deleting it.

| # | Category | The specific risk, with the exact path or failure mode | Reversible? | Cost if wrong, and how you know | Row from section 2 | Mitigation (the actual change) | Owner (a name) | Review date | Status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Prompt injection | | | | | | | | |
| 2 | Data and privacy | | | | | | | | |
| 3 | Regulatory | | | | | | | | |
| 4 | Bias and fairness | | | | | | | | |
| 5 | Operational | | | | | | | | |
| 6 | | | | | | | | | |
| 7 | | | | | | | | | |
| 8 | | | | | | | | | |

A row that reads like these is a list of worries, not a register row:
"Prompt injection is a risk we should think about" with owner "the team" and a
review "whenever someone remembers". A working row names the specific input path,
one person, and a date. Example of the level of specificity (not a finding for
your feature): "An uploaded PDF's text can currently reach the system prompt
unescaped."

The five categories, each taken in depth later in the section:

| Category | What a row in it looks like | Lecture |
| --- | --- | --- |
| Prompt injection | Untrusted input silently overrides an instruction | 8.2 |
| Data and privacy | Personal data surfaces in a response or a log | 8.3 |
| Regulatory | The feature falls under a rule nobody has checked | 8.4 |
| Bias and fairness | Quality or outcome varies by group | 8.5 |
| Operational | Nobody owns what happens when it breaks | 8.6 |

## 4. Red-team checklist (the 20-minute workshop)

Not a security audit. Five blocks, five specific findings. For each block write
either a real gap named precisely, or a real check you confirmed. A specific,
honest "not yet measured" beats a vague "should be fine". Finding nothing in a
category is not the goal.

Suggested pacing: minutes 0 to 4, 4 to 8, 8 to 12, 12 to 16, 16 to 20.

### Block 1. Try to break it (lecture 8.2)

Prompt injection is content, typed by a user or hidden in something the model
reads, that overrides an instruction the developer intended. The model cannot
fully separate instructions from the content it is processing.

| Check | Your answer |
| --- | --- |
| Every place untrusted content reaches the model: user input, retrieved documents, fetched pages, uploaded files, email text | |
| For each one, what the model is allowed to do immediately afterwards (what tools it can call, what it can write) | |
| One direct injection attempt you actually made, and what happened | |
| One indirect injection attempt you actually made (a hostile line inside content the feature reads), and what happened | |
| Is reading kept apart from acting? Does the step that reads untrusted content only produce a structured output, with any consequential action a separate call against an approval gate? | |
| Finding | Real gap / confirmed check |

An instruction to the model to ignore instructions in content it reads helps a
little. It is not a reliable fix on its own.

### Block 2. The three data questions (lecture 8.3)

Ask and answer them separately. Never bundle them into one reassurance.

| Question | Where the answer lives | Your answer, with the source |
| --- | --- | --- |
| PII: what personal data reaches the model, and where does it go afterwards (the model call, logs, any third party)? Trace one real request through every stop. | Your own architecture | |
| Residency: which country's servers and laws govern the data at each stop? | The vendor's infrastructure or trust documentation | |
| Training rights: can the vendor use your data to improve its models? | The contract or account settings | |
| Evidence for training rights: the actual setting, captured, dated and named to an owner | The account | |
| Finding | | Real gap / confirmed check |

Residency and privacy law differ by country and by sector. These are the
questions to take to counsel, not the answers.

### Block 3. Sort it into the four tiers (lecture 8.4)

Sort the feature by what it is used for, not what it is built with. Start from
the consequence to a real person. This is a mental model, not a permanent
checklist: guidance and enforcement are still evolving, so confirm the current
position with counsel.

| Tier | What it covers (as lecture 8.4 describes it) | Where this feature sits, and why |
| --- | --- | --- |
| Unacceptable | Banned outright | |
| High-risk | Risk management, human oversight and documentation obligations | |
| Limited risk | Transparency obligations, such as disclosing that a user is talking to an AI | |
| Minimal risk | No specific obligations | |

| Check | Your answer |
| --- | --- |
| The consequence to a real person if the output is wrong (hiring, credit, access, eligibility, or none) | |
| Can the feature's output reach users in the EU? HQ location is not the question | |
| Checked against the high-risk examples first, before assuming minimal | |
| Who is confirming this with counsel, and by when (a name and a date) | |
| Finding | Real gap / confirmed check |

### Block 4. One fairness slice (lecture 8.5)

"Is it biased?" cannot be answered. "Does the pass rate vary by group, measured?"
can. A clean aggregate pass rate is not evidence of fairness. It is often
evidence nobody measured at enough resolution to find the gap.

| Check | Your answer |
| --- | --- |
| One plausible dimension your feature's quality could vary by (for example how formal or informal the phrasing is, language, region, account type). Pick one that would matter for this feature. | |
| How many golden set cases (A02) you have in each segment of that dimension | |
| Is that enough to score each segment separately? If not, how many more, and who gathers them | |
| The pass rate per segment, if you can already measure it | |
| Finding | Real gap / confirmed check |

### Block 5. Detection and kill switch (lecture 8.6)

A server that is down is obvious. A feature that is quietly wrong looks exactly
like one that is working. The signals that catch an outage (errors, latency,
uptime) usually do not move for a quality failure.

| Check | Your answer |
| --- | --- |
| Could you detect a quality-only incident today, before a user complained? Which signal would show it? | |
| Who owns quality incidents, by name, and who is on call | |
| The kill switch: a fast, safe way to turn the feature off without a full deploy | |
| Tested once, deliberately, on a real date, and the result. Tested beats assumed, every time. | |
| The rule that every real failure becomes a new case in the golden set (A02), so it is caught automatically next time | |
| Finding | Real gap / confirmed check |

## 5. After the twenty minutes

1. Turn every real gap into a dated, owned row in the register (section 3).
2. Check no row in the bottom row of section 2 is missing its approver.
3. Check no mitigation is "someone will review it".
4. Send the register to the person who would fix the first row, and ask which
   row they would challenge.
5. Set the next review. Rows are reviewed on their dates, not when someone
   remembers.

## 6. Honest test

- Does every row name one person, not a team?
- Does every mitigation describe a change, not a reviewer?
- Is anything written as certain that is really a guess?
- For every "confirmed check", could you show the evidence?
- Which of the five blocks did you only imagine instead of attempting?

## 7. Open gaps

| Block or category | What is missing | Owner and date |
| --- | --- | --- |
| | | |
