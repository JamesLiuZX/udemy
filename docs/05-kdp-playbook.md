# KDP playbook: the book that grows the course

> There is no book in this repo yet. This document is the strategy from zero:
> what the book is, the craft bar, the production pipeline (reusing what this
> repo already does well), and the Amazon mechanics. Written to the same
> standard as `00-strategy.md`: decisions with reasons, so they don't get
> relitigated.

---

## 1. "NYT bestseller level" needs translating before it can be a target

Say this plainly once, then aim at the right thing.

The New York Times list is curated, weights sales through reporting physical
retailers, and in practice excludes almost all self-published KDP nonfiction
regardless of sales. A KDP-first book does not get on that list; that is a
distribution fact, not a quality judgement.

So split the ambition into its two real parts:

- **NYT-level craft:** achievable, and this document's job. The bar is "a
  reader cannot tell this from a good trade-published business book", which
  means developmental structure, line-level voice, professional cover and
  interior, and zero AI tells.
- **Bestseller mechanics, translated to Amazon:** the achievable equivalents
  that actually drive income and referrals:

| Target | Threshold | Why it matters |
| --- | --- | --- |
| Amazon Best Seller flag | #1 in a well-chosen niche category | Social proof on the listing, screenshot for everything |
| Ratings | 50+ at 4.6 within 6 months, 100+ in year one | The browse-page conversion driver |
| Rank durability | Top 20k overall store rank sustained | Where organic Amazon recommendation traffic switches on |
| Referral test | A reader gifts it to their boss or team | The book equivalent of "tell a friend", and the actual sales engine for business books |

The referral test shapes everything below: business books get referred when
they are short, opinionated, and give the reader language they can reuse.

---

## 2. What the book is (and is not)

**The book is not the course transcript.** They do different jobs and cannibalise
nothing: the course teaches *doing* (workshops, artifacts, hands-on); the book
carries *the argument and the stories*, readable on a flight, giftable to a
manager who will never watch a course.

**Comparable models** (structure and length, not content): *The Mom Test*,
*Continuous Discovery Habits*. Short, first-person, one big idea, ruthlessly
concrete, cited in meetings for years. Note what they are not: 300-page
compendiums. In this genre, length is inversely correlated with referrals.

**Spec:**

| Property | Decision | Reason |
| --- | --- | --- |
| Length | 35,000 to 45,000 words, 12 to 14 chapters | Airport-readable; matches the comps; short books get finished, finished books get reviewed |
| Spine | The course's big idea: an AI feature is a distribution, not a function | Already validated positioning; one book, one idea |
| Story | The full Fernhill serial (see `story-bible.yaml`), told properly | The course rations it to beats; the book is where it breathes |
| Voice | Same house voice: second person, concrete, names the cost | The rules in CLAUDE.md §4 transfer verbatim |
| English | en_GB, same as the scripts | One lexicon, one spellcheck, reuse of course prose without a translation pass. It reads as a voice, not an error |
| Formats | Ebook + paperback at launch; hardcover only if the paperback earns it | Hardcover setup cost is real, signal at launch is not |

**Working titles** (main title memorable, subtitle carries the keywords, since
Amazon search indexes both):

1. *Distributions, Not Functions: How to Spec, Evaluate and Ship AI Features
   That Actually Work*
2. *The Eval: Judgement Work for People Accountable for AI*
3. *Fix the Ruler: Evaluating AI Features When Nobody Can Agree What Good
   Looks Like*

Validate the shortlist against Amazon search autocomplete for "AI product
management", "AI evaluation", "LLM evals" before committing.

---

## 3. The craft bar, and how to beat the long-form LLM failure modes

Every rule from CLAUDE.md §4 applies to the manuscript. These are additional,
book-specific, and each targets a known failure mode of generated long-form:

1. **Chapters open cold.** A scene, a number, or an artifact. Never "In this
   chapter we will". The agenda-opener is the same tell in print as on video.
2. **No symmetric scaffolding.** Chapters must not share a template shape
   (hook, three points, recap, done). Uniform chapter architecture is the
   book-length version of uniform sentence rhythm. Vary length deliberately:
   the incident chapter should be the shortest and hit the hardest.
3. **State lives in files, not in memory.** The length constraint on generated
   text is really a *state* constraint: drift in names, numbers and claims
   across 40,000 words. The fix is the same as the course's: the story bible
   holds every fact, a `terms.yaml` lexicon holds every coined phrase, and a
   continuity QC pass literal-matches the manuscript against both. Write
   chapter by chapter, one file each; consistency comes from the bible, not
   from context length.
4. **Each chapter ends in the world, not in summary.** The closing move is
   "what to do Monday", one concrete action, not a recap.
5. **The stories must eventually be the instructor's.** Fernhill carries the
   teaching, but a book with zero true first-person war stories reads hollow
   and is the print version of the Udemy presence problem.
   `[INSTRUCTOR-INPUT]` markers work in manuscript files too, and the book QC
   pass must block on them identically.
6. **Read-aloud pass on every chapter.** The scripts earned their voice by
   being written for the ear; the book keeps it the same way. If it cannot be
   read aloud, it gets cut or recast.
7. **Em dash ban, filler ban, tell ban:** carried over, enforced by the same
   regexes.

---

## 4. Production pipeline: reuse, don't rebuild

The repo's core insight (single markdown source, deterministic rendering,
quality gates as code) transfers whole. Target layout:

