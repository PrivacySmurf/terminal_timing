from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone, timedelta
from typing import Iterable

from .models import PhasePoint, DataQuality


@dataclass
class DataQualityConfig:
    """Configuration for data-quality evaluation.

    For now this is a simple in-code config that can later be wired to env/CLI
    without changing call sites.
    """

    expected_point_count: int = 4
    max_age_hours: int = 24


def evaluate_data_quality(
    points: Iterable[PhasePoint],
    *,
    now: datetime | None = None,
    config: DataQualityConfig | None = None,
) -> DataQuality:
    """Evaluate dataQuality = complete | partial | stale for a PhasePoint series.

    Rules (MVP):
    - No points → "stale" (nothing current to show)
    - If last point is older than max_age_hours → "stale"
    - Else if number of points < expected_point_count → "partial"
    - Else → "complete"
    """

    pts = list(points)
    if config is None:
        config = DataQualityConfig()

    if not pts:
        return "stale"

    # Determine age of the latest point
    latest_ts = max(p.timestamp for p in pts)
    if latest_ts.tzinfo is None:
        latest_ts = latest_ts.replace(tzinfo=timezone.utc)

    if now is None:
        now = datetime.now(timezone.utc)
    elif now.tzinfo is None:
        now = now.replace(tzinfo=timezone.utc)

    age = now - latest_ts
    if age > timedelta(hours=config.max_age_hours):
        return "stale"

    if len(pts) < config.expected_point_count:
        return "partial"

    return "complete"  # type: ignore[return-value]
