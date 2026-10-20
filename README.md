# AI-produced Udemy courses — production system

An end-to-end pipeline for building courses that pass Udemy's quality bar and
earn 4.5+ ratings: source scripts → designed slides → SOTA narration → 1080p MP4
+ captions, with a quality gate that blocks anything not ready to submit.

**Three courses, fully written and rendered:** *AI Product Skills for PMs &
Analysts* (`ai-for-pms`, 102 lectures), *AI Agents for Your Job*
(`ai-agents-for-work`, 76) and *AI UGC & Video Ads* (`ai-ugc-ads`, 81). A sibling
system in `books/` produces the KDP titles. Current state and what is left before
submission: `CLAUDE.md` §10.

---

## Read this first

**Udemy does not accept courses that are entirely AI-generated.** AI may
"enhance and support the expertise of the instructor" but "cannot replace the
instructor's subject matter knowledge and expertise." Violations mean rejection
at review, takedown after publication, or account suspension.

**But TTS narration is explicitly allowed** — Udemy accepts audio and video
"created using quality text-to-speech (TTS) and artificial intelligence (AI)
programs" — with a mandatory disclosure line.

So this system industrialises *production*, never expertise. Two gates enforce
that, and both are code, not honour-system:

- Every lecture carries `verified: false` until you read it and sign off.
- Every spot needing your real experience is `[INSTRUCTOR-INPUT: …]`.

`qc.py` **fails** while either is outstanding. That friction is the design.

Full analysis and sources: [`docs/00-strategy.md`](docs/00-strategy.md).

---

## Quickstart

```bash
apt-get install -y ffmpeg hunspell hunspell-en-gb espeak-ng \
                   fonts-inter-variable fonts-jetbrains-mono
pip install pyyaml

# Slides only — fast, no TTS spend
python3 pipeline/build.py --course courses/ai-for-pms --slides-only

# Full build with the free scaffold voice
python3 pipeline/build.py --course courses/ai-for-pms

# Quality gate
python3 pipeline/qc.py --course courses/ai-for-pms --release
```

---

## Layout

```
docs/
  00-strategy.md            Research: policy, pitfalls, positioning, the "wow" plan
  01-compliance-checklist.md Pre-submission checklist (auto + manual)
  02-production-playbook.md  Lecture format, writing rules, troubleshooting
  03-launch-playbook.md      Title, promo script, pricing, reviews, cadence

courses/ai-for-pms/
  course.yaml               Single source of truth: curriculum, landing copy, config
  lectures/*.md             Narration + slides in one file per lecture

pipeline/
  build.py                  Orchestrator (incremental, cached)
  lecture.py                Source → slides + narration
  markup.py                 Slide markup → HTML
  slides.py                 Slide → standalone 1920×1080 page
  figures.py                Data → inline SVG charts and schematics
  render.py                 HTML → PNG (headless Chromium)
  tts.py                    Narration → speech (pluggable providers)
  video.py                  PNGs + audio → MP4
  captions.py               Timings → .srt
  qc.py                     Quality gate

theme/
  deck.css                  Design system
  vendor/                   KaTeX, Mermaid, TeX Gyre Schola, IBM Plex (offline)
```

---

## The design system

The deck is set as a **teaching page, not a product deck**: white paper,
printed-ink colour, and structural devices that carry meaning rather than
decorate.

| | |
| --- | --- |
| Headings | **TeX Gyre Schola** — a Century Schoolbook cut, the face designed for school textbooks |
| Body | **IBM Plex Sans** |
| Data, code, labels | **IBM Plex Mono** |
| Accent | Ink blue `#1B4F8F`; deep green / red / ochre for semantics |

Layouts exist because a textbook has them, and each encodes something true:
figures are **numbered** so they can be referenced, definitions are **boxed**,
worked examples are **marked**, and margin notes hold commentary that would
otherwise interrupt the argument.

**Figures are generated from data**, never drawn and never produced by an image
model, so a chart cannot ship with a mangled label or an invented number.
`figures.py` renders dot plots, threshold histograms and schematics to inline
SVG; Mermaid handles flows. The chart palette is validated for colour-vision
separation rather than eyeballed — the deck's own green and red failed that
check and were replaced for charts.

Content is top-aligned by default so the eyebrow and heading hold position from
slide to slide. In video a header that jumps between cuts reads as sloppy; steady
furniture makes the cut invisible. Add `class: center` to balance a
content-light slide.

---

## Design decisions worth knowing

**One file per lecture.** Narration and slides live together, so a script edit
and a slide edit are the same edit. Nothing is authored twice.

**Deterministic visuals.** Typeset HTML, KaTeX and Mermaid — no generative
imagery. Learners specifically call out AI images with mangled text and extra
limbs; this pipeline cannot produce them.

**Narration ≠ slide text.** QC fails above 25% verbatim phrase overlap. The most
common complaint about slide courses is a voice reading the bullets aloud.

**Incremental and cached.** Narration is keyed by spoken text, so editing one
line re-synthesises one slide, not the course.

**Zero Python dependencies beyond PyYAML.** Everything else shells out to ffmpeg
and Chromium, both pinned by the OS rather than a lockfile.

**Offline vendored assets.** Fonts, KaTeX and Mermaid are committed (~5 MB), so
renders are byte-identical on any machine with no network.

---

## Status

| | |
| --- | --- |
| Pipeline | Working end to end: 1080p MP4 + SRT, release QC with zero technical failures on all three courses |
| Courses | `ai-for-pms` 102 lectures, `ai-agents-for-work` 76, `ai-ugc-ads` 81; all written, rendered and checked |
| Blocking gates | 259 instructor sign-offs (`verified: true`) and the `[SCREENSHOT-NEEDED]` screenshots, both James's alone |
| Missing downloadables | `ai-for-pms` A01 to A04, A06 to A12 and all of `ai-ugc-ads` B01 to B11 are promised in `course.yaml` but not built |

Details, counts per course and the upload steps: `CLAUDE.md` §10 and
`docs/PRODUCTION-REPORT.md`.

**Rendered videos.** The final MP4s and SRTs (Kokoro `af_heart` voice, all three
courses, 259 lectures, about 4 GB) live at git tag `mp4/af_heart-2026-09-02`,
formerly branch `claude/mp4-builds`. They are deliberately kept out of `main`
because video is regenerable and would bloat every clone. Fetch them with
`git clone --depth 1 --branch mp4/af_heart-2026-09-02 https://github.com/JamesLiuZX/udemy mp4s`,
or regenerate with `python3 pipeline/build.py --course courses/<slug> --provider kokoro`.
