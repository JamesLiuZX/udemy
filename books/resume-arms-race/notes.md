# Status and chapter map

Not part of the build. Working notes for continuing across sessions, same
pattern as the other books.

## Status: manuscript complete, editorial pass done. English proofs ready
## for the author's own read-through and sign-off.

**19 chapters, ~35,700 words, 149 pages.** `book.yaml`'s `target_pages` is
`[130, 165]`, brought down from an initial `[180, 240]` aspiration to match
where the manuscript actually landed after a genuine, substantial expansion
pass, the same honesty discipline `one-person-business/notes.md` and
`ai-employee/notes.md` used before this. See "The 180-240 gap, honestly"
below for the full account; don't read the lower number as the effort
having been small, it wasn't.

Interior PDF built clean, `qc.py --release` passes with no failures other
than the `verified` gate, all three TeX Gyre Schola weights embedded and
subsetted per `pdffonts`, gutter correctly at 0.375in for a 149-page book.
EPUB builds clean (`build_epub.py`, 401 KB). TOC spot-checked visually,
no page-number drift, no collisions. Front matter, back matter, and
roughly a dozen interior spreads across the book (chapters 1, 4, 7, 8, 10,
13, and the toolkit) were visually inspected; all render correctly:
KEY-INSIGHT boxes, PULLQUOTE italics, tables, and the toolkit's blank
fill-in worksheets all format as intended, no widow/orphan issues on any
inspected page.

**Interior PDF committed to `proofs/resume-arms-race.pdf`**, the same
author-sanctioned exception to the never-commit-builds rule used by
`one-person-business`. Re-run `python3 books/pipeline/build.py --book
resume-arms-race` and re-copy to `proofs/` any time the manuscript
changes; this file goes stale otherwise.

## What got built, start to finish

Chapters 01-03 existed already (drafted in an earlier session). Chapters
04-09 were the original core-technique arc from the initial 10-chapter
outline. During this pass, the outline expanded from 10 chapters to 19,
in order, because a first full build came in at 97 pages against the
180-240 target and the honest paths available were "more chapters" or
"more depth" (the same fork `one-person-business/notes.md` names); this
pass took both, in this order:

1. **Four new technique chapters** slotted into the middle of the book
   (10 Coaching Your Hiring Managers, 11 Skills Assessments and Work
   Samples, 12 Referrals/Internal Moves/Warm Pipelines, 13 Verifying the
   Person), extending the same discipline chapters 4-9 built for reading
   a resume and running an interview into parts of the process a single
   recruiter doesn't fully control alone.
2. **One more new chapter** (14 Rejecting Well, at Scale), added after
   noticing the manuscript had thirteen chapters about deciding who gets
   in and nothing about the much larger group who don't, tied directly to
   Greenhouse's 2024 ghosting research and the volume-pressure argument
   from chapter one.
3. **A depth pass** across nearly every chapter: chapters 1-3 (predating
   the two-worked-examples standard the later chapters were held to) got
   the largest additions, including a second KEY-INSIGHT each; most other
   chapters gained a second worked beat, a resolved callback, or a named
   limit that wasn't there in the first draft.
4. **The toolkit chapter roughly doubled**, gaining a full "complete req,
   start to finish" worked example (a real filled job posting, four-fifths
   check, scorecard, and documentation log all from the same req, shown
   together) and a short glossary, the same low-word-density,
   real-page-count lever `ai-employee`'s templates chapter used.

This required renumbering the tail of the book three separate times as
new chapters landed in the middle rather than at the end (new chapters
belonged in the technique cluster, not after the closing chapter). Each
pass included a full grep sweep for both `chapter <word>` and
`chapters <word> through <word>` patterns, since the second form isn't
caught by a simple word-boundary substitution, that gap produced a real,
caught-and-fixed bug during this pass, worth remembering for any future
renumbering: `chapters X through Y` range references need checking
separately from single `chapter X` references, because `Y` in that
pattern isn't preceded by the word "chapter" and a `sed` rule anchored on
"chapter " won't touch it.

## The 180-240 gap, honestly

