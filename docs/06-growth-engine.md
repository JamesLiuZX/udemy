# Growth engine: automated, compounding, and ban-proof

> The production pipeline turns one markdown file into a finished lecture.
> This document does the same for marketing: every finished lecture already
> contains a week of distribution material, and most of the labour of
> extracting it is automatable with cron jobs or Claude Cowork sessions.
> Paste-ready prompts live in `growth/prompts/`; wiring is in `growth/README.md`.

---

## 1. Three principles, or the automation eats the brand

1. **Automate production, never authenticity.** Claude drafts, monitors,
   summarises, and packages. A human approves everything that appears in
   public under your name. This is the same division of labour the course
   itself is built on, and the same reason: the penalty for crossing it
   (platform bans, brand damage) is paid in an account you cannot re-earn.
2. **Own the audience.** Every channel routes to the email list, because it is
   the only asset no algorithm change or platform ban can take. The lead
   magnet already exists: the rubric template and golden-set starter kit are
   genuinely wanted by exactly the target buyer.
3. **Help first, in public.** The growth loop on Reddit, X and LinkedIn is
   answering real questions well, with the product mentioned rarely and only
   where it genuinely completes the answer. A 9:1 help-to-promotion ratio is
   not generosity, it is what the platforms' cultures convert on.

### What is deliberately off the table

Each of these is an account-death mechanism, not an edge:

| Never | Why |
| --- | --- |
| Auto-posting to Reddit, mass DMs, comment bots | Sitewide spam policy plus per-subreddit self-promo rules; detection is good and bans are permanent |
| Fake accounts, upvote/engagement rings | Same, faster |
| Paid, incentivised, or swapped reviews (Udemy or Amazon) | Both platforms filter, penalise, and sometimes remove the product |
| Auto-replying at scale on X | Against automation rules; reads as spam even when allowed |
| Blasting free Udemy coupons to coupon sites | Documented to crater review rate and price integrity (see `03-launch-playbook.md`) |

---

## 2. Where the audience actually is

The ask was Reddit and X. Both are in the plan, but ranked honestly for a
PM/analyst audience:

| Rank | Channel | Role | Reality check |
| --- | --- | --- | --- |
| 1 | **LinkedIn** | Primary broadcast. The buyer scrolls it at work, and the deck's figures are visually distinctive in that feed | Text + single-image posts from the figure library; carousels from slide sequences |
| 2 | **YouTube** | Search engine, not social. "LLM evals explained", "AI PM skills" | Publish the 3 free-preview lectures in full, plus Shorts cut from figure moments; description links to list and course |
| 3 | **Email list** | The only owned channel; where course coupons and the book ARC live | Weekly, one idea per issue, built from the lecture repurposing pipeline |
| 4 | **Reddit** | Answer engine, not broadcast. r/ProductManagement, r/ProductManagers, r/BusinessIntelligence, r/artificial | Value answers with no links in the post; product lives in the profile. Most PM subs hard-ban self-promo, and that rule is enforced |
| 5 | **X** | The AI-builder crowd; smaller PM density but high amplification | Threads built on figures and numbers; scheduled posting of approved drafts is fine, auto-engagement is not |

---

## 3. The asset flywheel

One verified lecture decomposes into a week of distribution with near-zero
marginal effort, because the hard part (a tight argument, a distinctive
figure, concrete numbers) is already made. A verified book chapter works the
same way: its scene opener and `[KEY-INSIGHT]` citation are a ready-made
LinkedIn post and thread, so the repurposer treats chapters as an alternate
source once books start shipping:

```
lecture.md (verified)
  ├─ LinkedIn post        the argument, 150 to 250 words, one figure attached
  ├─ X thread             the numbers: 5 to 8 tweets, figure as the hook image
  ├─ YouTube Short spec   30 to 45s clip: which slide, which narration lines
  ├─ Blog post            the full argument, SEO title, on your own domain
  └─ Newsletter item      the idea plus one thing to do Monday
```

