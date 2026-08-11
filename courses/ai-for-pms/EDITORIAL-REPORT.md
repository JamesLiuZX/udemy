# Editorial report: AI Product Skills for PMs & Analysts

Two passes over Sections 0-11, plus the QC/pipeline additions each was
built on. §1-5 cover the original editorial verification pass. §6 covers
the later accessibility and story pass (CLAUDE.md §4 rule 7 / docs/04's
plug-and-play rule), which used this verified course as its input. This
is a status report, not a sign-off: nothing here sets `verified: true`,
and it doesn't need to.

---

## 1. Where the course stands

**Every lecture in every section (0 through 11) has been rendered, visually
inspected slide by slide, read for craft, checked against `qc.py`, and
checked against `story-bible.yaml` for running-case continuity.**

Full-course QC, as of this report:

```
104 fail · 0 warn
NOT ready to submit.
```

Every one of the 104 FAILs is one of exactly two things, both correct and
expected:

- `verified: false` on all 102 lectures — the instructor's read-and-sign-off
  gate. Nobody but the instructor may clear this.
- 4 unfilled `[INSTRUCTOR-INPUT: ...]` markers in `11.5`, the closing
  lecture — see §3.

Zero WARN. Every craft-level QC check this pass added (sentence rhythm,
static-frame cap, figure floor, bullets share, opener diversity, direct
address, question presence, story-bible continuity) is clean across the
whole course, not just Section 11.

Before this pass, `qc.py` did not have most of these checks at all (they
were added as step 1 of the underlying assignment, see §4). Comparing
against the checks that existed before this pass: the original
pre-existing FAILs (verified/INSTRUCTOR-INPUT/description line) were
already clean except for the two exemptions above. The new checks surfaced
roughly 60-70 WARNs across the course over the pass (opener runs, static
frames, missing questions, low direct address, bullet-heavy slides, weak
continuity), all now fixed section by section.

---

## 2. Per-section status

| Section | Rendered | Visually viewed | QC | Story-bible callbacks | Notes |
| --- | --- | --- | --- | --- | --- |
| 0 (Orientation) | Yes | Yes | Clean | n/a (pre-anchor) | `0.2` got a question added this pass to clear a question-presence warning that only appeared once that check existed; otherwise untouched. `0.1`'s 4 INSTRUCTOR-INPUT markers are welcome/credibility bookends, see §3. |
| 1 (Mental model) | Yes | Yes | Clean | Confirmed | |
| 2 (Vocabulary) | Yes | Yes | Clean | Confirmed | |
| 3 (Specifying) | Yes | Yes | Clean | Confirmed | `3.7` had a borderline static-frame warning found on a later course-wide re-check; fixed by splitting the closing paragraph into its own slide. |
| 4 (Evaluation) | Yes | Yes | Clean | Confirmed | First section to use the new `trend`/`grid` figure kinds (`4.5`). |
| 5 (RAG) | Yes | Yes | Clean | Confirmed | |
| 6 (Agents) | Yes | Yes | Clean | Strengthened (`6.1`) | Generic example swapped for the running refund-agent case. |
| 7 (Cost) | Yes | Yes | Clean | Strengthened (`7.2`, `7.5`, `7.7`) | Also where the `$…$` math-stash bug (see `CLAUDE.md` §7) was found and fixed in narration containing two currency figures on one line. |
| 8 (Risk) | Yes | Yes | Clean | Strengthened (`8.1`, `8.2`, `8.3`, `8.6`, `8.7`) | A `story-bible.yaml` YAML bug (unquoted `": "` inside two plain-scalar values) silently broke every subsequent QC/build run using the file until diagnosed and fixed here; the whole course was re-checked afterward to confirm nothing regressed while it was broken. |
| 9 (Analytics) | Yes | Yes | Clean | Strengthened (`9.1`, `9.2`, `9.3`, `9.6`) | Second use of `trend`/`grid` figures. |
| 10 (Doing the job) | Yes | Yes | Clean | n/a | `10.7`'s opener converted from `statement` to `callout` this pass, to break a three-in-a-row same-layout run that only became visible once Section 11 existed. |
| 11 (Capstone) | Yes | Yes | Clean | Strengthened (`11.1`, `11.2`, `11.3`) | See §3 for its INSTRUCTOR-INPUT markers. `11.3`'s opener also converted `statement` → `callout` for the same opener-diversity reason. |

