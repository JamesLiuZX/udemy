# Research and sourcing standard for `[KEY-INSIGHT: ...]`

Applies to every `[KEY-INSIGHT: claim || source]` marker in any book in
this repo. This is the bar a claim has to clear before it's allowed to
appear in a chapter, not a suggestion.

## Why this device exists

`[AUTHOR-INPUT: ...]` marks a personal anecdote or credential only the
real author can supply, and the rule on it has never changed: never invent
one on their behalf. But a book still needs load-bearing evidence, a
moment where an abstract argument touches something a reader can verify
for themselves. When the real author has no anecdote to give, a real,
checked, cited statistic or case study fills that structural role instead.
`[KEY-INSIGHT: ...]` is not a loophole around the no-fabrication rule.
It's the same rule applied to a different kind of claim: don't invent a
personal story, and don't invent a statistic either. Both are fabrication;
one just sounds more official.

## The standard, in order

1. **Every claim inside a `[KEY-INSIGHT: ...]` marker must be independently
   verified with an actual search before it's written down.** Not recalled
   from training data and assumed correct. Not "this sounds like the kind
   of thing that's true." A live lookup, every time, no exceptions for a
   number that feels familiar.
2. **Prefer primary sources: the court ruling itself, the named study, the
   named survey publisher.** A secondary aggregator ("72 Verified Stats on
   X" listicle sites are common in search results and are themselves
   compiling from somewhere else, sometimes accurately, sometimes not) is
   a last resort, and if that's genuinely the best available source, say
   so plainly in the source line rather than dressing it up as more
   authoritative than it is.
3. **Never put words in quotation marks you have not confirmed verbatim.**
   If a search surfaces a compelling quote but you can't independently
   confirm it's the actual wording, either find a source that confirms it
   or drop the quotation marks and paraphrase the fact instead. This
   happened once already in this repo: a draft citation for ai-employee's
   chapter 1 attributed a specific quote to the judge in Mata v. Avianca
   that couldn't be confirmed against the opinion. It was cut before the
   chapter shipped. Treat that as the standard, not an exception.
4. **Name the actual source in the citation line**: the court case and
   citation, the study name and publisher and year, the survey and who
   ran it. "Studies show" is not a source. A reader (or a KDP reviewer,
   or a fact-checker, or a reviewer leaving a one-star rating) should be
   able to go find the thing you cited.
5. **When confidence in an exact figure is moderate, say so in the
   claim's own wording** ("a survey found roughly a third...") rather
   than manufacturing false precision. A hedge in the prose is honest.
   A confident-sounding wrong number is the exact failure mode
   `books/CLAUDE.md` exists to prevent on the video side, applied here to
   print.
6. **One well-chosen `[KEY-INSIGHT: ...]` per chapter is the target**, the
   same discipline as pull quotes and takeaway boxes. A chapter with five
   citations reads like a term paper, not a book a friend would recommend.
   Pick the one statistic or case that does the most real work for the
   argument, not every fact that turned up in research.

## What this changes about `[AUTHOR-INPUT: ...]`

Nothing, when a real author does have a genuine story to add later; the
mechanism stays in the pipeline and `qc.py` still gates on it. What
changes is the default: new chapters in this repo should reach for
`[KEY-INSIGHT: ...]` first, not `[AUTHOR-INPUT: ...]`, given the real
author's stated preference to draw on researched, citable material rather
than personal anecdotes across these titles. If a genuinely strong,
specific personal story does exist for a moment in a chapter, it's still
the stronger device where it fits; the two aren't mutually exclusive
within one book, they just aren't both the default anymore.
