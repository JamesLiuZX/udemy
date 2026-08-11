# Job: lecture repurposer (weekly)

You are running inside the udemy repo. Turn the most recent finished lecture
into a week of distribution assets for human review. Do not post anything
anywhere. Do not modify course files.

## Select the source

1. Find lectures with `verified: true` in `courses/*/lectures/*.md`.
2. Pick the most recently modified one that has no folder yet under
   `growth/queue/` from a previous run (check past weeks before writing).
3. If none qualifies, write `growth/queue/<iso-week>/NOTHING-TO-DO.md`
   explaining why, and stop.

## Produce, in `growth/queue/<iso-week>/<lecture-id>/`

1. `linkedin.md`: 150 to 250 words. The lecture's argument, recast for a feed:
   cold open with the most concrete fact in the lecture, the insight, one
   "what to do Monday" line. Name which rendered figure to attach (path under
   `build/`, and the `figure`/`mermaid` block to re-render it from if build/
   is absent). No hashtag pile: two at most. No link in the post body; note
   the link for the first comment instead.
2. `x-thread.md`: 5 to 8 posts. Post 1 is a specific number or contradiction
   from the lecture, never a vague hook. One idea per post. Last post may
   reference the course. Name the figure for post 1's image.
3. `short-spec.md`: one 30 to 45 second vertical clip spec: which slide, which
   narration lines verbatim, the on-screen hook text for the first 2 seconds,
   and the end card text.
4. `blog.md`: 700 to 1,100 words, the argument in full prose (not the
   narration pasted: rewrite for the page), with an SEO title containing one
   of the course's primary keywords, meta description, and the figure(s)
   inline.
5. `newsletter.md`: 120 to 200 words for the weekly issue: the idea, one
   concrete example from the lecture, one action.

## Voice rules (non-negotiable, same as the course)

- No em dashes anywhere. No LLM tells ("delve", "game-changer",
  "unlock", "it's important to note"). No emoji as decoration.
- Second person. Short sentences. Concrete before abstract: keep the
  lecture's real numbers and names (Ticket #4471 beats "a support ticket").
- Every asset must name a cost or limitation, not just a win. That is the
  house credibility signal and it transfers to marketing copy.
- British English, matching the scripts.

Finish by writing `SUMMARY.md` in the same folder: what was produced, which
lecture, and the one asset you judge strongest this week and why.
