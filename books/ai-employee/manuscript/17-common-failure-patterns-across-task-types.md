# Common Failure Patterns Across Task Types

Every chapter so far built a failure-mode list one task at a time, the way chapter five recommends: specific to this task, this tool, discovered through your own trial. That's still the right way to build the list that actually governs a task you're running. But after a dozen examples across this book, a second, useful pattern comes into view: tasks that share a basic shape tend to share a basic failure pattern too, before you've run a single trial of your own. This chapter organizes what's already been shown by task type, so the next task you delegate starts with a head start instead of a blank slate.

[KEY-INSIGHT: A large-scale study that automatically catalogued AI model errors across 21 datasets and 73 different models found that some of the most common failure types are also among the least discussed: quietly omitting a required piece of information from an otherwise complete-looking answer, and misinterpreting exactly what was being asked, rather than the more commonly assumed failure of simply stating a wrong fact. || Source: Ashury-Tahan, S., Mai, Y., Bandel, E., Shmueli-Scheuer, M., & Choshen, L., "ErrorMap and ErrorAtlas: Charting the Failure Landscape of Large Language Models," arXiv:2601.15812, January 2026.]

That finding matters for how you read the patterns below. The instinct is to watch for a tool inventing something false, and that's real and worth watching for. It's just not the only shape a failure takes, and quiet omission or subtle misreading of the actual request are, per that research, at least as common and considerably easier to miss on a casual read.

## Writing and drafting tasks

The pattern across Priya's listing descriptions, Renata's review replies, and Devon's proposal drafts: fluent, well-structured prose that's wrong in a way the structure itself hides. A generically pleasant sentence reads exactly as confidently whether the fact inside it is real or invented, whether the tone matches your actual voice or a plausible generic approximation of it. Watch for: specific claims dressed in confident prose, especially numbers, dates, and names filling a gap the source material didn't actually cover. The fix that recurs across every writing-task example in this book is the same one: a concrete brief with your own real example, chapter two, and a spot-check aimed specifically at any claim that sounds more specific than the input actually was.

## Categorization and triage tasks

Maria's expense categories, James's maintenance-ticket triage, the McDonald's drive-thru case: this task type fails at boundaries, not at the middle of an obvious case. A clearly routine ticket gets triaged correctly almost every time. The failure clusters at the edge between two categories that look similar on the surface and aren't, fuel versus equipment, routine versus a genuine water-leak emergency. Watch for: any input that could plausibly belong to two categories at once, and check that specific overlap completely rather than sampling the whole batch evenly, chapter four's seam-finding applied at its most literal.

## Scheduling and calendar tasks

Devon's timezone-confused calendar assistant is the model case here: a small, silent assumption, that "3pm" meant the same thing to both people in the exchange, propagating into a real conflict nobody noticed until it was nearly too late. This task type's failures are rarely dramatic. They're quiet defaults, an assumed timezone, an assumed date format, an assumed recurrence pattern, that go unquestioned because nothing about the output looks wrong until it collides with a fact the tool never had. Watch for: any date, time, or recurrence detail that depended on an assumption rather than an explicit statement in the original request, and make explicit confirmation of exactly that detail part of the brief itself.

## Research and summarization tasks

Ola's fundraising letter and the AI legal research tools from chapter five share this task type's signature failure: an invented or misattributed specific fact, built into a larger, otherwise accurate-sounding piece of writing, that's nearly impossible to catch without checking against the actual source. Unlike a writing task's generic fabrication, this failure often traces to a real but different source, a statistic that's true of a different year, a claim that's true of a different case, close enough to sound right and wrong enough to matter. Watch for: any number or named fact that could be checked against a specific, retrievable source, and check it against that source directly rather than against how plausible it sounds.

## Chained, multi-step tasks

Chapter nine covered this in depth and it's worth summarizing here for completeness: a chain's failure isn't usually any single step failing badly. It's an ordinary, small imperfection in an early step getting built on, restated, and dressed up in confident prose by every step that follows, until the final output shows no trace of where the actual problem started. Watch for: this is the one pattern that isn't caught by watching the finished output more carefully. It's only caught by checking each step's output before it becomes the next step's input, chapter nine's checkpoint discipline, because by the time a chain's output looks finished, the evidence of where it went wrong is usually already gone.

## Using this chapter

None of these five patterns replace the failure-mode list chapter five asks you to build for your own specific task and tool. They're a starting hypothesis, not a substitute for the evidence a real trial produces. A new writing task probably fails somewhere close to the writing-task pattern above; confirm that with your own three to five attempts rather than assuming it, the same discipline chapter three has argued for from the start. What this chapter buys you is a better first guess about where to look first, not a reason to skip looking.

[TAKEAWAYS]

- Tasks that share a basic shape tend to share a basic failure pattern: writing tasks fabricate specifics inside fluent prose, categorization tasks fail at category boundaries, scheduling tasks fail on silent assumptions, research tasks misattribute real facts, and chains compound an early, small error.
- Quiet omission and misreading the actual request are, per large-scale error research, at least as common as outright invention, and considerably easier to miss on a casual read.
- Use these patterns as a starting hypothesis for a new task's likely seam, then confirm or correct that hypothesis with a real trial, chapter three's discipline, rather than trusting the pattern blindly.

[/TAKEAWAYS]

## Where this goes next

Chapter eighteen covers a discipline this book has mentioned in passing several times without giving it its own space: periodically revisiting a task you already fired, on purpose, rather than assuming a closed door stays closed forever.