All Section 11 durations were confirmed against `course.yaml` targets with
a full offline-voice build (espeak scaffold, correct timings):

| Lecture | Target | Actual | Within tolerance |
| --- | --- | --- | --- |
| 11.1 | 6 min | 5.8 min | Yes |
| 11.2 | 10 min | 8.1 min | Yes |
| 11.3 | 10 min | 8.8 min | Yes |
| 11.4 | 6 min | 4.8 min | Yes |
| 11.5 | 4 min | 2.8 min | Yes |

---

## 3. Instructor-gate review

The editor's directive asked for the instructor's remaining involvement to
be reduced to the minimum that stays honest and policy-safe: restructure
and remove an `[INSTRUCTOR-INPUT: ...]` marker wherever its point can be
carried by the running case or by verifiable general material instead of a
personal anecdote, but not to zero, and never by inventing a personal
story or credential.

**Finding: a full-course grep found exactly 8 markers, all in two
lectures.**

| Lecture | Markers | What they ask for |
| --- | --- | --- |
| `0.1` (Welcome) | 4 | The instructor's own background, why they built this course, a direct-to-camera credibility moment, and the specific promise they're making to the learner. |
| `11.5` (Where to go next, and thank you) | 4 | A direct-to-camera close, a specific personal thank-you, a genuine ask (review/referral), and a closing line. |

**No markers have been removed.** These 8 are exactly the bookend moments
both the editor's directive and `CLAUDE.md` §1 agree must stay: real
instructor presence at the course's open and close is what the "AI
enhances, doesn't replace, the instructor" policy line is actually about,
and nothing in the other 100 lectures was gated behind an unfillable
personal-anecdote marker that could have been restructured away. The
course's design already put every instructor-only moment at the two
places policy specifically protects; there was no slack between "reduce
to the minimum" and "already at the minimum."

This was confirmed via `AskUserQuestion` before the survey, and the
survey's result (no removable markers exist) is the outcome, not a
decision made in place of the one already given.

---

## 4. Pipeline changes made this pass

- **`pipeline/qc.py`**: added sentence-rhythm, static-frame cap (>90s),
  figure-floor (>4min needs a visual), bullets-share (>50%), opener-diversity
  (3 same-layout in a row), direct-address (<1 you/your per 100 words),
  question-presence (no `?` in >4min), and story-bible continuity checks.
  Tested clean against Section 0 first, then wired into the full run.
- **`pipeline/figures.py`**: added `trend` (line chart, fixed 0-100% scale,
  emphasis-only end labels) and `grid` (table-as-SVG with highlightable
  cells) figure kinds, used in `4.5` and `9.1`.
- **`pipeline/tts.py`**: added a `[pause]` narration marker (~700ms
  silence), stripped from captions and cache keys, tested on `0.3` with the
  offline voice.
- **`pipeline/build.py`**: one-line fix so captions strip the `[pause]`
  marker instead of leaking it.

**Not mine, found during this pass**: another session added a free local
Kokoro-82M TTS provider (`pipeline/tts.py`, commit `22dce30`) and changed
`course.yaml`'s default provider from `elevenlabs` to `kokoro`. Reviewed
the diff; it doesn't conflict with anything in this pass, and every build
this session ran used `--provider offline` explicitly regardless of the
default.

---

## 5. What remains, and it's all instructor-only

Nothing left in this list can be done by further editing:

1. **Read and sign off**: read each of the 102 lectures and set
   `verified: true` once its claims are ones you can personally defend.
   This is the load-bearing gate `CLAUDE.md` §1 describes; no pass, however
   thorough, can substitute for it.
2. **Fill the 8 `[INSTRUCTOR-INPUT]` markers** in `0.1` and `11.5` with your
   own background, your own reasons for building this, and your own
   closing ask. Nothing was invented to fill these, and nothing should be.
