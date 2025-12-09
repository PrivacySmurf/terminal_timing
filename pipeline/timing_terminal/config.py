"""Configuration management for Timing Terminal pipeline."""

import os
from typing import Literal

from .providers.inmemory import InMemoryFixtureProvider
from .providers import MarketDataProvider
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

    For Story 1.4 MVP, only an in-memory fixture provider is wired,
    but the abstraction allows later addition of file-backed or HTTP providers.
    """

    mode = get_pipeline_mode()
    # For now, provider mode still uses the same in-memory fixture provider;
    # future stories can branch here based on provider type.
    if mode == "provider":
        return InMemoryFixtureProvider()
    # In fixture mode, the CLI continues to use its existing fixture path,
    # but tests can still exercise this provider directly.
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