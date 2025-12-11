from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from typing import List, Literal


Zone = Literal["retention", "neutral", "distribution"]
DataQuality = Literal["complete", "partial", "stale"]


@dataclass
class PhasePoint:
    """Single point in time for BTC price and LSD value.

    Note:
        The `phase_score` field name is kept for backwards compatibility
        with earlier stories, but semantically it now represents the
        LTH Supply Dynamics (LSD) value in [0, 100].
    """

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
    """In-memory representation of chart-data.json.

    The second series now represents **LTH Supply Dynamics (LSD)**,
    exported under the `lsd` key in the JSON payload.
    """

    btc_price: List[TimeValue]
    lsd: List[TimeValue]
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
            "lsd": [
                {"time": tv.time, "value": float(tv.value)} for tv in self.lsd
            ],
            "lastUpdated": ts.isoformat() + "Z",
            "dataQuality": self.data_quality,
        }
