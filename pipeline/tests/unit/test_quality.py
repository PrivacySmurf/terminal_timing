from datetime import datetime, timedelta, timezone

from timing_terminal.models import PhasePoint
from timing_terminal.quality import DataQualityConfig, evaluate_data_quality


def _pp(ts: datetime, price: float = 40000.0, score: float = 50.0) -> PhasePoint:
    return PhasePoint(timestamp=ts, btc_price=price, phase_score=score, zone="neutral")


def test_evaluate_data_quality_complete_when_enough_fresh_points():
    now = datetime(2024, 1, 10, tzinfo=timezone.utc)
    cfg = DataQualityConfig(expected_point_count=3, max_age_hours=24)

    points = [
        _pp(now - timedelta(hours=6)),
        _pp(now - timedelta(hours=4)),
        _pp(now - timedelta(hours=2)),
    ]

    dq = evaluate_data_quality(points, now=now, config=cfg)
    assert dq == "complete"


def test_evaluate_data_quality_partial_when_insufficient_points():
    now = datetime(2024, 1, 10, tzinfo=timezone.utc)
    cfg = DataQualityConfig(expected_point_count=3, max_age_hours=24)

    points = [
        _pp(now - timedelta(hours=6)),
    ]

    dq = evaluate_data_quality(points, now=now, config=cfg)
    assert dq == "partial"


def test_evaluate_data_quality_stale_when_too_old():
    now = datetime(2024, 1, 10, tzinfo=timezone.utc)
    cfg = DataQualityConfig(expected_point_count=1, max_age_hours=24)

    points = [
        _pp(now - timedelta(hours=48)),
    ]

    dq = evaluate_data_quality(points, now=now, config=cfg)
    assert dq == "stale"


def test_evaluate_data_quality_stale_when_no_points():
    now = datetime(2024, 1, 10, tzinfo=timezone.utc)
    cfg = DataQualityConfig(expected_point_count=3, max_age_hours=24)

    dq = evaluate_data_quality([], now=now, config=cfg)
    assert dq == "stale"
