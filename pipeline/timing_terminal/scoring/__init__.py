"""
Scoring module for computing Bitcoin phase scores and zone classifications.

This module provides the core logic for transforming normalized PhasePoint data
into proprietary 0-100 phase scores and their corresponding zone classifications
(retention, neutral, distribution).
"""

from dataclasses import dataclass


@dataclass
class ScoringConfig:
    """Configuration for phase score calculation and zone classification.
    
    All scoring parameters are configurable to allow tuning without code changes.
    """
    
    # Zone boundary thresholds (decision-critical zones: <20 and >80)
    retention_threshold: float = 20.0  # phase_score < retention_threshold
    distribution_threshold: float = 80.0  # phase_score > distribution_threshold
    
    # Scoring parameters (MVP: simplified momentum-based calculation)
    momentum_window: int = 30  # days for price momentum calculation
    momentum_weight: float = 1.0  # weight for momentum component
    
    # Price normalization bounds for MVP scoring
    max_price_change_pct: float = 100.0  # cap for normalizing price changes


__all__ = ["ScoringConfig"]
