# KDP listing sheets: paste-ready answers for the eBook Details form

> One section per title, mirroring the KDP "Kindle eBook Details" form field
> by field. Fill top to bottom, paste, done. Where a field is identical for
> every book it appears once in §1. Amazon's category tree and policies move;
> the categories below are targets, pick the nearest live match in the picker.

**ISBN, since it prompted this sheet:** Kindle eBooks do not get an ISBN at
all; Amazon assigns an ASIN automatically when the ebook publishes. The
**free KDP ISBN is offered on the *paperback* Content tab** (the step after
this form, when you upload the interior PDF and cover). Note before taking
it: the free ISBN lists "Independently published" as the imprint and is
valid only on Amazon; owning your own ISBN block keeps one identity across
every channel (`docs/08-channels.md` §6). Fine to take the free one for
speed and revisit later, since a new edition can carry a new ISBN.

---

## 1. Answers shared by every title

| Form field | Answer |
| --- | --- |
| Language | English |
| Author | Primary: **James** / **Liu** |
| Contributors | None |
| Edition Number | Leave blank (first edition) |
| Series | Leave blank for launch. Optional later: one series name across the shelf (e.g. "Working With AI Field Guides") builds a shared series page; decide once, applies to all |
| Publishing Rights | "I own the copyright and I hold the necessary publishing rights" |
| Sexually Explicit Images or Title | No |
| Reading age | Leave blank |
| Primary marketplace | Amazon.com |
| Pre-order | "I am ready to release my book now" (no pre-order; velocity strategy in `docs/05-kdp-playbook.md` wants launch-week sales concentrated, and the files must be final anyway) |
| Description | Paste-ready HTML per title in §9 below (switch the KDP editor to Source view, paste, switch back). All under the 4,000-character limit including tags |

**Two gates before pressing Publish on any title** (they are not on this
form but come right after it): the AI-content questionnaire on the Content
tab must be answered deliberately per `books/docs/00-kdp-compliance.md`,
and the book's `verified: true` must be a real read-through. Listing copy
can be drafted any time; publishing waits for the signature.

---

## 2. Stop Guessing Whether It Works

| Field | Value |
| --- | --- |
| Book Title | Stop Guessing Whether It Works |
| Subtitle | The Product Manager's Field Guide to Evaluating, Costing, and Shipping AI Features |
| Categories (3) | Computers & Technology → Artificial Intelligence; Business & Money → Management & Leadership → Project Management; Business & Money → Industries → Computers & Technology |
| Keywords (7) | `LLM evals` · `acceptance criteria` · `golden dataset` · `AI PM skills` · `generative AI testing` · `AI risk register` · `machine learning for managers` |

## 3. Your First AI Employee

| Field | Value |
| --- | --- |
| Book Title | Your First AI Employee |
| Subtitle | How to Delegate Real Work to AI, Check Its Output, and Know When to Fire It |
| Categories (3) | Business & Money → Management & Leadership → Delegation & Empowerment (nearest match); Computers & Technology → Artificial Intelligence; Business & Money → Skills → Time Management |
| Keywords (7) | `AI for managers` · `ChatGPT at work` · `AI workflow` · `automation for business` · `managing AI tools` · `practical AI guide` · `AI task management` |

## 4. AI for the Rest of Us

| Field | Value |
| --- | --- |
| Book Title | AI for the Rest of Us |
| Subtitle | The Plain-English Guide to Getting Real Help From AI, No Tech Background Required |
| Categories (3) | Computers & Technology → Artificial Intelligence; Self-Help → Personal Transformation; Reference → Consumer Guides (nearest match) |
| Keywords (7) | `AI for beginners` · `ChatGPT for everyday life` · `how to use AI` · `AI for seniors` · `non technical AI` · `practical AI at home` · `first steps with AI` |

## 5. The One-Person Business's AI Stack

| Field | Value |
| --- | --- |
| Book Title | The One-Person Business's AI Stack |
| Subtitle | How Freelancers and Solopreneurs Use AI to Handle the Admin So They Can Do the Work They're Actually Paid For |
| Categories (3) | Business & Money → Small Business & Entrepreneurship → Home-Based; Business & Money → Small Business & Entrepreneurship → Entrepreneurship; Computers & Technology → Artificial Intelligence |
| Keywords (7) | `AI for freelancers` · `solopreneur tools` · `automate your business` · `AI invoicing proposals` · `self employed productivity` · `solo business systems` · `ChatGPT for small business` |

## 6. The Resume Arms Race