3. **Record the human-voice lectures**: everything marked `voice: human` in
   `course.yaml` (all of Section 11's worked-example and closing lectures,
   plus the section intros/outros elsewhere) needs a real recorded voice,
   not the offline scaffold or a synthesised one, per the course's own
   voice policy.
4. **Production TTS pass**: once scripts are signed off, run
   `pipeline/build.py --provider kokoro` (or `elevenlabs`/`openai` with a
   real key) for every `voice: tts` lecture to replace the free scaffold
   audio used throughout this pass.
5. **The release gate**: `pipeline/qc.py --release` against Udemy's
   technical standards, after 1-4 are done.
6. **The promo video**, and anything else in `docs/03-launch-playbook.md`
   that depends on a human presenting.

Everything upstream of that list, every script, every slide, every figure,
every continuity check, is done and QC-clean.

---

## 6. Story pass: accessibility and plug-and-play delivery

A second author directive, applied after the verification pass above and
using its output as input: adapt the course's delivery for an ordinary
office worker or manager who wants an instant, plug-and-play improvement
to their daily work, per `CLAUDE.md` §4 rule 7 and docs/04's plug-and-play
rule. The instruction was explicit that the spine, the judgement, the
rigour, the honest caveats, is the moat and was not to be gutted: this
pass changes framing and delivery, not the underlying discipline.

Four things were audited across all 102 lectures: jargon translated at
first use, technical depth kept only where it changes a decision the
learner owns, story-first (scene, not category) openers, and a single
plug-and-play close per lecture wired to an artifact where one exists.

### 6.1 What changed, mechanically, everywhere

The most common structural gap was the close. 78 of 102 lectures ended
with a "Two things worth doing now" bullet slide, one step beyond what
the rule asks for. All 78 were rewritten to end on **one** action
(merging the two steps where they were genuinely sequential parts of the
same task, e.g. "download the template, then use it" became one
instruction). Every rewritten close was rebuilt and re-viewed as a
rendered slide, not just edited as text. Two side effects turned up
repeatedly during the merge and were fixed in the same commit each time
they appeared:

- **New slide/narration overlap.** Compressing two bullets into one
  sentence sometimes made the closing slide's on-screen text and the
  narration restating it too similar, tripping the (pre-existing)
  verbatim-overlap QC check. Fixed by rewording the narration side to
  cover the same instruction in different words (`1.2`, `1.4`, `2.1`,
  `3.8`, `11.2` all needed this).
- **Lost question marks.** A few merges accidentally deleted the
  lecture's only narration question, tripping the question-presence
  check. Restored as a real question in the merged sentence rather than
  re-adding a throwaway one (`2.4`, `2.6`).

### 6.2 Story-first openers

Sections 0 through 11 were read opener by opener against the "a lecture
that opens on a category gets reopened on a moment" rule. The large
majority already qualified: this course's openers were already built
from the pattern library in docs/04 §3 (a real quote from a review, a
specific number, a before/after gap, an incident replay), which is
mostly synonymous with "a moment, not a category." Only three genuinely
needed rewriting:

- **`1.1`** ("What an LLM actually does") opened by stating the
  mechanism first and illustrating it after. Reordered to lead with the
  demo-vs-production gap as a scene, then state the mechanism; no
  content cut.
- **`1.3`** (temperature) opened on a meta "a correction, on purpose"
  callout with no scene underneath it. Given one sentence of scene (the
  same prompt run twice this morning, two different answers) ahead of
  the existing correction framing.
