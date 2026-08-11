# Status and chapter map

Not part of the build. Working notes for continuing across sessions, same
pattern as the other books.

## Status: editorial pass complete. Manuscript is print-ready except the author's own read-through.

The book went through three phases: initial draft (10 chapters), an
expansion pass toward a 180-240 page target, and a full editorial pass
(structural continuity, line edit, citation re-verification, AUTHOR-INPUT
resolution, final build). All three are done. What's left is entirely the
real author's: read it, sign off, supply a byline and bio, commission a
cover, and answer KDP's dashboard questionnaire. See "Remaining author
actions" below.

**Final page count: 129 pages, 15 chapters, ~30,000 words.** `book.yaml`'s
`target_pages` has been brought down from `[180, 240]` to `[120, 150]` to
match reality, honestly, rather than left pointing at an aspiration the
book didn't reach. Report this straight to the author: the expansion pass
that preceded this editorial pass was told mid-run to reach 180-240 pages
and landed at 129, short of even the 180 floor. When the next directive
arrived, it said to finish what was in flight and then stop writing new
material and move to editorial-only work. That instruction is what closed
the expansion effort at 129 pages rather than pushing further; it wasn't a
decision made unilaterally to abandon the target. If the author wants
180-240 pages, that's a fourth pass, deliberately not attempted here, and
the honest paths to it are the same two named in this file's prior
revision: **more chapters** (Client Onboarding and post-sale
follow-up/retention were both scoped out as credible, unclaimed topics)
or **more depth** in what exists (a third worked example per chapter, more
filled-in template examples in chapter 15, which is short on prose and
long on layout, so it's the cheapest lever for real pages without new
research). Bringing `target_pages` down was necessary regardless of that
future decision, because the KDP gutter margin is computed from
`target_pages`'s midpoint (`book.margins()` -> `gutter_for_pages()`), and
shipping with it still pointed at 180-240 would have produced a
0.5in-gutter interior on a 129-page book instead of the correct 0.375in.
If the book grows past 150 pages in a future pass, bump `target_pages`
back up and re-render; `build.py` will flag the mismatch automatically
(`gutter was set for the N-M target band; actual page count P wants
Xin, not Yin`) so it isn't a silent error to chase.

## What the editorial pass did

