"""Configuration management for Timing Terminal pipeline."""

import os
from .scoring import ScoringConfig


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