- **`0.2`** picked up a new question-presence gap only once that QC
  check existed (see §1); fixed with a direct question, not reframed as
  a scene, since `0.2` is the course-map/orientation lecture and exempt
  from the scene-opener expectation by its own nature (this exemption
  also applies to `10.x`'s occasional table-first openers where the
  lecture's whole job is a reference document, not an argument).

Two lectures (`10.7`, `11.3`) had their openers changed from `statement`
to `callout` for the unrelated reason of opener-*diversity* (three
same-layout lectures in a row), not scene quality; both already opened
on a moment and stayed that way, just in a different slide layout.

### 6.3 Mechanism depth: the seven flagged candidates

The assignment named seven lectures to inspect hard for machinery beyond
what changes a decision the learner owns: `1.2`, `1.3`, `2.3`, `4.8`,
`5.2`, `5.3`, `7.6`. Each was read in full against that test. The honest
finding: **six of the seven were already correctly scoped**, and one
(`1.2`) had a small trim worth making.

| Lecture | Verdict | Reasoning |
| --- | --- | --- |
| `1.2` (tokens) | Trimmed | The token-mechanics table listed individual word-splitting examples ("the" = 1 token, "summarisation" = 3). No decision depends on the exact splitting rule, only on the rough ratio and the practical size (a ticket reply runs 40-60 tokens). Compressed to that, with an explicit "the mechanics don't change any decision you own" line replacing the removed detail. |
| `1.3` (temperature) | Kept, already flagged | The lecture already opens by naming itself an optional refinement to `1.1`'s simplified model ("a correction, on purpose") before going into it, exactly the pattern the rule asks for. Content itself never exceeds what's needed to choose low vs. high temperature. |
| `2.3` (embeddings/vector search) | Kept, given explicit flag | The pipeline diagram was already scoped ("without the maths"). Left the content intact but added one sentence tying it explicitly to the one decision it informs (who owns re-indexing when a source document changes), so it reads as "here's the machinery behind a real decision" rather than required background. |
| `4.8` (statistical significance) | Kept | Already exemplary before this pass: teaches a plain-English rule of thumb for sample-size intuition, explicitly declines to teach p-values, confidence intervals, or hypothesis-testing formalism, and calls itself "a rule of thumb, not something you'd hand a statistician as proof." Added one line pointing to a data analyst for real statistics, mirroring `4.3`'s existing Cohen's kappa aside. |
| `5.2` (RAG pipeline stages) | Kept | The seven-stage table has an explicit "whose decision" column separating PM calls (ingestion scope, top-k, citation) from stages marked "mostly engineering" (embed & index, generation), and never goes into the mechanics of those engineering-owned stages. This is what decision-scoped depth looks like. |
| `5.3` (chunking) | Kept | Stays entirely inside product trade-offs (precision vs. context, cost per query) and never touches embedding mathematics. |
| `7.6` (latency budgets) | Kept | Stays inside decisions a PM owns (which interaction pattern sets which budget, streaming/narration vs. a real infrastructure fix) and never touches network or infrastructure internals. |

No lecture outside this list of seven needed a mechanism-depth edit; the
per-section commits note this explicitly where a section (6, 8, 9, 10)
had no flagged candidates at all and none were found on inspection either.

### 6.4 Jargon before translation

Spot-checked across every section: this was already close to universal
practice in the drafted course (e.g. "context window" is defined in the
same sentence it's introduced in `1.2`; "temperature" gets its plain
definition before its mechanism in `1.3`; "MCP" is defined by what it
standardises, not by name, in `6.2`). No lecture was found using an
undefined technical term as a load-bearing fact. No edits were needed
specifically for this criterion beyond the mechanism-depth trims in §6.3,
which double as jargon compressions.

### 6.5 Widened course.yaml audience and description

Proposed in a single, clearly marked commit
(`[PROPOSED, PLEASE REVIEW] Widen course.yaml audience/description to
managers and team leads`) for the author to review in the diff before it
ships. Widens the subtitle, the description's "Who this is for" line, and
the `audience:` list to include managers and team leads whose team ships
or operates an AI feature, without "product" in the job title, alongside
the existing PM/analyst/delivery-manager audience. The technical
vocabulary that differentiates this course (eval-based acceptance
criteria, golden-set harness, token economics) was deliberately left
untouched in every changed field, since that vocabulary is the
positioning, not friction to remove. The title, the description's
opening hook (already audience-neutral), and outcomes/pricing were left
alone as out of scope for this proposal.

### 6.6 QC status after the story pass

Every section was rebuilt and QC-checked immediately after its edits,
and the full course was re-checked after each section commit. Final
state, identical in shape to §1:

```
104 fail · 0 warn
NOT ready to submit.
```

Same two expected FAIL causes as before (`verified: false` on all 102
lectures, the 4 legitimate `INSTRUCTOR-INPUT` markers in `11.5`). No
`INSTRUCTOR-INPUT` marker was touched during this pass. `story-bible.yaml`
was re-validated as parseable YAML after every section that referenced
it. Every changed slide (new openers, new closes, the `1.2` table trim)
was rebuilt with `--slides-only --provider offline` and visually
inspected as a rendered PNG before its section was committed.

### 6.7 What remains after this pass

Nothing new. The instructor-only list in §5 is unchanged and still
complete: sign-off, filling the 8 `INSTRUCTOR-INPUT` markers, recording
the `voice: human` lectures, the production TTS pass, the release gate,
and the promo video. This pass only touched narration, slide layout, and
`course.yaml` marketing copy: it neither closes nor reopens any item on
that list.

---

## 7. Visual-standard pass (docs/09), 2026-08-11

A dedicated audit of all 102 lectures against `docs/09-visual-standard.md`
§2, run after the story pass above concluded.

### 7.1 The audit result

The visual floor was already met before this pass touched anything: every
substantive lecture carries at least one figure, mermaid diagram, table,
or metrics band. The only lectures with none are the twelve section
intros, the eleven recaps, and 0.1, exactly the connective-tissue
exceptions docs/04 §7's severity note anticipates, and none of them
warrants a decorative addition. Sections 4 and 9 already use the `trend`
and `grid` figure kinds docs/04 §6 asked for (4.5, 9.1). Full-course QC
stood at 0 warnings before and after this pass.

### 7.2 What this pass added

**The screenshot lane** (docs/09 §2). Three lectures genuinely teach or
lean on a real tool surface, and each now carries a `[SCREENSHOT-NEEDED]`
marker with capture instructions:

- `2.6` (in frontmatter notes): a current public model-card benchmark
  table, annotated to the two things the lecture teaches learners to
  find. Public and headlessly capturable; waiting only on a slide-DSL
  image-embed lane, which does not exist yet (see 7.3).
- `6.2` (on the tool-call diagram slide, rendered and inspected): the
  author's own assistant-connector settings showing a real Workspace or
  Notion connection, annotated to the permission-scope line.
- `10.4` (in frontmatter notes): a real vibe-coding session from the
  author's own account, cropped to prompt and generated diff.

No other lecture clears the "teaches a tool surface" bar: the course is
deliberately judgment-led, its numbers-bearing visuals are all
pipeline-generated (the only lane allowed to carry them), and adding
screenshots of surfaces the course doesn't actually teach would be
decoration.

**The missing gate.** docs/09 §2 says `[SCREENSHOT-NEEDED]` markers
"block the release build like INSTRUCTOR-INPUT does," but `qc.py` never
implemented that. Implemented now, next to the INSTRUCTOR-INPUT check.
Verified against both courses: the three markers above fail correctly,
and ai-ugc-ads's ten pre-existing markers (added by its own
visual-standard session) are now actually enforced instead of decorative.

### 7.3 Flagged for the pipeline, not silently built

The slide DSL has no image-embed lane, so even a public, headlessly
capturable screenshot (2.6's) currently has nowhere to land on a slide.
That lane (markup.py image directive + house-style annotation pass per
docs/09 §2's mechanics) is the one piece of pipeline the screenshot
standard still needs. Flagged here rather than built mid-pass: it is
shared infrastructure both courses will use, and it deserves its own
focused session rather than a bolt-on at the tail of an audit.

### 7.4 QC state after this pass

107 fail · 0 warn: the 102 sign-off gates, the 4 INSTRUCTOR-INPUT
markers in 11.5, and the 3 new SCREENSHOT-NEEDED markers, every one an
intentional block owned by the instructor or the capture session. Zero
warnings. All three touched lectures re-rendered and their changed
slides visually inspected (6.2's marker renders below the diagram; 2.6's
sits in notes after a first placement made the table slide dense, caught
by QC's own density warning and fixed).
