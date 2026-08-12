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

Target: 12 sections, 102 lectures, 614 min (10h14m).

| Section | Lectures | Built | Narration | Notes |
| --- | --- | --- | --- | --- |
| 0 | 4 | 4/4 | 17.6 min | Visually spot-checked (0.1 slide 2, 0.3 slide 5): design system renders correctly, no overflow/collision. LUFS on 0.3: -16.5 integrated, -4.3 dBTP true peak, both within spec (-14 to -18 LUFS, under -1.5 dBTP). |
| 1 | 9 | 9/9 | 33.0 min | Visually spot-checked (1.5 slide 3, two-col comparison card): clean. Release QC: only the expected verified:false gate on all 9, no technical failures. |
| 2 | 9 | 9/9 | 33.0 min | Visually spot-checked (2.1 slide 2, mermaid diagram): renders at full width with numbered figure caption, no postage-stamp sizing bug. Release QC clean except pre-existing [SCREENSHOT-NEEDED] on 2.6 (unrelated to TTS work). |
| 3 | 10 | 10/10 | 38.6 min | Visually spot-checked (3.7 slide 4, bad/good two-col cards): correct semantic green/red palette, no overflow. Release QC clean. |
| 4 | 11 | 11/11 | 48.7 min | Visually spot-checked (4.6 slide 5, metrics band): big-figure layout clean. Release QC clean. Section 4 is the eval-mindset core of the course; renders and technical checks solid throughout. |
| 5 | 10 | 10/10 | 40.0 min | Visually spot-checked (5.4 slide 4, callout/name-the-cost): ochre accent, centred content-light layout correct. Release QC fully clean, no warnings at all. |

Build throughput observed: section 0 (17.6 min narration, 4 lectures) took
14m13s wall clock on CPU (`time` command, `user` 39m52s reflecting
multi-threaded ffmpeg/Chromium work). Roughly 0.8x real time. At that rate
the full course (614 min) is in the region of 8 hours of build time,
consistent with docs/07-tts.md's "overnight job, not a blocker" framing.

Disk: section 0's `build/ai-for-pms` was 456MB before pruning, 165MB after
deleting the regenerable `narration.wav` (concatenated audio, rebuilt from
the per-slide cache on every run) and `tmp/` (video-encode scratch) from
each lecture's work directory. The per-slide TTS cache under
`work/<lecture>/audio/` is kept: that's the expensive part
(Kokoro synthesis), not the cheap part (ffmpeg concat/encode). `dist/*.mp4`
kept for now while disk headroom is comfortable (~29GB free); will start
pruning those too if headroom drops.

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
