# Quality bar: from a good course to a referrable one

> The existing system already clears "competent". This document is the gap
> between competent and the course a learner tells a colleague about unprompted.
> Everything here is an upgrade to what exists, not a rewrite.

The measurable definition of "top course level" used throughout:

| Signal | Target | Why this number |
| --- | --- | --- |
| Rating | 4.7+ sustained | 4.5 is table stakes; referrals start above 4.6 |
| Completion rate | > 40% | Udemy median is ~15%; completion is a ranking input |
| Review velocity | 10 in 30 days, 50 in 6 months | Social proof threshold, then compounding |
| Q&A response | < 24h | Direct ranking input |
| Referrability test | A learner can retell the core idea in one sentence at work, and look smart doing it | This is what "tell a friend" actually is |

The last row is the design target. Nobody refers a course because it was
polished. They refer it because it gave them a sentence, a picture, or a story
they got to use in a meeting.

---

## 1. Honest review of the current state

State at the time of writing: **all 102 lecture files are drafted** across
Sections 0 to 11. Section 0 is built and visually verified; the rest is
unrendered, unverified, and unsigned. Sibling system `books/` has seven KDP
titles in flight (reviewed in `docs/05-kdp-playbook.md`).

**What is already top-decile and must not be diluted:**

- The positioning ("distributions, not functions") is a real spine, not a topic
  list. Almost no competing course has one.
- Narration craft rules (ear-first, name the cost, no tells, no em dashes) are
  enforced by code, and the drafted lectures hold the voice.
- The compliance engineering (sign-off gate, INSTRUCTOR-INPUT, disclosure) is
  ahead of virtually every AI-assisted course on the platform.
- Deterministic figures. No competing course can say "no AI images anywhere".
- Ticket #4471 already threads the course as a deliberate callback (0.4, 1.2,
  2.4, 4.1, 5.5). The instinct was right; §2 finishes the job.

**The gaps between this and a course people refer:**

| # | Gap | Cost if unfixed |
| --- | --- | --- |
| 1 | 98 of 102 lectures have never been rendered or read aloud; the callback thread is unaudited | Drafted is not done; continuity or visual bugs ship silently |
| 2 | Instructor presence is budgeted at intros and outros only | The single Udemy policy risk left, and the top complaint driver ("no human here") |
| 3 | TTS has voice settings but no delivery direction | Uniform pacing across 10 hours reads as robotic regardless of voice quality |
| 4 | No engineered referrability: concepts are good but unnamed, artifacts are functional but not shareable | Word of mouth left to chance |
| 5 | Visual density and rhythm are unchecked by QC | Text-heavy or monotone lectures pass the gate |

---

## 2. Upgrade 1: finish the callback thread (biggest single lever)

Top nonfiction runs one story through the whole thing. The drafted course
already half-does this: **Ticket #4471** recurs deliberately in at least five
lectures. Two moves complete it:

1. **Ledger it.** Every fact and number the running case uses now lives in
   `courses/ai-for-pms/story-bible.yaml`. During the verification pass,
   confirm each existing callback against the ledger, append new ones as
   found, and treat any drifted value as a continuity bug. Number drift
   between distant lectures is exactly the failure long-form generated
   writing is prone to; the ledger removes it by making state explicit
   instead of remembered.
2. **Strengthen the weak stretches.** Sections 6 to 9 carry the strongest
   material (reliability math, the margin trap, incident response) but the
   thinnest connection to the running case. Where a lecture already uses a
   generic example, swapping it for the summariser is a narration-only edit:
   cheap during verification, expensive after TTS is rendered. Do it in the
   same pass as sign-off, not as a separate project.

**Not worth doing now:** a fully named serial (a company with a name, a cast,
per-section beats). That is the strongest version of this device, but
retrofitting it across 102 drafted lectures re-opens every file for marginal
gain over the callback thread. Reserve the named serial for course #2, where
it can be designed in from the outline. The referral sentence the callback
thread already earns: "the same support ticket follows you through the whole
course, and by the end you can measure, price, and de-risk the feature that
mangled it."

---

## 3. Upgrade 2: cold opens

Every section's first TTS lecture opens with 30 to 45 seconds of story or
tension **before** any framework content. Not "in this section we will".
The eyebrow-heading-agenda opener is the strongest structural tell of
generated courseware, because a human instructor with something to say never
starts with the agenda.

### Opener pattern library

