# Production report: full-TTS conversion and Kokoro builds

> Status: IN PROGRESS. This file is being filled in as the production run
> completes; do not treat an unfinished section below as a final result.

Date: 2026-08-12. Author decision: full-TTS delivery across all three
courses, superseding the `human_voice_required` policy in every
`course.yaml`. Rationale and the exact commits are in the git history on
`claude/keep-writing-apht23`.

---

## 1. What changed in the source

- `human_voice_required` emptied to `[]` in all three `course.yaml` files,
  each replaced with a dated comment recording the author's decision.
- Every lecture front matter across all three courses switched
  `voice: human` to `voice: tts` (71 files: 23 in ai-for-pms, 23 in
  ai-ugc-ads, 25 in ai-agents-for-work).
- All 11 `[INSTRUCTOR-INPUT]` markers across the three courses resolved,
  using only the author's supplied bio facts (years building AI products in
  Silicon Valley and at major technology companies including ByteDance;
  Bachelor of Computing in Computer Science from NUS with distinction,
  specialising in AI; a year at Stanford). Where a marker asked for a
  personal anecdote the facts don't supply (a failed project, a lost ad
  campaign, a specific past incident), the moment was restructured rather
  than filled with invented content — see the commit messages on
  `claude/keep-writing-apht23` for the specific approach per file.
- `ai-agents-for-work` 11.2 and 11.3 needed more than a marker fill: they
  were originally authored as live screen-recording placeholders, not
  scripts. Rewritten as narrated walkthroughs of the worked example already
  specified in the file (a missing-documents checklist agent over Priya's
  renewal pipeline).
- `docs/01-compliance-checklist.md` and `docs/03-launch-playbook.md` carry
  dated notes recording that the promo and all narration are TTS by the
  author's decision, superseding the face-and-voice advice, with an honest
  note that this likely costs some conversion.

---

## 2. Voice choice

Both `bf_emma` (British female) and `bm_george` (British male) were
generated locally from the same narration excerpt for a technical check:
neither clipped (`max_volume` -0.3dB and -4.8dB respectively, mean volume
within a fraction of a dB of each other), both rendered cleanly. I cannot
myself listen to audio, so I did not make an independent naturalness
judgement between the two. **Voice used: `bf_emma`**, the pipeline's
existing default and docs/07-tts.md's own recommendation for the en_GB
scripts in this repo. No course.yaml needed changing, since `bf_emma` was
already configured as `production.tts.voice` in all three.

---

## 3. Per-course build results

### ai-for-pms

*(filled in as sections complete)*

### ai-ugc-ads

*(filled in as sections complete)*

### ai-agents-for-work

*(filled in as sections complete)*

---

## 4. QC state

Authoring QC (`qc.py`, non-release) on all three courses, after the source
changes above and before any build: every `FAIL` is the expected
`verified: false` sign-off gate (one per lecture — this is a pass, not a
problem, per CLAUDE.md §1) or a pre-existing `[SCREENSHOT-NEEDED]` marker
unrelated to this work. No em dashes, no remaining
`[INSTRUCTOR-INPUT]` markers, no narration/slide overlap failures.

**Known, accepted warning:** switching short section-divider lectures
(section intros/recaps, `duration_target` 1-2 min) from `voice: human` to
`voice: tts` newly triggers `qc.py`'s "very short for a lecture" warning,
which is explicitly skipped for human-voice lectures. This fires on roughly
3-21 lectures per course (see per-course sections above for the current
count) — an intentional design choice (spare section dividers), not a
narration defect, and not something a mass content-padding pass was run to
silence, since that would mean inventing filler content beyond this task's
scope. Left for the author to decide: accept as-is, or add a sentence to
each divider.

Release QC (`qc.py --release`) results per course are recorded below as
each section's build completes.

---

## 5. Regenerating everything

One command per course, once Kokoro is set up (docs/07-tts.md §2,
`KOKORO_MODEL` / `KOKORO_VOICES` pointed at the downloaded model files):

```bash
python3 pipeline/build.py --course courses/ai-for-pms --provider kokoro
python3 pipeline/build.py --course courses/ai-ugc-ads --provider kokoro
python3 pipeline/build.py --course courses/ai-agents-for-work --provider kokoro
python3 pipeline/qc.py --course courses/<slug> --release
```

Narration is cached by spoken text (`build/<course>/work/<lecture>/`), so a
re-run only re-synthesises lines that actually changed.

---

## 6. What still blocks a real Udemy upload

*(filled in at the end — tracks `[SCREENSHOT-NEEDED]` markers, the
`verified: false` sign-off gate on every lecture, and anything else found
during the build pass)*
