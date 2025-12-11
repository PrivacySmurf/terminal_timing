"""Configuration management for Timing Terminal pipeline."""

import os
from typing import Literal

from .providers.inmemory import InMemoryFixtureProvider
from .providers import MarketDataProvider
from .providers.chartinspect import ChartInspectMarketDataProvider
from .scoring import ScoringConfig


PipelineMode = Literal["fixture", "provider"]


def get_pipeline_mode() -> PipelineMode:
    """Return the current pipeline mode (fixture or provider).

    Defaults to "fixture" to preserve existing behavior if not configured.
    """

    raw = os.getenv("TT_PIPELINE_MODE", "fixture").lower()
    if raw not in ("fixture", "provider"):
        return "fixture"
    return raw  # type: ignore[return-value]


def get_market_data_provider() -> MarketDataProvider:
    """Factory for MarketDataProvider instances.

    In fixture mode we return the in-memory provider used in earlier
    stories. In provider mode, Story 1.6 will construct a provider
    from real ChartInspect dataframes (wired at a higher level).

    Note:
        This function currently returns the in-memory provider in both
        modes. Story 1.6 will later extend the wiring so that provider
        mode can be backed by `ChartInspectMarketDataProvider` with
        pre-loaded SOPR/MVRV data. Keeping this branch explicit makes
        that migration straightforward.
    """

    mode = get_pipeline_mode()
    if mode == "provider":
        # Placeholder for ChartInspect-backed provider wiring; for now,
        # still use in-memory provider to avoid behavior changes until
        # LSD integration is fully implemented.
        return InMemoryFixtureProvider()
    return InMemoryFixtureProvider()


def get_scoring_config() -> ScoringConfig:
    """Load scoring configuration from environment or use defaults.
    
    Returns:
        ScoringConfig with parameters from environment variables or defaults
    """
    return ScoringConfig(
        retention_threshold=float(os.getenv("TT_RETENTION_THRESHOLD", "20.0")),
        distribution_threshold=float(os.getenv("TT_DISTRIBUTION_THRESHOLD", "80.0")),
        momentum_window=int(os.getenv("TT_MOMENTUM_WINDOW", "30")),
        momentum_weight=float(os.getenv("TT_MOMENTUM_WEIGHT", "1.0")),
        max_price_change_pct=float(os.getenv("TT_MAX_PRICE_CHANGE_PCT", "100.0")),
    )