# Editorial report — AI UGC & Video Ads

Full-course editorial pass, completed after all 81 lecture files across 12
sections (0–11) were drafted, rendered, visually inspected, built with the
free offline voice, and run through `qc.py`. This report is the handoff to
the human author: what's done, what the pipeline can't check, and exactly
what's left before this course can be recorded and submitted.

**Course-wide `qc.py --course courses/ai-ugc-ads` result: 0 warnings.**
Every remaining failure is one of the three gates CLAUDE.md §1 requires to
stay open until a human closes them, plus one pipeline-side dictionary gap
(§below). Nothing in this report is a defect the pipeline should have caught
and didn't.

---

## 1. Per-section status

| # | Section | Lectures | Status |
| --- | --- | --- | --- |
| 0 | Orientation | 0.1–0.4 (4) | Drafted, rendered, QC clean. 0.1 free preview. |
| 1 | The Case for Distributions | 1.0–1.6 (7) | Drafted, rendered, QC clean. |
| 2 | The Brief System | 2.0–2.7 (8) | Drafted, rendered, QC clean. Delivers B01, B02-preview. |
| 3 | Generating Statics at Volume | 3.0–3.7 (8) | Drafted, rendered, QC clean. Delivers B03. |
| 4 | Generating Video at Volume | 4.0–4.7 (8) | Drafted, rendered, QC clean. Delivers B04. |
| 5 | Platform Playbooks | 5.0–5.6 (7) | Drafted, rendered, QC clean. Freshness_watch: 5.1, 5.2, 5.5. |
| 6 | Claims, Rights & Disclosure | 6.0–6.7 (8) | Drafted, rendered, QC clean. Delivers B05. Freshness_watch: 6.3. |
| 7 | The Testing Machine | 7.0–7.6 (7) | Drafted, rendered, QC clean. Delivers B06, B07. |
| 8 | Reading Results | 8.0–8.6 (7) | Drafted, rendered, QC clean. Delivers B08, B09. |
| 9 | Scale Ops | 9.0–9.6 (7) | Drafted, rendered, QC clean. Delivers B10, B11. Freshness_watch: 9.2. |
| 10 | Doing the Job | 10.0–10.4 (5) | Drafted, rendered, QC clean. |
| 11 | Capstone | 11.1–11.5 (5) | Drafted, rendered, QC clean. Closes with instructor sign-off. |

**Total: 81 lecture files, 11 artifacts (B01–B11) delivered, 0 QC warnings
course-wide.**

Every section carrying more than one lecture had an explicit end-of-section
editorial sweep before the next section started: em dashes, banned
filler/LLM-tell phrases, en_GB consistency, opener-layout diversity (no
three consecutive lectures sharing a first-slide layout), story-bible
number-continuity, and a full `qc.py` re-run confirming zero warnings. Real
issues caught and fixed during these sweeps are listed in section 3 below.

---

## 2. What the pipeline cannot check (author-only actions)

These are not bugs. They are exactly the three gates CLAUDE.md §1 names as
load-bearing for the Udemy "not entirely AI-generated" rule, plus the two
genuine instructor-presence moments. None of them should be filled in by an
AI, this session included.

### 2.1 `verified: false` on all 81 lectures

