# Status and chapter map

Not part of the build. Working notes for continuing across sessions, same
pattern as the other books.

## Status: manuscript complete, editorial pass done, both editions shipped as proofs. English manuscript is print-ready except the author's own read-through.

All 12 chapters are written, edited, citation-re-verified, and built.
**English: 181 pages, 12 chapters, ~62,000 words.** `target_pages` was
raised from the original `[120, 170]` to `[180, 240]` at the start of this
pass; the book lands just inside the floor of that band. **Simplified
Chinese: 141 pages**, full translation of all 12 chapters plus About the
Author; see "Simplified Chinese edition" below.

Both interior PDFs are committed to `proofs/` (`ai-didnt-close-that-deal.pdf`,
`ai-didnt-close-that-deal-zh.pdf`), an author-sanctioned exception to the
normal never-commit-builds rule, same as every other title in this repo.
Re-run `python3 books/pipeline/build.py --book ai-didnt-close-that-deal`
(and the `--book books/ai-didnt-close-that-deal/book-zh.yaml` equivalent)
and re-copy to `proofs/` any time either manuscript changes; these files
go stale otherwise.

## What this pass did

1. **Expanded the chapter roster from 10 to 12** to give the raised
   `[180, 240]` target a realistic path through substance rather than
   padding: chapter 10 "Objections and Edge Cases" (FAQ format, new) and
   chapter 12 "The Scripts and Templates" (worksheet/reference chapter,
   new) were added, and the original closing chapter "Selling in a Room
   Full of Robots" moved from slot 10 to slot 11 so the book still closes
   on its thesis before the templates appendix, the same shape as
   one-person-business's ch14-closes/ch15-templates pattern.
2. **Wrote chapters 03-12 from scratch** (chapters 01-02 already existed).
   Each chapter: a concrete cold-open scene, two worked examples (Theo,
   mid-market; Naomi, enterprise), one `[KEY-INSIGHT: ...]` verified live
   against real sources at drafting time, one `[PULLQUOTE: ...]` pulled
   verbatim from the chapter's own body, a "what this chapter will not
   do" section naming the limits of the advice, a `[TAKEAWAYS]` box, and
   a practical reader-facing exercise. Drafted by parallel agents against
   a shared story bible (character names, established terms, house
   section skeleton) to keep voice and continuity consistent without
   requiring full serialization.
3. **Structural and continuity pass** across all 12 chapters: found and
   fixed a stakeholder-name collision (chapter 4 had named an enterprise
   contact "Owen," colliding with chapter 9's dedicated buyer-side
   persona of the same name; renamed to "Grant Castellano"), replaced
   chapter 12's fabricated "Bellwood Systems"/"Priya" worked examples
   with the real Bellcrest Supply (ch3) and Corrigan Industrial Supply
   (ch4) accounts since ch12 explicitly presents itself as collecting
   material that already appeared in the book, and fixed a real
   inconsistency between chapter 3's stated research-time range
   (12-25 minutes depending on stakeholder count) and chapter 12's
   checklist, which had claimed chapter 3 "converged on" a hard 15-minute
   number it never actually states as a single fixed rule.
4. **Verbatim pull-quote audit, all 12 chapters.** 5 of 12 (ch1, ch2, ch4,
   ch6, ch12) had PULLQUOTE boxes that were close paraphrases rather than
   character-for-character quotes from their own body text, the same
   failure mode one-person-business's editorial pass found in 11 of 15
   chapters. All fixed to true verbatim quotes.
5. **Every `[KEY-INSIGHT: ...]` citation independently re-verified**
   against live sources (not recalled from training data), same
   discipline as one-person-business's pass. Of 11 citations, 7 confirmed
   accurate as written (ch2 Google/Yahoo bulk sender rules, ch3 Gartner
   73%, ch6 CSO Insights coaching stats, ch7 Salesforce State of Sales,
   ch8 Apple Mail Privacy Protection/Litmus, ch9 TrustRadius, ch11 Gartner
   69%). 4 needed correction:
   - **ch01**: vague "aggregated cold-email benchmark reporting" upgraded
     to named reports (Instantly's 2026 Cold Email Benchmark Report,
     Woodpecker, corroborated by Cleanlist and Belkins) with corrected
     figures (reply rates ~8% in 2019 to low-3% now; volume 3-5x 2023
     levels).
   - **ch04**: Gartner personalization-regret citation used the wrong
     multiplier ("more than three times" vs. the real 3.2x) and
     attributed the wrong causal mechanism (Gartner's own explanation is
     task-switching cognitive load at journey transition points, not
     "read as intrusive").
   - **ch05**: "wide margin" overclaim on first-follow-up vs. opener
     reply rates; the real sources show the follow-up matches or
     slightly exceeds the opener, not beats it decisively.
   - **ch10**: SDR ramp-time figures (3.9 months, a 2.5-6.2 month range)
     traced to uncited SEO content-farm pages, not the Bridge Group
     report they were attributed to. Replaced with the report's actual
     2025 findings (3.1-3.2 month ramp, 57% of SDRs hit quota, 41% for
     software specifically).