```
books/distributions-not-functions/
  book.yaml            # metadata, spine, pricing, categories, keywords
  chapters/NN-slug.md  # one file per chapter, front-matter: verified, status
  figures/             # figure specs (same YAML dialect as lectures)
```

- **Figures:** `pipeline/figures.py` already produces deterministic,
  typo-proof SVG. Add a print profile: 300dpi-equivalent sizing, and a
  **greyscale-safe palette**, because the paperback interior should be black
  and white (colour interior printing costs multiples per page and the comps
  are all mono). The blue/orange pair must be re-validated for luminance
  separation in greyscale; if it fails, the print profile swaps to
  solid-vs-outline or solid-vs-hatched marks instead of hue pairs. The
  no-generative-images rule is absolute in print too.
- **Interior (paperback):** the same Chromium already rendering slides can
  print-to-PDF a typeset interior from HTML/CSS (`theme/book.css`: 6×9in trim,
  KDP margin spec, running heads, front matter, embedded fonts). Same
  toolchain, zero new dependencies. The design direction transfers: a printed
  textbook page is literally what the deck was imitating.
- **Ebook:** EPUB is a zip of XHTML; buildable with the standard library, or
  hand off the final manuscript to Calibre/Pandoc locally if preferred. KDP
  accepts EPUB and docx. Decide at build time; nothing upstream depends on it.
- **Cover:** commission a human designer (roughly $300 to $800 for the tier
  that matters). The cover is the one asset where "generated" is instantly
  legible to buyers and where this repo's design system does not apply. Brief
  the designer with the deck's aesthetic (white paper, printed ink, Schola).
  Non-negotiable: no AI-generated cover art.
- **QC:** a `--book` mode on `qc.py` running: spellcheck (en_GB), em dash FAIL,
  filler/tell WARN, `verified` gate per chapter, `[INSTRUCTOR-INPUT]` FAIL,
  continuity match against the story bible and lexicon, sentence-rhythm
  variance WARN, and a chapter-shape check (WARN when consecutive chapters
  have near-identical section counts and lengths).

**Sequencing:** draft the book after course Section 4 is written and verified.
Sections 0 to 4 contain the book's first two thirds in raw form, the Fernhill
beats will have been stress-tested, and the strongest material (evaluation)
will be fresh. Drafting from verified course scripts also means every claim
was already signed off once. Expect the de-verbalising pass (script prose to
page prose) to be a real rewrite, not a copy-edit: narration says "look at
this picture", pages don't.

---

## 5. Amazon mechanics

Decisions with reasons; revisit only with new evidence.

| Lever | Decision | Reason |
| --- | --- | --- |
| Categories | 3 (chosen at upload). One winnable niche (e.g. product management), one mid-size, one aspirational | The Best Seller flag comes from the niche one |
| Keywords | All 7 slots, phrase-level from autocomplete research, no repetition of title words | Title words are already indexed; slots are for what the title doesn't say |
| Ebook launch price | $0.99 for launch week, then $4.99, then $9.99 once 25+ ratings exist | Velocity first (rank compounds), then the 70% royalty band ($2.99 to $9.99) |
| Paperback price | $19 to $24 | Business-book norm; also makes the ebook look cheap |
| KDP Select / KU | Enrol for the first 90 days, then reassess | Free-day and countdown promos help launch velocity; B2B nonfiction KU read-through is modest, so exclusivity is cheap early and reviewable later |
| A+ content | Yes, from day one | Free conversion surface almost no self-pub business book uses well; reuse course figures |
| Author page | Set up before launch, photo and bio matching the Udemy instructor profile | Cross-surface trust; buyers do check |
| Ads | Amazon Ads auto campaign at launch ($5 to $10/day) to harvest search terms, then one exact-match campaign on the winners | Cheap keyword research plus steady visibility; kill anything above break-even ACOS after 30 days |

**Review engine, strictly inside Amazon's rules:** never pay, never
incentivise, never swap, no friends-and-family (Amazon filters and sometimes
penalises). What works and is allowed:

1. An ARC team recruited from the email list (see the growth engine doc):
   advance copy in exchange for nothing but the ask; readers disclose they
   received an advance copy.
2. The back-matter ask, placed immediately after the final chapter's last
   line, one sentence, honest.
3. The course as a review flywheel: course students who liked Section 4 are
   the highest-intent early readers, and vice versa.

---

## 6. The loop with the course

The book is top-of-funnel; the course is the monetisation depth; the email
list connects them (only the book's back matter can link out freely, and only
Udemy's bonus lecture can promote off-platform).

- Book back matter: one page offering the companion artifact pack (the rubric
  template and golden-set spec from the course) via email signup on your own
  site, which then drips a course coupon.
- Course bonus lecture: the book, one line, one link.
- Shared lexicon: the named concepts (`the margin trap`, `fix the ruler`)
  appear identically in both. Someone who hears a phrase in a meeting should
  find both products when they search it.

## 7. Order of work

1. Finish course Section 4 (the book depends on it).
2. Write `books/.../book.yaml`, the chapter outline, and chapters 1 to 3;
   run the read-aloud pass; recalibrate the outline before drafting on.
3. Build the book QC mode and the print figure profile while chapters draft.
4. Instructor pass: war stories in, `verified: true` chapter by chapter.
5. Commission the cover as soon as the title survives autocomplete research.
6. ARC to the list 3 weeks before launch; launch week per §5; ads on day one.
