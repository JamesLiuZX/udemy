# B03 · The Batch Generation Prompt System

Part of *AI UGC Video Ads*. Built in lecture 3.6, the Section 3 workshop, from
lectures 3.2 to 3.5. The companion file is `B03-batch-prompt-sheet.csv`, an empty
sheet with one row per angle and the columns this system needs. It opens in any
spreadsheet. Use it to turn the twenty-row angle map from your brief (B01) into a
batch of static ads with every check built in from the start, and to catch what is
wrong before it reaches a test.

---

## 1. How to use this

1. **Use the same product and brief as B01.** Starting fresh wastes the work you
   already did. Your angle map is the input.
2. **Work in this order,** and expect the whole workshop to run over an hour:

| Step | Time | What "done" looks like |
| --- | --- | --- |
| Translate the 20 angle rows into prompts | 20 min | The five questions in section 2 answered for every row |
| Generate the batch | 5 to 10 min | Twenty statics back |
| Colour and product check | 10 min | Anything off-brand or off-spec flagged |
| Regenerate the flagged statics | 10 min | Only the flagged ones fixed, not the whole batch redone |
| Add overlay text where needed | 15 min | Every exact claim added afterwards, not baked in |

3. **Do not take the two shortcuts.** Describing a colour in words instead of
   supplying a hex code and a reference image causes colour drift on regeneration.
   Baking an exact claim into the image because it is faster than a design tool
   causes garbled text on anything longer than a word.
4. **Expect problems in the first batch.** A batch with none on the first try is
   rare. In the course's own example batch, seven of twenty needed real fixes, and
   both failure types were named and fixable. What matters is catching what is
   wrong before a test, not generating perfectly first time. Do not start over
   because the first batch is imperfect.
5. **Save the finished, checked batch as your B03 record.** It is what the Section 3
   recap summarises and what Section 7 tests.

**Batch: [product name]**

| | |
| --- | --- |
| Product | |
| Brief (B01) version | |
| Owner (a name) | |
| Person who answers for the claims (a name) | |
| Generation tool and version used (record it: results change when the tool does) | |
| Date | |

## 2. The prompt system: five questions per angle row

Answer all five for every row before you generate anything.

| # | Question | The rule |
| --- | --- | --- |
| 1 | Subject | The product plus a scene, matched to the angle's awareness rung |
| 2 | Brand lock | A hex code plus a reference image. Never a colour word alone |
| 3 | Text rule | Bake text into the image only if it is one word or a bare number. Generate everything else clean and overlay it afterwards |
| 4 | Face rule | Include a face only if the angle genuinely needs one |
| 5 | Type | Packshot (a locked reference) or lifestyle (the feeling, not a fact) |

A row from the angle map becomes a prompt row. The shape, with your own product
details where the brackets are:

```text
ANGLE MAP ROW
"[angle]" | [rung] | "[core feeling it interrupts]"

BECOMES THIS PROMPT ROW
[Photorealistic or other style] [product] in [colour name], [scene matched to
the rung], [lighting]. Brand colour: [hex code] exactly, matched to the attached
reference image, no colour interpretation. [No overlay text. / One word or number
only: "..."] [No face close-up. / Face needed because: ...]
```

## 3. Packshot or lifestyle (lecture 3.5)

Sort every row of your angle map into one of two columns before the workshop. They
fail differently when they fail.

| | Packshot | Lifestyle scene |
| --- | --- | --- |
| Has to get right | To be exactly, literally accurate | To feel true, not to be literally documentary |
| If wrong | A customer could receive something that does not match | A missed vibe, not a broken promise |
| Anchor | A locked reference image | The real product's hex code and reference image |

| Image type | Safe to generate? | Why |
| --- | --- | --- |
| Ad packshot, for testing creative | Yes, from a locked reference | You are testing creative, not the listing itself |
| Product listing photo | No | It is what the customer actually receives |
| Lifestyle scene, no face | Yes | The feeling, not the documentation |
| Lifestyle scene with a face | Yes, with the face checks in section 5 | The same uncanny-valley risk applies |

