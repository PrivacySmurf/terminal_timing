# Timing Terminal Fullstack Architecture Document

## Change Log

| Date       | Version | Description                                      | Author   |
|------------|---------|--------------------------------------------------|----------|
| 2025-12-09 | v0.1    | Initial fullstack architecture skeleton created | Architect |

## Introduction

Timing Terminal Fullstack Architecture Document

This document outlines the complete fullstack architecture for Timing Terminal, including the Bitcoin phase-scoring data pipeline, the static web experience, and the integrations that connect them. It serves as the single source of truth for how data flows from external on-chain providers into a proprietary phase score and is then delivered as an interactive chart embedded in Notion.

The architecture intentionally favors a simple, high-reliability stack: a Python-based batch pipeline generates daily phase scores, which are published as static assets to Netlify and rendered via TradingView Lightweight Charts. Notion acts as the content and access-control wrapper, while Stripe/Gumroad, Discord, and email infrastructure provide payments, monitoring, and communication.

Because the product’s core value is timing confidence rather than feature breadth, this document prioritizes reliability, transparency, and performance over adding more moving parts. It unifies backend (data ingestion and calculation), frontend (interactive visualization), and infrastructure (Netlify, Notion, monitoring) into a coherent system that can be safely extended in later phases (Sarah onboarding, multi-chart platform) without destabilizing the MVP.

### Starter Template or Existing Project

Timing Terminal is a greenfield project and is not based on any existing starter template or cloned codebase.

- No fullstack starter (e.g., Next.js or Nx monorepo) is being adopted initially.
- No legacy repository or brownfield system imposes constraints on languages, frameworks, or infrastructure.
- All architectural decisions in this document are made from first principles and can be optimized specifically for Timing Terminal’s data pipeline and static chart delivery model.

Decision: **N/A – Greenfield project with no inherited template or codebase constraints.**

## High Level Architecture

Timing Terminal uses a simple, reliability-first architecture:

- **Data Pipeline (Backend)**
- A Python batch job runs once per day, fetching LTH SOPR, LTH MVRV, and related series from one or more on-chain/market data providers.
  - The job computes a proprietary Bitcoin phase score (0–100), plus supporting series (BTC price, phase zones).
  - The pipeline writes a versioned `chart-data.json` and regenerates a static `index.html` (TradingView chart + glue JS).
  - On success, it triggers a Netlify deployment and sends a Discord “✅ updated” notification; on failure, it sends a “⚠️ failed” alert and can fall back to a manual runbook.

- **Presentation Layer (Frontend)**
  - A single static HTML page, hosted on Netlify, renders the interactive chart using TradingView Lightweight Charts.
  - The page loads `chart-data.json` at build time (or as a static asset), overlays BTC price and phase scores, and exposes zoom/pan/tooltips.
  - The page is designed desktop-first (1920×1080) with acceptable tablet behavior; mobile is best-effort but not a primary target for MVP.

- **Access & Content (Notion)**
  - The Netlify-hosted chart is embedded into a Notion page that provides:
    - Value prop copy, methodology explainer, historical track record, and disclaimers.
    - A clear onboarding path to the chart (above-the-fold embed).
  - Netlify edge functions enforce referer validation so only requests from approved Notion pages can load the chart.

- **API Surface (MVP)**
  - No public REST or GraphQL API is exposed in the MVP.
  - The only externally-consumed interface is the **embedded chart** plus its backing `chart-data.json` file.
  - Any future programmatic access (e.g., institutional APIs) is explicitly treated as Phase 2+ work.

- **Payments & Membership**
  - Stripe/Gumroad handle subscription purchases and trials; no card data is stored by Timing Terminal.
  - Notion membership / access is granted or revoked based on Stripe/Gumroad webhook events (Phase 1 may implement this manually; Phase 2 can automate).

- **Monitoring & Alerts**
  - Discord webhooks report pipeline success/failure and current phase score.
  - During critical phase zones (<20 or >80), failures escalate via SMS/email and a manual fallback runbook is used to compute/post the score if automation breaks.

