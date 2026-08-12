# Launch calendar: AI Product Skills for PMs & Analysts (course)

**Deviation from `growth/prompts/launch-calendar.md`:** the author has not
picked a launch date yet, so every row below is a **T-day offset** (T =
launch day, the day the course goes live on Udemy at the personal-network
$9.99 price). Substitute the real calendar date once one is picked; do not
treat any offset in this file as a scheduled date.

**Second deviation, flagged rather than silently patched:** the source
job spec (`growth/prompts/launch-calendar.md`) asks for an "ARC
invitation" file, a book-launch device (advance reader copies). Udemy has
no equivalent mechanism, so this calendar substitutes the closest real
thing: an early-access coupon email to the personal network at T-7, which
plays the same "seed honest reviews before the public price kicks in"
role §4 assigns the book's ARC step. See `email-personal-network.md`.

**Gating fact, stated once here so this calendar isn't read as ready to
run today:** per `CLAUDE.md` §10, only Section 0 of `ai-for-pms` is built,
rendered and visually verified; Sections 1-11 are drafted but unrendered
and unsigned. Every lecture needs `verified: true` from the instructor
(never set by this pipeline) before launch. This calendar is the
execution plan for the day the course clears that gate, not a signal that
it already has.

Sources: `docs/03-launch-playbook.md`, `docs/06-growth-engine.md`, house
voice rules (no em dashes, no tells, concrete numbers, name the cost,
British English for course-facing copy).

| When | Action | Who / where | Copy |
| --- | --- | --- | --- |
| T-14 | Record the 60-90 second promo video in your own voice and face, per `docs/03-launch-playbook.md` §2's beat sheet | You, screen recording + webcam | — |
| T-14 | Confirm the 3 free-preview lectures are set: 0.1 Welcome, 0.3 The one idea, 4.1 The eval mindset | You, Udemy course settings | — |
| T-10 | Draft the Udemy course description exactly as `course.yaml`'s `description` field (AI disclosure line must stay last) | You, Udemy course landing editor | `course.yaml` (already the source of truth) |
| T-7 | Send the early-access email to the personal network at a $9.99 coupon, ahead of the public $24.99 week | You, email tool | `email-personal-network.md` |
| T-6 | Finalise LinkedIn posts 1-3 and the X thread for launch week; queue, do not publish | You | `linkedin-post-1.md`, `linkedin-post-2.md`, `linkedin-post-3.md`, `x-thread.md` |
| T-3 | Set up Udemy Q&A monitoring: confirm notifications reach you within a few hours, not just daily digest | You, Udemy instructor settings | — |
| T-1 | Set launch pricing: $9.99 coupon reserved for the personal-network segment already emailed at T-7 | You, Udemy pricing dashboard | — |
| **T0 — LAUNCH** | Publish the course live, personal-network coupon active at $9.99, post LinkedIn post 1, post the X thread | You | `email-personal-network.md` (if not already sent), `linkedin-post-1.md`, `x-thread.md` |
| T+1 | Post LinkedIn post 2 | You, LinkedIn | `linkedin-post-2.md` |
| T+2 | First Q&A check: reply to anything posted within 24 hours of it landing | You, Udemy Q&A | — |
| T+3 | Post LinkedIn post 3 | You, LinkedIn | `linkedin-post-3.md` |
| **T+7 (start of week 1)** | Move price from the $9.99 personal-network coupon to the public $24.99 enrolment-velocity price | You, Udemy pricing dashboard | — |
| T+7 | Publish the one-line `stop-guessing` cross-sell in the course's final lecture / resource page | You, course source | `book-cross-sell-mention.md` |
| Daily, T0 through T+30 | Answer Q&A within 24 hours; this is the cheapest ranking lever available and slow replies actively hurt rank | You, Udemy Q&A | — |
| Ongoing from T+3 | Watch for students reaching lecture 0.4 (the review-ask moment, already written into the lecture text itself per `docs/03-launch-playbook.md` §5) | You, Udemy analytics | `review-ask-lecture-text.md` (goes into the lecture, not a separate email) |
| T+14 | Engagement digest: check ratings/reviews so far, reply to anything critical within 48 hours, harvest any usable testimonial quotes | You | — |
| **T+21 (start of week 3)** | Move price from $24.99 to the standard $74.99 | You, Udemy pricing dashboard | — |
| T+21 | Send the LinkedIn "still time to catch the early price" style post is skipped on purpose: a public price-increase countdown reads as urgency-marketing on a platform where that erodes trust; the pricing ladder does its own work | You | — |
| T+30 | Tally reviews against the 10+ in 30 days target (`docs/03-launch-playbook.md` §4); if short, check whether Q&A response time or completion rate is the actual bottleneck before doing anything about price | You, Udemy analytics | — |
| T+30 | Confirm completion-rate protection held: no lecture over 12 minutes, every section ends in a workshop, Section 0 delivers a real win in the first 15 minutes | You, spot-check the actual published course | — |

**Beyond this calendar's T+30 window** (flagged, not dropped, per
`docs/03-launch-playbook.md` §6): the quarterly freshness pass is
mandatory for this course specifically, since Sections 1.4, 2.6, 7.1 and
7.4 are the fastest-decaying (model names, prices, capabilities). Each
freshness pass becomes an announcement to enrolled students, which Udemy
surfaces and which drives completions and reviews. `growth/facts.yaml`
now carries the registry that pass runs against.

**Rules this calendar does not break:** no blanket free-coupon blasts to
coupon aggregator sites (documented to crater review rate and price
integrity, `docs/03-launch-playbook.md` §4), review ask lives inside
lecture 0.4's own text at the moment of value, not a cold email, and
nothing above claims a launch date that hasn't actually been picked.
