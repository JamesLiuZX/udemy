# Working in this repo

Production system for AI-assisted Udemy courses. Lecture source becomes designed
slides, narration, 1080p video and captions, with a quality gate that blocks
anything not ready to submit.

Read this file fully before your first edit. It encodes decisions that are
expensive to rediscover.

---

## Branching: one trunk, no side branches (James, 2026-10-20)

`main` is this repo's only long-lived branch. Every session starts from it
and every session ends by landing on it.

Why: from July to October 2026 sessions each worked on a fresh `claude/*`
branch and rarely merged. The next session started from a stale trunk, could
not see the work, and rebuilt it. On 2026-10-20 every branch was consolidated
into `main`. Do not let it drift again.

The harness gives each Claude Code session a `claude/<random>` branch and tells
it not to push anywhere else without explicit permission. **This section is
that permission, standing and explicit, from James.** Treat the session branch
as scratch space. The work has to end up on `main`.

1. **Start current.** `git fetch origin main`, then `git merge origin/main`
   into your session branch before you change anything.
2. **Look before you build.** Run `git branch -r`, and read the status log in
   `JamesLiuZX/command` `AUTOPILOT.md`. If the work already exists somewhere,
   continue it instead of starting again.
3. **Land before you stop.** Run the gate (`for c in ai-for-pms ai-agents-for-work ai-ugc-ads; do python3 pipeline/qc.py --course courses/$c; done`), then
   `git push origin HEAD:main`. If the push is rejected because `main`
   moved, merge `origin/main`, run the gate again and push again. Never
   force-push `main`.
   If your session's permission layer refuses a direct push, open a pull
   request from your session branch to `main` and merge it yourself in the
   same session, using a merge commit. If that is refused as well, tell James in
   your final message exactly which merge is waiting.
4. **Half-done is fine on `main`. Broken is not.** Unfinished work that
   passes the gate goes to `main`. Only work that fails the gate may stay on
   a branch. In that case, push the branch and record its name, state and next
   step in the command repo's `AUTOPILOT.md` status log, so the next session
   resumes it instead of restarting. That is the only reason a branch may
   outlive its session.
5. **Delete the session branch after it lands** (`git push origin --delete
   <branch>`). If deletion is refused, leave it: James runs the "Prune merged
   branches" workflow (Actions tab), which deletes every branch whose commits
   are all on the trunk. A SessionStart hook (`.claude/hooks/branch-check.sh`)
   lists the other branches on origin at the start of each session.

**The gate, in this repo.** `qc.py` exits non-zero on every course until James
has signed off every lecture, so a pass means: no FAIL line other than
`verified: false`, `[INSTRUCTOR-INPUT]` and `[SCREENSHOT-NEEDED]` (section 1),
and no WARN the trunk did not already have. This prints nothing on a pass:

```bash
for c in ai-for-pms ai-agents-for-work ai-ugc-ads; do
  python3 pipeline/qc.py --course courses/$c | grep -E '^\s+FAIL' \
    | grep -v -E 'verified: false|INSTRUCTOR-INPUT|SCREENSHOT-NEEDED'
done
```

If you touch `books/`, also run `python3 books/pipeline/qc.py --book <slug>` (a
pass is its single `verified: false` fail).

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
  (`dotplot`, `histogram`, `composition`, `sampling`, `trend`, `grid`).
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
- **The TTS cache is keyed by spoken text only**, not by voice, provider or
  speed. Change any of those with a populated `build/` and stale audio from the
  old voice silently leaks into the new build. Wipe `build/` first. (Learned
  when the voice moved from `bf_emma` to `af_sarah` to `af_heart`.)

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
STATUS.md                         Portfolio status page (dated; CLAUDE.md §10 is current)
docs/PRODUCTION-REPORT.md         Full-TTS conversion, Kokoro builds, what blocks upload
proofs/video/                     Three short preview videos, one per course
courses/<slug>/course.yaml        Curriculum, landing copy, config (source of truth)
courses/<slug>/story-bible.yaml   Canonical facts for the running case study
courses/<slug>/EDITORIAL-REPORT.md  What each editorial pass changed and checked
courses/<slug>/artifacts/         Downloadable files promised in course.yaml
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

