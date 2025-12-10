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

## Pipeline Daily GitHub Actions Workflow

A GitHub Actions workflow runs the Bitcoin phase-scoring pipeline on a schedule.

- **Workflow file:** `.github/workflows/pipeline-daily.yml`
- **Schedule:** daily at `06:00` UTC (and manually via **Run workflow** in GitHub)
- **What it does:**
  - Checks out the repo and sets up Python 3.11.
  - Installs dependencies using `uv`.
  - Runs the full pipeline test suite via `./run-tests`.
  - Runs the `timing-terminal-pipeline` CLI (fixture mode by default).
  - Fails the job if `pipeline/out/chart-data.json` is not generated.

To adjust the schedule or enable provider mode, edit the workflow file and
configure the appropriate environment variables and GitHub Secrets.

## Frontend Chart Page (Story 2.1)

A minimal frontend chart page lives under `web/`.

- **Entry HTML:** `web/index.html`
- **Script:** `web/main.js`
- **Data source:** expects a `chart-data.json` file in the same directory, with
  the schema produced by the pipeline:
  - `btcPrice[]` and `phaseScore[]` arrays of `{ time, value }` (Unix seconds, UTC).

To run locally:

1. Generate `chart-data.json`:
   ```bash
   ./run-tests  # or run the pipeline CLI to produce pipeline/out/chart-data.json
   cp pipeline/out/chart-data.json web/
   ```
2. Serve the `web/` directory with a simple static server from the repo root:
   ```bash
   cd web
   python -m http.server 8000
   # then open http://localhost:8000 in your browser
   ```

The page will render BTC price and phase score using TradingView Lightweight
Charts, with zoom/pan and hover tooltips.

## Netlify Deployment (Story 2.2)

For deployment, a minimal Netlify configuration is provided:

- **Config file:** `netlify.toml`
- **Publish directory:** `web/`
- **Build command:** none required for MVP (static HTML + JS + `chart-data.json`).

To deploy:

1. Create a new site in Netlify from this repository.
2. In the Netlify UI, ensure the publish directory is set to `web/`.
3. Make sure `web/chart-data.json` exists and is committed when you trigger a deploy.
4. After deploy, visit the Netlify URL and verify that the chart loads and behaves
   the same as it does locally.

A later story can automate the refresh of `chart-data.json` via CI; for now,
updating the data file and re-deploying Netlify is a manual step.

## Notion Integration Scripts

For the Notion "⚡ Timing Terminal 2 (Source)" database, there is a helper
script to ensure each chart row has a matching Embed block on its page.

- **Example env:** `.env.example` (copy to `.env` and fill in values)
  - `NOTION_API_KEY` – Notion integration secret
  - `TT2_DATABASE_ID` – database ID of ⚡ Timing Terminal 2 (Source)
- **Script:** `scripts/notion_sync_chart_embeds.py`

Usage:

```bash
cd timing_terminal_test
python scripts/notion_sync_chart_embeds.py
```

This will:

- Query the Timing Terminal 2 source database
- For each row with a `Chart URL` value, append a real Notion Embed block for
  that URL to the row's page

Run this after adding/updating rows in the Timing Terminal 2 source database
so the individual chart pages stay in sync.

## License

MIT License - see [LICENSE](LICENSE)

---

*Powered by BMAD-METHOD™ for Warp Agent Mode*
