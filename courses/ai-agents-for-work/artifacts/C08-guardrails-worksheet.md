# Guardrails and Approval Worksheet

*From AI Agents for Your Job. Fill this in before you connect any new credential or add any new capability to an existing agent, not only when you build one from scratch.*

## 1. What is actually being added

Name it in one sentence, the way you would explain it to a colleague.

> Example: "A search tool so the follow-up chaser can check whether a
> client already replied before drafting a chase."

## 2. Does this change the scope?

- What can this new piece reach that the agent could not reach before?
- Is that reach narrower than, equal to, or wider than the agent's existing job description?

If the answer is "wider," stop and go back to C05. A new capability with wider reach is a new job description, not an addition to the old one.

## 3. The credential check

- What exact permission level does this connection ask for?
- Is there a narrower option? (Provider consent screens often offer one, easy to miss under time pressure)
- Would you recognise it immediately if this credential's access were wider than you intended?

## 4. Approval gate

- Does this capability's output need a human step before anything leaves the workflow?
- If yes, name the exact node or step where a human is required. If you cannot name one, there isn't one.
- Who is that human, specifically, not "someone"?

## 5. The blast radius question, one more time

**If this new piece did the worst plausible thing it is capable of, right now, what would it reach and what would it cost?**

Answer this for the new piece specifically, not for the agent as a whole. A narrow agent with one wide-scoped addition is a wide-scoped agent.

## 6. Sign-off

- [ ] Scope confirmed narrower than or equal to the existing job description
- [ ] Credential permission level checked against the narrowest option available
- [ ] Approval gate named, or explicitly not needed and why
- [ ] Blast radius question answered honestly

---
*Part of the AI Agents for Your Job artifact set. Run this worksheet every time, including for changes that feel small. The incident in Section 8.4 started as a small change.*