As of 2026-10-20 everything is on `main`. Three courses are fully written,
rendered, visually inspected and checked against their story bibles (per
`courses/<slug>/EDITORIAL-REPORT.md` and `docs/PRODUCTION-REPORT.md`):

| Course | Lectures | Narration, final render | `qc.py` today | Artifacts promised / built |
| --- | --- | --- | --- | --- |
| `ai-for-pms` | 102 in 12 sections | 8.2 h | 105 fail, 8 warn | 12 / 7 (A01 to A07) |
| `ai-agents-for-work` | 76 in 12 sections | 3.6 h | 78 fail, 21 warn | 10 / 10 |
| `ai-ugc-ads` | 81 in 12 sections | 6.0 h | 91 fail, 4 warn | 11 / 0 |

Every FAIL is a gate that is deliberately James's: 259 `verified: false`
sign-offs (102, 76, 81) and `[SCREENSHOT-NEEDED]` markers (ai-for-pms 2.6,
6.2, 10.4; ai-agents-for-work 3.2, 5.2; ai-ugc-ads 3.1, 3.2, 4.1, 4.3, 5.1,
5.2, 5.5, 6.3, 6.4, 9.2, with 30 markers). No `[INSTRUCTOR-INPUT]` markers
remain. Release QC on the final renders had zero technical failures. The
WARNs are accepted: short section dividers (3, 21 and 3), one dense slide in
ai-ugc-ads 0.1, and five ai-for-pms narrations more than two minutes under
their `duration_target` (1.6, 4.7, 5.4, 5.5, 5.7). Narration hours are from the
final render's manifests; the 7.3, 3.4 and 5.4 h in `docs/PRODUCTION-REPORT.md`
are the earlier `bf_emma` build.

**The final rendered MP4s and SRTs (Kokoro `af_heart`, all three courses, 259
lectures, about 4 GB) live at git tag `mp4/af_heart-2026-09-02`, formerly
branch `claude/mp4-builds`. They are deliberately kept out of `main`: video is
regenerable, and merging it would put 4 GB into every future clone. Never
merge that tag or branch into `main`.**

Sibling system `books/` (own CLAUDE.md, own pipeline) has seven KDP titles,
English and Simplified Chinese, with proofs built. Its gate is
`python3 books/pipeline/qc.py --book <slug>`; each English edition reports
`1 fail, 0 warn`, the `verified: false` sign-off. Finish publishing
`stop-guessing` before any other title (`docs/05-kdp-playbook.md` §1).

**What stands between the courses and submission to Udemy:**

1. James reads and signs off every lecture (`verified: true`). Nothing else
   may set it.
2. James captures the `[SCREENSHOT-NEEDED]` screenshots from his own accounts.
3. A session builds the missing downloadables: ai-for-pms A08
   to A12, and ai-ugc-ads B01 to B11. The landing copy promises 12 and 11
   artifacts and lectures say "Download A0x". One artifact per session.
4. James fixes listing details: Udemy titles are limited to 60 characters (per
   the 2026-09-04 listing session) and `ai-for-pms` is 71, `ai-agents-for-work`
   67. Keep the AI-disclosure sentence as the last line of every description.
5. James re-checks Udemy's current policy on AI narration (flagged in each
   `course.yaml`), decides whether `ai-agents-for-work` ships at about 3.6 h,
   and uploads the MP4 and SRT files from the tag above.

After any script edit, wipe `build/` and re-run the build for that course
(section 7 explains why); the narration cache makes that cheap.

A half-finished section is worth less than one finished lecture, and seven
three-chapter manuscripts are worth less than one finished book.

---

## 11. Git

`main` is the only long-lived branch; "Branching: one trunk" at the top of this
file says how to start, land and clean up. The repo holds three courses and the
`books/` system, and all of it lands on `main`. Do not commit `build/`, and
never merge the `mp4/af_heart-2026-09-02` tag (formerly branch
`claude/mp4-builds`) into `main`.
