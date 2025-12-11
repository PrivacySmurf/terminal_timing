from datetime import datetime, timedelta, timezone
from pathlib import Path

import pandas as pd

from timing_terminal.models import PhasePoint
from timing_terminal.history import HistoryConfig, update_lsd_history


def _pp(ts: datetime, price: float, lsd: float) -> PhasePoint:
    return PhasePoint(timestamp=ts, btc_price=price, phase_score=lsd, zone="neutral")


def test_first_run_creates_parquet(tmp_path, monkeypatch):
    history_path = tmp_path / "data" / "lsd_history.csv"
    cfg = HistoryConfig(path=history_path)

    now = datetime(2024, 1, 1, tzinfo=timezone.utc)
    points = [
        _pp(now - timedelta(days=3), 40000.0, 10.0),
        _pp(now - timedelta(days=2), 42000.0, 20.0),
    ]

    df = update_lsd_history(points, config=cfg)

    assert history_path.exists()
    assert list(df.columns) == ["timestamp", "lsd", "btc_price"]
    assert len(df) == 2
    # Timestamps should be parseable as datetimes (timezone info handled by history module)
    assert pd.api.types.is_datetime64_any_dtype(df["timestamp"])


def test_second_run_upserts_and_sorts(tmp_path):
    history_path = tmp_path / "data" / "lsd_history.csv"
    cfg = HistoryConfig(path=history_path)

    base = datetime(2024, 1, 1, tzinfo=timezone.utc)

    # First run
    first_points = [
        _pp(base + timedelta(days=0), 40000.0, 10.0),
        _pp(base + timedelta(days=1), 41000.0, 20.0),
    ]
    df1 = update_lsd_history(first_points, config=cfg)
    assert len(df1) == 2

    # Second run with an overlapping timestamp (updated LSD) and a new one
    second_points = [
        _pp(base + timedelta(days=1), 41500.0, 25.0),  # upsert
        _pp(base + timedelta(days=2), 43000.0, 30.0),  # new
    ]
    df2 = update_lsd_history(second_points, config=cfg)

    # We should have 3 unique timestamps, sorted
    assert len(df2) == 3
    assert list(df2["timestamp"]) == sorted(df2["timestamp"])

    # Upsert behavior: day+1 row should reflect the second run values
    mid_row = df2.iloc[1]
    assert mid_row["btc_price"] == 41500.0
    assert mid_row["lsd"] == 25.0


def test_empty_points_still_writes_empty_frame(tmp_path):
    history_path = tmp_path / "data" / "lsd_history.csv"
    cfg = HistoryConfig(path=history_path)

    df = update_lsd_history([], config=cfg)
    assert history_path.exists()
    assert list(df.columns) == ["timestamp", "lsd", "btc_price"]
    assert len(df) == 0
