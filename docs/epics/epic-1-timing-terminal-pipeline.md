# Epic 1: Timing Terminal Bitcoin Phase Pipeline

## Summary

As the creator of Timing Terminal, I want a reliable, transparent daily Bitcoin phase-scoring pipeline so that I can publish an interactive chart to my Notion-based hub and use it to make systematic timing decisions.

## High-Level Outcome

- A single Bitcoin Market Phase chart is generated daily as a static HTML + `chart-data.json` bundle and deployed to Netlify.
- The chart is embedded into the Timing Terminal Notion hub with referer-based access control.
- The pipeline is monitored and can be run locally and via GitHub Actions on a schedule.

## Stories

1. **Story 1.1 – Pipeline Bootstrap and Local CLI**  
   Minimal Python package for the Timing Terminal pipeline, with a `timing-terminal-pipeline` CLI command that runs a deterministic demo pipeline using local fixtures and writes a `chart-data.json` file matching the architecture schema.

2. **Story 1.2 – External Provider Adapters (Read-Only)**  
   Implement provider adapter interfaces and a first concrete provider client that loads BTC price and long-term-holder series from one on-chain/market data source into the internal `PhasePoint` model, using local configuration and without yet wiring deployment.

3. **Story 1.3 – Phase Scoring Engine**  
   Implement the `scoring` module that takes normalized `PhasePoint` series and produces phase scores (0–100) and zones (retention/neutral/distribution), with clear configuration and unit tests.

4. **Story 1.4 – Real Data Pipeline Run & `chart-data.json` Generation**  
   Replace demo fixtures with real provider data, integrating configuration loading (`config.py`), error handling, and end-to-end integration tests that validate schema, alignment, and `dataQuality` behavior.

5. **Story 1.5 – GitHub Actions Scheduled Run & Artifacts**  
   Add a GitHub Actions workflow that runs the pipeline daily on a schedule, publishes the generated `chart-data.json` and `index.html` to Netlify (or commits them into the repo as needed), and posts success/failure notifications to Discord.

6. **Story 1.6 – Operational Runbook & Error Handling**  
   Document and implement a manual fallback runbook for critical-phase failures (e.g., when providers are unavailable), including a simple manual script to compute and post the current phase score to Discord and update Notion copy.

## Dependencies

- PRD: `docs/prd/`
- Architecture: `docs/architecture.md`
- Future epics: Multi-chart expansion and Sarah onboarding will build on this pipeline foundation.

## Notes

- This epic is intentionally scoped to a single-asset (BTC) pipeline to validate the Timing Terminal methodology and operational flow before expanding to additional charts.