Real, substantial effort went into the expansion pass described above:
four new chapters, a fifth added after that, a depth pass across the
other fourteen, and the toolkit's worked example, roughly 14,000 words
added across two rounds. The manuscript still landed at 149 pages, not
180. Two honest reasons, not excuses:

- **This book's chapters are naturally leaner than some siblings'.**
  `stop-guessing` needed 17 chapters averaging ~2,400 words to reach 181
  pages; this book's 19 chapters average ~1,880. The voice this book
  established in chapters 1-3, tight, concrete, one clean argument per
  chapter, doesn't stretch to 2,400 words without padding, and `books/
  CLAUDE.md` and this session's own instructions are explicit that padding
  isn't an acceptable lever, so it wasn't pulled.
- **The topic genuinely closed out around 19 chapters.** Every chapter
  added past the original 10 filled a real, previously-missing gap
  (stakeholder coaching, work samples, referrals, identity verification,
  rejection communication); by chapter 19 the honest remaining gaps were
  much smaller ones (a metrics/quality-of-hire feedback loop chapter was
  considered and set aside as marginal, not clearly distinct enough from
  material chapters 4 and 16 already cover) rather than another chapter's
  worth of genuinely new material.

**If a future pass wants to close the rest of the gap**, the same two
levers `one-person-business` named apply here: more chapters (a
quality-of-hire feedback-loop chapter, closing the gap between what
chapter four's tests predict and what a hire's first six months actually
show, is the most credible unclaimed topic) or more depth (a third
worked example per chapter is the next honest lever, since two is
currently the floor every technique chapter meets, not a ceiling). Either
one means rebuilding and re-checking the gutter band; 149 pages is close
enough to the 150-page boundary that even a modest further expansion
should trigger `gutter_for_pages()`'s 0.5in band, and `build.py` will flag
the mismatch automatically if `target_pages` isn't updated to match.

## Register

Peer-to-peer with a working recruiter, not a general audience book.
Vocabulary (ATS, screen, pipeline, req, ghosting) can be used without
re-explaining it every time, unlike ai-for-the-rest-of-us. Closer in
register to stop-guessing than to ai-employee: professional stakes,
professional accountability, but the accountability here is fairness and
legal exposure as much as product quality.

Two recurring personas carry every worked example: Marcus (in-house
recruiter/TA, established chapter one) and Sana Iyer (agency/staffing
recruiter, introduced chapter four), the same "two seats on the same
problem" pattern `one-person-business` used with Priya and Marcus. Keep
using both for any new chapter; a chapter with only one worked example
falls short of this book's own established standard.

## Chapter map (final, 19 chapters)

| Chapter | Core idea |
| --- | --- |
| 01 The Arms Race | Naming the problem: AI-written resumes vs AI screening crushing the real signal in the middle |
| 02 How We Got Here | The mechanism: cheap generation + cheap screening, why this doesn't reverse; the SEO/content-farm precedent |
| 03 What AI Screening Actually Gets Wrong | Keyword gaming, false negatives, screening bias predates AI (Bertrand & Mullainathan) |
| 04 Reading Past the Polish | Three-test technique for spotting real signal in fluent text |
| 05 The Interview Is the Only Thing Left That's Real | Structured interview format, why unstructured barely beats a resume read |
| 06 Writing Job Posts That Don't Get Gamed | Job description phrasing vs AI resume-tailoring |
| 07 Bias In, Bias Out | Disparate impact, four-fifths rule, NYC Local Law 144; not legal advice |
| 08 Building a Screen You Can Defend | Documentation habit, 29 CFR 1602 recordkeeping floor |
| 09 Candidates Use AI Too, and That's Not Automatically Cheating | Assistive vs. deceptive AI use; the fairness pivot |
| 10 Coaching Your Hiring Managers | Getting a panel to actually use structure; the one-page brief |
| 11 Skills Assessments and Work Samples | Work samples as interview complement; their own AI-cheating problem |
| 12 Referrals, Internal Moves, and Warm Pipelines | Warm-channel trust still needs verification; referral homophily |
| 13 Verifying the Person, Not Just the Resume | Reference checks, FCRA floor, remote identity fraud (FBI/DPRK) |
| 14 Rejecting Well, at Scale | What you owe candidates you don't hire; ghosting and volume pressure |
| 15 Objections and Edge Cases | FAQ-format pushback, answered with citations and cross-references |
| 16 Two Recruiters, Two Pipelines | Extended worked case studies, Marcus and Sana, one full quarter each |
| 17 The First Ninety Days | Week-by-week implementation roadmap |
| 18 The Recruiter's Actual Value Now | Closing: judgment, relationship, context as the irreplaceable part |
| 19 The Toolkit | Every scorecard/worksheet collected, plus a complete worked req and a glossary |

## Things worth holding onto continuing this

- Every `[KEY-INSIGHT: ...]` was verified against a live search at writing
  time, not recalled from training data; several early candidate
  statistics turned out to be unverifiable myths once checked (a "60% vs
  100% qualifications by gender" claim, a "cost of a bad hire is 30% of
  salary, per the Department of Labor" claim with no findable DOL source)
  and were either dropped or turned into their own "here's the real,
  checked number" beat, the same device chapter two's ATS-rejection myth
  already used. Don't assume a familiar-sounding hiring statistic is
  real; check it the way this book keeps insisting the reader check
  theirs.
- **Every `[PULLQUOTE: ...]` was audited for verbatim compliance this
  pass and 13 of 19 needed a fix.** The failure mode was consistent: a
  pullquote that captured the right idea but was composed as a cleaner,
  more compressed version of the nearby prose rather than lifted
  character-for-character, exactly the mistake `one-person-business`'s
  editorial pass found and fixed at a similar rate (11 of 15). Re-check
  this on any future editorial pass rather than trusting it stayed fixed;
  a pullquote drifts easily during any later edit to its surrounding
  paragraph. A same-file grep script comparing each `[PULLQUOTE: ...]`
  span against the rest of the chapter body (excluding the marker itself)
  catches this reliably; a simple substring check is enough, no need for
  fuzzy matching.
- Chapter 07 and chapter 08 (and now 13) all touch legal exposure. Same
  discipline as the health chapter in ai-for-the-rest-of-us and the
  contracts chapter in one-person-business: not legal advice, said
  plainly in-chapter, not just once in a disclaimer.
- Chapter 09 is the fairness pivot of the whole book: candidates using AI
  are not automatically the enemy the way a fabricated credential is.
  Chapter 14 extends the same fairness lens to the rejection side.
- No `[AUTHOR-INPUT: ...]` markers anywhere in the manuscript; every
  chapter reached for `[KEY-INSIGHT: ...]` per the repo's stated default,
  and the real author has no lived recruiting experience to draw on for
  this title (per the About the Author bio), so that default was the
  only honest option throughout, not a shortcut.

## Remaining author actions (English)

1. **Read the whole book and set `verified: true`** once every claim and
   citation is one the author can personally stand behind. No one else
   may set this flag.
2. **Commission a cover.** This pipeline only produces the interior;
   spine width depends on the locked page count (currently 149, may move
   slightly after the author's own edits).
3. **Answer KDP's AI-disclosure questionnaire** at upload time
   (AI-assisted, not AI-generated; see `books/CLAUDE.md` §1).
4. **Decide whether to pursue the rest of the 180-240 gap** (17 pages
   short of the floor at 149) via the two levers named above, or accept
   `target_pages: [130, 165]` as the honest final band. Nothing about
   shipping at 149 pages requires that decision be made before
   publishing; it's a length preference, not a compliance gate.

## Simplified Chinese edition

Not yet started as of this note. Per the standing plan: parallel
manuscript at `manuscript-zh/`, `book-zh.yaml` with `lang: zh`, built with
the class's `[zh]` option (see `one-person-business/notes.md` for the
full CJK setup story and the shared-class changes that made it possible).
KDP does not accept Chinese-language books; this edition targets Google
Play, Apple Books, and direct/lead-gen distribution once shipped.
