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

# 6. Production voice, only once the script is final (free local Kokoro;
#    setup and alternatives in docs/07-tts.md)
python3 pipeline/build.py --course courses/ai-for-pms --provider kokoro

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
7. **Story before mechanism, plug-and-play before theory.** The buyer is an
   ordinary office worker or manager, not an engineer. Open on a scene, not a
   framework. Translate every technical term into plain speech at first use.
   End every lecture with one thing the learner can do at work tomorrow, using
   an artifact where one exists. Technical depth earns its place only where it
   changes a decision the learner actually owns; anything deeper gets a plain
   "if you want the machinery" flag or gets cut.

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

## 6. Figures, charts, screenshots and images

Visual policy lives in `docs/09-visual-standard.md`; read it before adding
any visual. The short version: real annotated screenshots are first-class
and mandatory in tool lectures; anything carrying numbers, labels or factual
structure is **generated from data** (figures pipeline, mermaid), never
drawn and never image-generated, so it cannot ship with a mangled label;
AI-generated images are allowed only as subject-matter specimens or
text-free atmosphere, never as diagrams. Learners specifically call out AI
images with broken text.

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
- **`markup.py`'s math stash pairs any two `$` on the same line.** A table cell
  or line of prose with two literal currency amounts ("$3/M ... $15/M") reads as
  one LaTeX span and mangles everything between them, dropping spaces and the
  closing `$`. Costed real time in Section 7. Write currency as a bare number
  ("3/M") wherever a second `$` would land on the same line.

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
docs/04-quality-bar.md            Callback thread, cold opens, presence, QC additions
docs/05-kdp-playbook.md           Book portfolio strategy: sequencing, launch, Amazon mechanics
docs/06-growth-engine.md          Channels, asset flywheel, automated growth jobs
docs/07-tts.md                    Voice decision: Kokoro default, costs, audiobook routes
docs/08-channels.md               Channel map: Udemy, KDP, Spotify, YouTube; cuts and requirements
docs/09-visual-standard.md        Screenshots, diagrams, AI-image lanes, the hook standard
growth/                           Paste-ready automation prompts (cron / Cowork)
books/                            KDP publishing system (own CLAUDE.md; read it first)
courses/<slug>/course.yaml        Curriculum, landing copy, config (source of truth)
courses/<slug>/story-bible.yaml   Canonical facts for the running case study
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

Course #1 `ai-for-pms`: 12 sections, 10h targeted. **All 102 lecture files
are drafted.** Section 0 is built and visually verified; Sections 1 to 11
are unrendered, unverified and unsigned.

Sibling system `books/` (own CLAUDE.md, own pipeline) has seven KDP titles
with chapters 1 to 3 drafted each.

**Next, in order (rationale in `docs/04-quality-bar.md` §9 and
`docs/05-kdp-playbook.md` §7):**

1. Implement the QC additions specced in `docs/04-quality-bar.md` §7.
2. Run the course verification pass section by section: render, view, read
   aloud, confirm story-bible callbacks, then instructor sign-off.
3. On the book side, finish `stop-guessing` end to end before touching the
   other six titles.

A half-finished section is worth less than one finished lecture, and seven
three-chapter manuscripts are worth less than one finished book.

---

## 11. Git

Develop on `claude/keep-writing-apht23` (the course and `books/` share it).
Push with `git push -u origin <branch>`. Do not commit `build/`.
