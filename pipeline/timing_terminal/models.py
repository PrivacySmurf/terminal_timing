from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from typing import List, Literal


Zone = Literal["retention", "neutral", "distribution"]
DataQuality = Literal["complete", "partial", "stale"]


@dataclass
class PhasePoint:
    """Single point in time for BTC price and phase score."""

    timestamp: datetime
    btc_price: float
    phase_score: float
    zone: Zone


@dataclass
class TimeValue:
    time: int  # unix epoch seconds (UTC)
    value: float


@dataclass
class ChartData:
    """In-memory representation of chart-data.json."""

    btc_price: List[TimeValue]
    phase_score: List[TimeValue]
    last_updated: datetime
    data_quality: DataQuality

    def to_json_dict(self) -> dict:
        # Normalize to seconds precision and strip offset; always use trailing Z
        ts = self.last_updated.replace(microsecond=0)
        # If timezone-aware, convert to UTC and drop offset in string
        if ts.tzinfo is not None:
            ts = ts.astimezone(timezone.utc).replace(tzinfo=None)
        return {
            "btcPrice": [
                {"time": tv.time, "value": float(tv.value)} for tv in self.btc_price
            ],
            "phaseScore": [
                {"time": tv.time, "value": float(tv.value)} for tv in self.phase_score
            ],
            "lastUpdated": ts.isoformat() + "Z",
            "dataQuality": self.data_quality,
        }