This architecture is intentionally minimal: one Python batch pipeline, one static chart page, one Notion wrapper, and a thin layer of infrastructure around them.

## Tech Stack

The following stack is treated as the single source of truth for Timing Terminal. Versions are indicative targets and can be adjusted as implementation progresses.

### Technology Stack Table

| Category              | Technology                             | Version        | Purpose                                      | Rationale                                                                 |
|-----------------------|----------------------------------------|---------------|----------------------------------------------|---------------------------------------------------------------------------|
| Frontend Language     | TypeScript                             | ES2020 target | Chart glue code and build tooling            | Strong typing around TradingView config; good ecosystem and editor support |
| Frontend Runtime      | Browser (static HTML + JS)             | n/a           | Render chart and interactions                | No SPA needed; keeps bundle small and hosting simple                      |
| Charting Library      | TradingView Lightweight Charts         | Latest stable | Time-series visualization                    | Battle-tested, performant financial charting                              |
| Styling               | Custom CSS (dark theme)                | n/a           | Visual polish, contrast, brand feel          | Keeps dependencies low; easy to tweak for Notion embedding                |
| Backend Language      | Python                                 | 3.11          | Data pipeline and phase-score computation    | Excellent ecosystem for data work; aligns with existing scripts           |
| HTTP Client           | `httpx` or `requests`                  | Latest stable | Fetch external time-series data              | Mature, widely used, good error handling                                  |
| Scheduling            | External scheduler (cron / CI runner)  | n/a           | Trigger daily pipeline runs                  | Allows using GitHub Actions, cron, or Netlify Scheduled Functions         |
| Package Manager       | `uv`                                   | Latest stable | Manage Python dependencies and environments  | Matches your global preference; fast, modern Python packaging             |
| Hosting Platform      | Netlify                                | n/a           | Host static HTML + JSON with CDN             | Simple static hosting, built-in CI/CD, edge functions                     |
| Edge Runtime          | Netlify Edge Functions                 | n/a           | Referer/token validation at the edge         | Lightweight way to enforce Notion-only access                             |
| Content Platform      | Notion                                 | n/a           | Wrap chart with copy, onboarding, disclaimers| Fast to iterate on content and layout; coarse-grained access control      |
| Payments              | Stripe / Gumroad                       | n/a           | Subscription billing and trials              | Outsource PCI and billing logic; mature SaaS billing providers            |
| Monitoring Channel    | Discord Webhooks                       | n/a           | Pipeline success/failure notifications       | Low-friction alerting channel you already use                             |
| Escalation Channel    | SMS / Email                            | n/a           | Critical decision-zone alerts                | Ensures issues during Phase <20 or >80 get immediate attention            |
| Pipeline Testing      | `pytest`                               | Latest stable | Unit/integration tests for scoring logic     | Standard Python testing stack                                             |
| E2E Smoke Tests       | Simple scripted HTTP + JS checks       | n/a           | Verify chart-data + HTML render cleanly      | Lightweight assurance without heavy test framework                         |

- **Languages & Runtimes**
  - Python 3.11 – data pipeline and orchestration
  - TypeScript (ES2020 target) – any custom chart glue code and tooling around TradingView

- **Frontend**
  - Rendering: Static HTML + vanilla TypeScript/JavaScript
  - Charting: TradingView Lightweight Charts (latest stable)
  - Styling: Minimal custom CSS, dark theme tuned for TradingView defaults

- **Backend / Data Pipeline**
  - Python 3.11
  - HTTP client: `httpx` or `requests` for external provider integration
  - Scheduling: **GitHub Actions scheduled workflow** (cron) triggering the daily pipeline run
  - Package management: `uv` (per project standards) for dependency management and virtualenv handling

- **Hosting & Infrastructure**
  - Static hosting & CDN: Netlify
  - Edge logic: Netlify Edge Functions for referer validation and simple token logic (Phase 2)
  - Content wrapper: Notion pages embedding the Netlify-hosted chart

- **Payments & Membership**
  - Stripe and/or Gumroad for subscription payments and trials
  - Webhooks from Stripe/Gumroad feeding into a lightweight membership management script or manual runbook (Phase 1), automated in later phases

