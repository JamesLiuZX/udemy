# Working in this repo

Production system for AI-assisted Udemy courses. Lecture source becomes designed
slides, narration, 1080p video and captions, with a quality gate that blocks
anything not ready to submit.

Read this file fully before your first edit. It encodes decisions that are
expensive to rediscover.

---

## 1. The rule that protects the account

**Udemy declines courses that are entirely AI-generated.** AI may "enhance and
support the expertise of the instructor" but "cannot replace the instructor's
subject matter knowledge and expertise". Penalties escalate from rejection at
review, to takedown, to account suspension.

**TTS narration is explicitly allowed** with a disclosure line. So this system
industrialises *production*, never expertise.

Three things are therefore load-bearing. Do not weaken them to make a build pass:

1. Every lecture carries `verified: false` until a human reads it and signs off.
   **Never set `verified: true` yourself.** It is the instructor's signature.
2. `[INSTRUCTOR-INPUT: ...]` marks content only the instructor can supply
   (their background, their war stories). **Never invent content to fill one.**
   Leaving it blocking the build is correct behaviour.
3. The description must end with exactly:
   `This course contains the use of artificial intelligence.`

`qc.py` fails on all three. A QC run that reports only these is a **pass**, not a
problem to fix.

---

## 2. The loop

```bash
# 1. Write or edit courses/<slug>/lectures/<id>-<name>.md

# 2. Slides only. Fast, no TTS spend.
python3 pipeline/build.py --course courses/ai-for-pms --slides-only --only 4.2

# 3. LOOK AT THE RENDERS. Not optional. See §3.
#    build/ai-for-pms/work/<lecture-slug>/png/*.png

# 4. Full build (free espeak scaffold voice, correct timings)
python3 pipeline/build.py --course courses/ai-for-pms --only 4.2

# 5. Authoring checks
python3 pipeline/qc.py --course courses/ai-for-pms

# 6. Production voice, only once the script is final
export ELEVENLABS_API_KEY=... ELEVENLABS_VOICE_ID=...
python3 pipeline/build.py --course courses/ai-for-pms --provider elevenlabs

# 7. Release gate against Udemy's technical standards
python3 pipeline/qc.py --course courses/ai-for-pms --release
```

Narration is cached by its spoken text, so editing one line re-synthesises one
slide rather than the course.

`build/` is gitignored. Video is regenerable and far too large for git.

---

## 3. Always look at the rendered slide

**A slide that parses is not a slide that reads.** Every visual bug found in this
repo so far was invisible in the source and obvious in the PNG.

After rendering, convert and actually view a few:

```bash
ffmpeg -y -loglevel error -i build/ai-for-pms/work/<slug>/png/slide-003.png \
  -vf scale=1500:-1 /tmp/check.jpg
```

Then Read the .jpg. Check for: text overflowing the frame, labels colliding,
figures the wrong size, prose breaking mid-sentence, empty regions that look
accidental.

Do not report a lecture as done without having viewed its slides.

---

## 4. Authoring a lecture

Full format reference: `docs/02-production-playbook.md`.
Copy `courses/_template/lecture-template.md` to start.
For the step-by-step procedure use the **`write-lecture`** skill.

### Structure

`@slide <layout>` opens a slide. `@narrate` opens the narration under it.
Directives (`kicker:`, `lead:`, `figcap:`, `class:`) can sit anywhere in a slide
body and are lifted out automatically.

### Narration rules, in priority order

1. **Narration must not read the slide.** The slide carries the skeleton, the
   narration carries the argument. QC fails above 25% verbatim phrase overlap.
   If you find yourself restating a bullet, say *why* it is true instead.
2. **No em dashes** in anything a learner reads or hears. They are a strong tell
   of generated text and correspond to nothing a speaker does. Use a colon, a
   full stop, or brackets. QC fails on any.
3. **Write for the ear.** Short sentences. Second person. If you run out of
   breath reading it aloud, cut it.
4. **Concrete before abstract.** "Ticket #4471" beats "a customer enquiry".
5. **Name the cost.** Every technique has a downside. Saying it is the single
   strongest credibility signal available, and no competing course does it.
6. **No LLM tells.** "delve", "in today's fast-paced world", "unlock the power",
   "game-changer", "it's important to note", "in conclusion". QC flags these.

### The voice, by example

> Good: "You will feel that friction, and someone on your team will push back on
> it. Here is the argument that wins."

> Bad: "It's important to note that implementing evaluation frameworks can
> present certain organisational challenges."

Pacing model is 150 words per minute. A 7 minute lecture is roughly 1,050 words
of narration.

---

## 5. The design system

Direction is **a teaching page, not a product deck**. White paper, printed ink.

| Role | Face |
| --- | --- |
| Headings | TeX Gyre Schola (a Century Schoolbook cut, drawn for school textbooks) |
| Body | IBM Plex Sans |
| Data, code, labels | IBM Plex Mono |

Accent is ink blue `#1B4F8F`, with deep green, red and ochre for semantics.

**Things that were tried and rejected. Do not reintroduce them:**

- Dark background with a single neon accent, and Inter as the typeface. That is
  the exact cluster generated design defaults to, and it reads as AI slop.
