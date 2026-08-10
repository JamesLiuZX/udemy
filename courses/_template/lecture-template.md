---
# Copy to courses/<slug>/lectures/<id>-<short-name>.md
id: "4.2"
title: "Building a golden set: 50 examples that matter"
section: 4
duration_target: 8          # minutes; ~150 spoken words per minute
voice: tts                  # tts | human  (human = instructor records it)
verified: false             # NEVER set true yourself. Instructor signs off.
hands_on: false
objectives:
  - "One capability the learner has after this that they did not have before"
notes: >-
  Anything the instructor needs to know when reviewing or recording this.
---

# ---------------------------------------------------------------------------
# Layouts: title statement bullets two-col table code math diagram figure
#          metrics callout definition example sidenote quote section
# Directives (anywhere in a slide body):
#          kicker: lead: note: attrib: sec_num: class: figcap:
# Inline:  **bold**  *accent*  `code`  ==highlight==  $math$
#
# Rules that QC enforces:
#   - narration must NOT restate the slide (fails above 25% phrase overlap)
#   - no em dashes anywhere a learner reads or hears
#   - no unfilled [INSTRUCTOR-INPUT] markers in a release build
# ---------------------------------------------------------------------------

@slide statement
kicker: Section 4 · The instrument
class: center
## The one sentence this lecture exists to deliver.
lead: A second line that sharpens it, not one that repeats it.

@narrate
Open with the problem the learner already feels, in their words, not yours.

Then say what this lecture will let them do. Short sentences. Second person. Do
not describe the slide, argue for it.


@slide two-col
kicker: The contrast
## What changes

::: cols
:: card bad
### What people do now
- The familiar, broken habit
- A second symptom of it
:: card good
### What you will do instead
- The replacement, stated concretely
- With a number where possible
:::

@narrate
Explain why the left column is reasonable rather than stupid. Learners have to
recognise themselves without feeling insulted, or they stop listening.

Then earn the right column. This is the argument, and it belongs here in the
narration rather than on the slide.


@slide figure
kicker: The evidence
## What the data actually looks like
figcap: One sentence saying what the reader should take from this figure.

```figure
kind: dotplot
lo: 1
hi: 5
axis_label: "Score out of 5"
series:
  - {label: "Before", note: "judgement alone", values: [2, 3, 3, 4, 5]}
  - {label: "After",  note: "with a rubric",   values: [3, 3, 3, 3, 4]}
```

@narrate
Walk the picture. Say what the reader is looking at, then what it means, then
what it does not mean. The third part is where credibility is won.


@slide definition
kicker: Stating it precisely

::: definition Key idea
The term, defined tightly enough to be usable and short enough to remember.
:::

::: example Try this yourself
A concrete thing the learner can do in under five minutes with their own work.
:::

@narrate
Do not read the definition aloud. Point at the one word in it that carries the
weight, and explain why that word is there.


@slide callout
kicker: The honest trade

::: callout Be straight about this
Where this technique is expensive, slow, or the wrong tool. Name the cost
plainly, then give the ==argument that wins== anyway.
:::

@narrate
Say the cost out loud. This is the single strongest credibility signal available,
and almost no competing course does it.


@slide bullets
kicker: Before you move on
## What to do now

1. The concrete action, with the artifact attached to this lecture
2. The version they can do against their own work today

@narrate
Close with the action, then one sentence of forward motion into the next lecture
so the learner keeps going.
