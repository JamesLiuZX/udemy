# Job: engagement digest (daily during launch, weekly after)

You are running inside the udemy repo. Turn learner and reader feedback into
draft replies, testimonial material, and a fix backlog. You never publish a
reply; every draft goes to the queue for the instructor to send.

## Inputs, in order of preference

1. If you are running in Cowork with a browser: open the Udemy instructor
   dashboard the user is logged into, and read new Q&A, reviews, and messages
   since the last digest (the last digest's date is in the newest
   `engagement-digest.md` under `growth/queue/`).
2. Otherwise: process whatever the user has dropped into `growth/data/`
   (pasted reviews, exported CSVs, forwarded notification emails).
3. If neither yields anything new, write a one-line digest saying so and stop.

## Produce `growth/queue/<iso-week>/engagement-digest.md`

**1. Q&A replies (the ranking lever, target < 24h).** For each unanswered
question: the question, a draft reply in the instructor's voice (helpful,
direct, no em dashes, no tells, admits limits where real), and a flag when the
question exposes a course gap worth a new lecture or an announcement.

**2. Review triage.**
- 4 to 5 stars with quotable lines: extract the quote verbatim, note where it
  could work (landing page, A+ content, LinkedIn). Mark the exact wording;
  testimonials must never be paraphrased into something the learner didn't say.
- 3 stars and below: the complaint in one line, whether it is actionable, and
  which lecture or expectation it traces to. Three complaints with the same
  root cause is a fix-this-week item; say so explicitly.

**3. The scoreboard (Fridays).** Enrollments, rating, review count, email
subscribers, book sales/rank (from the latest KDP telemetry report if one
exists), completion signals. Five numbers, each against last week, and ONE
recommended decision for next week. Not three. One.

## Boundaries

- Never draft a reply that asks for a rating change or offers anything for a
  review. Both platforms treat that as manipulation.
- Negative reviews get a reply draft only when there is something concrete to
  fix or clarify; never argue with a review.
