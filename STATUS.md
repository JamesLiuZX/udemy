# Portfolio status

The one page to open to see everything: three courses, seven books (English
+ Simplified Chinese each), and the launch/growth assets that support them.
Built 2026-08-12. Every "next command" below is copy-pasteable; every QC
number was run live against the current source, not pulled from memory.

**The one rule every row below obeys:** nothing here has `verified: true`,
and nothing in this file sets it. That signature is the instructor's or
author's alone (`CLAUDE.md` §1, `books/CLAUDE.md` §1). "Complete" in the
tables below means *ready for that signature*, not signed.

---

## 1. Courses

| Course | Lectures | Live QC | Editorial state | Author-only gates remaining |
| --- | --- | --- | --- | --- |
| **ai-for-pms** — AI Product Skills for PMs & Analysts | 102 (12 sections) | `107 fail · 0 warn` — every FAIL is a sign-off or `[INSTRUCTOR-INPUT]` gate | Rendered, visually inspected, QC-clean, story-bible continuity checked. Full report: [`courses/ai-for-pms/EDITORIAL-REPORT.md`](courses/ai-for-pms/EDITORIAL-REPORT.md) | Read and `verified: true` on all 102 lectures; fill 4 `[INSTRUCTOR-INPUT]` markers in 11.5; capture 1 flagged screenshot |
| **ai-agents-for-work** — AI Agents for Your Job | 76 (12 sections) | `78 fail · 0 warn` (bar the accepted divider warnings) — sign-off + 2 screenshot gates | Editorial pass, then a **full narration-expansion pass (2026-08-19)**: the course had been authored at skeleton length (~92 min total against a ~6h target) and every content lecture was rewritten to teaching depth (~4.3h nominal, ~3.5h actual audio). Defect story and pipeline fixes in [`docs/PRODUCTION-REPORT.md`](docs/PRODUCTION-REPORT.md) §3. | Read and `verified: true` on all 76 lectures; capture 2 screenshots (3.2, 5.2) once the instructor's own email/Google accounts exist; add Ravi Chandra to `story-bible.yaml` cast list; decide whether ~3.5h actual duration is accepted or sections 3-6 get deeper build lectures |
| **ai-ugc-ads** — AI UGC & Video Ads | 81 (12 sections) | `93 fail · 0 warn` — same two gate types | Draft + plug-and-play retrofit (Sections 0-6) + visual-standard pass (all sections) complete. Full report: [`courses/ai-ugc-ads/EDITORIAL-REPORT.md`](courses/ai-ugc-ads/EDITORIAL-REPORT.md) | Read and `verified: true` on all 81 lectures; record 0.1/11.5 and other `voice: human` lectures; capture 18 screenshots + generate 5 AI specimens (blocked on `pipeline/` image-embed support, see report §7.2); re-verify the 9 `freshness_watch` lectures against current tool/policy state before recording |

**Next command, once the sign-offs above are done, per course:**
```bash
python3 pipeline/build.py --course courses/<slug> --provider kokoro
python3 pipeline/qc.py --course courses/<slug> --release
```
`build/` is gitignored and not present in this container; every render
described in the editorial reports above was verified in the session that
produced that report, not re-verified here. Re-run before trusting a slide
that hasn't been touched since.

**Free-preview picks** (already wired in each `course.yaml`, referenced by
the YouTube pack below): `ai-for-pms` → 0.1, 0.3, 4.1. `ai-agents-for-work`
→ 0.1, 0.3, 3.1. `ai-ugc-ads` → 0.1, 0.3, 7.1.

---

## 2. Books

