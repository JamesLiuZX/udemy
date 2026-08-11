# Status and chapter map

Not part of the build. Working notes for continuing across sessions, same
pattern as the other books.

## Status: manuscript, editorial pass, and both editions' proofs shipped.
## Ready for the author's own read-through and sign-off.

**19 chapters, ~37,400 words, 163 pages (English); 135 pages (Simplified
Chinese).** `book.yaml`'s `target_pages` is `[155, 175]`, moved twice this
project: down from an initial `[180, 240]` aspiration once the manuscript's
real length became clear (see "The 180-240 gap, honestly" below), then up
again from `[130, 165]` once a later editorial pass (worked-visual tables
and the new SOTA-tools section, see below) pushed the real page count from
149 to 163, past the 150-page gutter-band boundary. `target_pages`'s
midpoint has to select the same gutter band as the true rendered count or
`qc.py --release` fails the gutter check; this happened once for real
during this project and is worth checking again after any future
substantial edit, the same way page count itself gets checked.

Interior PDF built clean, `qc.py --release` passes with no failures other
than the `verified` gate, all three TeX Gyre Schola weights embedded and
subsetted per `pdffonts`, gutter correctly at 0.5in for a 163-page book.
EPUB builds clean (`build_epub.py`, ~407 KB). TOC spot-checked visually,
no page-number drift, no collisions. Front matter, back matter, and
interior spreads across the book, including every chapter's new worked
visual and the toolkit's new SOTA-tools section, were visually inspected;
all render correctly: KEY-INSIGHT boxes, PULLQUOTE italics, tables, and
the toolkit's blank fill-in worksheets all format as intended, no
widow/orphan issues on any inspected page.

**Interior PDF committed to `proofs/resume-arms-race.pdf`**, the same
author-sanctioned exception to the never-commit-builds rule used by
`one-person-business`. **Simplified Chinese interior PDF committed to
`proofs/resume-arms-race-zh.pdf`** under the same exception. Re-run
`python3 books/pipeline/build.py --book resume-arms-race` (or
`--book books/resume-arms-race/book-zh.yaml` for the zh edition) and
re-copy to `proofs/` any time either manuscript changes; these files go
stale otherwise.

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

## Standards update (docs/09-visual-standard.md): what got done and one thing that deliberately didn't

Mid-project, a message arrived instructing three additions per
`docs/09-visual-standard.md`, folded into the editorial pass and inherited
by the zh edition. Documenting the response here for the real author's
review, since one part of it was a deliberate partial-compliance decision
rather than a straightforward build task.

1. **Hook and golden nugget per chapter** (§4): done, see the table below.
   Reviewed all 19 for weakness before writing this table; none needed a
   chapter rewrite to earn a genuine hook or a genuine one-thing-to-use-
   today nugget, the material was already there in each chapter's existing
   argument.
2. **A worked visual in every chapter** (§3): done, using the pipeline's
   existing, already-proven markdown-table mechanism, the same device
   `books/CLAUDE.md` already documents and this book was already using in
   a handful of chapters. 16 chapters needed one added (all but 04, 15,
   and 19, which already had one from initial drafting); each table
   presents worked, chapter-specific data (a four-fifths ratio, a rubric,
   a before/after comparison) rather than decoration. All 16 additions
   were translated into the zh edition too, since they landed after those
   chapters' Chinese translations were already written; see "Chinese
   edition" below for how that reconciliation was tracked.
3. **AI-generated images (the "specimen" lane)**: **not done, on purpose.**
   `docs/09-visual-standard.md` §3 permits AI-generated images narrowly, in
   a "specimen" lane (an example of an AI-written resume passage shown as
   a specimen, for instance), and explicitly not for diagrams, covers, or
   factual content. This book had no chapter where that lane was actually
   load-bearing: chapters 1, 3, and 4 already quote and analyze real,
   AI-generated-*sounding* prose as text, in the manuscript's own voice,
   which does the same instructional job as a rendered "specimen" image
   without the compliance question at all. Generating and embedding an
   actual AI image would flip this book's own KDP AI-disclosure answer
   from "AI-assisted" toward "AI-generated" content being present in the
   interior, per `books/CLAUDE.md` §1, a real and not easily reversible
   consequence, on a book that is otherwise close to a clean sign-off. I
   judged the marginal instructional value of an actual image over the
   text-based equivalent already in the manuscript to not be worth that
   trade, and did not generate one. **If the real author disagrees and
   wants a specimen image added deliberately, that's a legitimate call for
   them to make directly, with the disclosure consequence understood
   going in; it isn't something this pass should decide unilaterally by
   just doing it.**

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

