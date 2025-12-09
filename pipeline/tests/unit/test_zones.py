"""Unit tests for zone classification logic."""

from datetime import datetime, timezone

import pytest

from timing_terminal.models import PhasePoint
from timing_terminal.scoring import ScoringConfig
from timing_terminal.scoring.zones import classify_zone, enrich_phase_points_with_zones


@pytest.fixture
def default_config():
    """Default scoring configuration with standard thresholds (20, 80)."""
    return ScoringConfig()


@pytest.fixture
def custom_config():
    """Custom configuration with different zone thresholds."""
    return ScoringConfig(
        retention_threshold=25.0,
        distribution_threshold=75.0,
    )


def test_classify_zone_retention(default_config):
    """Scores below retention threshold classify as retention."""
    assert classify_zone(0.0, default_config) == "retention"
    assert classify_zone(10.0, default_config) == "retention"
    assert classify_zone(19.9, default_config) == "retention"


def test_classify_zone_neutral(default_config):
    """Scores between thresholds classify as neutral."""
    assert classify_zone(20.0, default_config) == "neutral"
    assert classify_zone(50.0, default_config) == "neutral"
    assert classify_zone(80.0, default_config) == "neutral"


def test_classify_zone_distribution(default_config):
    """Scores above distribution threshold classify as distribution."""
    assert classify_zone(80.1, default_config) == "distribution"
    assert classify_zone(90.0, default_config) == "distribution"
    assert classify_zone(100.0, default_config) == "distribution"


def test_classify_zone_exact_boundaries(default_config):
    """Test exact boundary values (19.9, 20.0, 20.1, 79.9, 80.0, 80.1)."""
    # Lower boundary tests
    assert classify_zone(19.9, default_config) == "retention"
    assert classify_zone(20.0, default_config) == "neutral"
    assert classify_zone(20.1, default_config) == "neutral"
    
    # Upper boundary tests
    assert classify_zone(79.9, default_config) == "neutral"
    assert classify_zone(80.0, default_config) == "neutral"
    assert classify_zone(80.1, default_config) == "distribution"


def test_classify_zone_custom_thresholds(custom_config):
    """Custom zone thresholds (25, 75) are respected."""
    # With retention_threshold=25.0, distribution_threshold=75.0
    assert classify_zone(24.9, custom_config) == "retention"
    assert classify_zone(25.0, custom_config) == "neutral"
    assert classify_zone(75.0, custom_config) == "neutral"
    assert classify_zone(75.1, custom_config) == "distribution"


def test_enrich_phase_points_with_zones_basic(default_config):
    """Enrich phase points with scores and zones."""
    points = [
        PhasePoint(
            timestamp=datetime(2025, 1, 1, tzinfo=timezone.utc),
            btc_price=30000.0,
            phase_score=0.0,  # placeholder
            zone="neutral",  # placeholder
        ),
        PhasePoint(
            timestamp=datetime(2025, 1, 2, tzinfo=timezone.utc),
            btc_price=32000.0,
            phase_score=0.0,  # placeholder
            zone="neutral",  # placeholder
        ),
    ]
    
    scores = [15.0, 85.0]
    
    enriched = enrich_phase_points_with_zones(points, scores, default_config)
    
    assert len(enriched) == 2
    
    # First point: score 15.0 → retention
    assert enriched[0].phase_score == 15.0
    assert enriched[0].zone == "retention"
    assert enriched[0].timestamp == points[0].timestamp
    assert enriched[0].btc_price == points[0].btc_price
    
    # Second point: score 85.0 → distribution
    assert enriched[1].phase_score == 85.0
    assert enriched[1].zone == "distribution"
    assert enriched[1].timestamp == points[1].timestamp
    assert enriched[1].btc_price == points[1].btc_price


def test_enrich_phase_points_all_zones(default_config):
    """Enrich with scores spanning all three zones."""
    points = [
        PhasePoint(
            timestamp=datetime(2025, 1, i, tzinfo=timezone.utc),
            btc_price=30000.0,
            phase_score=0.0,
            zone="neutral",
        )
        for i in range(1, 4)
    ]
    
    scores = [10.0, 50.0, 90.0]
    
    enriched = enrich_phase_points_with_zones(points, scores, default_config)
    
    assert enriched[0].zone == "retention"
    assert enriched[1].zone == "neutral"
    assert enriched[2].zone == "distribution"


def test_enrich_phase_points_length_mismatch(default_config):
    """Raises ValueError if lengths don't match."""
    points = [
        PhasePoint(
            timestamp=datetime(2025, 1, 1, tzinfo=timezone.utc),
            btc_price=30000.0,
            phase_score=0.0,
            zone="neutral",
        ),
    ]
    
    scores = [50.0, 60.0]  # Length 2, but points is length 1
    
    with pytest.raises(ValueError, match="Mismatch"):
        enrich_phase_points_with_zones(points, scores, default_config)


def test_enrich_phase_points_empty(default_config):
    """Empty inputs produce empty output."""
    enriched = enrich_phase_points_with_zones([], [], default_config)
    assert enriched == []


def test_enrich_phase_points_preserves_timestamp_and_price(default_config):
    """Original timestamp and btc_price are preserved in enriched points."""
    original_timestamp = datetime(2025, 6, 15, 12, 30, 45, tzinfo=timezone.utc)
    original_price = 42123.45
    
    points = [
        PhasePoint(
            timestamp=original_timestamp,
            btc_price=original_price,
            phase_score=0.0,
            zone="neutral",
        ),
    ]
    
    scores = [55.5]
    
    enriched = enrich_phase_points_with_zones(points, scores, default_config)
    
    assert enriched[0].timestamp == original_timestamp
    assert enriched[0].btc_price == original_price
    assert enriched[0].phase_score == 55.5
    assert enriched[0].zone == "neutral"


def test_zone_classification_boundary_consistency(default_config):
    """Verify zone boundaries are consistent across score range."""
    # Test a range of scores to ensure no gaps or overlaps
    test_scores = [0.0, 10.0, 19.9, 20.0, 20.1, 50.0, 79.9, 80.0, 80.1, 90.0, 100.0]
    
    expected_zones = [
        "retention",  # 0.0
        "retention",  # 10.0
        "retention",  # 19.9
        "neutral",    # 20.0
        "neutral",    # 20.1
        "neutral",    # 50.0
        "neutral",    # 79.9
        "neutral",    # 80.0
        "distribution",  # 80.1
        "distribution",  # 90.0
        "distribution",  # 100.0
    ]
    
    for score, expected in zip(test_scores, expected_zones):
        assert classify_zone(score, default_config) == expected
