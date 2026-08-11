# Status and chapter map

Not part of the build. Working notes for continuing across sessions, same
pattern as the other books.

## Status (expansion pass to a 180-240pp target, in progress)

Author directive, mid-run: the book was tracking to ~54 pages against the
original `target_pages: [110, 160]`, and the author wanted a substantially
fuller book grown through substance, never padding. `target_pages` is now
**[180, 240]**. `build.py` computes the gutter from `target_pages`'
midpoint automatically (`book.margins()` -> `gutter_for_pages`), so once
the real page count lands inside 151-300 the 0.5in gutter band will be
correct on both counts; right now `qc.py --release` correctly flags a
mismatch (0.5in baked in for the target, 0.375in is what the *current*
129 pages actually call for) because the manuscript isn't at target
length yet. That FAIL will resolve itself once page count catches up;
it's expected, not a bug to chase.

**Where this pass actually landed: 129 pages, still short of the 180
floor.** Read this honestly rather than as a finished expansion. Three
full rounds of genuine, non-padding expansion happened, in order:

1. **Structural pass**: renamed the old closing chapter (`10-when-to-...`
   → `13-when-to-...`, then → `14-...` again after the pricing chapter
   landed), added four new chapters (Objections, Two Businesses Ninety
   Days, The 30-Day Build, The Templates), added back-matter stubs.
