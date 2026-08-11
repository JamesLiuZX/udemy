# Editorial report: AI Product Skills for PMs & Analysts

Full editorial verification pass, Sections 0-11, plus the QC/pipeline
additions it was built on. Written per the editor's directive extending the
original verification-pass assignment. This is a status report, not a
sign-off: nothing here sets `verified: true`, and it doesn't need to.

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