## Hook and golden nugget per chapter (docs/09-visual-standard.md §4)

The one-line hook and the one concrete, usable-today thing, per chapter.
Reviewed for weakness before writing this table; none of the 19 needed a
chapter rewrite to earn a real version of both.

| Ch | Hook | Golden nugget |
| --- | --- | --- |
| 01 | Two AIs are fighting over Marcus's queue, and neither is optimizing for the thing he actually needs to know. | Fluency used to cost something, and that cost was the signal. It's free now, which is the whole mechanism in one sentence. |
| 02 | The screening side didn't react to cheap generation. It was already there, years earlier, waiting. | ATS keyword filtering and automated ranking predate ChatGPT by a decade; this was never a fair fight to begin with. |
| 03 | The filter isn't malfunctioning. It's doing exactly what it was built to do, and that's the actual problem. | Three literal criteria (exact keyword match, any employment gap, a habitual degree requirement) systematically filter out exactly the candidates worth a second look. |
| 04 | A fluent lie and a fluent truth now read identically on the page. | The three-test read: specificity, decision, verifiability, run in under a minute on any bullet you're unsure about. |
| 05 | The interview only stays the one honest part of hiring if you run it like one. | A four-question scorecard with 1-4 anchors written before the first candidate, plus a genuine unscripted follow-up on every answer. |
| 06 | Your own job posting is training data for the tool you're trying to beat. | Swap every trait-word for a task-word a candidate can honestly self-assess against before they even apply. |
| 07 | The filter nobody remembers setting up is the one most likely to be quietly breaking the law. | The four-fifths self-check: one ratio, no special tooling, runnable alone from numbers already in your ATS. |
| 08 | The best defense against a demand letter is a habit that started months before the letter did. | A one-page, dated log: criteria, decision, one-sentence reason, under two minutes per candidate. |
| 09 | Not every candidate who used AI is lying to you, and treating them all as suspects costs you your best ones. | The fast test: would this claim survive being said out loud, unprompted, in the room. |
| 10 | A thirty-minute debrief that argues in the abstract is a process problem, not a personality problem. | Independent written scores before the room talks, plus a one-page brief sent ahead, turns 30 minutes into 8. |
| 11 | A candidate can describe great work beautifully and still not be able to do it under your team's real constraints. | A short work sample, graded against a rubric fixed before anyone sees the task, catches exactly that gap. |
| 12 | Trust is evidence worth weighing, not a finished conclusion that exempts anyone from the process. | Run the same three questions on a referral that you'd run on a stranger, every time, regardless of who vouched. |
| 13 | The person in the interview and the person doing the job are no longer guaranteed to be the same fact. | One live, unscripted video round plus an identity check before offer closes almost the entire gap, for almost no cost. |
| 14 | How you treat everyone you reject is part of the same arms race, not a separate courtesy question. | A two-tier floor: a timely, honest template for every screened candidate; a real personal note for every interviewed one. |
| 15 | Every technique in this book has a real objection waiting for it on a Tuesday afternoon. | The quick-reference table: each objection answered with a specific citation, never a reassurance. |
| 16 | Neither case study in this chapter is friction-free, which is exactly what makes them worth believing. | The real payoff wasn't one dramatic win. It was having a specific, dated answer ready the moment someone asked why. |
| 17 | Building all of this in one ambitious week produces exactly the undertested system this book warns against. | A month-by-month sequence: fastest, lowest-setup win first, trust-heavy techniques only once the small ones have proven out. |
| 18 | None of the last seventeen chapters were ever really about winning a detection arms race. | Three things neither side of the arms race can do: read unwritten context, build real trust, own a judgment call with real accountability. |
| 19 | Eighteen chapters of technique, collapsed into pages you copy instead of rebuild from memory on a busy Tuesday. | The complete, filled-in example req shows how every worksheet actually connects to the others on one real requisition. |

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
- **Chapter 19 was missing both a `[PULLQUOTE: ...]` and a closing
  `[TAKEAWAYS]` box** until this pass, a pre-existing gap against
  `books/CLAUDE.md` §5's own house rule that predates the standards
  update; found and fixed while adding the SOTA-tools section below,
  worth a spot-check on any future chapter that's mostly worksheet/
  reference material, since that format is the one most likely to slide
  on this particular rule.
