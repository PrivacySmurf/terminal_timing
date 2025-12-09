# Epic 1: Data Pipeline – Phase Score Computation

## Epic Goal

Establish a reliable, testable data pipeline that computes the Bitcoin phase score from external time-series providers and produces `chart-data.json` for the Timing Terminal chart, with clear monitoring and failure semantics.

## Story List (High-Level)

- **Story 1.1 – Data Pipeline Bootstrap**  
  Bootstrap a minimal daily batch pipeline that uses fixture data to compute a demo phase score and emit a valid `chart-data.json` for wiring the rest of the system.

- **Story 1.2 – Provider Adapter Abstraction**  
  Introduce a provider-agnostic data adapter layer that can load time-series data from multiple external/on-chain providers behind a common interface.

- **Story 1.3 – Real Provider Integration (Single Source)**  
  Replace fixtures for one configured provider with real API calls, including auth, rate limiting, and error handling, while preserving the `chart-data.json` contract.

- **Story 1.4 – Reliability & Data Quality Handling**  
  Implement robust handling of missing/partial data and pipeline failures, including `dataQuality` states, retries, and clear logging.

- **Story 1.5 – Production Scheduling & GitHub Actions Job**  
  Add a GitHub Actions scheduled workflow (cron) that runs the pipeline daily, stores logs, and fails fast on schema or scoring regressions.

> Detailed, fully fleshed-out story documents will be created just-in-time for each story (e.g., `1.2`, `1.3`, etc.), using this epic outline plus the PRD and architecture docs.
