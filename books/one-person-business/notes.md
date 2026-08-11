# Status and chapter map

Not part of the build. Working notes for continuing across sessions, same
pattern as the other books.

## Status (revised: expansion pass to a 180-240pp target)

Author directive, mid-run: the book was tracking to ~54 pages against the
original `target_pages: [110, 160]`, and the author wants a substantially
fuller book. `target_pages` is now **[180, 240]**, which moves the KDP
gutter band from 0.375in (24-150pp) to **0.5in (151-300pp)**. `build.py`
computes the gutter from `target_pages`' midpoint automatically
(`book.margins()` -> `gutter_for_pages`), so no manual class option to
touch; just rebuild after `book.yaml` changes and confirm the band note in
`qc.py --release`'s output once the real page count settles near the new
target.

This is an expansion pass, not a rewrite: chapters 01-09 keep their
existing scenes and arguments and get real substance added (a second
worked example, a second `[KEY-INSIGHT: ...]` where independent evidence
genuinely earns its place, a chapter-end exercise/checklist), never
padding. Padding rules stay absolute: no restating, no inflated prose, no
drop in information density. If a chapter is complete at its length, the
book grows through a new chapter instead.

**Structural changes so far:**
- `manuscript/10-when-to-actually-hire-a-human.md` renamed to
  `13-when-to-actually-hire-a-human.md` (git mv) and its `book.yaml` id
  updated. It's the strongest closing chapter written so far and earned
  the actual closing slot; four new chapters now sit between chapter 9
  and it. Cross-references to "chapter ten" in chapters 01, 04, 08, and 09
  updated to point at the correct new chapter numbers.
- Four new chapters added to the outline (see revised chapter map below):
  10 Objections and Edge Cases, 11 Two Businesses, Ninety Days (worked
  case studies), 12 The 30-Day Build (implementation roadmap), 14 The
  Templates (every worksheet in the book, rendered as fill-in pages).
- `back-matter/acknowledgments.md` and `back-matter/about_the_author.md`
  added (both `[AUTHOR-INPUT: ...]`-gated, matching the sibling books'
  pattern; `build.py` already skips missing back-matter files silently, so
  these weren't previously required, but the sibling titles all have them
  now).
- Chapter 13 itself expanded in this pass: added a second worked example
  (Marcus, a freelance developer, on an S-corp election an AI tool got
  confidently wrong) and a second `[KEY-INSIGHT: ...]` (Adobe's 2026
  survey on AI tax-filing adoption), plus a "Try this" two-minute
  professional-check exercise, and a "Where this goes next" pointer to the
  new chapter 14.

**In progress:** expanding chapters 01-09, then writing new chapters 10,
11, 12, 14. Each gets the same per-chapter treatment as before: build
`--only NN`, visually inspect the render, `qc.py`, commit, push. Check
this file's "Chapter map" table below for per-chapter status as the pass
continues; update the word/page count note here again once the full book
is reassembled near the end of the pass.

## Register

Peer-to-peer, not expert-to-novice. The reader already runs a business,
sometimes for years; this book doesn't explain freelancing to them, it
respects that they're competent at the craft and only underwater on the
admin around it. Avoid anything that reads as "let me teach you your own
job." Money and contracts come up constantly; be explicit every time that
this isn't legal or tax advice, same discipline as the health chapter in
ai-for-the-rest-of-us.

A second recurring persona, Marcus (a freelance backend developer), is
being introduced across the expansion pass as the "second worked example"
in several chapters, alongside Priya. The point is genuine: showing the
same systems generalize past one kind of freelance work (a project-based,
higher-ticket, more IP/entity-sensitive practice, versus Priya's ongoing
design retainers), not just repeating Priya's scenario with different
words.

## Chapter map (revised outline, 14 chapters)

| Chapter | Core idea | Status |
| --- | --- | --- |
| 01 The Job Behind the Job | Naming the real problem: admin ate the hours that should've gone to the craft | written; expansion pending |
| 02 The Stack, Not the Tool | Mental model: several small automations, not one app, overview of the stack | written; expansion pending |
| 03 The Proposal That Writes Itself | Proposals and quotes | written; expansion pending |
| 04 Invoicing Without the Dread | Invoicing, chasing late payment, the money conversation | written; expansion pending |
| 05 The Inbox That Doesn't Own You | Client email triage and drafting | written; expansion pending |
| 06 Contracts You Can Actually Understand | Reviewing/drafting basics, scope language, not-legal-advice framing | written; expansion pending |
| 07 Your Marketing Department of One | Content, positioning, staying visible without burning the week's energy | written; expansion pending |
| 08 Bookkeeping Without a Bookkeeper | Expense tracking, categorization, not-tax-advice framing | written; expansion pending |
| 09 Protecting Your Scope | Using AI to draft the boundary-setting conversation, not just avoid it | written; expansion pending |
| 10 Objections and Edge Cases | FAQ-format pushback: client distrust of AI, confidentiality, industries with heavy compliance, "isn't this dishonest," what happens when a template fails | new; not yet written |
| 11 Two Businesses, Ninety Days | Extended worked case studies: Priya's design retainer practice and Marcus's project-based dev practice, each building the full stack over one quarter | new; not yet written |
| 12 The 30-Day Build | Week-by-week implementation roadmap for building the whole stack from scratch, referencing back to each chapter's specific template | new; not yet written |
| 13 When to Actually Hire a Human | Honest limits: the point a real accountant, lawyer, or professional earns their fee. Closing chapter. | written and expanded (second example, second KEY-INSIGHT, exercise) |
| 14 The Templates | Every template/worksheet/script in the book, collected as fill-in-ready pages: proposal brief, invoice template, follow-up sequence, contract flag checklist, positioning statement, weekly bookkeeping checklist, scope-creep scripts, the two-minute professional check | new; not yet written |

## Things to hold onto while writing the rest

- Every chapter should produce a real artifact the reader keeps: a
  template, a saved prompt, a checklist, not just an explanation. This
  is the most "workbook" of the books running so far, lean into that.
  Chapter 14 makes that literal: it's the collected reference version of
  every artifact named across chapters 01-13.
- `[AUTHOR-INPUT: ...]` markers want the author's own numbers where
  possible (hours saved, an invoice that went out same-day instead of two
  weeks late), concrete over general. Don't add more than the five already
  placed (chapters 04, 06, 07, 08, 09) just to hit length; the new
  chapters lean on `[KEY-INSIGHT: ...]` and the Marcus/Priya case studies
  instead, per the research-and-sourcing doc's stated preference.
- Chapter 13 (was 10) existing at all is the credibility chapter. Don't
  let it shrink to a paragraph; a book that never admits AI's limits on
  money and contracts is the exact pattern that gets a business book
  flagged as reckless rather than useful.
- Every new `[KEY-INSIGHT: ...]` in the expansion pass must be verified
  against a live search at writing time, same as the original nine.
  Second KEY-INSIGHTs are worth adding where they genuinely diversify the
  evidence (a different domain, a different kind of source), not where
  they just repeat the first one's point with a bigger number.
