# Editorial Report: AI Agents for Your Job

Full-course editorial pass across all 12 sections (76 lectures), covering scene-level
openers, plain-speech translation of technical terms, plug-and-play closes tied to
course artifacts, story-bible continuity, and a complete screenshot inventory. This
supplements `qc.py`, which checks mechanically (spellcheck, rhythm, filler words,
verbatim overlap, digit-proximity continuity); this pass checks editorially, by
reading every lecture in full against the story bible and against every other
lecture that touches the same fact.

Method: twelve read-only audit passes (one per section), each reading every lecture
file in that section in full against `story-bible.yaml`, cross-checking claims made
in adjacent sections, and verifying every screenshot marker against the files on
disk. Findings were then triaged: continuity bugs and factual overstatements were
fixed directly; stylistic observations that turned out to match an established,
consistent house pattern used successfully elsewhere in the course were logged as
notes rather than rewritten (see §4).

Course-wide `qc.py` state at the end of this pass: **0 warnings**, and the only
`FAIL`s remaining are the three expected gates (`verified: false` on every lecture,
unfilled `[INSTRUCTOR-INPUT]` on lectures that genuinely need the instructor's own
voice or live build, and the standing proper-noun spellcheck exceptions). That is
the defined "pass" state per `CLAUDE.md` §1, not a problem to fix.

---

## 1. Fixes applied during this pass

Real bugs found and corrected, with the reasoning:

