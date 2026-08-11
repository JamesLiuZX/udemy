---
name: write-lecture
description: Author one course lecture end to end, from the curriculum spec to a verified render. Use when writing, drafting, or rewriting a lecture for a course in courses/, when asked to "write lecture 4.2" or "do the next lecture", or when continuing work on a section. Handles script, slides, figures, render, visual check and QC.
---

# Write one lecture

Produce a single lecture to the repo's quality bar. One lecture, finished and
verified, beats three drafted.

Take the lecture id from the user (for example `4.2`). If they said "the next
one", find the first lecture in `course.yaml` with no matching file in
`lectures/`.

---

## Step 1. Read the spec before writing

```bash
python3 - <<'EOF'
import yaml
c = yaml.safe_load(open('courses/ai-for-pms/course.yaml'))
want = "4.2"                     # <-- set this
for s in c['sections']:
    for l in s['lectures']:
        if str(l['id']) == want:
            print('SECTION', s['id'], s['title'])
            print('GOAL   ', s.get('goal'))
            print('LECTURE', l)
EOF
```

Note the target duration and whether it is `hands_on` or carries an artifact.
Then read the two adjacent lectures in `lectures/` so the voice and the running
example stay continuous. The Fernhill serial (Ticket #4471 and everything
around it) runs through the whole course: read
`courses/ai-for-pms/story-bible.yaml` and quote its facts exactly rather than
inventing new ones. If the lecture needs a new story fact, add it to the bible
first. This section's story beat is in the bible's `timeline`.

---

## Step 2. Plan before drafting

Write down, in your head or to the user:

- **The one thing** a learner can do after this lecture that they could not before
- **The moment it lands**: the example, number or figure that makes it real
- **The cost**: where this technique is expensive, slow, or wrong
- **The opener**: pick a cold-open pattern from `docs/04-quality-bar.md` §3,
  different from the previous lecture's. Never open with the agenda.
- **6 to 9 slides** for a 7 minute lecture, one idea per slide

If you cannot name the one thing, the lecture is not ready to write.

---

## Step 3. Draft

Copy `courses/_template/lecture-template.md` and fill it in.

Keep front matter honest:
- `verified: false` always. Never set it true.
- Use `[INSTRUCTOR-INPUT: ...]` for anything requiring the instructor's real
  experience. Never invent a war story or a credential.

Narration pacing is 150 words per minute, so a 7 minute lecture is about 1,050
words. Vary the layouts: a lecture of eight `bullets` slides is a failure even if
every word is right.

Obey the narration rules in `CLAUDE.md` §4. The two that get violated most:
**narration must not restate the slide**, and **no em dashes**.

---

## Step 4. Add at least one real figure

A lecture with no picture is usually a lecture that has not found its idea.

- Quantities, spreads, thresholds, distributions: a ` ```figure ` block
  (`dotplot`, `histogram`, `sampling`). See `pipeline/figures.py`.
- Processes, architectures, dependencies: ` ```mermaid `.
- Structured comparison: a table.

Always pair with `figcap:` so it is numbered.

If an existing figure kind does not fit, add one to `figures.py` rather than
forcing the data into the wrong form or dropping the picture. Follow the rules in
`CLAUDE.md` §6, especially: no hover layer exists, so label directly.

---

## Step 5. Render and look

```bash
python3 pipeline/build.py --course courses/ai-for-pms --slides-only --only <id>
```

Convert several slides and **actually view them**:

```bash
D=build/ai-for-pms/work/<slug>/png
for n in 001 003 005; do
  ffmpeg -y -loglevel error -i $D/slide-$n.png -vf scale=1500:-1 /tmp/s$n.jpg
done
```

Read those .jpg files. Look for text past the frame edge, colliding labels,
figures too small or too large, prose broken mid-sentence, and dead regions that
look accidental rather than composed.

Fix and re-render until the slides read well. This loop is the job.

---

## Step 6. Build and gate

```bash
python3 pipeline/build.py --course courses/ai-for-pms --only <id>
python3 pipeline/qc.py    --course courses/ai-for-pms
```

Target: **zero warnings**, and no failures except the sign-off and
`[INSTRUCTOR-INPUT]` gates. Those two are supposed to fail.

Common warnings and what they actually mean:

| Warning | Real fix |
| --- | --- |
| narration repeats N% of the slide text | Rewrite the narration to argue, not restate |
| estimated N min, consider splitting | Split it. Long lectures hurt completion rate |
| N chars of slide text, dense | The slide is doing two jobs. Make it two slides |
| filler/LLM-tell phrases | Delete them |
| possible slide typos | Fix, or add genuine domain terms to `ALLOW` in `qc.py` |

Check the reported duration against the `course.yaml` target. More than about two
minutes over means cut, not shrink the font.

---

## Step 7. Report honestly

Say which lecture is done, its duration and slide count, whether you viewed the
renders, and anything you left unresolved. If you did not visually check the
slides, say that plainly rather than implying it is finished.

Do not mark a lecture complete because it compiled.
