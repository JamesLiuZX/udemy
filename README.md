# AI-produced Udemy courses — production system

An end-to-end pipeline for building courses that pass Udemy's quality bar and
earn 4.5+ ratings: source scripts → designed slides → SOTA narration → 1080p MP4
+ captions, with a quality gate that blocks anything not ready to submit.

**Course #1 in progress:** *AI Product Skills for PMs & Analysts: Spec, Evaluate
& Ship AI Features* — 12 sections, 100 lectures, 10h00m of target runtime.

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
| Pipeline | Working end to end — 1080p MP4 + SRT verified |
| Curriculum | All 12 sections / 100 lectures specced in `course.yaml` (10h00m) |
| Scripts written | Section 0 — 4 lectures, production-ready (15.1 min built) |
| Scripts remaining | Sections 1–11 — 96 lectures |
| Blocking gates | Instructor sign-off on all scripts + 4 `[INSTRUCTOR-INPUT]` markers in 0.1 |

Next: write Section 4 (Evaluation) — it is the section that justifies the price,
and everything else leans on it.