Every derived asset obeys the house voice rules (CLAUDE.md §4): no em dashes,
no LLM tells, no emoji confetti, hooks made of specifics ("5 reviewers, same
summary, scores from 2 to 5") rather than hype.

---

## 4. The automations

Six jobs. Each has a paste-ready prompt in `growth/prompts/`, runs on cron
(local `claude -p`), as a Cowork scheduled session, or as a Claude Code web
routine, and ends at a **review queue** (`growth/queue/`, gitignored), never
at a publish button. Suggested schedule:

| Job | Prompt file | Cadence | What it does | Human step |
| --- | --- | --- | --- | --- |
| Lecture repurposer | `repurpose-lecture.md` | Weekly (Mon) | Newest verified lecture → the five assets above, in queue | Approve, schedule posts |
| Question miner | `question-miner.md` | Daily | Finds fresh, relevant questions on Reddit/HN; drafts genuinely complete answers; quotes each sub's self-promo rules alongside | Post manually, or don't |
| Freshness sentinel | `freshness-sentinel.md` | Weekly (Fri) | Diffs model names/prices/limits cited in lectures against providers' current pages; emits a decay report | Re-verify flagged lectures |
| Engagement digest | `engagement-digest.md` | Daily during launch, then weekly | Summarises Udemy reviews/Q&A (pasted or browsed via Cowork), drafts replies in your voice, harvests testimonial quotes, patterns complaints into a fix backlog | Approve replies (<24h target) |
| KDP telemetry | `kdp-telemetry.md` | Weekly | Reads KDP report exports you drop in `growth/data/`; trends sales, KU reads, rank and review velocity per title; recommends the next promo action | Act on one recommendation |
| Launch calendar | `launch-calendar.md` | Once per launch | Expands the launch playbooks into a dated, day-by-day checklist with pre-drafted copy for every post and email. One launch at a time: the book portfolio ships sequentially (see `05-kdp-playbook.md` §1) | Execute the days |

Notes on the honest edges:

- **Udemy has no instructor API.** The engagement digest runs on pasted
  exports, email notifications, or a Cowork session driving the instructor
  dashboard in a browser. That last mode is the strongest argument for Cowork
  in this stack.
- **The question miner reads public JSON/RSS endpoints politely** (Reddit's
  `.json`, HN's Algolia API) and never posts. If a platform objects even to
  polite reading, the fallback is running it inside Cowork against the pages
  you'd read anyway.
- **The freshness sentinel is a review-protection device**, not marketing: a
  confidently wrong price in a lecture is the fastest 3-star review in this
  genre. It needs a one-time pass adding a `facts` registry (lecture id, claim,
  source URL) as lectures are verified; the prompt file specifies the format.

---

## 5. Compounding tactics that need a human (do these anyway)

Automation covers the repeatable middle. The compounding wins are manual and
worth the hours:

1. **Publish the free-preview lectures on YouTube in full.** The course's
   production quality is the ad. Top comment, pinned: the artifact pack link.
2. **The artifact footer** (see `04-quality-bar.md` §8): forwarded artifacts
   are the highest-intent channel that exists for this product.
3. **Podcast guesting** once Section 4 ships: the "distributions, not
   functions" argument is a ready-made 40-minute episode, and PM podcasts
   book months out, so start early.
4. **One genuinely great answer per week** somewhere public, written by you,
   fed by the question miner's queue. Twenty of those is a durable reputation.
5. **Quarterly**: the freshness pass doubles as an announcement to enrolled
   students, which Udemy surfaces and which drives completions and reviews.

---

## 6. The weekly scoreboard

One page, assembled by the engagement digest job on Fridays, five numbers
against last week: enrollments, course rating and review count, email
subscribers, book sales and rank, completion rate. One decision per week comes
off the scoreboard, no more. Growth systems die of dashboard sprawl, not of
missing data.
