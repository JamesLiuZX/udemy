# Strategy: How this course gets to "wow" instead of "passable"

> Everything in this document is derived from research into why AI-produced courses
> get rejected, refunded, or 2-starred — and what the top-decile courses do instead.
> Sources are listed at the bottom.

---

## 1. The constraint that shapes everything

**Udemy does not accept courses that are entirely AI-generated.**

The policy language is specific and worth internalising, because it tells you exactly
where the line is:

- AI tools may be used to **"enhance and support the expertise of the instructor"**
- AI **"cannot replace the instructor's subject matter knowledge and expertise"**
- Fully AI-generated courses with minimal instructor input **"fail to provide the
  personal connection learners seek"**
- Explicitly: *"even high-quality video and audio content can lead to a poor learner
  experience if it lacks meaningful instructor participation, engagement, or presence"*

Enforcement is real and escalating: decline at review → disable content
post-publication → **account suspension** for repeated violations.

### What is actually allowed

This is the part most people get wrong in both directions. Udemy **does** accept
"audio and video instruction created using quality text-to-speech (TTS) and
artificial intelligence (AI) programs."

So the banned thing is not synthetic narration. **The banned thing is the absence of
a human expert behind the content.**

### The line, stated plainly

| Allowed | Not allowed |
| --- | --- |
| TTS narration of *your* script | A course whose content you cannot personally defend |
| AI-assisted scripting, editing, slide generation | Prompting an LLM for a curriculum and shipping it unread |
| AI-generated diagrams and B-roll | AI-generated "facts" you never verified |
| AI voice for bulk lectures | Zero instructor presence anywhere in the course |

**Design consequence:** this repo treats AI as a *production* multiplier, never as the
source of expertise. Every claim in a script is yours to verify. Every lecture that
depends on lived experience is marked `[INSTRUCTOR-INPUT]` and will fail the QC gate
until you fill it in. That is deliberate friction.

---

## 2. Mandatory disclosure

If AI tools are used, you **must** disclose in the course description. Required triggers:

- content-generation tools used to write scripts or lecture content
- video/audio tools generating artificial speech meant to emulate human instruction

Recommended placement: **end of the course description.**

Exact phrase to include:

> This course contains the use of artificial intelligence.

`pipeline/qc.py` fails the build if this string is missing from `course.yaml`'s
description. Non-negotiable — this is the cheapest possible insurance against takedown.

---

## 3. Hard technical gates (auto-checked)

| Requirement | Value | Enforced by |
| --- | --- | --- |
| Minimum video content | 30 minutes | `qc.py` |
| Minimum lectures | 5 | `qc.py` |
| Resolution | ≥ 720p (we ship **1080p**) | `qc.py` |
| Aspect ratio | 16:9, horizontal | `qc.py` |
| Audio | present on every lecture, **both** L/R channels | `qc.py` |
| Audio quality | clear, non-distracting | `qc.py` loudness check |

We exceed rather than meet these: 1080p, −16 LUFS normalised stereo, 30fps.

---

## 4. Why most AI-assisted courses get bad reviews

Research into learner complaints surfaces a consistent, specific list. These are the
failure modes we engineer against:

| Failure mode | Our countermeasure |
| --- | --- |
| **Robotic delivery / reading the slides aloud** | Narration and slides are *deliberately different content*. Slides carry the skeleton; narration carries the argument. `qc.py` flags lectures where narration overlaps slide text too heavily. |
| **AI images with extra limbs, misspelled text** | Zero generative raster images in the core deck. All visuals are typeset HTML, KaTeX, and Mermaid — deterministic and typo-free by construction. |
| **Typos on slides** | Automated spell/lint pass over every slide before render. |
| **Low energy** | Scripts are written for the ear: short sentences, second person, direct address. Prosody markers drive TTS pacing. |
| **Factual errors nobody reviewed** | Every lecture front-matter carries `verified: false` until you sign it off. QC fails on unverified lectures in a release build. |
| **Too long / unfocused (25h+ overwhelms)** | Hard cap: 8–10 hours, ~80 lectures, average 7 minutes. |
| **No hands-on work** | 11 downloadable artifacts; every section ends in a workshop. |
| **"I could have just used ChatGPT"** | The course teaches judgement and process, not information retrieval. See §6. |

---

## 5. What top-decile courses do (and we copy)

- **A quick win in the first minutes.** Engagement in the opening lectures
  disproportionately drives ratings and completion. Section 0 delivers a usable skill
  in under 15 minutes.
- **Project-based and hands-on**, with downloadable templates — repeatedly cited as
  the differentiator in best-seller analyses.
- **Fast instructor response.** Response time to Q&A directly feeds the bestseller
  ranking; slow replies actively pull you down. Target < 24h.
- **Quarterly freshness updates.** Ranking rewards recency; AI topics decay fast.
- **4.5+ rating maintained**, acting on feedback quickly.

### Ranking factors we optimise for

1. Title keyword relevance
2. Enrollment velocity + conversion rate
3. Average rating + review count
4. **Completion rate** ← most instructors ignore this; short lectures and momentum help
5. Instructor engagement metrics

---

## 6. Positioning: why *this* course, and not the 400 others

### The saturated version (do not build this)

"AI for Project Managers — learn ChatGPT prompts to write user stories faster!"

This is commodity. It's a prompt list. A learner genuinely *could* replace it with an
afternoon of ChatGPT, and the reviews will say exactly that. Market research confirms
the generic angle is crowded: *"if your AI PM value proposition is 'I added AI features
to our product', that's no longer differentiated."*

### The differentiated version (what we build)

**Positioning statement:**

> For product managers, project managers, and analysts who are now accountable for AI
> features they don't feel qualified to judge. This course teaches you to *specify,
> evaluate, cost, and de-risk* an AI feature — the judgement work that doesn't
> disappear when the model gets better.