| Field | Value |
| --- | --- |
| Book Title | The Resume Arms Race |
| Subtitle | How Recruiters Stay Useful and Fair When Every Resume Is AI-Written and Every Screen Is AI-Powered |
| Categories (3) | Business & Money → Human Resources → Recruiting & Staffing (nearest match); Business & Money → Job Hunting & Careers; Computers & Technology → Artificial Intelligence |
| Keywords (7) | `AI hiring` · `talent acquisition` · `ATS screening` · `HR technology` · `fair hiring practices` · `interviewing candidates` · `people operations` |

## 7. AI Didn't Close That Deal

| Field | Value |
| --- | --- |
| Book Title | AI Didn't Close That Deal |
| Subtitle | How Sales Leaders Cut Through AI-Generated Noise and Actually Get Replies |
| Categories (3) | Business & Money → Marketing & Sales → Sales & Selling; Business & Money → Management & Leadership; Computers & Technology → Artificial Intelligence |
| Keywords (7) | `cold outreach` · `B2B prospecting` · `sales coaching` · `reply rates email` · `SDR playbook` · `sales team management` · `outbound sales strategy` |

## 8. The Reclaimed Hour

| Field | Value |
| --- | --- |
| Book Title | The Reclaimed Hour |
| Subtitle | A Guide to Using AI to Buy Back Your Time, Not Fill It With More Work |
| Categories (3) | Self-Help → Time Management; Business & Money → Skills → Time Management; Computers & Technology → Artificial Intelligence |
| Keywords (7) | `AI productivity` · `work life balance` · `digital minimalism` · `automation habits` · `slow productivity` · `ChatGPT daily routine` · `overwork recovery` |

---

Keyword rules applied above, keep them when editing: phrases a buyer types
(not single vague words), under 50 characters, and no repetition of words
already in the title or subtitle (those are indexed automatically; the
slots are for what the cover copy doesn't say).

---

## 9. Descriptions, paste-ready HTML

Built from each book's `book.yaml` description (kept as the source of the
prose) plus an "inside the book" list drawn from its real chapters. In the
KDP editor click **Source**, paste the block, click Source again to check
the preview. Bullets under six entries, hook bolded, no headline hype.

### Stop Guessing Whether It Works

```html
<p><b>You are accountable for an AI feature you're not sure how to judge.</b></p>
<p>Every method you learned for shipping software assumes it behaves the same way twice. This one doesn't, so your acceptance criteria stop working, QA passes things that fail in production, and quality arguments get settled by whoever is most senior rather than by evidence.</p>
<p>This book gives you the judgment work that survives every model upgrade. Inside:</p>
<ul>
<li>Acceptance criteria written as evaluation thresholds instead of pass/fail wishes</li>
<li>The golden set: fifty examples you can actually defend in a launch review</li>
<li>Rubrics two reviewers can agree on, and the calibration protocol that proves it</li>
<li>The reliability math of agents, and why a 95%-per-step system fails 40% of the time</li>
<li>What a feature really costs per user, and the margin trap that hides in engagement dashboards</li>
<li>A risk register that gets you through legal review instead of stalling in it</li>
</ul>
<p>Plus three worked case studies, a first-ninety-days plan, and a chapter on exactly where this method breaks, because advice that claims to be universal isn't advice.</p>
<p>Written for product managers, delivery leads, and analysts who are now responsible for AI work. No engineering background required.</p>
```

### Your First AI Employee

```html
<p><b>You don't need to become technical to get real leverage from AI. You need to manage it.</b></p>
<p>Treat it the way you'd treat a fast, eager, occasionally overconfident new hire: give it a real job description instead of a vague request, check its first attempts closely, learn exactly how it fails, and know which tasks it should never touch.</p>
<p>This is a practical, tool-agnostic system for delegating real work to AI, one task at a time, starting with the one already eating your Tuesday afternoon. Inside:</p>
<ul>
<li>The job description that turns a vague request into delegable work</li>
<li>The trial task, and how to check output without redoing it</li>
<li>Learning a tool's failure modes before they cost you, and when to fire a task entirely</li>
<li>Four delegations worked end to end, and six businesses running the same method</li>
<li>What changes when the task involves money, and what to tell clients and customers</li>
<li>A 30-day delegation plan, plus the templates and worksheets to run it</li>
</ul>
<p>No feature tours, nothing that goes stale the next time an app redesigns its interface. Just the management skill underneath, which doesn't change when the tools do.</p>
<p>Written for anyone with a repetitive task and no patience left for either hype or a 40-tab browser of "best AI tools" listicles.</p>
```

### AI for the Rest of Us

