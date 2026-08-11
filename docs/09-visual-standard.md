# Visual standard: screenshots, diagrams, and where generated images belong

> Author directive, August 2026. The original blanket rule ("no generative
> images anywhere") protected against real failure modes: mangled text in AI
> images is a top learner complaint, and a slide of bullets was never at
> risk of hallucinating. But the cure overshot: text-and-table slides read
> as a relic, and a page of unbroken prose is dry. This standard replaces
> the blanket ban with lanes. The safeguards survive; the dinosaur dies.

## 1. The hierarchy (courses and books both)

For any visual moment, prefer the highest lane that fits:

1. **Real screenshots of real tools.** First-class citizens now, and
   mandatory in any lecture that teaches a tool. Capture actual UIs
   (n8n canvases, ad managers, dashboards, KDP forms), crop tight, and
   annotate deterministically (numbered callouts, boxes and arrows drawn by
   the pipeline or an image editor, never baked into an AI generation).
   Every screenshot is freshness-tracked (`freshness_watch` / `facts.yaml`):
   a stale UI screenshot is the visual version of a wrong price.
2. **Diagrams and charts generated from data.** The existing figures
   pipeline, mermaid, and new figure kinds as needed. Still the only lane
   allowed to carry numbers, labels, and factual structure, because it is
   the only lane that cannot mangle them.
3. **AI-generated images, two narrow lanes only:**
   - **Specimens**: where AI output *is the subject matter* (an AI-generated
     ad creative in the UGC course, an example of AI slop being critiqued).
     These are content, not decoration; caption them as what they are.
   - **Atmosphere**: scene-setting illustrations with **zero embedded text,
     numbers, charts, UI, or factual claims** (a workspace, an abstract
     texture, a chapter-opening illustration). Human-reviewable at a glance
     precisely because nothing in them can be factually wrong.
   Never for diagrams, never for anything a learner might read data from,
   never for covers (covers stay human-commissioned), and never passed off
   as a photograph of something real.

## 2. Course slides

- A lecture teaching a tool without a screenshot of it is a defect, not a
  style choice. Target for tool-led lectures: screenshots on most slides.
- Slides that are pure bullets remain capped (docs/04 §6). The upgrade
  path for an existing text slide, in order: screenshot, diagram, table,
  and only then keep the bullets because the content genuinely is a list.
- Screenshot mechanics: capture at 2x for 1920-wide slides, crop to the
  region that matters, house-style annotation (ink-blue callouts, numbered
  in the sans). Sessions capture what is reachable headlessly (public UIs,
  self-hosted tools like n8n, marketing/docs pages) and record a
  `[SCREENSHOT-NEEDED: tool, state, what to show]` marker where only the
  author's logged-in account can reach the state; those markers block the
  release build like INSTRUCTOR-INPUT does, and the list goes in the
  editorial report.
- Licensing note: screenshots of software UIs for instruction are standard
  practice; open-source tools (n8n is source-available) are safest ground.
  Do not screenshot content owned by third parties (someone's ad, someone's
  dashboard data); reconstruct with the running case's fictional data.

## 3. Book interiors

Print is black and white and the dryness fix is structural, not clip-art:

- Every chapter gets at least one **worked visual**: a diagram from the
  figures pipeline (print profile), a filled-in worksheet page, an
  annotated before/after, or a screenshot where the book teaches a tool
  (same annotation and freshness rules as slides).
- AI-generated images in books are limited to the specimen lane, and each
  one flips the KDP dashboard answer for AI-generated *images* to yes;
  weigh that per title deliberately (`books/docs/00-kdp-compliance.md`).
  Atmosphere images are a poor trade in a B&W business paperback; prefer
  typographic devices (the existing pullquotes, key-insight boxes) plus
  real diagrams.

## 4. The hook standard (books and lectures both)

Visuals fix the eyes; the hook fixes whether anyone tells a friend. Every
chapter and every lecture must be able to answer, in one line each, written
in the session's notes or editorial report:

- **The hook**: why would someone who did not plan to read this keep
  reading after the first half page?
- **The golden nugget**: the one thing the reader gets here that they did
  not have this morning, stated so concretely they could use it today.

If either answer is weak, the chapter is not done, whatever the word count
says. "Rigorously researched" means the nugget is current (SOTA tools and
numbers verified live at writing time) and the audience fit is explicit:
who this chapter serves, and what they already know.
