from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from typing import Protocol, Sequence


@dataclass
class MarketSeriesPoint:
    """Domain-level time series point for market data.

    Already-parsed (no HTTP), using datetime + float.
    """

    timestamp: datetime
    value: float


class MarketDataProvider(Protocol):
    """Abstract provider for BTC price and LTH-derived metrics."""

    def get_btc_price_series(self) -> Sequence[MarketSeriesPoint]:
        """Return normalized BTC price series for PhasePoint construction."""

    def get_lth_metric_series(self) -> Sequence[MarketSeriesPoint]:
        """Return LTH-derived metric series.

        Implementations may return an empty sequence if LTH data is not available.
        """
