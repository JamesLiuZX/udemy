# Status and chapter map

Not part of the build. Working notes for continuing this manuscript across
sessions, same pattern as the other books.

## Status: manuscript complete, editorial pass done, English and Simplified
Chinese proofs both shipped. Only the author's own read-through and
sign-off are left blocking either edition.

Went from a 10-chapter, 1-verified-chapter draft to a complete 36-chapter,
~41,600-word manuscript in one pass: chapters 2-3 (originally drafted)
kept as-is content-wise but given a second worked example each (Marisol,
see "Register" below); chapters 4-36 written from scratch. `target_pages`
raised from `[110, 160]` to `[180, 240]` per the author's directive and hit
at **185 pages**, comfortably inside the band. `qc.py` and `qc.py --release`
both clean apart from the `verified: false` sign-off gate, which is
correct and untouched. Interior PDF and EPUB both build clean; all three
TeX Gyre Schola weights embedded and subsetted (`pdffonts` confirmed).
Spot-checked front matter, TOC (36 entries, no collision even with the
longer titles), every chapter opener, and all three box types
(KEY-INSIGHT green, PULLQUOTE italic blue, TAKEAWAYS light-blue) across
roughly 20 pages spanning the whole book. Interior PDF committed to
`proofs/ai-for-the-rest-of-us.pdf`, the author-sanctioned exception to the
never-commit-builds rule.

**Toolchain note for whoever picks this up next**: the container this was
built in had none of `pandoc`/`xelatex`/`latexmk`/`poppler-utils`/`hunspell`
preinstalled, despite `books/CLAUDE.md` assuming they exist. Installed via:
```
apt-get install -y pandoc texlive-xetex texlive-latex-extra \
  texlive-fonts-recommended texlive-lang-chinese latexmk poppler-utils \
  hunspell hunspell-en-us fonts-noto-cjk
```
(`texlive-lang-chinese` and `fonts-noto-cjk` are for the zh edition below;
skip those two if only building the English edition.) A future session on
a fresh container will hit the same gap.

## What the pass from 10 to 36 chapters actually did

1. **Finished the original outline** (chapters 4-10) to the definition of
   done in `books/CLAUDE.md` §7: two worked examples per chapter (Linda's
   established thread plus a new second household, Marisol's, introduced
   in chapter 1 and threaded through the rest of the book), a `[KEY-INSIGHT:
   ...]` per chapter independently verified against a live search at
   writing time, `[PULLQUOTE: ...]` and `[TAKEAWAYS]` in every chapter.
2. **Reached length through more real chapters, not padding**, the same
   honest lever `ai-employee`'s expansion pass used (it landed at 187pp
   via 24 chapters against a similarly short-sentence style). Added, in
   order: a practical setup run (choosing/setting up a tool, voice mode),
   a longer list of ordinary tasks (big purchases, hard-to-write messages,
   daily chores, real emergencies, resistant family members, job hunting,
   contracts/leases, tech troubleshooting, a hobby just for the reader,
   Medicare/insurance, a big family gathering, eldercare, financial aid,
   multilingual households, pet care, paychecks/taxes, staying close
   across generations, wills/advance directives, car repairs, income
   gaps), then the closing arc (teaching someone else, an extended
   two-household case study over a season, an honest time/money
   accounting, an objections FAQ, and a toolkit collecting every reusable
   prompt). 36 chapters total, avg. ~1,150 words each — deliberately many
   short chapters rather than a few long ones, to stay inside this book's
   own short-sentence, high-white-space voice instead of forcing padding
   into any single chapter.
