from __future__ import annotations

"""LTH Supply Dynamics (LSD) scoring logic.

This module ports the core ideas from `market_phase_score.py` into the
pipeline scoring layer. It computes a 0-100 LSD series from LTH SOPR and
LTH MVRV time series using rolling percentile ranks and simple
multipliers for capitulation and euphoria.

For Story 1.6, this is a **first pass** implementation intended to be
structurally compatible with the research script while staying small and
well-tested. It will be refined as we integrate real ChartInspect data
and validate against historical behavior.
"""

from typing import Iterable

import numpy as np
import pandas as pd


def _savitzky_golay_smooth(series: pd.Series, window: int = 21, poly_order: int = 3) -> pd.Series:
    """Apply Savitzky-Golay filter for smoothing while preserving peaks/troughs.

    This matches the `market_phase_savgol` smoothing from the research script.
    """
    from scipy.signal import savgol_filter

    # Ensure window is odd
    if window % 2 == 0:
        window += 1

    # Need at least window length of data
    if len(series) < window:
        return series

    # Handle NaN values
    valid_mask = ~series.isna()
    if valid_mask.sum() < window:
        return series

    smoothed = series.copy()
    smoothed[valid_mask] = savgol_filter(series[valid_mask], window, poly_order)

    # Clip again after smoothing to ensure 0-100 range
    return smoothed.clip(0.0, 100.0)


def _percentile_rank(series: pd.Series, window: int) -> pd.Series:
    """Rolling percentile rank of the latest value within the window.

    Returns values in [0, 100]. Uses a minimum window of window//2 to
    avoid excessive NaNs at the beginning of the series.
    """

    def rank_pct(x: pd.Series) -> float:
        if len(x) < 2 or pd.isna(x.iloc[-1]):
            return np.nan
        return float((x < x.iloc[-1]).sum()) / float(len(x)) * 100.0

    return series.rolling(window=window, min_periods=max(1, window // 2)).apply(
        rank_pct, raw=False
    )


def compute_lsd(
    lth_sopr: Iterable[float] | pd.Series,
    lth_mvrv: Iterable[float] | pd.Series,
    lookback_window: int = 365 * 2,
    mvrv_weight: float = 0.6,
    sopr_weight: float = 0.4,
    capitulation_threshold: float = 0.95,
    euphoria_threshold: float = 4.0,
) -> pd.Series:
    """Compute Long-Term Holder Supply Dynamics (LSD) as a 0-100 series.

    This mirrors the `market_phase_score` function from `market_phase_score.py`:

    - Computes rolling percentile ranks of LTH MVRV and LTH SOPR over a
      long lookback window (default 2 years).
    - Combines them with configurable weights.
    - Applies multiplicative adjustments in capitulation (low SOPR) and
      euphoria (high MVRV) regimes.
    - Clips the final scores into [0, 100].
    """

    lth_sopr_s = pd.Series(lth_sopr).astype("float64")
    lth_mvrv_s = pd.Series(lth_mvrv).astype("float64")

    # Align indexes if they come in as Series with existing indices
    if len(lth_sopr_s) != len(lth_mvrv_s):
        raise ValueError("lth_sopr and lth_mvrv must have the same length")

    # Rolling percentile ranks
    mvrv_pct = _percentile_rank(lth_mvrv_s, lookback_window)
    sopr_pct = _percentile_rank(lth_sopr_s, lookback_window)

    # Weighted combination
    base_score = (mvrv_pct * float(mvrv_weight)) + (sopr_pct * float(sopr_weight))

    # Apply multipliers for extreme conditions
    score = base_score.copy()

    # Capitulation: SOPR below threshold → down-weight score
    capitulation_mask = lth_sopr_s < float(capitulation_threshold)
    score[capitulation_mask] = score[capitulation_mask] * 0.5

    # Euphoria: MVRV above threshold → up-weight score
    euphoria_mask = lth_mvrv_s > float(euphoria_threshold)
    score[euphoria_mask] = score[euphoria_mask] * 1.2

    # Clip to [0, 100]
    score = score.clip(0.0, 100.0)

    # Apply Savitzky-Golay smoothing (canonical series per Story 1.6 AC3)
    score = _savitzky_golay_smooth(score, window=21, poly_order=3)

    return score