Rotate deliberately. No two adjacent lectures use the same pattern.

| Pattern | Example first line |
| --- | --- |
| Incident replay | "At 9:14 on a Tuesday, Fernhill's support queue started filling with a complaint nobody had seen before." |
| Wrong belief | "Most PMs believe a bigger test set means a better eval. The opposite is usually true, and here is why." |
| Artifact on screen | "This is a real PRD. It passed review. Every acceptance criterion on it is untestable." |
| The question you'll be asked | "Someone in a meeting is going to ask you: why can't we just fine-tune it? Here is the answer that holds up." |
| Number that shouldn't be possible | "Ninety-five percent reliable per step. Sixty percent reliable overall. Both of those are the same system." |
| Before and after | "Here is the argument before the eval existed. Forty minutes, no decision. Here it is after. Four minutes." |

Lectures 0.3 and 0.4 already do this instinctively. Since Sections 1 to 11
are drafted, this is now an audit rule: check each lecture's opener during
verification, and where one opens on the agenda, rewrite just the first
narration block. Openers are the cheapest high-leverage edit available in a
drafted course, because they decide whether the lecture gets watched at all.

---

## 4. Upgrade 3: instructor presence (policy moat and quality lever at once)

Udemy's policy language is about *presence*, and reviews of AI-assisted courses
fail on *presence*. The current budget (human voice on intros, outros, capstone)
is the minimum. Raise it to:

1. **Face on camera, webcam quality is fine:** promo video, lecture 0.1, and
   every section intro (60 to 90 seconds each). Batch-record all twelve intros
   in one sitting with one setup. Authenticity beats polish; a slightly rough
   webcam intro reads as "a real person made this", which is precisely the
   signal Udemy and learners are checking for.