1. **Structural read-through, all 15 chapters in order plus front/back
   matter.** Found and fixed: three false "chapter nine" attributions in
   chapter 2 (chapter 9 is exclusively about scope creep and never covered
   the claimed content), a dangling non-referential "chapter two's job
   description" phrase in chapter 3, a false attribution in chapter 3's
   TAKEAWAYS, an awkward third-person self-reference in chapter 9,
   terminology drift ("voice profile" vs. the established "voice
   reference") in chapter 5, a misattribution in chapter 11, undercounted
   chapter ranges in chapters 12 and 13 (a "common mistakes" section
   count and a "chapters built" count that both predated chapter 10 being
   added), a stale "the previous thirteen" count in chapter 15 that should
   have said fourteen, and a genuine continuity bug in chapter 12 where
   Priya sent a clarifying question "before anyone signed" on the exact
   contract chapter 6 already showed her signing (fixed by reframing it as
   a retroactive amendment, which is consistent with every other chapter
   that references the same contract).
2. **All 15 `[PULLQUOTE: ...]` boxes brought into verbatim compliance.**
   The house rule (`books/docs/01-production-playbook.md` §3) is that a
   pull quote is lifted character-for-character from a line already in
   the chapter, not composed fresh. A systematic check found 11 of 15
   were paraphrases, several with numbers or attributions that drifted
   from the body text they were supposedly quoting. Every one was swapped
   for an exact contiguous quote from its own chapter.
3. **All 5 remaining `[AUTHOR-INPUT: ...]` markers resolved** (chapters
   04, 06, 07, 08, 09), per `books/CLAUDE.md` §1: restructured each
   passage to carry its point through Priya's or Marcus's established
   running examples rather than inventing a personal anecdote. `verified`
   stays `false`. The two back-matter `[AUTHOR-INPUT: ...]` stubs
   (acknowledgments, about-the-author) and `book.yaml`'s `author: "Your
   Name"` placeholder were deliberately left as-is: those are the real
   author's identity and story, not something this pass can supply.
4. **Every `[KEY-INSIGHT: ...]` citation independently re-verified against
   live sources**, not recalled from training data. Of 20 citations, 9
   needed correction:
   - **ch02**, SaaS tool sprawl: the cited "~30% of software spending on
     unused licenses" was unsupported/misattributed. Replaced with Zylo's
     own published figure (46-53% of purchased licenses go unused).
   - **ch02**, Gloria Mark interruption-recovery: the widely repeated
     "23 minutes and 15 seconds" traces to an offhand remark rather than
     the 2023 book's own numbers, which round to ~25 minutes. Softened
     and added the underlying 2005 study to the citation.
   - **ch03**, proposal conversion rates: the cited "1-3% generic vs.
     15-25% personalized" actually **inverted** the real source data.
     Jobbers' real benchmarks are generic ~15-25%, semi-customized
     ~35-45%, fully personalized ~55-70%. Replaced throughout (including
     the chapter's TAKEAWAYS bullet).
   - **ch03**, HBR citation: real study, real numbers, wrong article
     title. Corrected to "The Short Life of Online Sales Leads" (HBR,
     March 2011) with full author list.
   - **ch05**, Toister customer-response citation: inverted a
     satisfaction threshold into an expectation claim. Toister's research
     shows replying within an hour *satisfies* 80-89% of customers, not
     that a majority *expect* an hour; asked what they actually expect,
     the largest group of customers names same-day or next-day. Rewrote
     the box and its follow-up paragraph, which if anything strengthens
     the chapter's actual argument for once-a-day triage.
   - **ch08**, GAO sole-proprietor tax figures: the cited 52%/40%
     underreporting thresholds were decades-old numbers (from a 2007 GAO
     report) grafted onto the 2024 report actually cited. Replaced with
     the 2024 report's real findings (~65% underreported, ~$13,500
     average understatement, $80B as ~16% of the total tax gap studied).
   - **ch09**, PMI scope-creep figure: "41 percent" doesn't appear in the
     2024 Pulse of the Profession report cited (that report covers
     remote/hybrid work, not scope creep). The real, well-documented PMI
     figure is 52% (up from 43% five years earlier), from PMI's 2018
     "Scope Creep Rising" report. Corrected the box, the body sentence,
     and the TAKEAWAYS bullet.
   - **ch11**, Cyberhaven sensitive-data figure: cited last year's number
     (34.8%) as current; corrected to the actual most-recent figure
     (39.7%).
   - **ch13**, Lally habit-formation figure: 66 days is the study's
     median, not its average. Corrected in the KEY-INSIGHT box and the
     TAKEAWAYS restatement.
   The other 11 citations (freelancermap, Upwork, Bonsai, McKinsey,
   LawGeex, Freelancers Union/Rodgers-Horowitz-Wuolo, Constant Contact,
   Nielsen, Fast Company, Mata v. Avianca, Adobe) were checked and
   confirmed accurate as written.
5. **Full rebuild and visual inspection.** Interior PDF and EPUB both
   build clean. `qc.py --release` passes with no failures other than the
   `verified` gate. All fonts embedded (`pdffonts` confirms TeX Gyre
   Schola Regular/Bold/Italic, all embedded and subsetted). Spot-checked
   roughly 20 pages spanning every chapter, including every box type
   (KEY-INSIGHT green, TAKEAWAYS blue, PULLQUOTE italic, and the orange
   AUTHOR-INPUT-NEEDED boxes correctly gating the two back-matter stubs)
   — all render correctly with the corrected content.
6. **Interior PDF committed to `proofs/one-person-business.pdf`**, a
   deliberate, author-requested exception to the normal never-commit-
   builds rule, so the author can read it directly on GitHub without
   running the pipeline themselves. `build/` itself stays gitignored and
   uncommitted. Re-run `python3 books/pipeline/build.py --book
   one-person-business` and re-copy to `proofs/` any time the manuscript
   changes; this file will go stale otherwise.

## Deliberately left alone

- **One stylistic deviation, noted rather than force-fixed**: the
  PULLQUOTE verbatim check (item 2 above) found the violations mid-pass;
  by the time all 15 were checked, all 15 had already been corrected, so
  there is nothing left deferred here. (An earlier version of this pass
  considered leaving some as "acceptable editorial license" before the
  full check was run; that judgment call was superseded once the full
  check showed the scale of the problem, and all 15 are now verbatim.)
- **The 51-page gap to the original 180-240 aspiration.** See the Status
  section above. Not attempted in this pass because the directive that
  started the editorial phase explicitly said to stop writing new
  material.

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

## Chapter map (final, 15 chapters, all written/expanded/edited)

| Chapter | Core idea |
| --- | --- |
| 01 The Job Behind the Job | Naming the real problem: admin ate the hours that should've gone to the craft |
| 02 The Stack, Not the Tool | Mental model: several small automations, not one app |
| 03 The Proposal That Writes Itself | Proposals and quotes |
| 04 Invoicing Without the Dread | Invoicing, chasing late payment, the money conversation |
| 05 The Inbox That Doesn't Own You | Client email triage and drafting |
| 06 Contracts You Can Actually Understand | Reviewing/drafting basics, scope language, not-legal-advice framing |
| 07 Your Marketing Department of One | Content, positioning, staying visible |
| 08 Bookkeeping Without a Bookkeeper | Expense tracking, categorization, not-tax-advice framing |
| 09 Protecting Your Scope | Boundary-setting scripts for scope creep |
| 10 Pricing and Raising Your Rates | Rate confidence, market research, the rate-math worksheet, the raise script |
| 11 Objections and Edge Cases | FAQ-format pushback: honesty, confidentiality, regulated industries, disclosure |
| 12 Two Businesses, Ninety Days | Extended worked case studies over one quarter each |
| 13 The 30-Day Build | Week-by-week implementation roadmap |
| 14 When to Actually Hire a Human | Honest limits. Closing chapter. |
| 15 The Templates | Every template/worksheet/script, collected, several with filled-in examples |

## Remaining author actions

Everything production-side is done. What's left is exclusively the real
author's:

1. **Read the whole book and set `verified: true` in `book.yaml`** once
   every claim and every anecdote is one they can personally defend. No
   one else may set this flag; it is the author's signature and the fact
   that keeps the KDP AI-assisted declaration true.
2. **Supply a real byline**: `book.yaml`'s `author` field is still the
   placeholder `"Your Name"`.
3. **Write the back matter**: `back-matter/acknowledgments.md` and
   `back-matter/about_the_author.md` are both real `[AUTHOR-INPUT: ...]`
   stubs (a real thank-you list; a real bio and the specific freelance or
   solo-business credentials that make this book's advice earned).
4. **Commission a cover.** This pipeline only produces the interior; KDP
   needs a separate cover file, and cover spine width depends on the
   final locked page count (129pp interior, once the author's own edits
   during read-through are accounted for).
5. **Answer KDP's dashboard AI-disclosure questionnaire** at upload time
   (AI-assisted, not AI-generated; see `books/CLAUDE.md` §1).
6. **Decide whether to pursue the 180-240 page expansion** that was
   paused for this editorial pass, and if so, which of the two paths
   above (more chapters vs. more depth) to take.

## Things to hold onto continuing this

- Every chapter should produce a real artifact the reader keeps. Chapter
  15 makes that literal: it's the collected reference version of every
  artifact named across chapters 01-14, and it's the cheapest place to
  add real pages next (more filled-in examples), not just blank
  templates.
- Every `[KEY-INSIGHT: ...]` must be verified against a live search, not
  just at writing time but again at any editorial pass — this pass found
  9 of 20 existing citations had drifted from their real sources (wrong
  year, inverted statistic, decades-old figure grafted onto a current
  citation, satisfaction rate presented as an expectation rate). Don't
  assume a citation that was verified once stays correct; sources update,
  and drift during expansion/renumbering passes is real.
- Before any future renumbering, `grep -n "chapter (ten|eleven|twelve|
  thirteen|fourteen|fifteen)"` (word forms, not digits) across the whole
  `manuscript/` directory first, fix every hit, then rebuild the full
  book and spot-check the TOC and a few interior pages. Also grep for
  "previous N" / "the last N chapters" style counts, which the word-form
  grep above will miss (this pass caught one such miss in chapter 15 that
  survived an earlier renumbering).
- `[PULLQUOTE: ...]` boxes drift toward paraphrase easily during drafting
  because a paraphrase often reads better in isolation than an exact
  quote does. Check verbatim compliance explicitly after any editorial
  pass, not just at the moment a chapter is first written; don't trust
  that a pull quote written correctly the first time stays that way
  through later edits to the surrounding paragraph.
- Watch for the `[$]`-placeholder LaTeX math-mode bug: an isolated `[$]`
  (a bare dollar sign not immediately followed by a digit) doesn't get
  escaped by Pandoc's markdown-to-LaTeX conversion the way `$100` does,
  so two of them in the same paragraph pair up as literal LaTeX math-mode
  delimiters and mangle everything between them. `$100`, `$2,400` (digit
  immediately after the `$`) render fine. Use `[dollar amount]` instead
  of `[$]` in worksheet templates.
