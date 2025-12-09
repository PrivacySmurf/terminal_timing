# Release Notes

## Story 1.3 – Phase Scoring Engine (2025-12-09)

- Implemented MVP phase scoring engine driven by BTC price momentum, producing 0–100 scores.
- Added configurable `ScoringConfig` with thresholds and window parameters (no hard-coded magic numbers).
- Implemented zone classification (retention / neutral / distribution) with configurable boundaries.
- Integrated scoring module into the CLI to populate `phaseScore[]` aligned with `btcPrice[]` in `chart-data.json`.
- Extended unit and integration test suite (32 tests) to cover scoring logic, zone boundaries, data quality semantics, and JSON schema.
- QA gate for Story 1.3: **PASS**; story status set to **Done**.