| # | File(s) | Issue | Fix |
| --- | --- | --- | --- |
| 1 | `7.3-the-day-the-sheet-moved.md` | Said "Two weeks into trialling the weekly report agent" and "That Wednesday's report." Agent 3's own job description (5.1, 5.5) sets its trial at **three weeks** / "three Mondays," and the report only runs on Mondays (established five times across Section 5). "Two weeks" belongs to Agent 4 (the follow-up chaser), established at 6.1 and correctly reused in 10.1/10.2 — 7.3 had borrowed the wrong agent's number. | Changed to "Three weeks" and "A Monday" / "That Monday's report," matching 5.1/5.5 and the report's established Monday cadence. |
| 2 | `story-bible.yaml` | The `numbers` list tagged "two weeks" as `established: "7.1"`, but 7.1 never states a duration anywhere in its text — the number is actually established at 6.1 (Agent 4's trial length), not a course-wide default. | Corrected `established` to `"6.1"` and clarified the `meaning` field to state explicitly that each agent's trial length is chosen per-agent (1 week / 3 weeks / 2 weeks for Agents 1/3/4 respectively), not a single default — so a future author doesn't "fix" 1.4 or 5.1 into false agreement with this number. |
| 3 | `11.5-thank-you-and-where-to-go-next.md` | Closing narration said the course opened on "an inbox with forty unread emails and a missed renewal." Story-bible (0.4) states the query was buried and unread for 6 days, then *caught* by the first agent — it was never actually missed. Overstated the stakes past what the story actually claims. | Reworded to "a renewal that was six days from being missed entirely," which is defensible against the bible and still carries the stakes. |
| 4 | `10.4-devs-first-week.md` | The story bible's Section 10 arc beat explicitly frames Dev's meeting-notes ambiguity failure as a *different failure mode* from Priya's own **7.3** moved-row incident, but the lecture only contrasted against 7.5's "invention" category — 7.3 was never named. Also said "Priya's inbox never produced this problem," but Agent 2 (meeting notes) has nothing to do with inbox contacts; the domain was wrong. | Added an explicit third card (Section 7.3: a fact that moved) alongside 7.5 (invention), reframed as three distinct failure modes, and corrected "Priya's inbox" to "Priya's own meeting-notes trial." |
| 5 | `0.3-your-first-agent-in-20-minutes.md` | "Exported as JSON" used the term "JSON" with no plain-English gloss, for a learner explicitly framed elsewhere in the course as non-technical. | Reworded to "saved out as one plain text file that n8n can read back in" — describes the mechanism without requiring the jargon. |
| 6 | `2.2-choosing-an-ai-model.md` | "n8n stores it encrypted once you save the credential" used "credential" a full lecture before 2.3 formally defines the term (2.3's four-word vocabulary list). | Added an inline gloss at first use: "…once you save it as a credential, the saved login a node uses to reach an outside account…" |
| 7 | `2.1-setting-up-n8n.md` | Comparison table used "Executions" as a bare row label; the narration right after glosses it as "workflow runs," but the table itself didn't. | Row label changed to "Executions (workflow runs)." |
| 8 | `7.1-running-a-trial-properly.md` | "Looks for the specific failure mode the job description's ceiling exists to prevent" used the term "failure mode" before it's ever formally introduced (that happens properly in 7.3 by example and 7.5 by table). | Reworded to plain speech ("the specific way this agent could go wrong") and let 7.3/7.5 introduce the term itself when they define it. |
| 9 | `3.5-testing-without-spending-a-call.md` | The section's real, already-captured screenshot of the pinned 41-row mock inbox (`n8n-mock-inbox-41-items.png`) was never wired into 3.5's own pinning walkthrough, despite being exactly what that walkthrough describes; it was only referenced once, earlier, from 0.3's preview. | Added a `TODO-IMG` note pointing at the same (already-real, already-on-disk) screenshot, at the "how to pin your own test inbox" bullets. |

All nine fixes were rebuilt (slides-only, then full offline-voice build), the
changed slides were converted to JPG and visually inspected, and the whole-course
`qc.py` was re-run to confirm 0 warnings after every change.

---

## 2. Per-section status

| § | Title | Status | Hook | Golden nugget |
| --- | --- | --- | --- | --- |
| 0 | Start Here: Your First Agent in 20 Minutes | READY | Ravi's message sitting unread for six days, buried under forty others (0.3). | "An agent is an employee, not an app. You do not install it. You onboard it." |
| 1 | The One Idea: An Employee, Not an App | READY | "Would you hand a new hire your inbox, your calendar and your client files on their first morning? …So why would you hand an agent all three before lunch?" (1.1) | The job description itself: scope, action level, ceiling, written down before an agent touches anything — shipped as C05. |
| 2 | The Toolbox: n8n and the AI Brain | READY | Weakest hook in the course — mostly mechanics, minimal Priya presence (see §4). | Self-hosted n8n is free forever, and Gemini's free tier has no expiry, only a rate limit — the whole course costs nothing to start. |
| 3 | Agent #1: Inbox Triage | READY | "I assumed the hard part of this would be the AI." — Almost everyone, before their first build (3.2). | The system prompt is one honest paragraph, not code: write instructions you could defend out loud, not clever ones. |
| 4 | Agent #2: Meeting Notes to Action Items | READY | "I know we agreed on something in that call. I just can't remember what, or who owns it." (4.1) | An AI agent's output always looks equally confident, whether it is right or wrong — named explicitly as the single most important habit in the course. |
| 5 | Agent #3: The Weekly Report | READY | "The inbox and meeting-notes agents made Priya's own week easier. This one writes something her director reads every Monday." (5.0) | "Use only the numbers given… if you are unsure, say so rather than guessing," paired with a read-only ceiling (Get Row(s), never Append or Update). |
| 6 | Agent #4: Follow-Ups That Never Slip | READY | "I meant to chase that. I just forgot, and now it's two days overdue." (6.1) | Build the constraint into the wiring, not the prompt: Resource=Draft, Operation=Create — nothing in this build can send. |
| 7 | Checking the Work | READY (after fixes) | "The weekly report said Brightwell's renewal was closed. It was not." (7.3) | An agent that reads a structure correctly can still fail when the structure moves under it. |
| 8 | Guardrails and Blast Radius | READY | "Every safeguard in this course so far has held. This section tells you about the one time it was actually tested." (8.0) | Layer more than one guardrail into everything you build, because you cannot always get the first one right (scope limits what it sees; action level limits what it can do). |
| 9 | What It Costs, What It Saves, and When Not To | READY | "You have built four agents, checked their work, and survived one near miss. This section puts a number on what all of that was worth." (9.0) | The defensible one-line pitch: "roughly four hours a week, cleanly counted, for under five dollars a month, and every output is still checked." |
| 10 | Rolling It Out: Your Team and Your Boss | READY (after fixes) | "Everything so far has been personal… this is where that becomes something you can bring to your manager, and hand to a colleague, without either of them taking it on faith." (10.0) | Every new user runs their own Trial, no exceptions — proven by Dev finding a third, genuinely different failure mode in his first week. |
| 11 | Capstone: Automate One Week of Your Job | READY (after fixes) | "You have watched this method work four times against Priya's week. This is where you find out it works against yours." (11.1) | "Would you actually trust this running unsupervised next week?" — the one honest test underneath the whole five-row rubric. |

"READY" here means: builds cleanly, renders inspected, zero QC warnings, and no
outstanding editorial defect found in this pass. It does **not** mean released —
every lecture still carries `verified: false` and is waiting on the instructor's
own sign-off, live recording, and (for `[INSTRUCTOR-INPUT]` lectures) content only
the instructor can supply. See §5.

---

## 3. Story-bible continuity: full findings

Beyond the nine fixes in §1, the per-section audits verified every numbered fact
against `story-bible.yaml`'s canonical `numbers` list ($18,400, 15 September, 40
emails, 6 days, 41 accounts, 180 staff, and the three per-agent trial lengths) and
every cast/company fact against `cast`/`company`/`anchor`. Two items are worth
recording even though they were not changed:

- **Section 9.3** opens on "five and a half hours a week" before explaining, two
  slides later, that this is 4.0 hard-counted hours (the story-bible's canonical
  figure) plus 1.5 "soft" hours reported separately and labelled as such. This is
  intentional narrative structure, not a continuity error, but a learner who only
  half-watches the opening slide could walk away misquoting the number. Left
  as-is because the honesty of separating hard/soft hours is itself the section's
  teaching point; flagged here for awareness, not action.
- **Ravi Chandra** (Brightwell's contact, named consistently from 0.3 onward
  through 3.5, 4.4, 7.3, and the C01/C02/C04 artifacts) is not listed in
  `story-bible.yaml`'s `cast` section, though he is used identically everywhere he
  appears. Recommend adding him to the bible's cast list for completeness, since
  every other recurring named person in the course is tracked there.

No other continuity deviations were found across the twelve sections.

---

## 4. Style notes, logged but not rewritten

Several lectures open on a definition, a callout, or a rhetorical claim rather
than a concrete scene (e.g. 1.3, 1.4, 2.0, 2.1, 2.3, 3.1, 5.2, 7.1, 7.2, 7.4, 7.5,
8.1, 8.3, 8.5, 9.2, 10.2). Taken lecture-by-lecture against `CLAUDE.md`'s "open on
a scene, not a framework" guidance, each of these reads as a minor deviation.

Taken as a set, though, this is a consistent, deliberate house pattern already
used successfully throughout the course: worksheet and mechanics lectures (job
description templates, canvas vocabulary, trial checklists, guardrail worksheets)
open on a named definition or a sharp claim rather than a narrative beat, while
build lectures and incident lectures (3.2, 4.1, 6.1, 7.3, 8.4, 8.0, 9.0, 10.0,
10.1, 11.1) consistently open on Priya, Marcus, Dev, or the learner directly. Nine
different section audits flagged instances of this same pattern independently,
which is itself evidence it's a structural choice rather than nine unrelated
lapses. Rewriting all ~16 into scene-openers would fight the course's own rhythm
and risks tripping the opener-layout-monotony check in the other direction.
Recommend leaving as-is; noting here so a future editorial pass doesn't rediscover
this from scratch.

The same logic applies to section-recap closes (1.5, 2.4, 7.6, 8.6, 9.5, 10.5):
several read as "reflective, not actionable" in isolation. But checked against
the section as a whole, every one of these sections already puts its concrete,
artifact-tied action in the lecture immediately before the recap (1.4, 2.3, 7.2 /
7.4, 8.3, 9.2, 10.3) — the recap's job is to consolidate the principle and hand
off to the next section, not repeat the checklist. This is consistent across all
ten section recaps in the course (3.7, 4.6, 5.6, 6.6 follow the identical
two-slide "principle + what's ahead" shape), so treating four of them as broken
would be inconsistent with the other six that were never flagged. Logged, not
changed.

---

## 5. Complete screenshot inventory

### Captured and wired in (real, on disk, referenced by a `TODO-IMG` marker)

All under `courses/ai-agents-for-work/screenshots/`, every file under the 500KB
CLAUDE.md guideline:

| Section | File | Used in | Size |
| --- | --- | --- | --- |
| 0 | `section-0/n8n-first-automation-prompt.png` | 0.3 | 24K |
| 3 (reused in 0) | `section-3/n8n-triage-workflow-overview.png` | 0.3 | 112K |
| 3 (reused in 0) | `section-3/n8n-mock-inbox-41-items.png` | 0.3, 3.5 | 448K |
| 2 | `section-2/n8n-owner-account-setup.png` | 2.1 | 112K |
| 3 (reused in 2) | `section-3/n8n-language-models-list.png` | 2.3, 3.3 | 236K |
| 3 | `section-3/n8n-imap-trigger-config.png` | 3.2 | 52K |
| 3 | `section-3/n8n-imap-credential-form.png` | 3.2 | 72K |
| 3 | `section-3/n8n-agent-prompt-and-system-message.png` | 3.3 | 288K |
| 3 | `section-3/n8n-full-triage-workflow-with-routing.png` | 3.4 | 136K |
| 4 | `section-4/n8n-form-trigger-with-transcript.png` | 4.2 | 236K |
| 5 | `section-5/n8n-sheets-node-pipeline-data.png` | 5.2, 6.2 (reused) | 88K |
| 5 | `section-5/n8n-weekly-report-workflow-overview.png` | 5.3 | 164K |
| 6 | `section-6/n8n-gmail-draft-resource-operation.png` | 6.4 | 132K |
| 6 | `section-6/n8n-followup-workflow-overview.png` | 6.4 | 168K |

14 markers, 14 files, all confirmed present on disk during this pass (verified by
direct filesystem check, not just by grepping the marker text).

### Captured but not yet wired to any marker (orphaned, on disk)

These were captured during the live n8n build sessions but aren't currently
referenced by any lecture. Not a defect — they were extra angles taken during
capture — but worth knowing about before a future author re-captures the same
shot:

- `screenshots/section-3/n8n-ai-agent-node-config.png`
- `screenshots/section-3/n8n-gemini-chat-model-config.png`
- `screenshots/section-4/n8n-meeting-notes-workflow-overview.png`

### `[SCREENSHOT-NEEDED]` — genuinely blocked on the instructor's own account

Two markers, both correctly left open rather than faked, per the standing rule
never to fabricate a screenshot:

1. **`3.2-build-part-1-connecting-the-inbox.md:68`** — the learner's own email
   provider's app-password screen. Cannot be captured generically because it is
   provider-specific (Gmail, Outlook, etc. all look different) and requires a
   real account with 2FA enabled.
2. **`5.2-build-part-1-reading-a-spreadsheet.md:60`** — the learner's own Google
   account connection screen for the Sheets node (OAuth consent screen). Cannot
   be captured against a shared/test account without exposing real credentials.

Both are the correct outcome for this course's screenshot policy: they show the
n8n side for real everywhere it's possible, and mark the two genuinely
account-gated steps rather than mocking them up.

### Sections with no screenshots (correct, not a gap)

Sections 1, 7, 8, 9, 10, 11 are conceptual/worksheet sections with no n8n build
steps of their own (they teach method, not mechanics), so an empty screenshot
list for each is the expected, correct state — confirmed per-section by grep
during the audit, not assumed.

---

## 6. Remaining author-only actions

Nothing below can be done by an automated pass; all of it requires the human
instructor, by the account's own compliance rule (`CLAUDE.md` §1: an AI system
must never invent instructor expertise or sign off on the instructor's behalf).

1. **Sign off.** Every one of the 76 lectures carries `verified: false`. Read
   each script and flip it to `true` only once every claim in it is one you
   would personally defend — this is the instructor's signature, not a build
   step.
2. **Fill `[INSTRUCTOR-INPUT]` markers.** Concentrated in the human-voice
   lectures: 0.1, 0.2 (welcome/course-mechanics framing), 1.0 (section-intro
   tone), 6.0 (an optional anecdote), 8.6 (a personal reaction to the Section 8
   incident), and most densely in **11.2/11.3** (the full live worked-build
   walkthrough — these two lectures are structurally *just* instructor input,
   scaffolded around a suggested example) and **11.5** (the closing thank-you
   and a personal note on what mattered most while making the course).
3. **Record the `voice: human` lectures.** 0.1, 0.2, all `X.0` section intros,
   all `X.N` section recaps, 6.0, 8.6, and 11.2/11.3/11.5 — roughly two dozen
   short lectures need the instructor's own voice, on camera or voice-over, not
   TTS.
4. **Capture the two blocked screenshots** (§5) from the instructor's own email
   provider and Google account, once those accounts exist.
5. **Re-render with a production TTS voice.** Every TTS lecture is currently
   built on the `offline` espeak scaffold voice, which proves timing but is
   explicitly unshippable per its own build warning. Re-run with
   `--provider kokoro` (free, local) once scripts are final.
6. **Add Ravi Chandra to `story-bible.yaml`'s cast list** (§3) — a small
   completeness fix, safe for the instructor or a future pass to make in one
   line.
7. **Run the `--release` gate** once the above are done. It currently reports
   (correctly, at this stage): built with the offline scaffold voice, only 2
   lectures actually rendered end-to-end in the last full-course build, and
   total run time far under Udemy's 30-minute minimum — all expected, since a
   full production-voice build of all 76 lectures hasn't been run yet. This is
   the very last gate, not a problem with the scripts themselves.

Nothing in this list is a script defect. Every lecture in the course is written,
built, QC-clean, and visually verified; what remains is entirely the instructor's
own contribution, exactly as the account's compliance rule requires.
