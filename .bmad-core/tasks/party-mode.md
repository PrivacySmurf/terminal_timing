# Party Mode - Multi-Agent Feedback Session

## Purpose

Party mode brings multiple relevant agents together to provide diverse perspectives on the current work. Use this after completing a workflow step to get feedback, identify gaps, and surface concerns before moving forward.

## When to Offer Party Mode

**Automatically suggest party mode after:**
- Completing a PRD section → Invite: Architect, Dev, QA
- Finishing architecture design → Invite: Dev, QA, PM
- Creating a story → Invite: Dev, QA, PO
- Completing implementation → Invite: QA, Architect
- Any major decision point → Invite relevant agents

## Execution Flow

### Step 1: Context Summary
Briefly summarize what was just completed:
- What artifact/section was created
- Key decisions made
- Any assumptions or trade-offs

### Step 2: Agent Selection
Based on the context, select 2-4 relevant agents:

| Current Agent | Relevant Party Agents | Focus Areas |
|---------------|----------------------|-------------|
| Analyst | PM, Architect | Feasibility, scope |
| PM | Architect, Dev, QA | Technical feasibility, testability, clarity |
| Architect | Dev, QA, PM | Implementation concerns, test strategy, requirement gaps |
| UX Expert | Dev, PM, Architect | Technical constraints, requirement alignment |
| SM | Dev, QA, PO | Story clarity, acceptance criteria, estimates |
| Dev | QA, Architect, SM | Test coverage, architecture compliance, blockers |
| QA | Dev, Architect, PM | Code quality, requirement coverage, risk areas |
| PO | All relevant | Alignment, priorities, trade-offs |

### Step 3: Structured Feedback Round

For each invited agent, provide perspective in this format:

```
---
🎭 [Agent Icon] [Agent Name] ([Role])
---

**Review of:** [artifact/section name]

**Observations:**
- [Key observations from this agent's perspective]

**Concerns:**
- [Any concerns or potential issues]

**Suggestions:**
- [Specific recommendations]

**Questions for clarification:**
- [Questions that need answers before proceeding]

---
```

### Step 4: Synthesis

After all agents have provided input:

1. **Consolidated Issues** - List all concerns raised, grouped by severity:
   - 🔴 Blockers (must address before proceeding)
   - 🟡 Important (should address soon)
   - 🟢 Minor (nice to have)

2. **Action Items** - Specific changes or investigations needed

3. **Decision Points** - Questions that need user input

### Step 5: Resolution Options

Present numbered options:
1. Address all blockers now, then proceed
2. Note concerns and proceed (tech debt)
3. Deep dive on specific concern (specify which)
4. Return to current agent and continue
5. Switch to specific agent to address their concerns

## Quick Party Mode

For faster feedback, use abbreviated format:

```
🎭 Quick Party Feedback on [artifact]

👨‍💼 PM: [one-line perspective]
🏗️ Architect: [one-line perspective]  
💻 Dev: [one-line perspective]
🧪 QA: [one-line perspective]

Key concern: [most critical issue if any]
Recommend: [suggested action]
```

## Party Mode Triggers

**Explicit:** User says `*party-mode` or "get feedback from other agents"

**Automatic offer after:**
- Any `elicit: true` section is completed
- A document draft is finished
- A story is created or approved
- Implementation is marked ready for review
- Any time user seems uncertain about a decision

## CRITICAL RULES

1. **Stay brief** - Each agent gets 3-5 bullet points max
2. **Be specific** - Generic feedback is useless
3. **Identify real issues** - Don't manufacture concerns
4. **Respect expertise** - Each agent only comments on their domain
5. **Actionable output** - Every concern should have a suggested resolution
6. **Don't overwhelm** - Max 4 agents per party session
