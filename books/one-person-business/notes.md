# Status and chapter map

Not part of the build. Working notes for continuing across sessions, same
pattern as the other books.

## Status

All 10 chapters are now written, built, and visually inspected, individually
(`--only NN`) and as the full assembled `master.pdf`. `qc.py` (authoring mode)
is clean except the standard gates: `verified: false` and 5 unresolved
`[AUTHOR-INPUT: ...]` markers (chapters 04, 06, 07, 08, 09), all intentionally
left blocking for the real author, per `books/CLAUDE.md` §1. No filler/LLM-tell
warnings, no em dash failures, no malformed `[KEY-INSIGHT: ...]` markers.

Each chapter has one `[KEY-INSIGHT: ...]`, sourced from a live search at
writing time (not recalled from memory): Bonsai late-invoice data (04),
McKinsey's 2012 "Social Economy" email-time benchmark (05), the 2018 LawGeex
AI-vs-lawyers NDA study (06), a 2024 Constant Contact small-business marketing
survey (07), IRS Fact Sheet FS-2017-12 on estimated-tax penalties (08), PMI's
2024 Pulse of the Profession scope-creep finding (09), and Mata v. Avianca,
678 F. Supp. 3d 443 (S.D.N.Y. 2023) (10). Full citation lines are in the
manuscript files themselves.

EPUB builds clean (`build_epub.py`). `qc.py --release` currently fails on
two things, both expected at this stage, not bugs: the 5 `[AUTHOR-INPUT]`
markers, and total page count. The full interior PDF is **54 pages**
(chapters average ~1,150 words each, consistent with chapters 01-03's
established length), well under the `target_pages: [110, 160]` band in
`book.yaml`. Closing that gap means either a deliberate pass to substantially
deepen each chapter (more worked examples, longer prompt walkthroughs, real
before/after numbers once `[AUTHOR-INPUT]` is filled) or revising
`target_pages` to match the book's actual voice. That's an editorial call
for the real author, not something to solve by padding chapters to hit a
number. Gutter margin (0.375in, correct for the 24-150pp band) and font
embedding both check out at the current page count.

## Register

Peer-to-peer, not expert-to-novice. The reader already runs a business,
sometimes for years; this book doesn't explain freelancing to them, it
respects that they're competent at the craft and only underwater on the
admin around it. Avoid anything that reads as "let me teach you your own
job." Money and contracts come up constantly; be explicit every time that
this isn't legal or tax advice, same discipline as the health chapter in
ai-for-the-rest-of-us.

## Chapter map

| Chapter | Core idea |
| --- | --- |
| 01 The Job Behind the Job | Naming the real problem: admin ate the hours that should've gone to the craft |
| 02 The Stack, Not the Tool | Mental model: several small automations, not one app, overview of the stack |
| 03 The Proposal That Writes Itself | Proposals and quotes |
| 04 Invoicing Without the Dread | Invoicing, chasing late payment, the money conversation |
| 05 The Inbox That Doesn't Own You | Client email triage and drafting |
| 06 Contracts You Can Actually Understand | Reviewing/drafting basics, scope language, not-legal-advice framing |
| 07 Your Marketing Department of One | Content, positioning, staying visible without burning the week's energy |
| 08 Bookkeeping Without a Bookkeeper | Expense tracking, categorization, not-tax-advice framing |
| 09 Protecting Your Scope | Using AI to draft the boundary-setting conversation, not just avoid it |
| 10 When to Actually Hire a Human | Honest limits: the point a real accountant, lawyer, or VA earns their fee |

## Things to hold onto while writing the rest

- Every chapter should produce a real artifact the reader keeps: a
  template, a saved prompt, a checklist, not just an explanation. This
  is the most "workbook" of the books running so far, lean into that.
- `[AUTHOR-INPUT: ...]` markers want the author's own numbers where
  possible (hours saved, an invoice that went out same-day instead of two
  weeks late), concrete over general.
- Chapter 10 existing at all is the credibility chapter. Don't let it
  shrink to a paragraph; a book that never admits AI's limits on money
  and contracts is the exact pattern that gets a business book flagged as
  reckless rather than useful.
