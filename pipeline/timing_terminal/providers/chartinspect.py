from __future__ import annotations

"""ChartInspect-backed MarketDataProvider.

This provider is the bridge between the existing research scripts
(`market_phase_score.py`) and the pipeline provider abstraction.

For Story 1.6, it is responsible for:
- Fetching LTH SOPR and LTH MVRV series from ChartInspect.
- Extracting a BTC price series.
- Returning normalized, datetime-indexed series that can be converted
  into PhasePoint instances and LSD inputs.

NOTE: Tests should NOT hit the live ChartInspect API. Instead, they
will monkeypatch or feed this provider with recorded JSON fixtures.
"""

from dataclasses import dataclass
from datetime import datetime
from typing import Sequence

import pandas as pd

from . import MarketDataProvider, MarketSeriesPoint


@dataclass
class ChartInspectConfig:
    sopr_url: str
    mvrv_url: str


class ChartInspectMarketDataProvider(MarketDataProvider):
    """MarketDataProvider implementation backed by ChartInspect.

    In production, this will call the real HTTP API (using the same
    semantics as `fetch_chartinspect_data` in `market_phase_score.py`).

    In tests, this class should be driven via monkeypatched helpers or
    pre-recorded JSON fixtures to avoid live network calls.
    """

    def __init__(self, sopr_df: pd.DataFrame, mvrv_df: pd.DataFrame) -> None:
        """Initialize provider from pre-loaded SOPR and MVRV dataframes.

        This constructor intentionally accepts already-loaded dataframes so
        that unit/integration tests can provide deterministic fixtures
        without performing any HTTP requests.
        """

        # Expect both frames indexed by datetime and sorted.
        self._sopr_df = sopr_df.sort_index()
        self._mvrv_df = mvrv_df.sort_index()

        # Derive BTC price from MVRV (preferred) or SOPR as fallback.
        if "btc_price" in self._mvrv_df.columns:
            btc_price = self._mvrv_df["btc_price"].copy()
        elif "btc_price" in self._sopr_df.columns:
            btc_price = self._sopr_df["btc_price"].copy()
        else:
            btc_price = pd.Series(dtype="float64")

        # Align on SOPR index for now (as in market_phase_score.py).
        aligned = pd.DataFrame({
            "lth_sopr": self._sopr_df["lth_sopr"],
            "lth_mvrv": self._mvrv_df["lth_mvrv"].reindex(self._sopr_df.index),
        }).dropna()

        if not btc_price.empty:
            aligned["btc_price"] = btc_price.reindex(aligned.index)

        self._aligned = aligned.dropna()

    def get_btc_price_series(self) -> Sequence[MarketSeriesPoint]:
        series: list[MarketSeriesPoint] = []
        if "btc_price" not in self._aligned.columns:
            return series

        for ts, value in self._aligned["btc_price"].items():
            if pd.isna(value):
                continue
            if not isinstance(ts, datetime):
                ts = pd.to_datetime(ts).to_pydatetime()
            series.append(MarketSeriesPoint(timestamp=ts, value=float(value)))
        return series

    def get_lth_metric_series(self) -> Sequence[MarketSeriesPoint]:
        """Return a synthetic LTH series derived from SOPR/MVRV.

        For now, this returns the LTH MVRV series as a single scalar
        metric per timestamp, mirroring the previous synthetic LTH input.
        The full LSD logic will consume both SOPR and MVRV from the
        aligned dataframe separately; this method exists to satisfy the
        existing interface and maintain backwards compatibility for the
        momentum-based scoring path.
        """

        series: list[MarketSeriesPoint] = []
        for ts, value in self._aligned["lth_mvrv"].items():
            if pd.isna(value):
                continue
            if not isinstance(ts, datetime):
                ts = pd.to_datetime(ts).to_pydatetime()
            series.append(MarketSeriesPoint(timestamp=ts, value=float(value)))
        return series