2. **Per-chapter substance pass 1**: every chapter 01-09 and the closing
   chapter got a second worked example (Marcus, a project-based
   developer, alongside Priya's retainer design practice), a second
   `[KEY-INSIGHT: ...]` where independent evidence genuinely earned its
   place (never forced when the search turned up only weak secondary
   sources — several searches came back with SEO-blog-quality "stats"
   that were deliberately rejected rather than used), and a "Try this"
   exercise.
3. **Per-chapter substance pass 2 and 3**: an "exact prompt" section
   (verbatim, copy-pasteable) added to chapters 3-9, a full new chapter
   10 (Pricing and Raising Your Rates, which triggered a second
   renumbering of chapters 10-14 to 11-15), "Common mistakes" sections
   added to chapters 2-10, three more Q&As in Objections, an honest
   "if your ninety days looks worse" section in the case studies, a
   troubleshooting section and end-of-week checkpoints in The 30-Day
   Build, and filled-in worked examples (not just blank templates) for
   six of the templates in the final chapter.

Total: 29,984 words across 15 chapters, all individually built with
`--only NN`, visually inspected page-by-page, and `qc.py`-clean. The full
book builds clean, the EPUB builds clean.

**A real bug was found and fixed along the way**, worth flagging for
whoever picks this up next on any book in this repo: an isolated `[$]`
placeholder (a bare dollar sign not immediately followed by a digit)
doesn't get escaped by Pandoc's markdown-to-LaTeX conversion the way
`$100` does, so two of them in the same paragraph pair up as literal
LaTeX math-mode delimiters and mangle everything between them into
italic, run-together text overflowing the page margin. `$100`, `$2,400`,
`$80 billion` (digit immediately after the `$`) all render fine and don't
need this workaround. Fixed in this book by writing `[dollar amount]`
instead of `[$]` in worksheet templates; worth checking for in any other
book's dollar-amount placeholders.

**What it would take to close the remaining gap** (129 → 180 minimum,
better yet toward 210, the midpoint): at roughly 240 effective
words/page including box overhead, that's another 12,000-20,000 words.
Two honest paths, not mutually exclusive:
- More chapters. Two credible, unclaimed topics surfaced during this
  pass and were deliberately left out rather than force-fit: **Client
  Onboarding** (the gap between a signed proposal in chapter 3 and the
  first invoice in chapter 4, kickoff calls, expectations-setting, a
  welcome packet) and **The Inbox After the Sale** style follow-up/retention
  content. Either would need the same renumbering discipline used for
  the Pricing chapter: rename files, update `book.yaml`, then grep the
  *whole* manuscript for `chapter (ten|eleven|...)` word-form
  cross-references and fix every one, not just the obvious ones (a
  leftover "Chapter ten" reference from the *first* renumbering pass was
  still wrong three edits later, caught only by a full-manuscript grep
  before the second renumbering — always grep the whole tree, don't rely
  on memory of what was already fixed).
- More depth in what exists. Every chapter here is 1,500-2,300 words,
  genuinely substantial but not maximal; a fourth pass could add a third
  worked example, deepen the "common mistakes" sections further, or add
  more filled-in template examples (the templates chapter is the
  cheapest lever: it's short on prose, long on whitespace-formatted
  worksheet layout, so filled-in examples add real pages fast without
  needing new research).

Do not close this gap by inflating sentence length, restating earlier
points, or adding a `[KEY-INSIGHT: ...]` that isn't independently
verified and genuinely load-bearing. Every addition in this pass was one
of: a new fact (verified, sourced), a new concrete scenario, a new
reusable artifact, or an honest acknowledgment of a limit. Keep it that
way.

## Register

Peer-to-peer, not expert-to-novice. The reader already runs a business,
sometimes for years; this book doesn't explain freelancing to them, it
respects that they're competent at the craft and only underwater on the
admin around it. Avoid anything that reads as "let me teach you your own
job." Money and contracts come up constantly; be explicit every time that
this isn't legal or tax advice, same discipline as the health chapter in
ai-for-the-rest-of-us.

A second recurring persona, Marcus (a freelance backend developer), runs
through the whole book as the "second worked example" alongside Priya.
The point is genuine: showing the same systems generalize past one kind
of freelance work (a project-based, higher-ticket, more IP/entity-
sensitive practice, versus Priya's ongoing design retainers), not just
repeating Priya's scenario with different words.

## Chapter map (current outline, 15 chapters)

| Chapter | Core idea | Status |
| --- | --- | --- |
| 01 The Job Behind the Job | Naming the real problem: admin ate the hours that should've gone to the craft | expanded (3 passes) |
| 02 The Stack, Not the Tool | Mental model: several small automations, not one app | expanded (3 passes) |
| 03 The Proposal That Writes Itself | Proposals and quotes | expanded (3 passes) |
| 04 Invoicing Without the Dread | Invoicing, chasing late payment, the money conversation | expanded (3 passes) |
| 05 The Inbox That Doesn't Own You | Client email triage and drafting | expanded (3 passes) |
| 06 Contracts You Can Actually Understand | Reviewing/drafting basics, scope language, not-legal-advice framing | expanded (3 passes) |
| 07 Your Marketing Department of One | Content, positioning, staying visible | expanded (3 passes) |
| 08 Bookkeeping Without a Bookkeeper | Expense tracking, categorization, not-tax-advice framing | expanded (3 passes) |
| 09 Protecting Your Scope | Boundary-setting scripts for scope creep | expanded (3 passes) |
| 10 Pricing and Raising Your Rates | Rate confidence, market research, the rate-math worksheet, the raise script | written |
| 11 Objections and Edge Cases | FAQ-format pushback: honesty, confidentiality, regulated industries, disclosure | written, expanded (3 more Q&As) |
| 12 Two Businesses, Ninety Days | Extended worked case studies over one quarter each | written, expanded |
| 13 The 30-Day Build | Week-by-week implementation roadmap | written, expanded |
| 14 When to Actually Hire a Human | Honest limits. Closing chapter. | written and expanded |
| 15 The Templates | Every template/worksheet/script, collected, several with filled-in examples | written, expanded |

## Things to hold onto continuing this

- Every chapter should produce a real artifact the reader keeps. Chapter
  15 makes that literal: it's the collected reference version of every
  artifact named across chapters 01-14, and it's the cheapest place to
  add real pages next (more filled-in examples), not just blank
  templates.
- `[AUTHOR-INPUT: ...]` markers want the author's own numbers where
  possible, concrete over general. Don't add more than the five already
  placed (chapters 04, 06, 07, 08, 09) just to hit length; new material
  leans on `[KEY-INSIGHT: ...]` and the Marcus/Priya case studies
  instead, per the research-and-sourcing doc's stated preference.
- Chapter 14 (the "hire a human" chapter) existing at all is the
  credibility chapter. Don't let it shrink to a paragraph.
- Every `[KEY-INSIGHT: ...]` must be verified against a live search at
  writing time. If a search only turns up SEO-blog-quality secondary
  aggregation with inconsistent numbers, that's a signal to skip the
  citation for that spot, not to use the least-bad option; several
  candidate stats were rejected this pass for exactly that reason
  (freelancer scope-creep dollar-cost claims, several "how much
  freelancers undercharge" round numbers).
- Before any future renumbering, `grep -n "chapter (ten|eleven|twelve|
  thirteen|fourteen|fifteen)"` (word forms, not digits) across the whole
  `manuscript/` directory first, fix every hit, then rebuild the full
  book and spot-check the TOC and a few interior pages before trusting
  it's actually consistent.
- Watch for the `[$]`-placeholder LaTeX math-mode bug (see above) in any
  new worksheet content.