3. **Full editorial pass**, run after the draft was complete rather than
   chapter-by-chapter, catching:
   - **26 of 36 `[PULLQUOTE: ...]` boxes were paraphrases**, not verbatim
     lifts from the chapter's own body prose (books/docs/01 §3's rule).
     3 of those were worse: lifted from inside the `[KEY-INSIGHT: ...]`
     box rather than body prose. All fixed to true character-for-character
     substrings, verified programmatically (a Python substring check, not
     eyeballing) after every fix. This is the same failure pattern
     `one-person-business`'s editorial pass found (11 of 15 there); it
     seems to be a default failure mode for pullquotes drafted alongside
     the chapter rather than pulled after, worth assuming will happen
     again in any future book here and checking for explicitly rather
     than trusting it was done right the first time.
   - One weak citation from the original chapter 2 draft ("aggregated
     usability findings... multiple published guides", which violates
     `books/docs/02-research-and-sourcing.md`'s "'studies show' is not a
     source" rule) replaced with a real, named source (Nielsen Norman
     Group's published CARE framework research).
   - Two filler words (`obviously`, flagged by `qc.py`'s FILLER regex).
   - A handful of real words/character names hunspell's en_US dictionary
     doesn't carry, added to `books/pipeline/qc.py`'s `ALLOW` set (same
     pattern as the other books' entries there): marisol, diego, sofia,
     pixma, autocorrect, chatbot(s), grandkids, reframe(d), résumé,
     stovetop, timeframe, tradeoff, walkability, and a couple more.
4. **Every `[KEY-INSIGHT: ...]` verified against a live search at writing
   time**, not recalled from training data. Full list of sources used,
   for reference if a future pass needs to re-verify (see
   `books/docs/02-research-and-sourcing.md`'s standard — re-verify at
   every future editorial pass too, sources drift):
   Pew Research Center (chatbot adoption, teen AI-for-schoolwork use, the
   age gap in chatbot use, AI concern-vs-excitement), Priceline (trip
   planning time), Nielsen Norman Group (prompt specificity/CARE),
   Consumer Financial Protection Bureau (written-complaint response
   rates), Brown University/PLOS ONE (patient recall of appointment
   information), Federal Reserve (the $400 emergency-expense survey),
   Wharton ("cognitive surrender" research on trusting wrong AI answers),
   FBI Internet Crime Complaint Center (elder fraud, AI-enabled fraud),
   Amanda L. Smith and Barbara S. Chaparro / Human Factors journal (voice
   vs. typing input for older adults), PowerReviews (review-reading
   behavior before big purchases), CFPB again, eHealth (Medicare plan
   confusion), AARP/National Alliance for Caregiving (unpaid caregiver
   count), NASFAA/EAB (FAFSA completion difficulty), U.S. Census Bureau
   ACS (households speaking a non-English language), Gallup (pet owners
   skipping vet visits), H&R Block (W-4/withholding preparedness, a 2018
   survey — flagged honestly in-text as dated rather than presented as
   current), Birati and Tzemah-Shahar / JMIR (rushed family tech help
   backfiring), Caring.com/YouGov (will/estate-planning rates), AAA
   (repair-shop distrust), Empower (job-loss savings gap), Jobscan (job
   search volume). One MIT lead from an earlier session (chatbots giving
   less-accurate info to vulnerable users) was never independently
   confirmed and was **not used** — dropped rather than cited on a
   half-verified basis; if revisited, verify properly first per the
   sourcing standard, don't recall it from this note as if it were
   already checked.

## Register, distinct from the other two books

This is the warmest, least jargon-tolerant of the three books running so
far. `stop-guessing` assumes a PM vocabulary; `ai-employee` assumes a
general office-work reader; this one assumes no professional context at
all, a reader who might be retired, might be a parent, might have picked
this up because their kid told them to. Concretely:

- No business examples as the default case. Household, family, and
  personal-admin examples throughout.
- Sentences even shorter than `ai-employee`'s.
- Never assume the reader has used AI tools before, never talk down to
  them either. The tone is a knowledgeable friend, not a manual.
- Chapters that touch health or safety (6, 9, 15, 21, 23, 26, 29) are
  explicit every time, not just once: this helps you prepare and
  understand, it is not a diagnosis, it does not replace a professional.
- **Two recurring households, not one.** Linda (retired, married to Hal,
  grown kids, a granddaughter named Sofia, a sister Rose) carries the
  original chapters 1-3. Marisol (a hotel front-desk supervisor raising
  two kids, Diego and an older daughter, mostly on her own) was
  introduced in chapter 1 and appears in every chapter from 2 onward as
  the second worked example, the same "two personas generalize the
  method past one kind of life" device `one-person-business` used with
  Priya and Marcus. The two threads converge explicitly in chapter 33
  (an extended, multi-month case study following both households) and
  chapter 32 (teaching someone else).
- Fictional character names in `books/pipeline/qc.py`'s `ALLOW` list:
  marisol, diego, sofia (this book's cast, distinct from `ai-employee`'s
  priya/ravi/malik/etc. and `one-person-business`'s priya/marcus).

## Chapter map (final, 36 chapters, all written and edited)

| # | Title | Core idea |
| --- | --- | --- |
| 01 | You Don't Need to Be a Tech Person | Reframe: this isn't a fixed trait, it's exposure. Introduces both Linda and Marisol. |
| 02 | The One Sentence That Changes Everything | The core mechanic: who/what matters/what to avoid |
| 03 | The Trip You Haven't Had Time to Plan | Travel planning as the first real win |
| 04 | The Letter You've Been Avoiding | Complaints, tenant rights, tone calibration |
| 05 | Homework Help Without Doing the Homework | The tutor-not-answer-machine line |
| 06 | Walking Into the Doctor's Office Prepared | Health literacy, not-a-diagnosis, every time |
| 07 | Money Questions You're Embarrassed to Ask | Financial literacy, no judgment |
| 08 | When It Gets It Wrong | Cognitive surrender, the check-before-you-act habit |
| 09 | The Scams and the Sketchy Stuff | Voice-cloning, elder fraud, the family password |
| 10 | Choosing and Setting Up Your Tool | Which app, free vs. paid, privacy settings |
| 11 | Talking Instead of Typing | Voice input as the *better* option for many, not a fallback |
| 12 | Big Purchases Without the Overwhelm | Narrow-then-verify, applied to real money |
| 13 | The Words You Can't Find | Eulogies, toasts, cards: shape, not feeling |
| 14 | Cooking, Cleaning, and the Rest of the List | The undramatic daily grind |
| 15 | The Ordinary Emergency | Speed over verification, for real; the 911 line |
| 16 | When Someone You Love Refuses to Try | Why pushing backfires; research on rushed help |
| 17 | Looking for Work Again | Résumé translation, never invention |
| 18 | The Fine Print | Leases, contracts, timeshares; not legal advice |
| 19 | Small Tech Problems That Aren't Really About AI | Printers, Wi-Fi, crashing apps |
| 20 | Something Just for You | A hobby, not a chore; the patient-tutor use case |
| 21 | Making Sense of Medicare and Insurance Choices | Plan literacy, SHIP counselors, never the final decision |
| 22 | A Big Family Gathering | Timelines and shopping lists at scale |
| 23 | Caring for a Parent | Organizing scattered caregiving info, from a distance |
| 24 | The College and Financial Aid Maze | FAFSA orientation, comparing real offers |
| 25 | When Your Family Speaks More Than One Language | Translation as bridge, not crutch; official docs need a real interpreter |
| 26 | Pet Care Questions | Same not-a-diagnosis line, applied to a vet |
| 27 | Understanding Your Paycheck and Taxes | W-4, withholding, reading a pay stub |
| 28 | Staying in Touch Across the Generations | Slang, voice messages, video calls |
| 29 | Advance Planning and the Conversation Nobody Starts | Wills, directives; the hard conversation comes first |
| 30 | When the Car Needs Real Repairs | Reading an estimate, knowing when a price is fair |
| 31 | Planning for a Layoff or Income Gap | Bare-bones budgeting, real unemployment-office numbers |
| 32 | Teaching Someone Else | The book's actual argument: become the person they call |
| 33 | Two Families, One Season | Extended case study, Sept-Dec, both households, everything at once |
| 34 | The Time and Money It Actually Saves | Honest accounting, including what doesn't show up on any ledger |
| 35 | Questions You Still Have | FAQ/objections, argued honestly, including the ones without a tidy answer |
| 36 | The Toolkit | Every reusable prompt from every chapter, collected |

## Simplified Chinese edition — shipped

Following `one-person-business`'s precedent exactly: separate config at
`book-zh.yaml` (own slug `ai-for-the-rest-of-us-zh`, `lang: zh`), parallel
`manuscript-zh/` and `back-matter-zh/` directories mirroring the English
ones file-for-file, built via `python3 books/pipeline/build.py --book
books/ai-for-the-rest-of-us/book-zh.yaml`. **Not a KDP title** — same
reason as `one-person-business-zh`: KDP does not accept a Chinese-language
paperback, and does not list Simplified Chinese as a supported ebook
language. Targets Google Play Books, Apple Books, and direct/lead-gen
distribution.

**Final: 159 pages**, comfortably inside the `[140, 190]` target band
(close to the ~84%-of-English ratio `one-person-business-zh` set as
precedent: 185 English pages × 0.84 ≈ 155, actual 159). Interior PDF and
EPUB both build clean. `qc.py --release` clean apart from the `verified`
gate and the known CJK word-count false positive (`~3pp estimated`,
harmless — `Book.word_count()` splits on whitespace and CJK has none; the
real, trusted number is the built PDF's actual page count via `pdfinfo`,
which is what `--release` itself checks). `pdffonts` confirms all
Latin-face and CJK-face glyphs embedded and subsetted; the CJK subset is
labeled "NotoSerifCJKjp-Regular" in `pdffonts`' output, a cosmetic
Super-OTC naming artifact documented in `one-person-business-zh`'s own
notes, not a wrong-region-glyph bug — visually confirmed on every
inspected page that the rendered forms are genuinely Simplified (e.g. 会
not 會, 问题 not 問題). Interior PDF committed to
`proofs/ai-for-the-rest-of-us-zh.pdf`.

Translation done by parallel agents (6 agents, ~6 chapters each, matching
`one-person-business`'s five-agent precedent scaled to this book's larger
chapter count), sharing one fixed glossary handed to every agent verbatim:
Linda 琳达, Hal 哈尔, Rose 罗丝, Sofia 索菲亚, Marisol 玛丽索尔, Diego 迭戈,
Biscuit (the dog) 饼干; "Try this: X" → "动手试试：X"; "Where this goes
next" → "接下来"; chapter cross-references → "第N章" with standard
numerals; currency `$X` → `X美元`; the four bracket-marker keywords stay
literal English since `build.py`'s regex matches those exact strings
regardless of surrounding language; product names stay English.

**One real bug this pass caught and fixed, worth remembering for any
future translation batch on this repo**: the two agents covering chapters
1-6 and 7-12 used half-width (ASCII) `,.:;!?` throughout their Chinese
prose instead of full-width Chinese punctuation (，。：；！？), roughly
100-160 stray marks per chapter, 12 chapters affected. The other four
batches (13-36) got this right unprompted despite receiving the identical
instruction — not an instruction-clarity problem, an execution
inconsistency between agents given the same brief. Caught by a
programmatic scan (a CJK character immediately touching an ASCII
punctuation mark immediately touching another CJK character), not by
eye, and not by any single agent's own self-report — several agents in
the first wave claimed "Chinese punctuation used throughout" in their own
summaries while the artifact showed otherwise. **Don't trust a
translation agent's self-reported punctuation compliance; verify with a
script across the actual files.** Two follow-up agents fixed all 12
files, converting only prose punctuation and correctly leaving numeral
thousand-separators (`21,279`), decimal points, marker syntax
(`[KEY-INSIGHT:`, `||`), and English-citation-internal punctuation
untouched. Re-verified clean with the same scan afterward: zero
remaining instances across all 36 chapters.

A second, smaller issue: the translating agents wrote each chapter's own
Chinese H1 title independently rather than pulling the pre-set title from
`book-zh.yaml` (which had been drafted before any chapter existed, so it
was really just a placeholder guess), so 27 of 36 titles didn't match
between the two. Resolved by syncing `book-zh.yaml`'s titles to whatever
each chapter file actually used (the file, written with full chapter
context, is the better translation), via a targeted line-level text
replacement script — not a full YAML re-dump, which corrupted quoting on
a small ID field earlier in this same session (see the English
`book.yaml` history) and is worth avoiding on principle for any file this
particular pipeline hand-parses expecting specific quoting.

## Remaining author actions (English and Chinese both)

1. **Read the whole book (both editions, once the Chinese one ships) and
   set `verified: true`** in `book.yaml` and, separately, `book-zh.yaml`
   once every claim and every anecdote is one you can personally defend.
   No one else may set this; it's the author's signature. The two flags
   are independent — different artifacts, read separately.
2. Byline and About the Author are already set (`author: "James Liu"`,
   real bio in `back-matter/about_the_author.md`) and were left untouched
   throughout this pass per instruction.
3. **Commission a cover** for whichever edition(s) ship — out of this
   pipeline's scope, needs the final locked page count (185pp English;
   Chinese count pending).
4. **KDP dashboard AI-disclosure questionnaire** at upload, English
   edition only: AI-assisted, not AI-generated (author direction, outline,
   and the required sign-off review). The Chinese edition doesn't go
   through KDP at all — see above for where it does go.
5. **Pick actual distribution channels for the Chinese edition** (Google
   Play Books, Apple Books, direct/lead-gen) and handle whatever
   author-identity or tax steps each separately requires — not covered by
   this repo's pipeline.

## Things to hold onto continuing this

- `[PULLQUOTE: ...]` boxes drift toward paraphrase easily during drafting,
  a paraphrase often just reads better in isolation than a true verbatim
  lift does. Check this explicitly, programmatically, after any future
  editorial pass on this book — don't assume a box written correctly the
  first time stays that way through later edits to the surrounding
  paragraph, and don't trust a visual skim to catch it (this pass's
  first skim missed several; a substring-match script caught all of
  them).
- Before any future renumbering, grep for chapter cross-references in
  both word form ("chapter thirty-one") and any `(Chapter N)` parenthetical
  form (the toolkit chapter, 36, uses the latter) across the whole
  `manuscript/` directory, fix every hit, then rebuild and spot-check.
  This pass went through several rounds of inserting chapters mid-book
  and it is very easy to leave a stale cross-reference or, worse, to
  break one with a careless regex (a `\b` word-boundary substitution
  mid-pass once turned "chapter thirty-one" into "chapter thirty-two-one"
  — caught by a full validation script, not by eye).
- Every `[KEY-INSIGHT: ...]` must be re-verified against a live search at
  any future editorial pass, not just at first-draft time — sources
  drift, get corrected, or turn out to have been misread the first time.
  `one-person-business`'s own editorial pass found 9 of 20 existing
  citations had drifted; treat that as the base rate to expect here too,
  not an exception.