6. **Chapters 01-02 expansion.** Both were written before `target_pages`
   moved to `[180, 240]` and were proportionally thin next to chapters
   3-12 (~5,700 words average): ch1 at 1,447 words, ch2 at 1,084. Both
   got real material that was genuinely missing, not padding: ch1 gained
   a concrete grounding scene (Diane mystery-shopping her own inbox) and
   a new section naming the gap opening between adapting and
   non-adapting teams; ch2 gained a worked numeric example of the
   complaint-rate math, a practical section on where a leader actually
   finds their domain's complaint-rate number (Google Postmaster Tools,
   Yahoo/AOL feedback loops), a domain warm-up note, and honest scoping
   of what does and doesn't transfer to other channels. This closed the
   page-count gap to 181pp without inflating either chapter artificially.
7. **Full rebuild and visual inspection**, English and Chinese.
   `qc.py --release` clean apart from the `verified` gate on both
   editions (the Chinese edition also carries a known false-positive
   word-count WARN, explained below). All fonts embedded (`pdffonts`
   confirms TeX Gyre Schola Regular/Bold/Italic + IBM Plex Mono on the
   English PDF, the same plus Noto Serif CJK SC on the Chinese one).
   Spot-checked front matter, TOC, every chapter opener (all recto),
   KEY-INSIGHT/PULLQUOTE/TAKEAWAYS boxes, dialogue formatting, and
   reference tables across ~30 sample pages on each edition.

## Simplified Chinese edition

Shipped as `proofs/ai-didnt-close-that-deal-zh.pdf`, 141 pages, full
translation of all 12 chapters plus About the Author. Source of truth is
`books/ai-didnt-close-that-deal/book-zh.yaml` (own slug
`ai-didnt-close-that-deal-zh`, `lang: zh`), so
`python3 books/pipeline/build.py --book books/ai-didnt-close-that-deal/book-zh.yaml`
builds this edition without touching the English path. Manuscript lives
in `manuscript-zh/01-...md` through `12-...md` and
`back-matter-zh/about_the_author.md`, mirroring the English filenames.

**Not a KDP title**, same as one-person-business-zh: Amazon KDP does not
accept a Chinese-language paperback at all, and does not list Simplified
Chinese as a supported KDP ebook language (only Traditional Chinese, in
beta, ebook-only). This edition targets Google Play Books, Apple Books,
and direct/lead-gen distribution instead, none of which this repo's
pipeline touches past producing the interior PDF.

**Build dependencies**: `apt-get install -y fonts-noto-cjk
texlive-lang-chinese`, same as documented in `books/theme/kdp-book.cls`
and one-person-business's notes. Both were installed and used in this
session; a fresh container needs the same install before building this
edition, or `xelatex` fails on `File 'xeCJK.sty' not found`.