```html
<p><b>You don't think of yourself as a tech person, and every AI guide you've opened so far was written by someone who forgot what that felt like.</b> This one wasn't.</p>
<p>No prompt engineering, no jargon, no seventeen-tab comparison of apps you've never heard of. Just plain help with the things actually on your plate:</p>
<ul>
<li>Planning the trip you haven't had time to think about</li>
<li>Writing the letter you've been avoiding</li>
<li>Helping with homework without doing it for your kid</li>
<li>Walking into a doctor's appointment with the right questions</li>
<li>Making sense of a bill, and the money questions you're embarrassed to ask</li>
<li>Knowing the difference between AI being wrong and AI being used against you, including the scams</li>
</ul>
<p>Written for the people every family already calls when the wifi breaks. Except this time the answer isn't "let me look at it", it's a book you can hand over instead, with a final chapter on teaching someone else.</p>
```

### The One-Person Business's AI Stack

```html
<p><b>You didn't start a one-person business to become an invoicing clerk, a part-time contract lawyer, and an unpaid bookkeeper.</b> But somewhere between the client work and the actual craft, that's most of what the job quietly turned into.</p>
<p>This book builds a real stack, not a single silver-bullet app, for the admin that eats a solo business alive. Inside:</p>
<ul>
<li>The proposal that writes itself, and invoicing without the dread</li>
<li>An inbox that doesn't own you, and contracts you can actually understand</li>
<li>The clause and the workflow that protect you from scope creep</li>
<li>Bookkeeping without a bookkeeper, and a marketing department of one</li>
<li>Two real businesses rebuilt over ninety days, worked in full</li>
<li>The 30-day build, the complete template pack, and the honest chapter on when to hire a human instead</li>
</ul>
<p>Every chapter ends with something you actually build that week, not a concept to think about later.</p>
<p>Written for freelancers, consultants, and solo agency owners who got into this to do the work, not to run its back office.</p>
```

### The Resume Arms Race

```html
<p><b>Every resume in your queue reads a little too well now, and the tool you're using to screen them was built by the same technology that wrote them.</b></p>
<p>Something in the middle, the actual signal about whether this person can do this job, is getting crushed between the two. Nobody trained you for what to do about it. This book is a practical answer, not a lament. Inside:</p>
<ul>
<li>What AI screening actually gets wrong, and who it wrongly filters out</li>
<li>Reading past a fluent resume to the real signal underneath</li>
<li>Why the interview just became the most important tool you have</li>
<li>Job posts that select for fit instead of keyword-matching</li>
<li>The bias and liability exposure your talent acquisition training never covered</li>
<li>A screening process you could defend in front of a regulator, or a rejected candidate's lawyer</li>
</ul>
<p>It also takes the candidate's side seriously: applicants use AI too, and that is not automatically cheating. The closing chapters are about what a recruiter's value actually is now.</p>
<p>Written for recruiters and talent acquisition professionals who didn't sign up to referee an arms race, but are standing in the middle of it regardless.</p>
```

### AI Didn't Close That Deal

```html
<p><b>Every prospect's inbox is drowning in AI-generated pitches that all sound the same. Including, if you're honest, some of yours.</b></p>
<p>Reply rates are falling across the board, and the instinct to fix it by sending more is exactly the instinct that caused the problem. This book is a practical reset for sales leaders and the teams they run. Inside:</p>
<ul>
<li>Why volume stopped being a strategy the moment it became free</li>
<li>The research an AI-generated template can't fake, and writing like you actually read their website</li>
<li>Follow-up that doesn't feel like a sequence</li>
<li>Coaching a team off spray-and-pray without losing their pipeline numbers mid-quarter</li>
<li>Where AI still genuinely helps a rep, named honestly</li>
<li>The metrics that lie to sales leaders, and the ones that actually predict revenue</li>
</ul>
<p>Buyers can tell. The last chapters are about what that already costs you, and how to be the one email in the inbox that reads like a person wrote it, because one did.</p>
<p>Written for sales leaders who need their team's outreach to actually get read again, not another tool promising to send more of it faster.</p>
```

### The Reclaimed Hour

```html
<p><b>Every "AI productivity" book on the shelf is quietly a hustle book: use AI to do more in the same hours. This isn't that book, and if that's what you want, it will disappoint you on purpose.</b></p>
<p>Most people who automate a task with AI don't actually get the hour back. They fill it with something else, usually more work, because reclaiming time turns out to be a behavioral problem wearing a technical costume. This book is about the actual behavioral work. Inside:</p>
<ul>
<li>The one-hour audit: finding the hour you already lost</li>
<li>Automating the task you resent most, not the one that demos best</li>
<li>The guilt of having free time, and why the relief evaporates within a week</li>
<li>Protecting the hour from being recolonized by work</li>
<li>When AI makes it worse, not better</li>
<li>Telling your team, or your family, what changed, and a week in the reclaimed life</li>
</ul>
<p>Written for anyone who has automated a task, felt briefly relieved, and then watched something else expand to fill the space.</p>
```
