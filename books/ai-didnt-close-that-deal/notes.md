# Status and chapter map

Not part of the build. Working notes for continuing across sessions, same
pattern as the other books.

## Status

- Chapters 01-02 written, built, rendered pages visually inspected, `qc.py`
  clean beyond the standard gates.
- Chapter roster expanded from 10 to 12 chapters to give the `[180, 240]`
  target (raised from `[120, 170]`) a realistic path through substance:
  chapter 10 "Objections and Edge Cases" (FAQ format, new) and chapter 12
  "The Scripts and Templates" (worksheet/reference chapter, new) were
  added, and the original closing chapter "Selling in a Room Full of
  Robots" moved from slot 10 to slot 11 so the book still closes on its
  thesis before the templates appendix, the same shape as
  one-person-business's ch14-closes/ch15-templates pattern. `book.yaml` is
  the source of truth for the current 12-chapter list.
- Chapters 03-12 in progress this session (drafting from scratch).
- Chapter 03 "The Research Nobody Does Anymore" drafted (~5,630 words).
  Theo and Naomi introduced here as specified (mid-market vs. enterprise).
  KEY-INSIGHT uses Gartner's own June 25, 2025 press release ("Gartner
  Sales Survey Finds 61% of B2B Buyers Prefer a Rep-Free Buying
  Experience"), citing the 73%-of-buyers-avoid-irrelevant-outreach figure
  from the same underlying Aug-Sep 2024 survey of 632 B2B buyers; verified
  live via WebSearch this session, not fetchable directly (gartner.com and
  every secondary mirror tried were blocked by the network egress proxy),
  so treat as reasonably but not fully independently confirmed and give it
  one more check before release if a fetchable source becomes available.
  Not yet built, rendered, or QC'd.

## Story bible (characters and terms established in ch01-02, hold these fixed)

- **Diane**: the recurring sales-leader persona, first name only (matches
  ch01-02's own convention of not giving her a surname). VP/Director-level,
  runs Monday pipeline reviews, has an ops lead she consults (unnamed
  role, not a named character). Team's reply rate fell from ~7% to ~2%
  over 18 months before ch01 despite adopting an AI writing tool a year
  before ch01 opens. Company is deliberately unnamed ("her company", "her
  team") so it reads as any B2B sales org, not a case study of one firm.
- **Theo**: individual-contributor AE on Diane's team, introduced starting
  ch03, carries the "how do I actually do this" throughline for the craft
  chapters (03-05) and the coaching chapter (06). Mid-market segment.
- **Naomi**: second AE on Diane's team, the contrast worked example
  (enterprise/regulated-industry segment, longer sales cycle, more
  stakeholders per deal) alongside Theo's mid-market motion, the same
  "two worked examples generalize the point past one kind of seller" role
  Marcus plays opposite Priya in one-person-business. Introduced no later
  than ch03 so both are available for every craft/coaching chapter after.
- **Owen**: buyer-side persona for ch09 specifically (a RevOps/marketing
  ops leader on the *receiving* end of outreach), giving the reader the
  view from the other side of the inbox. Not a running character outside
  ch09.
- Established terms, keep exact: "spray-and-pray", "reply rate",
  "deliverability", "complaint rate" (bulk-sender ceiling from ch02),
  "cadence"/"sequence" (ch05's subject), "ICP", "pipeline review", "quota".
- House section skeleton, established by ch01-02, keep for every chapter:
  concrete scene opener -> numbered/`##` sections building the argument ->
  "What this chapter will not do" section -> `[TAKEAWAYS]` -> "Where this
  goes next" closing paragraph. One `[KEY-INSIGHT: ...]` and one
  `[PULLQUOTE: ...]` (verbatim from the chapter's own body) per chapter,
  same discipline as every other book in this repo.
- Register: sales-leader peer register (see below), never em dashes
  (`style.em_dash: avoid`), US spelling, no LLM tells.

## Register

Sales-leader peer register: assumes fluency in pipeline, cadence, SDR,
reply rate, spray-and-pray without re-explaining every time. Closer to
resume-arms-race's register than ai-for-the-rest-of-us's. This book's
core argument mirrors resume-arms-race's structurally (a signal that used
to cost effort became free, so it stopped signaling anything), which is
fine, they're written for different readers and neither references the
other, but don't let the prose become a find-and-replace of one chapter
into the other. The sales version needs its own texture: quota pressure,
manager-rep dynamics, buyer-side trust erosion specifically.

## Chapter map

| Chapter | Core idea |
| --- | --- |
| 01 The Inbox Nobody Reads Anymore | Naming the problem: reply rates cratering as AI made volume free |
| 02 Why Volume Stopped Working | The mechanism, why sending more is the instinct that caused this |
| 03 The Research Nobody Does Anymore | Real research vs fake {{firstName}} personalization |
| 04 Writing Like You Actually Read Their Website | Craft chapter: genuinely specific outreach |
| 05 The Follow-Up That Doesn't Feel Like a Sequence | Cadence without feeling roboticized |
| 06 Coaching a Team Off Spray-and-Pray | Management chapter: retraining a team, not just an individual fix |
| 07 When AI Actually Helps a Rep | Legitimate uses: call prep, account research, objection-handling practice |
| 08 The Metrics That Lie to Sales Leaders | Vanity metrics (send volume, open rate) vs metrics that predict revenue |
| 09 Buyers Can Tell, and What That Costs You | Trust erosion, brand cost of being another AI-spam sender |
| 10 Objections and Edge Cases | FAQ format: "my competitors send more and win," ABM at scale, regulated industries, honesty about time cost |
| 11 Selling in a Room Full of Robots | Closing: the honest, durable differentiator |
| 12 The Scripts and Templates | Reference chapter: research checklist, cadence templates, coaching 1:1 script, metrics dashboard, collected last like one-person-business's ch15 |

## Things to hold onto while writing the rest

- Chapter 06 is a manager's chapter specifically, not an individual
  contributor's. The audience for this whole book is sales leaders, so
  every chapter should keep at least one eye on "what does the leader do
  differently," not just "what should a rep do."
- `[KEY-INSIGHT: ...]` for chapter 01 uses cold-email reply rate decline
  data; sourcing for this specific niche is noisier than the other books
  (mostly SaaS-vendor-published benchmark reports, not peer-reviewed
  research), so the citation is deliberately hedged rather than
  over-precise. Keep that same caution for any further sales-metrics
  citations in later chapters.