**Translation methodology.** All 12 chapters translated by four parallel
agents (three chapters each), each given an identical fixed glossary
(character transliterations, fixed terms, structural/markup rules) so
consistency didn't depend on cross-agent coordination. Key decisions:
- Character names transliterated: Diane -> 黛安, Theo -> 西奥, Naomi ->
  娜奥米, Owen -> 欧文 (ch9's buyer persona), Elena -> 埃琳娜 and Grant ->
  格兰特 (ch4's two enterprise stakeholders), Marcus -> 马库斯 (ch4's
  one-off prospect). The real author's name, James Liu, stays in Latin
  script throughout. Fictional company names (Bellcrest Supply, Corrigan
  Industrial Supply, Larkspur Health, etc.) were kept in English/Latin
  script rather than transliterated, matching standard Chinese business-
  writing convention for a foreign company name; only person names were
  transliterated.
- Fixed terms: "spray-and-pray" -> 广撒网, "reply rate" -> 回复率,
  "deliverability" -> 送达率, "complaint rate" -> 投诉率, "cadence" ->
  触达节奏, "sequence" -> 邮件序列, "pipeline review" -> 管道复盘会,
  "quota" -> 业绩配额, "merge field" -> 合并字段, "signal" -> 信号,
  "template" -> 模板. Abbreviations (ICP, SDR, AE, ACV, RevOps, ABM)
  glossed in Chinese on first use per chapter, then left bare.
- `[KEY-INSIGHT: ...]`/`[PULLQUOTE: ...]`/`[TAKEAWAYS]`/`[/TAKEAWAYS]`
  marker keywords stay in English exactly as written (the build
  pipeline's regex matches those literal English keywords regardless of
  book language); only the human-readable content inside them is
  Chinese. Every `[PULLQUOTE: ...]` was verified to be an exact
  character-for-character substring of its own chapter's translated
  body, same verbatim discipline as the English pass.
- `[KEY-INSIGHT: ...]` source lines keep the actual source title,
  publisher, and study name in original English/Latin form with a brief
  Chinese gloss added in parentheses, so a reader can still find and
  verify the actual source, e.g. `Source: Gartner《Gartner Sales Survey
  Finds 61% of B2B Buyers Prefer a Rep-Free Buying Experience》...`.
  Currency converted from `$X` to "X美元" throughout.
- A worked email (chapter 4, Theo to Marcus) and a scripted manager 1:1
  dialogue (chapter 6, Diane and Theo; reused in chapter 12) were
  translated as natural spoken/written Chinese business register, not
  literal transcriptions, since both are meant to model real usage for a
  Chinese-speaking reader.
- **One real punctuation bug caught after translation, systemically**:
  the parallel translation agents (and the English-to-Chinese process in
  general) defaulted to straight ASCII double quotes (`"..."`) around
  quoted Chinese phrases in 6 of 12 chapters (over 100 instances total),
  rather than proper Chinese quotation marks. Swept the whole
  `manuscript-zh/` directory with a script that converted every
  CJK-content `"..."` span to `「...」` (with nested `'...'` converted to
  `『...』`), while leaving quotes wrapping genuine English source/report
  titles untouched. Re-verified the pullquote-verbatim check afterward
  (the conversion is deterministic per span, so both the box and body
  occurrence of each pullquote transformed identically).

**Visual QA.** Full rebuild, `qc.py --release` clean apart from the
`verified` gate (the estimated-page-count WARN is the same known false
positive one-person-business-zh already documented:
`Book.word_count()`/`estimated_pages()` splits on whitespace, which
undercounts Chinese text severely since CJK has no spaces between words;
the real, accurate check is the built PDF's actual page count via
`pdfinfo`, which passed at 141 pages). All fonts embedded per `pdffonts`.
`pdffonts` labels the embedded CJK subset "NotoSerifCJKjp-Regular" despite
`\setCJKmainfont{Noto Serif CJK SC}` being used correctly; this is the
same cosmetic naming artifact one-person-business-zh's notes already
explain (Noto's CJK "Super OTC" files store all five regional variants'
internal PostScript name), not evidence of the wrong regional glyph set.
Spot-checked front matter, TOC, multiple chapter openers (all recto), the
KEY INSIGHT (关键洞察) and TAKEAWAYS (要点总结) boxes, quotation-mark
rendering after the punctuation fix, dialogue, and reference tables.
Every rendered page checked showed standard Simplified Chinese glyph
forms.

`target_pages` initially guessed at `[140, 210]` before a first build
existed (scaled from the English `[180, 240]`); brought down to
`[120, 160]` once the real 141-page count landed, same honesty discipline
as one-person-business-zh's own target-pages correction. Gutter stayed
0.375in throughout (both the target midpoint and the real count fall in
the 24-150pp band), so no gutter mismatch to chase.

## Register

Sales-leader peer register: assumes fluency in pipeline, cadence, SDR,
reply rate, spray-and-pray without re-explaining every time. Closer to
resume-arms-race's register than ai-for-the-rest-of-us's. This book's
core argument mirrors resume-arms-race's structurally (a signal that used
to cost effort became free, so it stopped signaling anything), which is
fine, they're written for different readers and neither references the
other; the prose was kept from becoming a find-and-replace of one chapter
into the other by giving the sales version its own texture throughout:
quota pressure, manager-rep dynamics, buyer-side trust erosion.

## Chapter map (final, 12 chapters, all written/edited)

