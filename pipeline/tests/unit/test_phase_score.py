"""Unit tests for phase score calculation logic."""

from datetime import datetime, timezone

import pytest

from timing_terminal.models import PhasePoint
from timing_terminal.scoring import ScoringConfig
from timing_terminal.scoring.phase_score import compute_phase_score


@pytest.fixture
def default_config():
    """Default scoring configuration."""
    return ScoringConfig()


@pytest.fixture
def custom_config():
    """Custom scoring configuration for testing config changes."""
    return ScoringConfig(
        retention_threshold=25.0,
        distribution_threshold=75.0,
        momentum_window=10,
        max_price_change_pct=50.0,
    )


def make_phase_point(timestamp_str: str, btc_price: float) -> PhasePoint:
    """Helper to create PhasePoint with placeholder score/zone."""
    return PhasePoint(
        timestamp=datetime.fromisoformat(timestamp_str).replace(tzinfo=timezone.utc),
        btc_price=btc_price,
        phase_score=0.0,  # placeholder
        zone="neutral",  # placeholder
    )


def test_empty_series(default_config):
    """Empty input returns empty scores."""
    result = compute_phase_score([], default_config)
    assert result == []


def test_single_point(default_config):
    """Single point returns neutral score (50.0)."""
    points = [make_phase_point("2025-01-01T00:00:00", 30000.0)]
    result = compute_phase_score(points, default_config)
    assert result == [50.0]


def test_flat_price_neutral_score(default_config):
    """Flat price over time produces mid-range scores around 50."""
    points = [
        make_phase_point(f"2025-01-{i:02d}T00:00:00", 30000.0)
        for i in range(1, 32)
    ]
    scores = compute_phase_score(points, default_config)
    
    # All scores should be 50.0 (no momentum)
    assert all(s == 50.0 for s in scores)


def test_uptrending_price_higher_score(default_config):
    """Uptrending price produces higher scores (approaching distribution)."""
    # Simulate 30-day uptrend: price increases 50% over 30 days
    points = [
        make_phase_point(f"2025-01-{i:02d}T00:00:00", 30000.0 + (i * 500))
        for i in range(1, 32)
    ]
    scores = compute_phase_score(points, default_config)
    
    # Later scores should be higher than earlier (momentum increasing)
    assert scores[-1] > scores[0]
    # Last score should be above neutral
    assert scores[-1] > 50.0


def test_downtrending_price_lower_score(default_config):
    """Downtrending price produces lower scores (approaching retention)."""
    # Simulate 30-day downtrend: price decreases 30% over 30 days
    points = [
        make_phase_point(f"2025-01-{i:02d}T00:00:00", 30000.0 - (i * 300))
        for i in range(1, 32)
    ]
    scores = compute_phase_score(points, default_config)
    
    # Later scores should be lower than earlier (momentum decreasing)
    assert scores[-1] < scores[0]
    # Last score should be below neutral
    assert scores[-1] < 50.0


def test_scores_bounded_0_100(default_config):
    """All scores are bounded within [0.0, 100.0]."""
    # Extreme price movements
    points = [
        make_phase_point("2025-01-01T00:00:00", 10000.0),
        make_phase_point("2025-01-31T00:00:00", 50000.0),  # +400% in 30 days
    ]
    scores = compute_phase_score(points, default_config)
    
    assert all(0.0 <= s <= 100.0 for s in scores)
    # Second score should be capped at 100.0 due to extreme momentum
    assert scores[-1] == 100.0


def test_exact_boundary_score_0(default_config):
    """Test score at exact 0.0 boundary."""
    # Maximum negative momentum: -100% change
    points = [
        make_phase_point("2025-01-01T00:00:00", 30000.0),
        make_phase_point("2025-01-31T00:00:00", 0.0),  # Price goes to 0
    ]
    scores = compute_phase_score(points, default_config)
    
    # Should produce score of 0.0 (or handle gracefully)
    assert scores[-1] == 0.0