### The one idea the course is built around

> **An AI feature is a probability distribution, not a function.**
> You cannot write acceptance criteria for it the way you write them for a button.
> You write them as **evaluation thresholds on a golden dataset**.
> This single shift is why most AI features die in QA.

Everything in the curriculum radiates from that. It is concrete, teachable, immediately
useful, and — critically — **not** something a learner extracts from a chat session,
because it's a process change, not a fact.

### Why this beats the alternatives commercially

| Angle | Demand | Defensibility | Udemy Business fit |
| --- | --- | --- | --- |
| **AI for PMs & Analysts** | High, growing (AI-driven project roles +42% since 2024; AI/big-data skill demand +87% to 2030) | **High** — frameworks outlive tool churn | **Strong** — corporate seats, where the real revenue is |
| AI UGC video ads | Very high right now | **Low** — Veo/Sora/Arcads/Creatify version-shift constantly; needs quarterly re-shoots | Weak |
| AI productivity workflows | Broad | **Lowest** — most saturated, lowest price ceiling | Medium |

The AI-in-project-management market is growing ~19.5% YoY ($3.58B → $4.28B, 2025→2026),
and 70% of surveyed UK project professionals report their org already uses AI. The
audience exists, has budget, and is anxious — the best combination for course sales.

---

## 7. The "wow" mechanism

Wow is not production polish. Polish is table stakes. Wow is **"I can do something on
Monday that I couldn't do on Friday, and it visibly makes me better at my job."**

Concretely, the learner leaves with **11 artifacts** they can use at work immediately
and put in a portfolio:

1. AI Feature PRD (acceptance criteria as eval thresholds)
2. Golden dataset spec + starter set
3. Working eval harness — spreadsheet version *and* 30-line Python version
4. Evaluation rubric with inter-rater calibration protocol
5. RAG system design doc
6. Retrieval quality scorecard
7. Agent scoping + blast-radius worksheet
8. Token-level unit economics model
9. Model selection scorecard
10. AI risk register + red-team checklist
11. AI feature metric tree + instrumentation plan

Every one is a real deliverable in a real job. That is the wow.

### Three deliberate "wow moments"

- **§0.4 (minute 12):** learner scores a real AI output against a rubric and discovers
  their own judgement is inconsistent. Visceral, immediate, sets up the whole course.
- **§6.3:** the reliability math of agents — `0.95^10 = 0.60`. One slide that
  permanently changes how they scope automation.
- **§7.5:** the margin trap — a live model showing a feature that loses money per
  power user. Most PMs have never seen this computed.

---

## 8. Production principles

1. **Single source of truth.** One `.md` per lecture holds narration, slides, and
   metadata. Nothing is authored in two places.
2. **Deterministic visuals.** Typeset HTML/KaTeX/Mermaid. No generative image artifacts.
3. **Narration ≠ slide text.** Enforced by QC.
4. **Everything regenerable.** Change a script line, rebuild that lecture only.
5. **Quality gates are code**, not vibes. `qc.py` blocks the release build.
6. **Human sign-off is a required field**, not an honour system.

---

## Sources

- [Course Quality Checklist: Use of AI – Udemy](https://support.udemy.com/hc/en-us/articles/30999984483607-Course-Quality-Checklist-Use-of-AI)
- [AI Policy Clarification: Course Quality Standards and New Disclosure Requirements – Udemy Community](https://community.udemy.com/en/discussion/161910/ai-policy-clarification-course-quality-standards-and-new-disclosure-requirements)
- [Udemy Course Quality Checklist](https://support.udemy.com/hc/en-us/articles/229604988-Udemy-Course-Quality-Checklist)
- [Video Standards – Udemy](https://support.udemy.com/hc/en-us/articles/229232767-Video-Standards)
- [Audio Standards – Udemy](https://support.udemy.com/hc/en-us/articles/229232367-Audio-Standards)
- [Course description: Rules and guidelines – Udemy](https://support.udemy.com/hc/en-us/articles/33490280024087-Course-description-Rules-and-guidelines)
- [5 mistakes new Udemy instructors make – Six Figure Instructor](https://sixfigureinstructor.com/learning-center/5-mistakes-new-udemy-instructors-make/)
- [common mistakes – Udemy Instructor Community](https://community.udemy.com/en/discussion/21399/common-mistakes)
- [5 Critical Success Factors Behind a Best-Selling Course – Sarah Cordiner](https://sarahcordiner.com/the-5-critical-success-factors-behind/)
- [Udemy Algorithm Decoded: How Course Rankings Really Work](https://skooldemyblog.com/udemy-algorithm-2/)
- [The AI Content Explosion: What Your Learners Actually Think – Dr Philippa Hardman](https://drphilippahardman.substack.com/p/the-ai-content-explosion-what-your)
- [College Professors Are Turning to ChatGPT... Student Asked for a Refund – Entrepreneur](https://www.entrepreneur.com/business-news/student-asks-for-money-back-after-professor-uses-chatgpt/491640)
- [AI PM Job Market in 2026 – Institute of Project Management](https://www.institutepm.com/knowledge-hub/ai-pm-job-market-2026)
- [AI in Project Management Global Market Report 2026](https://www.thebusinessresearchcompany.com/report/ai-in-project-management-global-market-report)
- [Best AI Courses for Project Managers Using Generative AI – Research.com](https://research.com/online-courses/artificial-intelligence/best-ai-courses-for-project-managers-using-generative-ai)
- [Udemy Introduces New Instructor Innovations – EdTech Innovation Hub](https://www.edtechinnovationhub.com/news/udemy-launches-new-instructor-innovations-reinforcing-the-role-of-human-expertise-alongside-ai)
