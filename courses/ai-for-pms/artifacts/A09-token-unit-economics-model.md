# A09 · Token Unit-Economics Model

Part of *AI Product Skills for PMs & Analysts*. Built in lecture 7.2 and used
again in the workshop, lecture 7.7. The companion file is
`A09-token-unit-economics-model.xlsx`. It opens in Excel, Google Sheets and
LibreOffice, uses no macros, and is empty: no price, volume or token count is
filled in for you. Use it to turn a token count into the number a launch review
asks about.

---

## 1. How to use this

1. **Make a copy of the workbook.** On the **Model** tab, fill the yellow cells:
   six inputs, a label for each, and a line saying where the number came from.
2. **Label every input Measured or Estimated.** The dropdown is not decoration.
   A model where every number is labelled tells a reviewer which ones to
   attack.
3. **Measure the token counts, do not guess them.** Run your golden set (A02,
   fifty real cases) through the actual feature and take the real input and
   output token counts per conversation. A few test conversations run by the
   team that built the feature are naturally shorter and tidier than real use.
4. **Get the prices from your provider's current price page.** Prices change.
   Enter the input price and the output price separately, per million tokens.
   Output is typically priced several times higher than input, so a short
   question with a long answer can cost more than a long question with a short
   one.
5. **Borrow usage assumptions from the closest real analogue.** For
   conversations per user, use the volume on the channel the feature replaces
   (ticket volume for a support tool, for example), not an invented figure. Say
   in column D where it came from.
6. **Read all three levels, and the one that changes your reaction most.**
7. **Read the checks.** All three should say OK before you show the model to
   anyone.

## 2. The three levels

| Level | Calculation | Tab and cell |
| --- | --- | --- |
| Per conversation | (input tokens x input price per million / 1,000,000) + (output tokens x output price per million / 1,000,000) | Model B12 |
| Per user, per month | cost per conversation x conversations per user per month | Model B13 |
| All users, per month | cost per user x active users | Model B14 |

The model also shows the share of the per-conversation cost that comes from
output tokens (B15), and the monthly total at half, double and triple your
usage assumption (row 19). The usage numbers are the least certain inputs, so
look at the right-hand end of that row before you present the middle one.

## 3. Worked example, from lecture 7.2

An example of the arithmetic only. Do not reuse these prices or volumes for your
own feature.

| Input | Example value |
| --- | --- |
| Input tokens per conversation | 8,000 |
| Output tokens per conversation | 1,200 |
| Input price per million tokens | 3 |
| Output price per million tokens | 15 |
| Conversations per user per month | 4 |
| Active users | 50,000 |

| Level | Calculation | Result |
| --- | --- | --- |
| Per conversation | (8,000 x 3 / 1,000,000) + (1,200 x 15 / 1,000,000) | 0.042 |
| Per user, per month | 0.042 x 4 | 0.168 |
| All users, per month | 0.168 x 50,000 | 8,400 |

In the example, about 43% of the per-conversation cost is output tokens even
though output is the smaller token count.

## 4. The Conversation tab (lecture 7.1)

A ten-turn conversation does not cost ten times one turn. Every turn resends the
whole history, so billed input grows with each turn.

1. Enter the new input tokens per turn, the output tokens per turn, and the
   number of turns (1 to 30).
2. The table shows, for each turn, the new content, the history resent, and the
   billed input.
3. Set output tokens per turn to 0 to count only what the user types, as lecture
   7.1's table does. With 200 new tokens per turn that gives 200 on turn 1 and
   2,000 on turn 10. Add output tokens per turn and the history grows faster,
   because the model's own replies are resent too.
4. The totals at the right give billed input, output and the part of the input
   that is resent history.

Use the totals as the Model tab's token counts only if the turn sizes come from
real conversations. Totals built from guessed turn sizes are estimates, and the
Model tab will tell you so if you label them that way.

## 5. Limits

- The model prices tokens only. It does not include caching, batching, model
  routing, retries, embedding or retrieval costs, or engineering time. Those are
  Section 7's later lectures, and each one changes the inputs rather than the
  structure.
- Resending history is not a mistake to eliminate. It is what keeps the model
  coherent across turns. The fix is to cache it cheaply, not to stop sending it.
- Steady state is assumed. A launch month, a spike or a campaign will not look
  like the average.
- Token counts can be measured precisely. Conversations per user and active
  users are guesses before launch. The model is only as honest as those two
  numbers.

## 6. Where this fits

A02 supplies the cases whose token counts you measure. This model feeds the
margin question in lecture 7.5 and the model comparison in the selection
scorecard (A10): a cheaper model is only cheaper once its quality on your golden
set is known. If the PRD (A01) states a cost per interaction, this is the sheet
that checks it.