- **Monitoring, Logging, and Alerting**
  - Pipeline notifications: Discord webhooks for success/failure + score summary
  - Escalation: SMS/email for failures during critical phase zones (<20 or >80)
  - Platform logs: Netlify deploy and edge function logs for operational debugging

- **Testing & Quality**
  - Pipeline tests: `pytest` (unit + integration around data transforms and score calculations)
  - Basic end-to-end smoke tests: simple scripted checks to ensure a fresh `chart-data.json` renders without JS errors and the Netlify page responds with correct headers.

## External Providers

Timing Terminal is designed to work with one or more external on-chain or market data providers without coupling the core logic to any single vendor.

- The pipeline treats all sources as **time-series providers** exposing:
  - BTC (or other asset) price
  - Long-term holder metrics (e.g., SOPR-like and MVRV-like series)
  - Any additional series needed to derive the phase score
- Provider-specific details (authentication, endpoints, throttling) are isolated in a thin adapter layer so the rest of the pipeline works against a stable internal interface.
- This allows you to:
  - Swap providers if pricing, reliability, or coverage changes
  - Combine multiple providers for redundancy or cross-checking
  - Add new sources in later phases without rewriting the scoring logic.

At a high level, each provider adapter is responsible for:

1. Fetching raw series for a given date range
2. Normalizing timestamps to UTC and a common resolution (daily bars)
3. Mapping raw fields into internal names used by the scoring engine
4. Reporting errors and partial data states in a way the pipeline can surface via `dataQuality`.

## Data Models

The core data models describe how Timing Terminal represents price and phase score time series for charting and monitoring.

### Conceptual Entities

- **PhasePoint**
  - `timestamp` (UTC datetime) – when the data point is valid
  - `btc_price` (float) – BTC/USD price
  - `phase_score` (float, 0–100) – proprietary phase score
  - `zone` (enum: `retention`, `neutral`, `distribution`) – derived label based on score bands

- **ChartData**
  - `btcPrice[]` – series of `{ time, value }` for BTC price
  - `phaseScore[]` – series of `{ time, value }` for phase scores
  - `lastUpdated` – ISO 8601 string for latest update time
  - `dataQuality` – enum: `complete`, `partial`, `stale`

### Data Quality

Data quality is a first-class architectural concern for the pipeline. It exposes
whether `chart-data.json` was produced from complete, partial, or stale input
series so that both the frontend and operational tooling can respond
appropriately.

#### Required Series

For the MVP Bitcoin phase pipeline, the scoring engine expects at least:

- **BTC price** – BTC/USD price time series.
- **LTH SOPR-like series** – long-term-holder realization / profit-taking proxy.
- **LTH MVRV-like series** – long-term-holder valuation / unrealized-profit proxy.

Future stories may add more inputs, but these three are the baseline required for
computing a meaningful phase score.

#### DataQuality States

The `dataQuality` field in `chart-data.json` is an enum with three values:

- `complete` – All required series are present and **fresh** relative to the
  configured freshness threshold.
- `partial` – Some, but not all, required series are present or up-to-date in
  the recent lookback window.
- `stale` – Data is older than the freshness threshold or entirely missing for
  the current window.

#### Evaluation Rules (MVP)

Implementation details can evolve, but the architectural contract for MVP is:

1. Let `PhasePoint[]` represent the normalized internal time series used for
   scoring.
2. Compute `latest_ts` as the maximum `timestamp` over all available
   `PhasePoint`s.
3. Compare `latest_ts` to `now` using a configurable maximum age (e.g. 24 hours)
   from configuration:
   - If there are **no points**, or `now - latest_ts` exceeds the maximum age →
     `dataQuality = "stale"`.
4. If data is not stale but the number of available points is less than the
   expected minimum for the lookback window (also configurable) →
   `dataQuality = "partial"`.
5. Otherwise → `dataQuality = "complete"`.

These rules are enforced in the pipeline by a dedicated evaluation function
(`evaluate_data_quality`) so that both unit and integration tests can exercise
`complete` / `partial` / `stale` scenarios deterministically.