Every lecture still carries `verified: false`. This is the instructor's
personal sign-off that they have read the script and would defend every
claim in it. **Do not set any of these to `true` in bulk** — read each
lecture (or at minimum each section's worked example and any claim you
didn't personally verify) and flip it once you're satisfied.

### 2.2 Eight unfilled `[INSTRUCTOR-INPUT]` markers, in two lectures only

- **`0.1-welcome.md`** (4 markers): your role and the accounts/creative
  you've actually run, the scale (spend/accounts/clients), and one campaign
  of yours that lost money and what it taught you. This is the free-preview
  lecture and Udemy reviewers' first impression — it carries the most
  weight of any instructor-input block in the course.
- **`11.5-where-next-thank-you.md`** (4 markers): a personal note on why
  you built this course, and a closing sign-off with where learners can
  find you.

No other lecture in the course has an `[INSTRUCTOR-INPUT]` marker. Per the
standing directive, every other moment that could plausibly have needed one
was instead carried through the Harlan Supply Co. / Dana / Sam story-bible
serial — real numbers, real failures, real decisions, invented once at the
story-bible level and never contradicted afterward, but not requiring your
personal biography to teach the lesson.

### 2.3 Production voice and release build

Every lecture has been built once with the free offline (espeak) scaffold
voice to prove timings, per CLAUDE.md §2. **None have been rendered with
the production Kokoro voice**, and none have run `qc.py --release` (the
technical-standards gate against Udemy's actual submission requirements).
Both are cheap, but deliberately left for after your sign-off pass, since
`verified: true` should happen before spending the render time.

### 2.4 Freshness_watch lectures need periodic re-verification, not just once

`course.yaml` marks 3.1, 3.2, 4.1, 4.3, 5.1, 5.2, 5.5, 6.3, and 9.2 for
recurring re-verification (platform mechanics, per-asset generation
pricing, disclosure law). Every one of these was verified via live web
search at writing time (August 2026) and the search dates/queries are
recorded in each lecture's `notes:` frontmatter field. These will drift.
11.5 already tells learners to re-check Sections 5 and 9.2 themselves;
you should do the same before each new cohort or significant update.

---

## 3. Real issues found and fixed during this session's sweeps

Listed so you don't need to re-audit these — they were caught by the
QC/build loop, not left for you to find:

- **Opener-layout monotony**, recurring across nearly every section (4
  through 10): three consecutive lectures opening on the same slide layout.
  Fixed each time by converting one lecture's opener to a different layout
  (`callout` or `sidenote`), preserving the exact heading/message.
- **Duration shortfalls**, most severe in 4.1–4.4 and recurring in most
  Section 8–11 lectures on first draft: narration consistently landed
  30–60% short of target because the nominal 150 wpm figure in
  `course.yaml` doesn't match the offline voice's actual rendered pace
  (~165–173 wpm). Fixed by expanding narration and re-measuring against
  actual build duration, not the nominal formula, for every TTS lecture.
- **A logic inversion** in 9.2's code slide: the ratio rule was written
  backwards (said "if the ratio is small" where the narration and the
  actual maths meant "if the ratio is large"). Caught on visual slide
  review before it shipped, fixed, re-verified.
- **A QC continuity false-positive** in 10.1: "Sections 7 through 9" sitting
  near the word "architecture" was misread as a stray ad-set count against
  the story-bible's `8` figure. Reworded to remove the coincidental
  adjacency; not a real continuity error.
- **Real filler-word/tell hits**: "obviously" (9.5, twice more in draft
  passes), "basically" (11.2). All rewritten, not just suppressed.
- **One Americanism**: "practiced" → "practised" in 10.4 (verb form, en_GB).
  Caught during this final pass, not earlier — worth a slower re-read if
  you're editing further, since single Americanisms in slide body text
  (not narration) are the easiest kind to miss.
- **The math-stash bug** (CLAUDE.md §7): consistently avoided all session by
  spelling currency as words ("25 dollars") whenever a second `$` would
  otherwise land on the same source line. Two legitimate exceptions exist
  in the whole course and are safe: 1.4's KaTeX formula (the `$...$` pair
  is the intended math delimiter, not currency) and two `notes:`
  frontmatter fields (6.2, 9.2) which aren't parsed as slide markdown.

---

## 4. Known pipeline-side gap (not fixable from `courses/`)

`qc.py`'s en_GB spellcheck flags real, correctly-spelled words absent from
its dictionary. `pipeline/` is read-only for this session per the standing
scope; a sibling session working on `pipeline/`/`theme/` would need to
extend the `ALLOW` list. Words flagged as "possible typos" that are not
actually errors, confirmed by manual review:

`Meta's, Packshot, Packshots, Playbooks, anymore, harlan, houreleven,
instream, mmHg, overclaiming, packshot, playbook, relitigated, rescore,
skippability, tagline, taglines, tiktok, unshippable, voiceover`

Most are proper nouns (`harlan`, `tiktok`, `Meta's`), the story's internal
naming convention (`houreleven`), medical/technical units (`mmHg`), or
ordinary compound words the dictionary doesn't recognise
(`overclaiming`, `playbook`, `rescore`, `skippability`, `unshippable`).
None require a lecture-side rewrite; the fix, if wanted, belongs in
`pipeline/qc.py`'s `ALLOW` list.

---

## 5. What "done" means from here

Per CLAUDE.md §1, a `qc.py` run reporting only `verified: false`, unfilled
`[INSTRUCTOR-INPUT]` markers, and this one dictionary gap **is a pass, not
a problem**. The course is authoring-complete. What remains is entirely
yours:

1. Read each lecture and set `verified: true` once you'd defend every claim
   in it personally.
2. Record 0.1 and 11.5 on camera, filling the eight `[INSTRUCTOR-INPUT]`
   markers in your own voice.
3. Record 11.2 and 11.3 (the two worked-solution walkthroughs) and every
   other `voice: human` lecture in your own voice — these were scripted in
   full but were never meant to be synthesised.
4. Re-verify the nine freshness_watch lectures against current
   policy/pricing before recording, since some time has likely passed
   since the August 2026 verification dates in their `notes:` fields.
5. Run the production build with `--provider kokoro` once every lecture
   above is signed off.
6. Run `qc.py --course courses/ai-ugc-ads --release` as the final gate
   against Udemy's technical standards before submission.