| Chapter | Core idea |
| --- | --- |
| 01 The Inbox Nobody Reads Anymore | Naming the problem: reply rates cratering as AI made volume free |
| 02 Why Volume Stopped Working | The mechanism: the deliverability/complaint-rate ceiling, why sending more is the instinct that caused this |
| 03 The Research Nobody Does Anymore | Real research vs. fake merge-field personalization; introduces Theo and Naomi |
| 04 Writing Like You Actually Read Their Website | Craft chapter: genuinely specific outreach, before/after email rewrites |
| 05 The Follow-Up That Doesn't Feel Like a Sequence | Cadence without feeling roboticized |
| 06 Coaching a Team Off Spray-and-Pray | Management chapter: retraining a team without torching the quarter |
| 07 When AI Actually Helps a Rep | Legitimate uses: call prep, account research synthesis, objection-handling rehearsal |
| 08 The Metrics That Lie to Sales Leaders | Vanity metrics (send volume, open rate) vs. metrics that predict revenue |
| 09 Buyers Can Tell, and What That Costs You | Trust erosion, brand cost, told from a buyer's (Owen's) point of view |
| 10 Objections and Edge Cases | FAQ format: the honest pushback this argument gets in every room |
| 11 Selling in a Room Full of Robots | Closing chapter: circles back to Diane's ch1 opening scene, the durable differentiator |
| 12 The Scripts and Templates | Reference chapter: every checklist/script/worksheet from the book, collected last |

## Remaining author actions

1. **Read the whole book (English and, if the Chinese edition is going
   out, the Chinese one too) and set `verified: true` in both
   `book.yaml` and `book-zh.yaml`** once every claim is one the author
   can personally defend. No one else may set this flag; it is the
   author's signature and the fact that keeps the AI-assisted
   declaration true. The two `verified` flags are independent.
2. **Commission a cover** for whichever edition(s) actually ship. This
   pipeline only produces interiors; a cover needs a separate file, and
   spine width depends on the final locked page count (181pp English,
   141pp Chinese), which will move again if the author's own read-through
   edits the manuscript.
3. **Answer KDP's dashboard AI-disclosure questionnaire** at upload time
   for the English edition (AI-assisted, not AI-generated; see
   `books/CLAUDE.md` §1). The Chinese edition doesn't go through this
   step at all, since it isn't going to KDP.
4. **Pick actual distribution channels for the Chinese edition** (Google
   Play Books, Apple Books, and/or direct/lead-gen sale) and go through
   whatever author-identity or tax steps each one separately requires;
   none of that is covered by this repo's pipeline.
5. **Decide on the byline/bio content.** `author: "James Liu"` and the
   bio in `back-matter/about_the_author.md` (and its Chinese translation
   in `back-matter-zh/`) were already set per the task's instruction not
   to change them; no action needed unless the author wants to revise it.

## Things to hold onto continuing this

- Every `[KEY-INSIGHT: ...]` must be verified against a live search, not
  just at writing time but again at any future editorial pass. This pass
  found 4 of 11 existing citations had a wrong multiplier, an
  unsupported causal claim, an overclaim, or figures traced to an
  uncited secondary source. Don't assume a citation verified once stays
  correct through later edits.
- `[PULLQUOTE: ...]` boxes drift toward paraphrase easily during
  drafting, in both languages, because a paraphrase often reads better
  in isolation than an exact quote does. Check verbatim compliance
  explicitly after any future editorial pass. A simple Python script
  (extract `[PULLQUOTE: ...]` content with regex, check it's a substring
  of the rest of the file) catches this fast; see this session's
  approach if reimplementing.
- Before any future renumbering, grep for word-form chapter references
  ("chapter one" through "chapter twelve") and "previous N chapters" /
  "the last N chapters" style counts across the whole `manuscript/`
  directory first, fix every hit, then rebuild and spot-check. This
  session's numbering (after inserting two new chapters and moving the
  closer) checked out clean across all 12 chapters on the first pass,
  but that was verified explicitly with a grep sweep, not assumed.
- Watch for the same-line-two-`$`-amounts LaTeX math-mode bug documented
  in `books/CLAUDE.md` §7 and one-person-business's notes: Pandoc's
  markdown reader has `tex_math_dollars` on by default, so two dollar
  figures on the same source line (common in a table row) can pair up as
  literal math-mode delimiters and mangle the text between them. Escape
  with a backslash (`\$34,000`) or avoid the second `$` on the same line
  entirely. Found and fixed two instances in ch8 and ch12 this pass.
- Character names are shared across the whole book and now across both
  language editions; if a future pass adds a new named character, check
  it doesn't collide with an existing one (this pass caught and fixed
  one such collision: ch4 had reused "Owen," which ch9 already owns as a
  distinct, unrelated persona) and add it to the glossary in this file
  and to any future zh-translation session's brief.
