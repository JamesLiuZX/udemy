---
name: new-course
description: Scaffold and position a second or third course in this repo, reusing the existing pipeline and design system. Use when starting a new course, adding a course, or when asked about the AI UGC video ads course or the AI productivity workflows course.
---

# Start a new course

The pipeline is course-agnostic. A new course is a new `courses/<slug>/`
directory, not new machinery. Do not fork or duplicate `pipeline/` or `theme/`.

---

## Step 1. Pressure-test the topic before building

Research established this order, and the reasoning still holds:

1. **AI for PMs and Analysts** (built). Highest willingness to pay, the only one
   that sells into Udemy Business, evergreen because frameworks outlive tools.
2. **AI UGC video and image ads.** Hottest demand and the best visual payoff,
   since students see ads they made. The catch is tool churn: the tools version
   shift constantly, so budget for a re-record every quarter and expect a shorter
   shelf life. Weak fit for Udemy Business.
3. **AI productivity workflows.** Broadest audience, most saturated, lowest price
   ceiling, hardest to differentiate.

Before writing a curriculum, answer in one sentence each:

- Who is the learner, and what are they accountable for that they feel unqualified to do?
- What is the **one idea** the whole course radiates from?
- What do they walk away holding? Artifacts, not notes.
- Why can this not be replaced by an afternoon with ChatGPT?

If the last answer is weak, the course will get "I could have just asked an LLM"
reviews. Sharpen the positioning before writing a single lecture.

Course #1's answer, as the standard to match: *an AI feature is a distribution,
not a function, so acceptance criteria must be evaluation thresholds on a golden
dataset.* Concrete, teachable, and a process change rather than a fact.

---

## Step 2. Scaffold

```bash
SLUG=ai-ugc-ads
mkdir -p courses/$SLUG/lectures
cp courses/ai-for-pms/course.yaml courses/$SLUG/course.yaml
```

Then edit `course.yaml`:

- `slug`, `title`, `subtitle`, `description`
- `big_idea`, `audience`, `prerequisites`
- `outcomes`: keep to **4 to 7**. More correlates with lower course scores.
- `pricing`, `primary_keywords`, `free_preview_lectures`
- Keep `ai_disclosure` exactly as it is, and keep it as the final line of
  `description`.
- Rewrite `sections` entirely.

### Curriculum shape that works

- 8 to 10 hours total. 25 hours overwhelms and hurts completion.
- Lectures average 7 minutes, hard cap 12.
- Section 0 delivers a usable win inside the first 15 minutes.
- Every section ends in a workshop or an artifact.
- Section intros and outros are 1 to 2 minutes and are recorded in the
  instructor's real voice. They are the cheapest way to satisfy the presence
  requirement.

Check the total after drafting:

```bash
python3 - <<'EOF'
import yaml
c = yaml.safe_load(open('courses/ai-ugc-ads/course.yaml'))
L = [l for s in c['sections'] for l in s['lectures']]
t = sum(l['duration'] for l in L)
print(f"{len(L)} lectures, {t} min = {t/60:.2f} h")
EOF
```

---

## Step 3. Landing page and compliance

Work through `docs/01-compliance-checklist.md` and `docs/03-launch-playbook.md`.
The parts people skip and regret:

- The disclosure line, verbatim, at the end of the description.
- Free preview set to the welcome, the big-idea lecture, and one strong
  mid-course lecture. Previewing only the intro converts badly.
- A promo video in the instructor's real voice and face.

---

## Step 4. Build Section 0 first, completely

Use the **`write-lecture`** skill, one lecture at a time, to verified renders.
Do not draft a whole section before rendering any of it.

For a tool-heavy course such as UGC ads, add a note in `course.yaml` recording
which lectures name specific tools and versions. Those are the ones the quarterly
freshness pass has to re-check, and a confidently wrong price or a dead feature is
the fastest way to lose credibility in reviews.
