# Job: question miner (daily)

You are running inside the udemy repo. Find fresh public questions this
course's expertise genuinely answers, and draft complete answers for human
review. You never post, vote, comment, or create accounts. Output only.

## Sources (read politely, no scraping beyond public endpoints)

- Reddit new-post JSON for: r/ProductManagement, r/ProductManagers,
  r/BusinessIntelligence, r/artificial, r/ChatGPTPro
  (`https://www.reddit.com/r/<sub>/new.json?limit=50`)
- Hacker News via Algolia: search recent stories/comments for the query set
- Query set: "LLM evals", "AI acceptance criteria", "golden dataset",
  "AI feature QA", "RAG quality", "AI PM", "hallucination production",
  "LLM as judge", "AI feature cost"

If an endpoint refuses or rate-limits, skip it and say so in the digest.
Never work around an access control.

## Filter hard

Keep a question only if all three hold:

1. It is a real question from a real person (not marketing, not a bot roundup).
2. The course material answers it *specifically* (you can cite which lecture's
   argument applies).
3. Answering it fully takes under 300 words. Longer means it becomes blog
   input instead: note it as such.

Expect 0 to 3 keepers on a normal day. Zero is a fine answer; do not pad.

## For each keeper, write to `growth/queue/<iso-week>/questions/<n>-<slug>.md`

- The question: link, sub/site, timestamp, and the poster's actual words.
- A complete, self-sufficient answer in the house voice (no em dashes, no
  tells, second person, concrete). The answer must fully solve their problem
  with no reference to the course. Someone who never learns the course exists
  should still be fully served.
- A `promotion:` field: almost always `none`. Only if the subreddit's rules
  explicitly permit self-promotion AND the course/book is the direct answer to
  a "what should I read/take" style question may you suggest `mention-ok`,
  and then include the sub's exact rule text you are relying on.
- The subreddit's self-promotion rules, quoted, so the human can judge.

## Also maintain `growth/queue/<iso-week>/questions/THEMES.md`

Append the day's observed themes: what people are actually confused about.
Recurring themes are course-update and content-calendar input, and over time
this file is the cheapest market research the project has.
