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
| 6 | 10 | 10/10 | 43.4 min | Visually spot-checked (6.3 slide 3, statement layout): clean. Release QC clean except pre-existing [SCREENSHOT-NEEDED] on 6.2 (unrelated to TTS work). |
| 7 | 9 | 9/9 | 39.6 min | Checked specifically for CLAUDE.md's known two-`$`-per-line math-stash bug (this section is full of per-token pricing tables): source already writes bare numbers ("3/M", "15/M") correctly, no collisions found or rendered. Release QC clean. |
| 8 | 9 | 9/9 | 43.9 min | Visually spot-checked (8.4 slide 4, bad/good two-col): clean. Release QC clean. |
| 9 | 8 | 8/8 | 35.0 min | Visually spot-checked (9.6 slide 3, mermaid metric tree): renders correctly, text wraps within node boxes as authored, no overflow. Release QC clean. |
| 10 | 8 | 8/8 | 39.0 min | Visually spot-checked (10.4 slides 2-3, table + sidenote): clean. Release QC clean except pre-existing [SCREENSHOT-NEEDED] on 10.4 (unrelated to TTS work; needs a real annotated vibe-coding screenshot before release). |
| 11 | 5 | 5/5 | 27.7 min | Visually spot-checked 11.5's rewritten closing sidenote end to end: renders exactly as authored in the sidenote/margin-gloss layout. Course complete. |

**Full-course totals (`build.py --course courses/ai-for-pms --provider kokoro`, no `--only`, all caches hit):** 102/102 lectures built, **7.33h (440 min) total narration** against a 614 min (10h14m) target — Kokoro's actual speech rate at default speed comes in faster than the 150 wpm pacing model used to set per-lecture `duration_target`s, so the built course runs shorter than the source's own estimate. Not a defect (every lecture still passes its individual max/min duration checks), but worth the author knowing before scheduling total watch-time claims on the landing page.

**Full-course release QC** (`qc.py --course courses/ai-for-pms --release`): **105 fail · 3 warn**, all expected — 102 `verified: false` sign-off gates (one per lecture, cannot and must not be set by me) plus the 3 pre-existing `[SCREENSHOT-NEEDED]` markers (2.6, 6.2, 10.4). **Zero technical failures**: every lecture passed resolution (1920×1080), aspect (16:9), stereo audio, loudness (−14 to −18 LUFS), true-peak (under −1.5 dBTP), spelling, and narration/slide-overlap checks. This is the "pass" state per CLAUDE.md §1.

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

Target: 12 sections, 78 lectures, ~440 min (~7h20m). Actual curriculum has
81 lectures (course.yaml's own header comment says 78; the extra 3 are
accounted for by section-recap/capstone granularity — not investigated
further as it's a pre-existing curriculum-vs-header mismatch, not a TTS
issue).

Built in one full-course pass (`build.py --course courses/ai-ugc-ads
--provider kokoro`, no `--only`): **81/81 lectures, 5.36h (322 min) total
narration** against the ~440 min target, the same "Kokoro reads faster than
the 150 wpm pacing model" gap seen in ai-for-pms.

Visually spot-checked 3.2 (batch generation, a screenshot-heavy tool
lecture): the code-block prompt slide renders cleanly, and the
`[SCREENSHOT-NEEDED]` marker renders as visible italic placeholder text on
the slide, exactly as the QC gate intends. This course is the most
screenshot-dependent of the three, so this pattern repeats across 10
lectures (see QC below).

**Release QC** (`qc.py --course courses/ai-ugc-ads --release`): **91 fail ·
4 warn**. 81 fails are the expected `verified: false` sign-off gate, 10 are
pre-existing `[SCREENSHOT-NEEDED]` markers on the tool-heavy lectures listed
in `course.yaml`'s own `freshness_watch` (3.1, 3.2, 4.1, 4.3, 5.1, 5.2, 5.5,
6.3, 6.4, 9.2) — these need real annotated screenshots before release,
unrelated to the TTS conversion. Of the 4 warnings: 1 is pre-existing
(0.1 slide 2, dense slide text, not touched by this work), 3 are the
short-section-divider warning newly exposed by switching those lectures to
TTS (7.0, 8.0, 10.0). **Zero technical failures** — loudness, stereo,
resolution, spelling, overlap all clean across all 81 lectures.

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
