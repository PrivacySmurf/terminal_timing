"""
Zone classification logic for phase scores.

This module maps phase scores (0-100) to decision-making zones:
- Retention: accumulation phase, low selling pressure (<20)
- Neutral: balanced market (20-80)
- Distribution: elevated selling pressure, higher risk (>80)

The <20 and >80 zones are decision-critical and trigger enhanced monitoring.
"""

from typing import List

from ..models import PhasePoint, Zone
from . import ScoringConfig


def classify_zone(phase_score: float, config: ScoringConfig) -> Zone:
    """
    Classify a phase score into retention/neutral/distribution zone.
    
    Args:
        phase_score: Float score in range [0.0, 100.0]
        config: ScoringConfig with zone boundary thresholds
        
    Returns:
        Zone literal: "retention", "neutral", or "distribution"
        
    Zone Definitions:
        - Retention (<20): Accumulation phase, low risk of selling pressure
        - Neutral (20-80): Market balanced, no strong directional signal  
        - Distribution (>80): Elevated selling pressure, higher risk
        
    Note:
        The <20 and >80 zones are decision-critical and should trigger
        enhanced monitoring/alerting per the architecture.
    """
    if phase_score < config.retention_threshold:
        return "retention"
    elif phase_score > config.distribution_threshold:
        return "distribution"
    else:
        return "neutral"


def enrich_phase_points_with_zones(
    phase_points: List[PhasePoint],
    phase_scores: List[float],
    config: ScoringConfig
) -> List[PhasePoint]:
    """
    Enrich PhasePoint objects with phase_score and zone fields.
    
    Takes a list of PhasePoint objects (which may have placeholder scores/zones)
    and returns new PhasePoint objects with computed phase_score and zone values.
    
    Args:
        phase_points: Original PhasePoint objects with timestamp and btc_price
        phase_scores: Computed phase scores (same length as phase_points)
        config: ScoringConfig for zone classification
        
    Returns:
        New list of PhasePoint objects with phase_score and zone populated
        
    Raises:
        ValueError: If phase_points and phase_scores have different lengths
    """
    if len(phase_points) != len(phase_scores):
        raise ValueError(
            f"Mismatch: {len(phase_points)} phase_points but {len(phase_scores)} scores"
        )
    
    enriched = []
    for point, score in zip(phase_points, phase_scores):
        zone = classify_zone(score, config)
        enriched.append(
            PhasePoint(
                timestamp=point.timestamp,
                btc_price=point.btc_price,
                phase_score=score,
                zone=zone
            )
        )
    
    return enriched