#### UX and Monitoring Implications

- **Frontend / Notion copy**:
  - When `dataQuality = "complete"`, the chart is presented as fully
    up-to-date.
  - When `dataQuality = "partial"`, the chart remains visible but should be
    accompanied by a banner or copy explaining that some inputs are degraded and
    decisions should be made with extra caution.
  - When `dataQuality = "stale"`, the chart should be visually de-emphasized
    and clearly labeled as historical only; users should be discouraged from
    making fresh timing decisions until data recovers.
- **Monitoring**:
  - Discord notifications (and later SMS/email during critical phase zones
    `<20` or `>80`) should include the current `dataQuality` value so on-call
    humans can see at a glance whether an automation failure is affecting
decision quality.

### JSON Schema (chart-data.json)

At the file level, the pipeline produces a JSON document with this structure:

```json path=null start=null
{
  "btcPrice": [
    { "time": 1609459200, "value": 29000.5 }
  ],
  "phaseScore": [
    { "time": 1609459200, "value": 45.2 }
  ],
  "lastUpdated": "2025-12-05T08:15:00Z",
  "dataQuality": "complete"
}
```

- `time` is a Unix timestamp in **seconds** (UTC).
- `btcPrice` and `phaseScore` arrays share the same time axis for overlaying in TradingView.
- `dataQuality` allows the frontend to expose transparency when the pipeline fails or recovers from partial data conditions.

## Phase-Based Architectural Changes

The core architecture remains stable across product phases. Changes are deliberately incremental:

- **MVP (Phase 1)**
  - Single BTC phase-scoring pipeline and chart.
  - Manual/semiautomatic membership updates based on Stripe/Gumroad.
  - No educational overlays; Marcus-only experience.
  - No public APIs.

- **Phase 1.5 (Sarah Onboarding)**
  - Adds tutorial overlays and state in the frontend (still a static page, potentially with more JS).
  - Adds email triggers based on tutorial progress (implemented outside the core chart, e.g., via email tooling tied to events).
  - Architecture remains batch-pipeline + static chart; no major infra changes.

- **Phase 2 (Multi-Chart Platform)**
  - Pipeline generalizes to multiple indices and possibly multiple assets.
  - Web layer may evolve to a small multi-page or multi-chart static site (still Netlify-hosted).
  - Stripe/Gumroad → Notion membership automation becomes required.
  - Optional introduction of more structured analytics and access tokens at the edge.

## High-Level Architecture Diagram

The following Mermaid diagram captures the main components and data flows in Timing Terminal:

```mermaid path=null start=null
graph TD
  subgraph ExternalData[On-Chain / Market Data Providers]
    D1[Provider 1]
    D2[Provider 2]
  end

  subgraph Pipeline[Timing Terminal Pipeline (Python)]
    P1[Fetch LTH SOPR & LTH MVRV]
    P2[Compute Phase Scores & Zones]
    P3[Generate chart-data.json & index.html]
  end

  subgraph Hosting[Netlify]
    NHTML[index.html + JS]
    NJSON[chart-data.json]
    NEDGE[Edge Function (Referer Validation)]
  end

  subgraph Content[Notion]
    NPage[Timing Terminal Notion Page]
  end

  subgraph Users[Subscribers]
    U[Investor Browser]
  end

  subgraph Monitoring[Monitoring & Alerts]
    D[Discord Webhook]
    SMS[SMS/Email Alerts]
  end

  D1 --> P1
  D2 --> P1
  P1 --> P2
  P2 --> P3
  P3 --> NHTML
  P3 --> NJSON

  U --> NPage
  NPage --> NEDGE
  NEDGE --> NHTML
  NEDGE --> NJSON

  P3 --> D
  D --> SMS
```

## Unified Project Structure

A simple, single-repo layout is sufficient for Timing Terminal’s MVP. The structure below assumes:

- Python lives under `pipeline/` for the scoring pipeline.
- Static chart code lives under `web/`.
- Architecture/PRD/stories live under `docs/`.
- BMAD configuration remains under `.bmad-core/`.

