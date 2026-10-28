# KDP listing package: Stop Guessing Whether It Works

Assembled 2026-10-29 by the Commander from `book.yaml`, `docs/05-kdp-playbook.md`
and `books/CLAUDE.md`. Nothing here is posted or submitted. Everything marked
`{{ }}` is James's call. The gate today is exactly one failure,
`verified: false`; that sign-off is James's alone.

## Before the upload (James)

1. Read the manuscript end to end, then set `verified: true` in `book.yaml`
   (`python3 books/pipeline/qc.py --book stop-guessing` then passes).
2. Build the files and run the release gate:
   `python3 books/pipeline/build.py --book stop-guessing`,
   `python3 books/pipeline/qc.py --book stop-guessing --release`,
   `python3 books/pipeline/build_epub.py --book stop-guessing`.
   Never commit the PDF or EPUB.
3. Cover: commissioned from a human designer (playbook section 3). The
   spine width needs the locked page count from step 2. No AI-generated cover art.
4. KDP account, the upload click, price and categories: James.

## Listing fields

| Field | Value |
|---|---|
| Title | Stop Guessing Whether It Works |
| Subtitle | The Product Manager's Field Guide to Evaluating, Costing, and Shipping AI Features |
| Author | James Liu |
| Trim | 6x9, genre: business, copyright year 2026 |
| Language | English (a Simplified Chinese edition exists as `book-zh.yaml`; list it separately) |
| Description | Copy the block below verbatim. |
| Keywords (7 slots) | {{ James picks }}. Rule from the playbook: phrase-level, no repeat of title or subtitle words; test each phrase against Amazon autocomplete at upload time. |
| Categories (3) | {{ James picks }}. One winnable niche, one mid-size, one aspirational; verify category sizes on the day. |
| Ebook price | {{ James }} (the playbook's launch plan is in section 3) |
| Paperback price | {{ James }} |
| KDP Select / KU | {{ James }} (playbook: first 90 days) |
| ISBN | {{ James }}: KDP free ISBN locks the imprint field; own ISBN if wider distribution is planned |

## Description (from `book.yaml`)

You are accountable for an AI feature you're not sure how to judge. Every
method you learned for shipping software assumes it behaves the same way
twice. This one doesn't, so your acceptance criteria stop working, QA
passes things that fail in production, and quality arguments get settled
by whoever is most senior rather than by evidence.

This book gives you the judgment work that survives every model upgrade:
writing acceptance criteria as evaluation thresholds instead of pass/fail
rules, building a golden set you can actually defend, pricing a feature
before it ships instead of on the invoice, scoping an agent with
reliability math instead of optimism, and running a risk register that
gets you through legal review instead of stalling in it.

Written for product managers, delivery leads, and analysts who are now
responsible for AI work with no engineering background required.

## AI disclosure (KDP dashboard)

KDP asks whether text, images or translations were AI-generated. The playbook
says to decide these answers deliberately, and they are James's to give, on his
own knowledge of how he used AI on this manuscript. Facts the repo supports:
the interior's figures are generated from data specs (`figures/*.yaml`), not
image-generated, and the playbook rules out an AI-generated cover. Answer text:
{{ James }}.

## Table of contents

1. The Accountability Gap
2. Seven Shapes
3. The Spec Nobody Can Argue With
4. The Golden Set
5. Getting Two People to Agree
6. What It Actually Costs
7. The Reliability Math of Agents
8. The Risk Register
9. Metrics That Survive Production
10. Managing the Room
11. Speaking Engineer Without Faking It
12. Why RAG, and How to Measure It
13. Where RAG Breaks in Production
14. Objections and Pushback
15. Field Notes: Three Worked Case Studies
16. The First Ninety Days
17. Where This Breaks

Back matter:
- Appendix A: The Golden Set Worksheet
- Appendix B: The Risk Register Template
- Appendix C: The Model Scorecard Template
- Appendix D: The Ninety-Day Plan Template
- Notes and Sources
- About the Author

## Launch (not before the sign-off)

Follow `docs/05-kdp-playbook.md` section 4 (launch sequence and review engine).
Cross-sell to the ai-for-pms course only per that section.
