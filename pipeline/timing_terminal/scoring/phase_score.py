"""
Phase score calculation logic.

This module implements the core proprietary scoring algorithm that computes
0-100 phase scores from normalized PhasePoint data.

For MVP, we use a simplified momentum-based formula. Future versions will
incorporate real LTH SOPR and MVRV metrics from external providers.
"""

from typing import List, Optional, Sequence

from ..models import PhasePoint
from . import ScoringConfig


def compute_phase_score(
    phase_points: List[PhasePoint],
    config: ScoringConfig,
    lth_series: Optional[Sequence[float]] = None,
) -> List[float]:
    """
    Compute phase scores (0-100) for a series of PhasePoint data.
    
    MVP Implementation:
    Uses BTC price momentum as a proxy for market phase. The scoring is:
    - Price increasing strongly → higher score (approaching distribution)
    - Price flat or declining → lower score (approaching retention/accumulation)
    
    The calculation is deterministic and bounded to [0.0, 100.0].
    
    Args:
        phase_points: List of PhasePoint objects with timestamp and btc_price
        config: ScoringConfig with scoring parameters
        lth_series: Optional LTH-derived metric values aligned with phase_points
        
    Returns:
        List of float phase scores, one per input point, in same order
        
    Note:
        This MVP formula will be enhanced in Story 1.4 when real LTH metrics
        (SOPR, MVRV) become available from external data providers.
    """
    if not phase_points:
        return []

    if lth_series is not None and len(lth_series) != len(phase_points):
        raise ValueError("lth_series length must match phase_points length")
    
    if len(phase_points) == 1:
        # Single point: default to neutral zone (mid-range score)
        return [50.0]
    
    scores = []
    window = config.momentum_window
    
    # Pre-compute simple LTH normalization if provided and enabled.
    # We normalize LTH values to [0.0, 100.0] using a clipped min-max range.
    lth_normalized: Optional[List[float]] = None
    if lth_series is not None and config.lth_weight > 0.0:
        # Avoid division-by-zero in normalization by using a small epsilon band.
        lth_min = min(lth_series)
        lth_max = max(lth_series)
        if lth_max == lth_min:
            # Flat series: treat as neutral 50.0
            lth_normalized = [50.0 for _ in lth_series]
        else:
            span = lth_max - lth_min
            lth_normalized = []
            for v in lth_series:
                ratio = (v - lth_min) / span
                lth_score = 0.0 + ratio * 100.0
                lth_score = max(0.0, min(100.0, lth_score))
                lth_normalized.append(lth_score)

    for i, point in enumerate(phase_points):
        # Calculate momentum relative to window periods ago
        # For early points with insufficient history, use shorter window
        lookback_idx = max(0, i - window)
        current_price = point.btc_price
        historical_price = phase_points[lookback_idx].btc_price
        
        # Avoid division by zero
        if historical_price == 0:
            scores.append(50.0)
            continue
        
        # Calculate percentage price change
        price_change_pct = ((current_price - historical_price) / historical_price) * 100
        
        # Normalize to 0-100 range
        # Positive momentum → higher score, negative → lower score
        # Cap at max_price_change_pct to prevent extreme outliers
        normalized_change = max(
            -config.max_price_change_pct,
            min(price_change_pct, config.max_price_change_pct)
        )
        
        # Map [-max_price_change_pct, +max_price_change_pct] to [0, 100]
        score = 50.0 + (normalized_change / config.max_price_change_pct) * 50.0

        # Optionally blend in LTH-derived component
        if lth_normalized is not None:
            lth_component = lth_normalized[i]
            w = max(0.0, min(1.0, config.lth_weight))
            score = (1.0 - w) * score + w * lth_component
        
        # Ensure bounded [0.0, 100.0]
        score = max(0.0, min(100.0, score))
        
        scores.append(score)
    
    return scores
