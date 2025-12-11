from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Iterable

import pandas as pd

from .models import PhasePoint


# Use CSV for portability (no optional Parquet deps required).
DEFAULT_HISTORY_PATH = Path("data/lsd_history.csv")


@dataclass
class HistoryConfig:
    """Configuration for LSD history persistence.

    This is intentionally minimal and file-based for Story 1.6.
    """

    path: Path = DEFAULT_HISTORY_PATH


def _phase_points_to_frame(points: Iterable[PhasePoint]) -> pd.DataFrame:
    rows: list[dict] = []
    for p in points:
        ts = p.timestamp
        if ts.tzinfo is None:
            ts = ts.replace(tzinfo=timezone.utc)
        rows.append(
            {
                "timestamp": ts,
                "lsd": float(p.phase_score),
                "btc_price": float(p.btc_price),
            }
        )
    if not rows:
        return pd.DataFrame(columns=["timestamp", "lsd", "btc_price"])
    df = pd.DataFrame(rows)
    df = df.dropna(subset=["timestamp"]).copy()
    df["timestamp"] = pd.to_datetime(df["timestamp"], utc=True)
    return df


def update_lsd_history(
    points: Iterable[PhasePoint],
    *,
    config: HistoryConfig | None = None,
) -> pd.DataFrame:
    """Merge new LSD points into on-disk history and return the updated frame.

    Upserts by `timestamp` and keeps the file sorted in ascending time.
    First run (no file) simply creates the Parquet file.
    """

    if config is None:
        config = HistoryConfig()

    history_path = config.path
    history_path.parent.mkdir(parents=True, exist_ok=True)

    new_df = _phase_points_to_frame(points)

    if history_path.exists():
        try:
            existing = pd.read_csv(history_path)
        except Exception:
            # If the existing file is corrupted/unreadable, treat as empty.
            existing = pd.DataFrame(columns=["timestamp", "lsd", "btc_price"])
    else:
        existing = pd.DataFrame(columns=["timestamp", "lsd", "btc_price"])

    if existing.empty and new_df.empty:
        # Nothing to write, but ensure an empty, typed frame is returned.
        empty = pd.DataFrame(columns=["timestamp", "lsd", "btc_price"])
        empty.to_csv(history_path, index=False)
        return empty

    # Ensure both have the same columns and datetime index semantics.
    if not existing.empty:
        existing["timestamp"] = pd.to_datetime(existing["timestamp"], utc=True)

    combined = pd.concat([existing, new_df], ignore_index=True)

    # Upsert by timestamp: keep the last occurrence of each timestamp.
    combined = (
        combined.sort_values("timestamp")
        .drop_duplicates(subset=["timestamp"], keep="last")
        .reset_index(drop=True)
    )

    combined.to_csv(history_path, index=False)
    return combined
