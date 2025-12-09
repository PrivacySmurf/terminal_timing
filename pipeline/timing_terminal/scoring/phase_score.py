"""
Phase score calculation logic.

This module implements the core proprietary scoring algorithm that computes
0-100 phase scores from normalized PhasePoint data.

For MVP, we use a simplified momentum-based formula. Future versions will
incorporate real LTH SOPR and MVRV metrics from external providers.
"""

from typing import List

from ..models import PhasePoint
from . import ScoringConfig


def compute_phase_score(
    phase_points: List[PhasePoint], config: ScoringConfig
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
        
    Returns:
        List of float phase scores, one per input point, in same order
        
    Note:
        This MVP formula will be enhanced in Story 1.4 when real LTH metrics
        (SOPR, MVRV) become available from external data providers.
    """
    if not phase_points:
        return []
    
    if len(phase_points) == 1:
        # Single point: default to neutral zone (mid-range score)
        return [50.0]
    
    scores = []
    window = config.momentum_window
    
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
        
        # Ensure bounded [0.0, 100.0]
        score = max(0.0, min(100.0, score))
        
        scores.append(score)
    
    return scores
