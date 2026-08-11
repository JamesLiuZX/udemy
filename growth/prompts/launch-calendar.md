# Job: launch calendar (run once per launch, course or book)

You are running inside the udemy repo. Expand the launch playbooks into a
dated, day-by-day execution checklist with every piece of copy pre-drafted,
so launch week is execution only, no writing.

## Inputs

- Which launch (course or book) and the launch date: the user supplies these
  when invoking the job; if absent, ask and stop.
- Course: `docs/03-launch-playbook.md` (pricing phases, preview selection,
  review ask, first-30-days actions).
- Book: `docs/05-kdp-playbook.md` §5 and §7 (price ladder, ARC timing, ads).
- Channel strategy and voice rules: `docs/06-growth-engine.md`.

## Produce `growth/queue/launch-<slug>/calendar.md`

A table from T-21 days to T+30, one row per day that has actions:

- The action, specific enough to execute without thinking ("switch Udemy
  price to $24.99", "email segment: ARC readers, send review-ask template B").
- Who does it (you) and where (which dashboard, which channel).
- A link to the pre-drafted copy for that action.

And alongside it, every piece of copy the calendar references, each in its own
file in the same folder: launch emails (announce, last-day, review ask),
LinkedIn posts (3 for launch week), X thread, the Udemy educational
announcement, the ARC invitation, and the price-change reminders. House voice
rules apply to all of it: no em dashes, no tells, concrete numbers, name the
cost, British English.

## Rules that override enthusiasm

- The review asks in emails must never offer anything or target a star value.
- Coupon codes go to the named segments in the playbook, never to coupon
  aggregator sites.
- If the launch date leaves less than 21 days of runway, compress honestly and
  flag what gets cut, rather than pretending the full sequence fits.
