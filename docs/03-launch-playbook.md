# Launch playbook

Building the course is half the job. This is the other half.

---

## 1. Title and search

Udemy's ranking weighs title keyword relevance first, and vague titles are a
documented cause of poor performance.

**Recommended:**

> AI Product Skills for PMs & Analysts: Spec, Evaluate & Ship AI Features

Why it works: leads with the searched term (*AI product*), names the audience
(*PMs, Analysts*), and promises capability (*spec, evaluate, ship*) rather than
topics.

**Avoid:** "Complete AI Masterclass for Project Managers 2026" — every one of
those words is contested by hundreds of courses and none of them is a capability.

Target keywords: `AI product management`, `AI evaluation`, `LLM evals`,
`RAG for product managers`, `AI PRD`.

---

## 2. Promo video (60–90 seconds)

> **2026-08-12 update:** the author has elected full-TTS delivery; the promo
> is narrated, not recorded on camera. The script and beats below still
> apply, "record it in your own voice and face" does not. This trades away
> some of the single highest-leverage human moment in the listing and will
> likely cost some conversion; the author has accepted that knowingly.
> Presence now has to be earned elsewhere: the personal sign-off in 0.1 and
> 11.5, and fast, genuine Q&A responses once the course is live.

Long promos that don't say what you'll learn are a documented failure. Keep it
tight, and **record it in your own voice and face**. This is the single
highest-leverage human moment in the whole listing.

```
[0:00–0:10]  THE PROBLEM — say it as a sentence they've thought themselves
  "You're responsible for an AI feature, and you can't tell if it actually
   works. Everyone in the room is waiting for you to say."

[0:10–0:25]  WHY IT'S HARD — the reframe, delivered fast
  "The methods you were trained on assume software that behaves the same way
   twice. This doesn't. Same input, different output — so your acceptance
   criteria stop working."

[0:25–0:45]  THE PROMISE — concrete, measurable
  "In this course you'll replace 'it seems to work' with '94% pass rate, three
   known failure modes'. You'll build an eval harness, a cost model, and a risk
   register — eleven artifacts you'll use at work, not notes."

[0:45–1:00]  CREDIBILITY — [INSTRUCTOR-INPUT] your real background, 2 sentences

[1:00–1:15]  WHAT IT'S NOT — this is your differentiator, don't skip it
  "This isn't a prompt library or a tour of this month's tools. It's the
   judgement work that survives the next model release."

[1:15–1:25]  CTA
  "First three lectures are free — watch 'The one idea' and decide from there."
```

Show real slides and a real artifact on screen while you talk. Do not use stock
footage.

---

## 3. Free preview selection

Set these three as free preview:

| Lecture | Why |
| --- | --- |
| **0.1 Welcome** | Your face and voice. Establishes a human made this. |
| **0.3 The one idea** | The strongest teaching in the course. Sells the rest. |
| **4.1 The eval mindset** | Proves depth mid-course, not just a nice intro. |

Most instructors preview only the intro. Previewing a mid-course lecture is what
converts skeptics who've been burned by thin courses.

---

## 4. Pricing and launch sequence

| Phase | Price | Purpose |
| --- | --- | --- |
| Week 0 (personal network) | $9.99 coupon | Honest early reviews |
| Weeks 1–2 | $24.99 | Enrollment velocity → ranking |
| Week 3+ | $74.99 | Standard |

**Do not blanket-give free coupons.** Free enrollments convert to reviews at a
much lower rate, and review count is a direct ranking input. Target interested
people who'll actually finish and leave honest feedback.

Aim for **10+ reviews in the first 30 days**. That's the threshold where social
proof starts doing work for you.

---

## 5. The first 30 days

Ranking factors, in the order they matter:

1. Title keyword relevance — fixed at launch
2. Enrollment velocity + conversion rate — driven by price and promo
3. Rating + review count — driven by the ask, below
4. **Completion rate** — most instructors ignore this
5. Instructor engagement — fully in your control

**Q&A within 24 hours.** Response time directly feeds bestseller ranking; slow
replies actively pull you down. This is the cheapest ranking lever you have.

**Ask for reviews at the right moment** — not at the end. Ask right after lecture
**0.4**, when they've just had the uncomfortable-discovery moment and feel the
value. A short, honest ask in the lecture text beats a popup.

**Protect completion rate:** lectures stay under 12 minutes, every section ends
in a workshop, and Section 0 delivers a real win in the first 15 minutes.

---

## 6. Ongoing

| Cadence | Action |
| --- | --- |
| Daily (first 30 days) | Answer Q&A |
| Within 48h | Act on critical feedback |
| **Quarterly** | Freshness pass — mandatory for AI topics |
| Each update | Announcement to enrolled students |

The quarterly pass is not optional. Model names, prices, and capabilities move
fast, and a confidently wrong price is the fastest way to lose credibility in
reviews. Sections 1.4, 2.6, 7.1 and 7.4 are the ones that decay first — check
those every quarter, and re-record if a number changed.

---

## 7. Courses 2 and 3

The pipeline is course-agnostic. To start the next one:

```bash
mkdir -p courses/<slug>/lectures
cp courses/ai-for-pms/course.yaml courses/<slug>/course.yaml
# edit metadata + curriculum, then write lectures
python3 pipeline/build.py --course courses/<slug>
```

Recommended order, based on the research in `00-strategy.md`:

1. **AI for PMs & Analysts** (this one) — highest willingness to pay, sells into
   Udemy Business, evergreen.
2. **AI UGC video/image ads** — hottest demand and the best visual wow factor,
   but budget for quarterly re-recording; the tools version-shift constantly.
3. **AI productivity workflows** — most saturated and lowest price ceiling. Build
   it last, and only with a sharp angle that the first two courses feed.

Cross-sell all three from each course's final lecture and resource pages.
