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

**What is already top-decile and must not be diluted:**

- The positioning ("distributions, not functions") is a real spine, not a topic
  list. Almost no competing course has one.
- Narration craft rules (ear-first, name the cost, no tells, no em dashes) are
  enforced by code. Lectures 0.3 and 0.4 genuinely read well aloud.
- The compliance engineering (sign-off gate, INSTRUCTOR-INPUT, disclosure) is
  ahead of virtually every AI-assisted course on the platform.
- Deterministic figures. No competing course can say "no AI images anywhere".

**The gaps between this and a course people refer:**

| # | Gap | Cost if unfixed |
| --- | --- | --- |
| 1 | Story exists per-scene, not per-course. Ticket #4471 appears once and vanishes. | The course is memorable per-lecture but not retellable as a whole |
| 2 | Instructor presence is budgeted at intros and outros only | The single Udemy policy risk left, and the top complaint driver ("no human here") |
| 3 | TTS has voice settings but no delivery direction | Uniform pacing across 10 hours reads as robotic regardless of voice quality |
| 4 | No engineered referrability: concepts are good but unnamed, artifacts are functional but not shareable | Word of mouth left to chance |
| 5 | Visual density is unchecked: a lecture can pass QC with zero figures | Text-heavy drift as sections get written under time pressure |

The five upgrades below map to these five gaps, in priority order.

---

## 2. Upgrade 1: the serial case study (biggest single lever)

Top nonfiction (books and courses) runs one story through the whole thing.
This course already owns the perfect seed: **Ticket #4471** from lecture 0.4.
Promote it from a prop to the spine.

### The setup

One fictional but rigorously realistic company, one AI feature, followed from
demo to production incident across all twelve sections. The learner watches one
feature live through everything the course teaches, then does the same for
their own feature in the capstone.

- **Company:** Fernhill, a mid-market subscription-billing platform.
  ~140 staff, ~9,000 business customers, a 14-person support team.
- **Feature:** AI summarisation of inbound support tickets, so agents triage
  without reading every thread.
- **Cast (keep it to three):**
  - *Priya*, support lead. Wants the feature yesterday; owns the outcome.
  - *Marcus*, staff engineer. Sceptical, usually right, wins arguments with
    numbers. The learner learns to argue like Marcus.
  - *Dana*, CFO. Appears twice: once to approve, once to ask what it costs.

### Section beats

The story advances once per section. Continuity of numbers is what makes it
feel real, so the numbers already shipped in Section 0 are canonical:

| Section | Beat | Canonical numbers |
| --- | --- | --- |
| 0 | The demo impresses; Ticket #4471 exposes the judgement problem | 5 reviewers score 2,3,3,4,5; rubric collapses spread to 3,3,3,3,4 |
| 1 | Why the summariser drops deadlines: mechanism, not malice | context window, token budget for a long thread |
| 3 | Priya writes the PRD; first draft says "summaries are accurate"; rewrite as thresholds | 50-case golden set; 92% target pass rate |
| 4 | Building the instrument; the baseline is uncomfortable | Baseline 68% (the histogram in 0.3); v3 prompt reaches 92% |
| 5 | Tickets reference account history; RAG enters; retrieval fails on billing-email mismatch cases | recall on the 12 "mismatched email" cases |
| 6 | Someone proposes the agent version (auto-refund). Marcus does the reliability math | 0.95^10 = 0.60 |
| 7 | Dana asks the cost question. The long-thread power users are under water | cost per summarised ticket vs revenue per seat |
| 8 | The incident: a tail-case summary invents a refund promise; legal gets involved | 1-in-400 failure rate that support finds at ~600 tickets/day |
| 9 | Instrumenting recovery: acceptance rate, deflection, override rate | the dashboard leadership actually reads |
| 10 | Priya presents the programme; the learner's portfolio mirrors hers | |
| 11 | Capstone: the learner runs the entire Fernhill playbook on their own feature | |

### Continuity rules

- Every number, name, and date in the story lives in
  `courses/ai-for-pms/story-bible.yaml` and is quoted from there, never
  re-invented. A number that drifts between sections destroys the illusion
  instantly, and this is exactly the failure long-form LLM writing is prone to.
  The bible is the fix: it removes the length constraint by making state
  explicit instead of remembered.
- The story never becomes a soap opera. One beat per section, 30 to 90 seconds
  of narration, always in service of the technique being taught.
- Failure beats land harder than success beats. The Section 8 incident is the
  most referrable moment in the course; write it like an incident review, with
  timestamps.

### Why this is worth the effort

- **Completion:** a serial creates pull between sections. Completion is a
  ranking input most instructors ignore.
- **Referrability:** "it follows one AI feature from demo all the way to a
  production incident" is a sentence a learner will say to a colleague.
- **Cohesion:** workshops stop being generic ("design RAG for a support use
  case") and become "fix Fernhill's retrieval problem", which is concrete,
  self-contained, and gradeable against the story bible.

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

Existing lectures 0.3 and 0.4 already do this instinctively. The upgrade is
making it a rule so Sections 1 to 11 hold the standard under production
pressure.

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
- Section 4 (eval dashboards, pass-rate trends, agreement matrices) will need
  two new figure kinds in `pipeline/figures.py`: `trend` (pass rate over
  prompt versions, with version labels on the x axis) and `grid` (rater
  agreement / confusion matrix with counts in cells). Build them when Section 4
  needs them, validate any new hue with the dataviz palette validator, and keep
  the no-generative-images rule absolute.

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

1. Create `story-bible.yaml` with the canonical Section 0 numbers (done, seed
   committed alongside this doc) and thread the Fernhill beat plan into the
   Section 4 lectures as they are written. Retrofit Sections 1 to 3 beats when
   those sections are authored; do not go back and rewrite Section 0, it
   already carries the seed.
2. Apply cold-open patterns and the visual floor to every new lecture from
   Section 4 onward.
3. Implement the QC additions before Section 4 is finished, so the whole
   evaluation section (the shop window of the course) is written against the
   raised bar.
4. Record the instructor presence batch (12 intros + promo) once Sections 4
   and 5 exist, so the intros can reference real content.
5. Add the pause layer to `tts.py` before the first ElevenLabs production
   render, so cached audio is not invalidated twice.
