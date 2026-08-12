# X thread (launch week)

**Post:** T0 (launch day), can repost/pin through the week

---

**1/**
A tribunal made an airline pay damages because its chatbot invented a
refund policy. The airline argued the bot was "a separate legal entity."

That's chapter 1 of a book I just shipped. Thread on why most AI feature
QA is built for the wrong kind of software.

**2/**
Normal software: same input, same output. Your acceptance criteria say
"click submit, see confirmation." You can write that as a yes/no test
once and be done.

AI features: same input, different output, every time. A yes/no test
breaks on the first re-run.

**3/**
So the fix isn't a better checklist. It's a different kind of criteria
entirely: evaluation thresholds on a golden dataset, not pass/fail rules.
"94% of the 40 hardest cases pass" instead of "it works."

**4/**
Agent reliability math nobody does before shipping: 95% success per step
sounds fine. Chain ten steps together and it's a coin flip. Chain twenty
and you're worse than a coin flip.

Multiply it out before you scope the agent, not after the incident.

**5/**
The cost model matters more than people think. Four cents times how many
conversations, times how many times a day, times how many months before
finance asks and nobody in the room has the number.

**6/**
The risk register chapter exists because "get a risk assessment done
first" is the sentence that kills more AI features in legal review than
any technical failure. A working register is one page: risk, owner,
mitigation, date. Most teams don't have one.

**7/**
Thirty real, independently verified cases run through the book: a
transcription tool that invented medical treatments, a benefits bot that
hallucinated a vacation policy a manager approved, a $25M wire transfer
authorized over a video call where every other participant was an AI
deepfake.

**8/**
Book's called Stop Guessing Whether It Works. Kindle's $0.99 today, then
the price moves up through the week.

[Amazon link]

For PMs, delivery leads, and analysts who are now accountable for an AI
feature and weren't trained to judge one.
