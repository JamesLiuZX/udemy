# KDP compliance notes

Research summary, not a substitute for reading Amazon's live KDP content
guidelines immediately before publishing. Policy wording changes; verify
before you upload, the same way the video side's `docs/00-strategy.md`
should be re-checked against Udemy's current policy before submission.

---

## 1. The AI-content disclosure

KDP's publishing flow asks, per title, whether the content is AI-generated
and whether it is AI-assisted, and defines them roughly as:

- **AI-generated**: text, images, or translations produced by an AI tool
  with no meaningful human creative control over the output. Must be
  disclosed to Amazon at submission.
- **AI-assisted**: a human author created or substantially edited the
  content, using AI as a tool somewhere in the process (drafting,
  research, editing, translation). Declared at submission; does not
  generally require an on-page reader disclosure the way AI-generated
  content might.

This system is built to produce **AI-assisted** work: a human (you) directs
the outline, supplies real expertise through `[AUTHOR-INPUT: ...]`, reads
every chapter, and signs off via `verified: true`. That sign-off is not
ceremony. It is the fact that makes the AI-assisted declaration true rather
than a technicality.

## 2. Why self-help specifically is watched harder

KDP has been actively removing low-quality, mass-produced AI content, and
self-help / how-to is one of the categories most associated with that
pattern: generic advice, no real credential or tested experience behind
it, published in volume. Enforcement here is account-level. A pattern of
low-effort titles risks your publishing rights broadly, not just a
takedown of one book.

The practical implication for this pipeline: **`[AUTHOR-INPUT: ...]` is
not optional friction, it's the thing that makes a title defensible.** A
self-help chapter with zero real anecdote, credential, or tested case
behind it is both a worse book and a flagged pattern. Do not ship a
chapter that never resolved its `[AUTHOR-INPUT]` markers; that is the
build correctly refusing to let you.

## 3. Content quality guidelines, generally

Independent of the AI question, KDP requires content to be reasonably
formatted, not misleading in its title/description/category placement,
and not duplicative of freely available public-domain text repackaged
with minimal change. None of this pipeline's output is public-domain
repackaging, but keep it in mind if a chapter ever leans heavily on
paraphrasing an existing source rather than the author's own synthesis or
tested method.

## 4. What this pipeline does NOT handle

- **The KDP dashboard disclosure questionnaire itself.** That's a
  publishing-step form filled in by the account holder, not a build
  artifact.
- **Cover design and the AI-generated-image disclosure that comes with
  it**, if a cover uses any AI-generated imagery. Separate policy surface
  from interior text, separate decision.
- **ISBN acquisition.** KDP can assign a free ISBN, or the author can
  supply their own; either way it's an account-level choice made at
  publish time, represented in `book.yaml` only as a placeholder field.

## 5. Before you actually publish a title

- [ ] Re-read Amazon's current KDP content guidelines page; this document
      may be stale by the time you use it.
- [ ] Confirm `verified: true` reflects a real, complete read-through by
      the author, not a build step.
- [ ] Confirm no `[AUTHOR-INPUT: ...]` markers remain unresolved anywhere
      in the manuscript (`qc.py --release` gates on this).
- [ ] Decide the AI-generated / AI-assisted answers for the dashboard
      questionnaire deliberately, not by default.