def test_exact_boundary_score_100(default_config):
    """Test score at exact 100.0 boundary."""
    # Maximum positive momentum: +100% change (doubling)
    points = [
        make_phase_point("2025-01-01T00:00:00", 30000.0),
        make_phase_point("2025-01-31T00:00:00", 60000.0),  # Price doubles
    ]
    scores = compute_phase_score(points, default_config)
    
    # Should produce score of 100.0
    assert scores[-1] == 100.0


def test_config_changes_affect_output(default_config, custom_config):
    """Changing config parameters affects score output."""
    points = [
        make_phase_point(f"2025-01-{i:02d}T00:00:00", 30000.0 + (i * 300))
        for i in range(1, 21)
    ]
    
    scores_default = compute_phase_score(points, default_config)
    scores_custom = compute_phase_score(points, custom_config)
    
    # With shorter momentum_window (10 vs 30), scores should differ
    # especially for later points that have more history
    assert scores_default[-1] != scores_custom[-1]


def test_zero_historical_price_handling(default_config):
    """Zero historical price is handled gracefully."""
    points = [
        make_phase_point("2025-01-01T00:00:00", 0.0),  # Zero price
        make_phase_point("2025-01-02T00:00:00", 30000.0),
    ]
    scores = compute_phase_score(points, default_config)
    
    # Should return neutral score (50.0) when dividing by zero
    assert scores[0] == 50.0  # First point (single point case)
    assert scores[1] == 50.0  # Second point (avoids division by zero)


def test_deterministic_output(default_config):
    """Same input produces same output (determinism)."""
    points = [
        make_phase_point(f"2025-01-{i:02d}T00:00:00", 30000.0 + (i * 200))
        for i in range(1, 11)
    ]
    
    scores_1 = compute_phase_score(points, default_config)
    scores_2 = compute_phase_score(points, default_config)
    
    assert scores_1 == scores_2


def test_short_history_uses_available_window(default_config):
    """Early points with insufficient history use shorter lookback."""
    points = [
        make_phase_point(f"2025-01-{i:02d}T00:00:00", 30000.0 + (i * 100))
        for i in range(1, 11)
    ]
    scores = compute_phase_score(points, default_config)
    
    # All scores should be computed (no errors from insufficient history)
    assert len(scores) == 10
    # All scores should be valid
    assert all(0.0 <= s <= 100.0 for s in scores)


def test_lth_series_length_mismatch_raises(default_config):
    """Providing LTH series with wrong length raises ValueError."""
    points = [
        make_phase_point("2025-01-01T00:00:00", 30000.0),
        make_phase_point("2025-01-02T00:00:00", 31000.0),
    ]
    lth_series = [0.1]  # wrong length

    with pytest.raises(ValueError, match="lth_series length"):
        compute_phase_score(points, default_config, lth_series=lth_series)


def test_lth_weight_zero_preserves_base_scores(default_config):
    """Passing LTH series with zero weight must not change scores."""
    points = [
        make_phase_point(f"2025-01-{i:02d}T00:00:00", 30000.0 + (i * 200))
        for i in range(1, 6)
    ]
    base_scores = compute_phase_score(points, default_config)

    lth_series = [10.0, 20.0, 30.0, 40.0, 50.0]

    # Explicitly set lth_weight to 0.0
    cfg_zero_weight = ScoringConfig(lth_weight=0.0)
    scores_with_lth = compute_phase_score(points, cfg_zero_weight, lth_series=lth_series)

    assert scores_with_lth == base_scores


def test_lth_positive_weight_influences_scores(default_config):
    """Non-zero LTH weight should influence scores in a predictable direction."""
    points = [
        make_phase_point(f"2025-01-{i:02d}T00:00:00", 30000.0)
        for i in range(1, 6)
    ]
    base_scores = compute_phase_score(points, default_config)

    # Increasing LTH series should push scores upward when weighted in
    lth_series = [10.0, 20.0, 30.0, 40.0, 50.0]
    cfg_lth = ScoringConfig(lth_weight=0.5)

    scores_with_lth = compute_phase_score(points, cfg_lth, lth_series=lth_series)

    # Ensure scores have changed and the last score is higher than base
    assert scores_with_lth != base_scores
    assert scores_with_lth[-1] > base_scores[-1]

    # Still bounded
    assert all(0.0 <= s <= 100.0 for s in scores_with_lth)
