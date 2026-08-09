# Production playbook

How to go from a blank lecture file to a finished, QC-passing MP4.

---

## Setup (once)

```bash
# System deps
apt-get install -y ffmpeg hunspell hunspell-en-gb espeak-ng \
                   fonts-inter-variable fonts-jetbrains-mono

# Python: standard library + PyYAML only
pip install pyyaml
```

Chromium is auto-detected (Playwright's build, or any system Chrome). Override with
`CHROME_BIN=/path/to/chrome` if needed. No Python packages beyond PyYAML — the
pipeline shells out to ffmpeg and Chromium deliberately, so there's no dependency
tree to rot.

---

## The loop

```bash
# 1. Write or edit  courses/ai-for-pms/lectures/<id>-<slug>.md

# 2. Check slides only — fast, no TTS spend
python3 pipeline/build.py --course courses/ai-for-pms --slides-only --only 4.2

# 3. Look at build/ai-for-pms/work/<slug>/png/*.png

# 4. Full build with the scaffold voice (free, correct timings)
python3 pipeline/build.py --course courses/ai-for-pms --only 4.2

# 5. Authoring checks
python3 pipeline/qc.py --course courses/ai-for-pms

# 6. When the script is final, render with the real voice
export ELEVENLABS_API_KEY=...  ELEVENLABS_VOICE_ID=...
python3 pipeline/build.py --course courses/ai-for-pms --provider elevenlabs

# 7. Release gate against Udemy's standards
python3 pipeline/qc.py --course courses/ai-for-pms --release
```

**Narration is cached by its spoken text.** Editing one line re-synthesises one
slide, not the course. That's what makes iterating on scripts affordable.

---

## Lecture file format

````markdown
---
id: "4.2"
title: "Building a golden set: 50 examples that matter"
section: 4
duration_target: 9
voice: tts            # tts | human  (human = you record it; see compliance doc)
verified: false       # YOU set this to true after reading every claim
objectives:
  - "Select 50 cases that predict production behaviour"
---

@slide statement
kicker: The core idea
## Fifty cases beat fifty thousand.
lead: Coverage of failure modes matters more than volume.

@narrate
Narration for the slide above. Written for the ear, not the eye.

@slide bullets
## How to choose them
1. Start from real traffic, never invented examples
2. Cover every failure mode you already know about
...
````

`@slide <layout>` opens a slide. `@narrate` opens its narration.

### Layouts

| Layout | Use for |
| --- | --- |
| `title` | Lecture opener |
| `statement` | One big idea, nothing else |
| `bullets` | Lists; `1.` renders as a numbered rail |
| `two-col` | Comparisons, before/after |
| `table` | Structured comparison |
| `code` | Code or verbatim text |
| `math` | KaTeX display formula |
| `diagram` | Mermaid diagram, with numbered figure caption |
| `metrics` | Big-figure band |
| `callout` | A single "watch out" |
| `definition` | Key-term box (textbook device) |
| `example` | Worked example (textbook device) |
| `sidenote` | Main column plus a margin gloss |
| `quote` | Pull quote |
| `section` | Section divider |

### Directives (anywhere in a slide body)

`kicker:` `lead:` `note:` `attrib:` `sec_num:` `class:` `figcap:`

`figcap:` numbers the figure automatically as `Figure <lecture>.<n>`, so
diagrams can be referenced in narration the way a textbook's are.

`class: center` vertically centres a content-light slide. Use it sparingly:
slides are top-aligned by default so the heading holds position between cuts.

### Inline

`**bold**` · `*accent*` · `` `code` `` · `==highlight==` · `$math$`

### Containers

````markdown
::: cols
:: card bad
### What breaks
- ...
:: card good
### What works
- ...
:::

::: callout Watch out
The thing they must not miss.
:::

::: metrics
- 0.60 :: End-to-end success after 10 steps :: bad
- 94% :: Pass rate on the golden set :: good
:::

::: definition Key idea
A **rubric** is a fixed set of pass/fail questions written *before* you look at
the output.
:::

::: example Worked example
Run the prompt ten times. Count how many outputs you would ship.
:::

::: split
:: main
1. First step
2. Second step
:: aside Why this matters
The margin gloss holds commentary that would otherwise interrupt the argument.
:::
````

---

## Writing narration that doesn't sound like AI

The QC gate enforces some of this; the rest is craft.

1. **Never write what's on the slide.** The slide is the skeleton, narration is
   the argument. QC fails you above 25% verbatim phrase overlap.
2. **Short sentences.** If you run out of breath reading it aloud, cut it.
3. **Second person.** "You'll hit this in week two", not "one may encounter this".
4. **Concrete before abstract.** Ticket #4471 beats "a customer enquiry".
5. **Say the cost.** Every technique has a downside. Naming it is the single
   biggest credibility signal you have.
6. **Read it aloud before you render.** Every time. Non-negotiable.
7. **No LLM tells.** "delve", "in today's fast-paced world", "unlock the power",
   "game-changer", "it's important to note". QC flags these.
8. **No em dashes in learner-facing copy.** They are one of the strongest
   written tells of generated text, and they do not correspond to anything a
   speaker does. Use a colon, a full stop, or brackets instead.

### Marking what only you can supply

```
[INSTRUCTOR-INPUT: 40-60 seconds on a project of yours that failed and why]
```

QC **fails** while any of these remain. That's deliberate: these are the moments
that make the course yours rather than a generated artifact, and they're the
difference between passing Udemy's AI policy and violating it.

---

## Voice

| Setting | Value |
| --- | --- |
| Provider | ElevenLabs (`eleven_v3`) — best for long-form narration |
| Alternatives | `openai`, or add one in `pipeline/tts.py::PROVIDERS` |
| Stability | 0.45 — enough variation to sound alive |
| Style | 0.35 — expressive without drifting |
| Scaffold | `offline` (espeak) for timing/tests. **Never ship it.** |

Add domain words to `_SPOKEN` in `tts.py` when the voice mispronounces them.
`RAG` → "rag", `LLM` → "L L M", and so on.

---

## Audio/video output

| Property | Value | Why |
| --- | --- | --- |
| Resolution | 1920×1080 | Udemy requires ≥720p |
| Aspect | 16:9 | Required |
| FPS | 30 | |
| Video | H.264 high, CRF 19, faststart | Quality with sane file size |
| Audio | AAC 192k, 48 kHz, **stereo** | Udemy fails single-channel audio |
| Loudness | −16 LUFS, −1.5 dBTP | Consistent level across lectures |

---

## Troubleshooting

**Slides render with the bottom cut off** — Chromium reserves window chrome, so
`--window-size=W,H` doesn't give a `W×H` viewport. `render.py` measures the
offset at runtime and compensates. If you swap the browser, delete the cached
offset (restart the process) so it re-measures.

**Mermaid diagram is tiny** — Mermaid writes an inline `max-width` on the SVG.
`deck.css` overrides it; keep that rule if you edit the theme.

**Diagram missing entirely** — Mermaid didn't finish before the screenshot.
Raise `--virtual-time-budget` in `render.py`.

**Spellcheck flags correct words** — add them to `ALLOW` in `qc.py`. Note the
scripts are written in British English (`spellcheck_lang: en_GB`); switching to
`en_US` means rewriting the scripts too. Don't mix.
