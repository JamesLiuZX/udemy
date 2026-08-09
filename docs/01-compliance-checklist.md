# Pre-submission compliance checklist

Run `python3 pipeline/qc.py --release` to auto-check everything marked **[auto]**.
The rest are manual sign-offs. Do not submit with any box unchecked.

---

## A. AI policy — the takedown risks

- [ ] **[auto]** Course description contains verbatim:
      `This course contains the use of artificial intelligence.`
- [ ] **[auto]** Disclosure appears at the **end** of the description (recommended placement).
- [ ] **[auto]** Every lecture has `verified: true` in front-matter — meaning *you* read
      the script and personally stand behind every factual claim in it.
- [ ] **[auto]** No lecture contains an unfilled `[INSTRUCTOR-INPUT]` marker.
- [ ] **Manual:** You can defend any claim in this course in a live conversation with a
      skeptical expert. If you can't, cut it or learn it.
- [ ] **Manual:** Instructor presence exists and is genuine — see §B.
- [ ] **Manual:** Every external fact (pricing, model capability, regulation) was checked
      against a primary source within the last 30 days. AI topics decay fast, and a
      confidently wrong price is the #1 credibility killer in reviews.

> Why this matters: Udemy may decline a course at review, disable it after publication,
> or suspend the account for repeated violations. The disclosure line costs nothing.
> Skipping it can cost the account.

---

## B. Instructor presence — the "personal connection" requirement

Policy states that even high-quality audio/video "can lead to a poor learner experience
if it lacks meaningful instructor participation, engagement, or presence."

Minimum bar this project targets:

- [ ] **Promo video** — your real voice and, ideally, your face. This is the single
      highest-leverage human moment in the whole course.
- [ ] **Lecture 0.1 (welcome)** — your real voice. Who you are, what you've shipped,
      why you're qualified.
- [ ] **Every section intro/outro** — your real voice (~30–60s each).
- [ ] **Capstone walkthrough** — your real voice; this is where judgement shows.
- [ ] **Q&A** — you personally answer, within 24h. This is presence *and* it feeds the
      bestseller ranking.
- [ ] At least 6 `[INSTRUCTOR-INPUT]` war stories filled with things that actually
      happened to you, including at least two failures.

Everything else may be TTS. Budget: ~35–50 minutes of real recording for a 9-hour course.

---

## C. Technical standards

- [ ] **[auto]** ≥ 30 minutes total video
- [ ] **[auto]** ≥ 5 lectures
- [ ] **[auto]** Every video ≥ 720p (we ship 1080p)
- [ ] **[auto]** 16:9 horizontal on every video
- [ ] **[auto]** Audio present on every lecture
- [ ] **[auto]** Audio on both L and R channels (true stereo, not one dead channel)
- [ ] **[auto]** Integrated loudness within −14 to −18 LUFS
- [ ] **[auto]** No true-peak clipping above −1 dBTP
- [ ] **[auto]** No slide typos (spell pass)
- [ ] **[auto]** Narration does not simply read the slides (overlap threshold)

---

## D. Landing page

- [ ] Title uses the keywords learners actually search, and is specific — vague titles
      are a documented cause of poor performance
- [ ] Promo video is short and states clearly what the learner will be able to *do*
- [ ] 4–7 learning outcomes, not 15–20 (too many outcomes correlates with lower scores)
- [ ] Outcomes are capability statements ("Write acceptance criteria as eval
      thresholds"), not topic names ("Evaluation")
- [ ] Requirements section is honest — no false "no experience needed" if untrue
- [ ] Target audience section names the job titles explicitly
- [ ] Disclosure line present at the end of the description

---

## E. Curriculum hygiene

- [ ] Free preview lectures set: **0.1**, **0.3**, and one high-value mid-course lecture
      (recommend **4.1**). Preview must showcase teaching quality, not just intro fluff.
- [ ] Quick win delivered inside the first 15 minutes
- [ ] Every section ends with a workshop or artifact
- [ ] All 11 downloadable artifacts attached to the correct lectures
- [ ] Captions (.srt) uploaded for every lecture — accessibility *and* watch-time
- [ ] No lecture over 12 minutes without a strong reason

---

## F. Post-launch operating cadence

- [ ] Q&A response target: **< 24 hours** (directly feeds ranking)
- [ ] Feedback acted on within 48 hours
- [ ] Content freshness review: **quarterly** (mandatory for AI topics)
- [ ] Announcement to enrolled students on every substantive update
