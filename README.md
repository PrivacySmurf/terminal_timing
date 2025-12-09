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

## Timing Terminal Pipeline (MVP)

For the Timing Terminal project, the MVP pipeline lives under `pipeline/`.

### Running the pipeline locally

```bash
cd pipeline
uv run timing-terminal-pipeline
```

This will:

- Execute the in-memory demo pipeline for Story 1.1.
- Write `pipeline/out/chart-data.json` with the architecture-defined schema:
  - `btcPrice[]` and `phaseScore[]` arrays with aligned Unix timestamps (seconds, UTC).
  - `lastUpdated` as an ISO 8601 string ending with `Z`.
  - `dataQuality` as `complete`, `partial`, or `stale`.

### Running tests

You can run the full test suite from the **repo root** using the helper script:

```bash
./run-tests
```

This will:
- `cd` into `pipeline/`
- Expose the `timing_terminal` package on `PYTHONPATH`
- Run `uv run pytest` with the project’s `pyproject.toml` config

You can still run tests directly inside `pipeline/` if you prefer:

```bash
cd pipeline
uv run -m pytest
```

Both approaches run the same unit and integration tests for the pipeline.

## License

MIT License - see [LICENSE](LICENSE)

---

*Powered by BMAD-METHOD™ for Warp Agent Mode*