```text path=null start=null
TimingTerminal/
├── .bmad-core/                  # BMAD agents, tasks, templates, checklists
├── docs/
│   ├── prd.md                   # Master PRD (Timing Terminal)
│   ├── prd/                     # Sharded PRD sections
│   ├── architecture.md          # Fullstack architecture (this doc)
│   └── architecture/            # (Future) sharded architecture sections
├── pipeline/
│   ├── timing_terminal/         # Python package for pipeline
│   │   ├── __init__.py
│   │   ├── data_providers/      # Provider adapters (Provider 1, Provider 2, etc.)
│   │   ├── scoring/             # Phase score calculation logic
│   │   ├── models.py            # PhasePoint, ChartData, internal types
│   │   ├── config.py            # Config loading (env, secrets)
│   │   └── cli.py               # Entry point for daily run
│   ├── tests/                   # pytest-based tests for pipeline
│   └── pyproject.toml           # Python project metadata (managed by uv)
├── web/
│   ├── public/
│   │   └── index.html           # Static HTML shell + TradingView integration
│   ├── src/
│   │   ├── chart.ts             # TradingView setup + data wiring
│   │   └── styles.css           # Minimal dark theme styling
│   └── package.json             # Optional: NPM scripts for bundling/minification
├── netlify/
│   └── edge-functions/
│       └── referer-guard.ts     # Netlify Edge Function for Notion-only access
├── netlify.toml                 # Netlify build/deploy configuration
├── .env.example                 # Example env vars for pipeline + Netlify
└── README.md                    # High-level repo overview and setup
```

This layout is intentionally minimal for MVP but leaves clear extension points:

- `pipeline/` can grow to support multi-asset scoring and additional providers.
- `web/` can evolve into a more complex build if you eventually need bundling or multi-page support.
- `docs/architecture/` can later mirror PRD sharding for more granular architectural views.

## Testing Strategy

Timing Terminal’s value depends heavily on reliability and trust in the phase score. The testing strategy focuses on the **Python pipeline** and a small set of **end-to-end checks** on the chart.

### Testing Pyramid (Conceptual)

```text path=null start=null
E2E Smoke Tests
/             \
Integration Tests
/                 \
Pipeline Unit Tests
```

- Most tests live at the **unit** and **integration** levels inside `pipeline/tests/`.
- A small number of **E2E smoke tests** ensure the latest build is serving correct, renderable data.

### Pipeline Unit Tests

- Location: `pipeline/tests/unit/`
- Focus:
  - Pure scoring logic (PhasePoint → phase_score)
  - Zone classification (retention/neutral/distribution)
  - Data normalization (timestamps, missing values)
- Characteristics:
  - No real HTTP calls – use in-memory fixtures.
  - Fast and deterministic; run on every change.

### Pipeline Integration Tests

- Location: `pipeline/tests/integration/`
- Focus:
  - Provider adapters: validate that each provider’s JSON/CSV format can be mapped into internal models.
  - End-to-end run of the pipeline against **recorded fixtures** (not live APIs) to produce `chart-data.json`.
  - Validation that `dataQuality` is correctly set for complete, partial, and error scenarios.
- Run:
  - As part of CI on main and feature branches.

### E2E Smoke Tests (Chart + Hosting)

- Location: `web/tests/e2e/` (or simple scripts under `scripts/`)
- Checks:
  1. Latest Netlify deploy responds with HTTP 200 for the chart URL.
  2. The HTML contains the TradingView container and required script tags.
  3. A headless browser (or lightweight JS runner) can execute the page without JS errors and confirms that data series are present.
- Frequency:
  - On deploy and/or nightly, to catch hosting or asset issues.

### Monitoring as a Testing Backstop

Monitoring complements tests by catching issues that sneak past CI:

- Discord webhook messages act as a **daily heartbeat** – absence or failure messages indicate problems.
- During decision zones, SMS/email alerts are treated as **critical test failures** that require manual investigation.
- Weekly uptime and failure reports are used to refine tests and add new cases when real-world issues arise.
- CI is considered red if pipeline integration tests fail **or** if E2E smoke tests detect HTTP/JS errors on the chart page.
