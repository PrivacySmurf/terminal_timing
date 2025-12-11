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

import logging
import os
import time
from dataclasses import dataclass
from datetime import datetime
from typing import Sequence

import pandas as pd
import requests

from . import MarketDataProvider, MarketSeriesPoint

logger = logging.getLogger(__name__)


@dataclass
class ChartInspectConfig:
    sopr_url: str
    mvrv_url: str
    timeout: int = 30
    max_retries: int = 3


def fetch_chartinspect_data(url: str, metric_name: str, timeout: int = 30, max_retries: int = 3) -> pd.DataFrame:
    """Fetch data from ChartInspect API with retry logic.

    Ported from market_phase_score.py for self-contained provider usage.
    Caching is omitted since the pipeline runs daily via CI.

    Args:
        url: ChartInspect API endpoint URL
        metric_name: Human-readable name for logging
        timeout: Request timeout in seconds
        max_retries: Number of retry attempts on failure

    Returns:
        DataFrame with datetime index and metric columns

    Raises:
        RuntimeError: If all retry attempts fail
    """
    logger.info(f"Fetching {metric_name} from ChartInspect...")

    last_error: Exception | None = None
    for attempt in range(max_retries):
        try:
            response = requests.get(url, timeout=timeout)
            response.raise_for_status()
            data = response.json()

            if "data" in data and isinstance(data["data"], list):
                df = pd.DataFrame(data["data"])
                # Try timestamp (ms) first, fall back to date string
                try:
                    df["date"] = pd.to_datetime(df["date"], unit="ms", utc=True)
                except (ValueError, TypeError):
                    df["date"] = pd.to_datetime(df["date"], utc=True)
                df.set_index("date", inplace=True)
                df.sort_index(inplace=True)
                logger.info(f"Fetched {len(df)} records for {metric_name}")
                return df
            else:
                raise ValueError(f"Unexpected data format from {url}")

        except Exception as e:
            last_error = e
            logger.warning(f"Attempt {attempt + 1}/{max_retries} failed: {e}")
            if attempt < max_retries - 1:
                time.sleep(2**attempt)  # exponential backoff

    raise RuntimeError(f"Failed to fetch {metric_name} after {max_retries} attempts: {last_error}")


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

    @property
    def aligned_frame(self) -> pd.DataFrame:
        """Return the aligned SOPR/MVRV/BTC frame used for LSD computation."""

        return self._aligned.copy()

    @classmethod
    def from_config(cls) -> "ChartInspectMarketDataProvider":
        """Construct provider by fetching live ChartInspect data.

        This is an opt-in path controlled by config/env. Tests should
        monkeypatch the underlying fetch helper rather than performing
        live HTTP calls.
        """
        base = os.getenv("TT_CHARTINSPECT_BASE_URL", "https://chartinspect.com/api/charts")
        sopr_url = f"{base}/onchain/lth-sopr"
        mvrv_url = f"{base}/onchain/lth-mvrv?timeframe=all"

        sopr_df = fetch_chartinspect_data(sopr_url, "LTH-SOPR")
        mvrv_df = fetch_chartinspect_data(mvrv_url, "LTH-MVRV")

        return cls(sopr_df=sopr_df, mvrv_df=mvrv_df)

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