All seven manuscripts are **English-complete and QC-clean**: live
`books/pipeline/qc.py` run today returns `1 fail · 0 warn` on every
English edition, the single fail being the `verified: false` sign-off
gate. Simplified Chinese editions are also complete; their QC run reports
one additional WARN, a known, documented false positive (`Book.word_count()`
splits on whitespace, which undercounts CJK text badly since Chinese has no
inter-word spaces — the real, correct page count is the built PDF's actual
page count, cited in the table below, not the WARN's estimate). See each
book's `notes.md` for the full writeup.

| Book | EN pages | ZH pages | EN proof | ZH proof | Author-only gates remaining |
| --- | --- | --- | --- | --- | --- |
| **stop-guessing** | 185 | 157 | [`proofs/stop-guessing.pdf`](books/stop-guessing/proofs/stop-guessing.pdf) | [`proofs/stop-guessing-zh.pdf`](books/stop-guessing/proofs/stop-guessing-zh.pdf) | Read + `verified: true`, each edition separately |
| **ai-employee** | 187 | 159 | [`proofs/ai-employee.pdf`](books/ai-employee/proofs/ai-employee.pdf) | [`proofs/ai-employee-zh.pdf`](books/ai-employee/proofs/ai-employee-zh.pdf) | Read + `verified: true`, each edition separately |
| **ai-for-the-rest-of-us** | 223 | 173 | [`proofs/ai-for-the-rest-of-us.pdf`](books/ai-for-the-rest-of-us/proofs/ai-for-the-rest-of-us.pdf) | [`proofs/ai-for-the-rest-of-us-zh.pdf`](books/ai-for-the-rest-of-us/proofs/ai-for-the-rest-of-us-zh.pdf) | Read + `verified: true`, each edition separately |
| **one-person-business** | 127 | 107 | [`proofs/one-person-business.pdf`](books/one-person-business/proofs/one-person-business.pdf) | [`proofs/one-person-business-zh.pdf`](books/one-person-business/proofs/one-person-business-zh.pdf) | Read + `verified: true`, each edition separately |
| **reclaimed-hour** | 213 | 183 | [`proofs/reclaimed-hour.pdf`](books/reclaimed-hour/proofs/reclaimed-hour.pdf) | [`proofs/reclaimed-hour-zh.pdf`](books/reclaimed-hour/proofs/reclaimed-hour-zh.pdf) | Read + `verified: true`, each edition separately |
| **resume-arms-race** | 163 | 135 | [`proofs/resume-arms-race.pdf`](books/resume-arms-race/proofs/resume-arms-race.pdf) | [`proofs/resume-arms-race-zh.pdf`](books/resume-arms-race/proofs/resume-arms-race-zh.pdf) | Read + `verified: true`, each edition separately |
| **ai-didnt-close-that-deal** | 181 | 141 | [`proofs/ai-didnt-close-that-deal.pdf`](books/ai-didnt-close-that-deal/proofs/ai-didnt-close-that-deal.pdf) | [`proofs/ai-didnt-close-that-deal-zh.pdf`](books/ai-didnt-close-that-deal/proofs/ai-didnt-close-that-deal-zh.pdf) | Read + `verified: true`, each edition separately |

Status narrative for each title lives in `books/<slug>/notes.md`
(chapter-by-chapter hook/nugget table, citation re-verification log,
worked-visual inventory). No book has a separate `EDITORIAL-REPORT.md`;
`notes.md` is the equivalent record on the book side.

**Sequencing reminder** (`docs/05-kdp-playbook.md` §1): finish
`stop-guessing` end to end before publishing any other title. The other
six are a finished asset shelf, not a launch queue — publishing several
AI-assisted titles under one new author account in a short window is the
exact pattern KDP's mass-produced-AI enforcement watches for.

**Next command, once sign-off is done, per edition:**
```bash
python3 books/pipeline/build.py --book <slug>              # English
python3 books/pipeline/build_epub.py --book <slug>
python3 books/pipeline/build.py --book books/<slug>/book-zh.yaml   # Chinese
python3 books/pipeline/qc.py --book <slug> --release
```

---

## 3. Cover design

[`books/docs/04-cover-briefs.md`](books/docs/04-cover-briefs.md) — one
brief per title, computed spine width and full-wrap dimensions from the
locked page counts above, ready for a designer with no further questions.
**Next click:** commission the series design as one project (not seven
separate ones), per the brief's own commissioning notes.

Chinese editions are ebook-only (Amazon KDP does not support Chinese-
language publishing at all — see `docs/08-channels.md` §4); their cover
need is a single 2560×1600 re-set, not a print wrap.

---

## 4. Launch readiness

| Asset | State | Path |
| --- | --- | --- |
| Facts registry (freshness sentinel) | Built, 248 entries (67 course, 181 book), first pass only — not yet independently re-verified against live sources | [`growth/facts.yaml`](growth/facts.yaml) |
| Launch calendar: stop-guessing | Full T-21 → T+30 calendar + all referenced copy | [`growth/launch-packs/launch-stop-guessing/`](growth/launch-packs/launch-stop-guessing/) |
| Launch calendar: ai-for-pms | Full T-14 → T+30 calendar + all referenced copy | [`growth/launch-packs/launch-ai-for-pms/`](growth/launch-packs/launch-ai-for-pms/) |
| YouTube metadata | 3 flagship preview lectures (title/description/tags/end-screen) + channel about-page copy | [`growth/launch-packs/youtube-metadata.md`](growth/launch-packs/youtube-metadata.md) |

Both launch calendars use **T-day offsets**, not real dates: no launch
date has been picked for either product yet. **Next click:** pick a launch
date for `stop-guessing` (it ships first per §2's sequencing rule), replace
the T-offsets with real dates, and the calendar becomes the day-by-day
execution plan as written.

**Next freshness-sentinel run** (`growth/prompts/freshness-sentinel.md`):
every entry in `growth/facts.yaml` needs its first live re-verification —
today's pass registered claims, it did not check them against current
source pages. Run it before any lecture or chapter above gets read for
final sign-off, so the instructor/author isn't signing off a stale number.

---

## 5. What's not covered here

Author identity and payout mechanics (`docs/08-channels.md` §6: ISBN
choice, W-8BEN tax interview, per-platform payout setup), the Amazon Ads
account itself, the Udemy instructor premium application, and the actual
recording of every `voice: human`/`[INSTRUCTOR-INPUT]` lecture are all
one-time account-level or on-camera steps no pipeline run can do. They're
named in the relevant docs (`docs/05-kdp-playbook.md`, `docs/08-channels.md`)
but not tracked here as a checklist item, since none of them are blocked on
anything this repo can build.

---

## Footer: what this pass did and didn't do

**Completed:** the facts registry (full scan, all 3 courses + all 7
English manuscripts); cover design briefs for all seven titles with real
computed print specs; both requested launch calendars with every piece of
referenced copy actually drafted, not stubbed; YouTube metadata for the
three flagship preview lectures plus channel about-page copy; this status
page, built from a live QC run against current source, not from the stale
"Section 0 only" state `CLAUDE.md` §10 describes (that section is now out
of date — all three courses are fully drafted, rendered and editorially
passed; update `CLAUDE.md` §10 in a future session so it stops
undercounting real progress).

**Skipped, and why:**
- **Live re-verification of every `growth/facts.yaml` claim against its
  source.** That's the freshness sentinel's actual job (§4 above), a
  separate, longer pass this session didn't have scope for; today's work
  was registering the claims, not checking them.
- **A launch calendar for any book besides `stop-guessing`.** Correct per
  the sequencing rule in `docs/05-kdp-playbook.md` §1: the other six
  titles don't get a launch plan until `stop-guessing`'s real 90-day data
  exists to pick title #2 from.
- **YouTube metadata beyond the three flagship lectures.** The task asked
  for the flagship pick per course specifically; the other two free
  previews per course (0.1 and the mid-course one) can reuse this file's
  format when they're published.
- **Any change to lecture/chapter content, `verified` flags, or
  `[INSTRUCTOR-INPUT]`/`[AUTHOR-INPUT]` markers.** Never in scope for this
  pipeline to touch; every one of those stayed exactly as found.