Generating a lifestyle scene does not replace real product photography everywhere.
The one photo a customer's purchase decision rests on stays real.

## 4. The batch table

One row per angle. Fill it before generating, then complete the check columns
afterwards. The CSV carries the same columns plus the full prompt and file name.

| # | Angle (from B01) | Rung | Type | Subject and scene | Hex + reference file | Text rule (baked word/number, or none) | Overlay text to add afterwards (exact, from product truth) | Face? |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | | | | | | | | |
| 2 | | | | | | | | |
| 3 | | | | | | | | |
| 4 | | | | | | | | |
| 5 | | | | | | | | |
| 6 | | | | | | | | |
| 7 | | | | | | | | |
| 8 | | | | | | | | |
| 9 | | | | | | | | |
| 10 | | | | | | | | |
| 11 | | | | | | | | |
| 12 | | | | | | | | |
| 13 | | | | | | | | |
| 14 | | | | | | | | |
| 15 | | | | | | | | |
| 16 | | | | | | | | |
| 17 | | | | | | | | |
| 18 | | | | | | | | |
| 19 | | | | | | | | |
| 20 | | | | | | | | |

## 5. The checks (lectures 3.2 to 3.4)

Run every generated static through all four. Record the result per row in the CSV.

| Check | What to look at | If it fails |
| --- | --- | --- |
| Product | Does the product match the real one's cut, texture and design? Has the generator quietly "improved" a detail? Would the owner recognise it as what they sell? | Regenerate that row with the reference image attached. Checking the colour code alone does not catch this |
| Colour | Is it the exact brand colour, not a nearby one? | Regenerate with the hex code and the reference image, no colour interpretation |
| Text | Is anything garbled? | Regenerate clean, with no text, and overlay it afterwards |
| Face | Is there anything almost-but-not-quite right in proportions, expression or skin? Show it to someone for two seconds and ask what felt off. If they cannot say but something did, that is the uncanny valley | Regenerate without the face, or change the angle |

Regenerate only the flagged rows. Redoing the whole batch discards the thirteen that
were fine.

Record counts for your own batch (do not carry numbers over from anywhere else):

| Count | Your batch |
| --- | --- |
| Generated | |
| Correct product and pose | |
| Correct brand colour | |
| Text fully legible | |
| Faces that pass | |
| Regenerated after checks | |
| Final usable | |

## 6. Text workflow (lecture 3.4)

| Safe to bake in | Always add afterwards |
| --- | --- |
| A single word, or a bare number | Any spec line |
| Short enough that one glyph error is the whole risk | Anything quoting the product truth word for word |

Generate the image clean, then add the exact claim in a design tool, copied from the
product truth document (B01, section 1). This is a manual step per image, and
twenty overlays by hand is real time. It is cheaper than one garbled claim reaching
a real customer. The exact line your product cannot afford to get wrong:

| Prompt | Your answer |
| --- | --- |
| The one line of exact copy my product cannot afford to get wrong | |
| Where it comes from in the product truth (B01, section 1) | |
| Who checks the overlay against it (a name) | |

## 7. Before anything is tested

| Check | Done? |
| --- | --- |
| Every overlay line matches the product truth wording and the claims boundary | |
| No outcome claim, endorsement or invented statistic appears in any image | |
| Each platform's current rules for AI-generated imagery and ad content checked, by the person named above | |
| Product listing images are real photography, not generated | |
| The congruence checklist (B01, section 6) is run against the landing page | |

This template does not tell you what each platform's rules say or what is lawful
for your product. Check them for yourself, with qualified advice where a claim
touches a regulated area.

## 8. Honest test

- Does every prompt row carry a hex code and a reference image, not a colour word?
- Is any exact claim baked into an image instead of overlaid afterwards?
- Did you check the product against the real one, not only the colour?
- Did you regenerate only the flagged rows?
- Is every number in section 5 from your own batch?

## 9. Open gaps

| Section | What is missing | Owner and date |
| --- | --- | --- |
| | | |
