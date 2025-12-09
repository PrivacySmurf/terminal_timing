# Project Template (BMAD-METHOD for Warp)

A project template using the BMAD-METHOD™ framework, optimized for Warp Agent Mode.

## Quick Start

1. **Copy this template:**
   ```bash
   cp -r bmad-template my-new-project
   cd my-new-project
   ```

2. **Initialize git:**
   ```bash
   git init
   git add -A
   git commit -m "chore: initialize project from BMAD template"
   ```

3. **Start Warp and activate BMAD:**
   ```
   "Read WARP.md and follow it strictly"
   ```

4. **Begin with the workflow:**
   - New idea? → Analyst creates project brief
   - Have requirements? → PM creates PRD
   - PRD done? → Architect designs system
   - Ready to build? → SM creates stories → Dev implements

## Project Structure

```
.bmad-core/           # BMAD agents, tasks, templates
  agents/             # Agent personas (PM, Dev, QA, etc.)
  tasks/              # Executable workflows
  templates/          # Document templates
  checklists/         # Validation checklists

.warp/rules/          # Warp integration rules

docs/                 # Your project documentation
  prd/                # PRD sections (after sharding)
  architecture/       # Architecture sections (after sharding)
  stories/            # Development stories
  epics/              # Epic definitions
  qa/                 # QA assessments and gates

WARP.md               # BMAD rules for Warp Agent Mode
```

## Available Agents

| Agent | Role | When to Use |
|-------|------|-------------|
| 📊 Analyst | Research & Briefs | New ideas, brainstorming |
| 👨‍💼 PM | Requirements | PRD creation |
| 🏗️ Architect | System Design | Technical architecture |
| 🎨 UX Expert | Frontend Specs | UI/UX requirements |
| 📋 PO | Validation | Document alignment, sharding |
| 📝 SM | Story Creation | Sprint planning |
| 💻 Dev | Implementation | Code development |
| 🧪 QA | Quality | Testing, reviews |

## Key Commands

- `*help` - Show available commands
- `*agent [name]` - Switch to agent (pm, dev, qa, etc.)
- `*party-mode` - Get multi-agent feedback
- `*exit` - Return to orchestrator

## Workflow Overview

```
NEW PROJECT:
  Analyst → PM → (UX) → Architect → PO → SM → Dev → QA

DEVELOPMENT CYCLE:
  SM (create story) → Dev (implement) → QA (review) → repeat
```

## License

MIT License - see [LICENSE](LICENSE)

---

*Powered by BMAD-METHOD™ for Warp Agent Mode*
