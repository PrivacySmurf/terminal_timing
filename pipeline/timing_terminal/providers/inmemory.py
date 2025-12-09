from __future__ import annotations

from datetime import datetime, timezone
from typing import Sequence

from . import MarketDataProvider, MarketSeriesPoint


class InMemoryFixtureProvider(MarketDataProvider):
    """Deterministic, in-memory provider for tests and local dev.

    Uses a fixed BTC price pattern and a simple synthetic LTH-like series.
    """

    def __init__(self) -> None:
        base_ts = datetime(2024, 1, 1, tzinfo=timezone.utc)
        prices = [40000.0, 42000.0, 45000.0, 43000.0]

        self._btc_series = [
            MarketSeriesPoint(timestamp=base_ts.replace(day=1 + idx), value=price)
            for idx, price in enumerate(prices)
        ]

        # Very simple synthetic LTH metric: scaled version of price
        self._lth_series = [
            MarketSeriesPoint(
                timestamp=pt.timestamp,
                value=pt.value * 0.0005,
            )
            for pt in self._btc_series
        ]

    def get_btc_price_series(self) -> Sequence[MarketSeriesPoint]:
        return list(self._btc_series)

    def get_lth_metric_series(self) -> Sequence[MarketSeriesPoint]:
        return list(self._lth_series)
