# Fixtures for data quality scenarios

This directory contains fixtures used (or reserved) for exercising data-quality
paths in the pipeline.

- `partial_example.json` – represents a scenario where some, but not all,
  required series are present or up-to-date (used conceptually for
  `dataQuality = "partial"`).
- `stale_example.json` – represents a scenario where all series are present
  but the last data point is older than the configured freshness threshold
  (used conceptually for `dataQuality = "stale"`).

Current tests primarily use in-memory fixtures via monkeypatching, but these
files document the intended shapes for future provider-backed tests.