- Gradients, glassy cards, heavy rounded corners, emoji as section markers.

Slides are **top-aligned** by default so the eyebrow and heading hold position
between cuts. A header that jumps between slides reads as sloppy in video. Use
`class: center` to balance a content-light slide.

---

## 6. Figures and charts

Every figure is **generated from data**, never drawn and never image-generated,
so it cannot ship with a mangled label or an invented number. Learners
specifically call out AI images with broken text.

- Charts: a ` ```figure ` block with a YAML spec, rendered by `pipeline/figures.py`
  (`dotplot`, `histogram`, `sampling`).
- Flows: ` ```mermaid `.
- Pair with `figcap:` so the figure is numbered and referenceable.

**Chart palette is computed, not chosen.** The two-series pair is blue `#2E6DB4`
and orange `#C1741A`. The deck's semantic green and red were tried first and
failed validation: deutan colour-vision separation ΔE 7.1, and the green falls
under the chroma floor so it reads grey. If you add a hue, validate it:

```bash
node /path/to/dataviz/scripts/validate_palette.js "#2E6DB4,#C1741A" --mode light
```

**These become video frames, so no hover layer can exist.** Every value must be
directly labelled or readable off the axis. Never hide a value in a tooltip.

Use emphasis (colour one thing, grey the rest) when the story is one boundary.
Solid hairline grids, never dashed. Chart text in the sans, never the serif.

---

## 7. Traps that have already cost time

These are fixed. Do not "simplify" them back out.

- **Chromium reserves window chrome.** `--window-size=1920,1080` yields a 993px
  viewport, silently cropping the bottom 87px of every slide. `render.py`
  measures the offset at runtime and compensates, then crops to exact size.
- **Mermaid writes an inline `max-width` on its SVG**, pinning diagrams at
  intrinsic size (a postage stamp on a 1920px slide). `deck.css` overrides it.
  Mermaid also renders into the `<pre>` it was authored in, so the code-block
  styling has to be stripped for `pre.mermaid`.
- **Markdown source is hard-wrapped**, so emitting one `<p>` per line breaks
  prose mid-sentence on the slide. `markup.py` folds continuation lines into the
  paragraph or list item they belong to.
- **Dot plot rows need measured heights.** Repeated values stack upward, so a
  fixed row pitch drives one row's dots through the row above's spread bracket.
- **Spellcheck language is `en_GB`** because the scripts are written in British
  English. Do not mix spellings. Switching to `en_US` means rewriting the scripts.

---

## 8. Definition of done for a lecture

- [ ] Slides rendered **and visually inspected**
- [ ] `qc.py` reports no warnings, and no failures other than the sign-off and
      `[INSTRUCTOR-INPUT]` gates
- [ ] Narration reads aloud naturally and does not restate the slides
- [ ] At least one figure, diagram or table where it genuinely aids understanding
- [ ] Duration within roughly 2 minutes of the `course.yaml` target, and under 12
- [ ] Any factual claim is one a real practitioner could defend

Report honestly. If a lecture is written but not visually checked, say so.

---

## 9. Repo map

```
CLAUDE.md                  This file
docs/00-strategy.md        Research: policy, pitfalls, positioning
docs/01-compliance-checklist.md   Pre-submission checklist
docs/02-production-playbook.md    Format reference, writing rules, troubleshooting
docs/03-launch-playbook.md        Title, promo script, pricing, reviews
docs/04-quality-bar.md            Serial case study, cold opens, presence, QC additions
docs/05-kdp-playbook.md           The companion book: craft bar, pipeline, Amazon mechanics
docs/06-growth-engine.md          Channels, asset flywheel, automated growth jobs
growth/                           Paste-ready automation prompts (cron / Cowork)
courses/<slug>/course.yaml        Curriculum, landing copy, config (source of truth)
courses/<slug>/story-bible.yaml   Canonical facts for the serial case study
courses/<slug>/lectures/*.md      One file per lecture
courses/_template/                Lecture template
pipeline/                         build, lecture, markup, slides, render, figures,
                                  tts, video, captions, qc
theme/deck.css                    Design system
theme/vendor/                     KaTeX, Mermaid, fonts (offline, committed)
```

Only Python dependency is PyYAML. Everything else shells out to ffmpeg and
Chromium on purpose, so there is no dependency tree to rot.

---

## 10. Current state and what to do next

Course #1 `ai-for-pms`: 12 sections, 100 lectures, 10h targeted.
**Section 0 is written and built (4 lectures, 19.6 min, 29 slides).**
Sections 1 to 11 are specced in `course.yaml` but unwritten.

**Next: Section 4, Evaluation.** It is the hub the rest of the course plugs into
and the section that justifies the price. It is also the most figure-hungry
section: eval dashboards, pass-rate trends over prompt versions, inter-rater
agreement.

Work one lecture at a time, all the way to verified renders, before starting the
next. A half-finished section is worth less than one finished lecture.

---

## 11. Git

Develop on `claude/ai-udemy-course-build-55erh5`. `main` tracks the same work.
Push with `git push -u origin <branch>`. Do not commit `build/`.