- **The "tools you're actually up against right now" section (chapter 19,
  before the glossary)** is this book's one deliberately perishable
  section, per `docs/09-visual-standard.md`'s SOTA-rigour instruction:
  named, specific, currently-real products (HireVue, Eightfold,
  HiredScore, Paradox, SeekOut on the screening/sourcing side; Cluely,
  Interview Coder, Final Round AI on the candidate side), every claim
  checked against live search at writing time (mid-2026) and hedged where
  the source is vendor-reported rather than independently audited.
  Concentrated there specifically, not scattered across chapters, so a
  future freshness pass is a single contained edit. Whoever does that
  pass should re-search each product name, not just update the prose
  around it; a market this fast-moving may have new leaders entirely by
  then, not just updated numbers for the same ones.

## Remaining author actions (English)

1. **Read the whole book and set `verified: true`** once every claim and
   citation is one the author can personally stand behind. No one else
   may set this flag.
2. **Commission a cover.** This pipeline only produces the interior;
   spine width depends on the locked page count (currently 163, may move
   slightly after the author's own edits).
3. **Answer KDP's AI-disclosure questionnaire** at upload time
   (AI-assisted, not AI-generated; see `books/CLAUDE.md` §1).
4. **Decide whether to pursue the rest of the 180-240 gap** (still short of
   the floor at 163 pages, though closer than the 149-page point where
   this was last assessed) via the two levers named above, or accept
   `target_pages: [155, 175]` as the honest final band. Nothing about
   shipping at 163 pages requires that decision be made before
   publishing; it's a length preference, not a compliance gate.
5. **Decide on the AI-generated "specimen" image question** named above:
   ship as-is (no AI imagery anywhere in the interior, the safer and
   currently-shipped default) or add one deliberately with the KDP
   disclosure consequence understood.
6. **Periodically refresh the SOTA-tools section** in chapter 19 (see
   above); it's the one part of this book with a real, built-in
   expiration date, by design.

## Simplified Chinese edition

**Complete and shipped.** Full idiomatic zh-CN translation of all 19
chapters at `manuscript-zh/`, `book-zh.yaml` with `lang: zh`, built with
the class's `[zh]` option (see `one-person-business/notes.md` for the
full CJK setup story and the shared-class changes that made it possible).
This was the first time this session actually exercised that toolchain
end to end for a real manuscript (previously only confirmed present via
grep); it built clean on the first attempt, no font or xeCJK errors.

**135 pages**, within the `[110, 150]` `target_pages` band in
`book-zh.yaml`. `qc.py --release` is clean apart from the expected
`verified: false` gate, plus one known, harmless false positive: the
`~Npp estimated` word-count WARN undercounts badly for CJK text (the
estimator splits on whitespace, which Chinese prose doesn't use), so
ignore that specific WARN for this edition and trust the real, rendered
page count instead. Interior PDF committed to
`proofs/resume-arms-race-zh.pdf`; EPUB builds clean, and needed one
narrow, backward-compatible fix to the shared `build_epub.py` (it
hardcoded English language metadata and never consulted `book.lang`, so
a zh EPUB would previously have shipped mislabeled as `en-US`; now emits
`zh-CN` for `lang: zh` books, verified English books are unaffected).

Front matter, back matter (About the Author), TOC, several interior
chapter openers, and the new SOTA-tools section (translated after the
fact, see below) were all visually inspected; Noto Serif CJK renders
cleanly at every weight used, chapter numerals use the Chinese "第 N 章"
format correctly, and the KEY-INSIGHT/PULLQUOTE/TAKEAWAYS boxes all
render with the same design as the English edition.

**One synchronization gap, found and fixed this pass, worth naming for
any future edit to either edition:** the 16 English worked-visual tables
added during the docs/09 standards-update work landed *after* most
chapters' Chinese translations were already done, so the zh files were
briefly out of sync with their English source. Caught by comparing table
counts per chapter across both manuscripts (`grep -c '^| ---'` on each
matching pair) and fixed by translating and inserting each missing table
at the correct structural location. The chapter 19 SOTA-tools section had
the same problem for the same reason and got the same fix. **If a future
pass edits one language's manuscript, re-run that same table-count
comparison before considering the other language's edition still current;
nothing in the pipeline enforces this automatically.**

KDP does not accept Chinese-language books; this edition targets Google
Play, Apple Books, and direct/lead-gen distribution once shipped, same as
the standing plan.

**Remaining author actions (Chinese edition), beyond the English ones
above:** a native-speaker read-through before `verified: true` covers
this edition too (the English sign-off does not imply the translation is
also correct); a separate cover for the zh edition once its own page
count is locked; confirm distribution mechanics for whichever of Google
Play Books, Apple Books, or a direct storefront the author actually
pursues, since none of those platforms' submission flows have been
touched by this pipeline.