2. **One war story per section**, delivered via `[INSTRUCTOR-INPUT]`. These are
   currently unbounded requests, which makes them easy to defer forever. Fix
   with a story bank: a one-page worksheet the instructor fills once, mining
   their history against ten prompts ("a launch that got rolled back", "a
   number a CFO challenged", "a demo that fooled you", "an estimate you got
   badly wrong", "the meeting where you had no answer"). Each story then slots
   into the section it teaches best. Fifteen minutes of instructor time per
   section is the cheapest quality-per-minute purchase available anywhere in
   this system.
3. **Real artifacts on screen.** One redacted screenshot of the instructor's
   actual work (a real PRD, a real dashboard, a real postmortem) per course
   third. This is the "an expert was here" watermark nothing else fakes.

Do not soften the QC gate to make any of this optional. It is the moat.

---

## 5. Upgrade 4: delivery direction for TTS

The scripts are good. The remaining robotic-delivery risk is *uniformity*:
ten hours at the same pace, same energy, same sentence rhythm. Three fixes,
in increasing order of pipeline work:

1. **Rhythm variance is an authoring rule, checked by QC** (see §7). Within any
   narration block, sentence lengths should swing. A block whose sentences are
   all 12 to 18 words reads as generated even when each sentence is fine. The
   0.4 reveal ("Two, three, three, four, five.") is the model: a five-word
   sentence after three long ones lands like a drum hit.
2. **A pause layer in the source format.** Support `[pause]` (roughly 700ms)
   inline in narration, stripped from captions and cache keys, rendered as
   silence by `tts.py` (either via provider SSML/tags where supported, or by
   splitting synthesis at the marker and concatenating with a silence gap).
   House move: a pause *before* the reveal number, not after.
   "The pass rate was [pause] sixty-eight percent."
3. **Per-slide delivery hints.** An optional `delivery:` directive
   (`deadpan`, `warm`, `urgent`, `slow`) mapped to provider settings per
   request (eleven_v3 supports style direction). Use sparingly: the incident
   beat in Section 8 wants `urgent`; definitions want `slow`.

Also decided, to save relitigating: **no music beds.** They add licensing
surface, fight the narration for attention, and their absence is consistent
with the teaching-page aesthetic. Keep the 300ms head/tail silence padding and
LUFS normalisation as the whole sound design.

---

## 6. Upgrade 5: visual density and variation

The pipeline can produce figures no competitor can match, but QC currently
allows an all-bullets lecture through. Codify the floor:

- Every TTS lecture over 4 minutes carries at least one figure, diagram, table
  or metrics band. (Definition of done already says this; make it a check.)
- No lecture is more than half `bullets` slides.
- No single slide holds more than ~90 seconds of narration. A static frame
  beyond that is the "video is really a podcast" failure learners refund.
  Split the slide or add a build.
- `pipeline/figures.py` still has only three kinds (dotplot, histogram,
  sampling). Sections 4 and 9 teach dashboards, pass-rate trends and rater
  agreement; add `trend` (pass rate over prompt versions, version labels on
  the x axis) and `grid` (agreement / confusion matrix with counts in cells)
  during their verification pass, and upgrade the lectures that currently
  describe these pictures in words to actually show them. Validate any new
  hue with the dataviz palette validator; the no-generative-images rule stays
  absolute.

---

## 7. QC additions

Concrete spec so a later session can implement without re-deriving. All are
`check_lectures` additions unless noted.

| Check | Severity | Threshold | Rationale |
| --- | --- | --- | --- |
| Sentence rhythm | WARN | stdev of sentence word-counts < 4 within a lecture's narration | Uniform rhythm is the strongest audible tell |
| Static frame | WARN | any slide's narration > 90s at configured wpm | Frame fatigue; "podcast with slides" complaints |
| Figure floor | WARN | TTS lecture > 4 min with no figure/diagram/table/metrics slide | Text-heavy drift under production pressure |
| Bullets share | WARN | > 50% of a lecture's slides are `bullets` | Same |
| Opener diversity | WARN | 3 consecutive lectures share the same opening slide layout | Agenda-opener monotony |
| Direct address | WARN | < 1 "you/your" per 100 narration words | Lecture drifting into essay voice |
| Question presence | WARN | zero "?" in narration of a lecture > 4 min | Monologue drift; questions are how a teacher holds attention |
| Story continuity | WARN | a number present in `story-bible.yaml` appears in narration with a different value | Serial integrity (simple literal match on the bible's `numbers` list) |

Severity note: these are WARNs, not FAILs, because each has legitimate
exceptions (a section recap has no figure; a definition lecture may be
question-free). The definition of done already requires zero WARNs, so they
still bite.

---

## 8. The referrability kit

Referral is an engineered outcome: give learners things that are easy to carry
into a meeting with their name attached.

1. **Name the concepts.** The course already coins good phrases and then
   fails to claim them. Maintain a lexicon in `course.yaml` and use each name
   consistently on slides, in recaps, and in artifacts. Current harvest:
   - *The margin trap* (7.5)
   - *Fix the ruler before you measure the model* (0.4)
   - *A hope with a checkbox next to it* (0.3, for untestable criteria)
   - *Blast radius* (6.5)
   - *The demo is one draw from the distribution* (0.3)
2. **One sentence per section.** Each recap slide ends with the section
   compressed into a single line a learner could say in a meeting. That
   sentence is the referral unit. Write it deliberately, not as a summary but
   as a quotable.
3. **Artifacts as gifts.** Each of the 11 artifacts gets a clean cover page,
   the course lexicon on the back page, and a footer line ("From *AI Product
   Skills for PMs & Analysts*"). Artifacts get forwarded to teammates; that
   footer is the highest-intent advertising the course will ever get, at zero
   cost. Keep artifacts genuinely complete rather than teasers: a crippled
   template does not get forwarded.
4. **The bonus lecture.** Udemy permits one final bonus lecture with promo
   content. Use it for the book, the next course, and the mailing list. This
   is the only place on Udemy where off-platform links are safe; keep them out
   of everything else.

---

## 9. Order of work

The course is fully drafted, so the critical path is verification, not
writing. Everything here folds into that pass rather than adding a separate
project:

1. Implement the QC additions (§7) **before** the verification pass starts,
   so every lecture is verified once against the raised bar instead of twice.
2. Run the verification pass one section at a time, in the release order a
   learner meets them: render slides, view them, read narration aloud, check
   openers (§3), confirm story-bible callbacks and strengthen the weak
   stretches (§2), apply the visual floor (§6). Sections 4 and 9 also get the
   two new figure kinds during their turn.
3. Add the pause layer to `tts.py` (§5) before the first ElevenLabs
   production render, so cached audio is not invalidated twice.
4. Record the instructor presence batch (§4): promo, 0.1, and all section
   intros in one sitting, referencing real content since it all now exists.
5. Ship the referrability kit (§8) with the release build: lexicon on recap
   slides, artifact cover pages and footers, the bonus lecture.
