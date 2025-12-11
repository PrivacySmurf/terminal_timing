from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path

from .models import ChartData, PhasePoint, TimeValue
from .quality import DataQualityConfig, evaluate_data_quality
from .config import get_pipeline_mode, get_scoring_config, get_market_data_provider
from .scoring.phase_score import compute_phase_score
from .scoring.zones import enrich_phase_points_with_zones


def _load_fixture_points() -> list[PhasePoint]:
    """Return a tiny, deterministic set of PhasePoints from in-memory fixtures.

    This keeps Story 1.1 self-contained without real external providers.
    Now updated in Story 1.3 to use scoring module to compute phase_score and zone.

    Tests can monkeypatch this function to simulate missing or stale fixture data
    in order to drive `dataQuality` away from "complete".
    """

    base_ts = int(datetime(2024, 1, 1, tzinfo=timezone.utc).timestamp())
    prices = [40000.0, 42000.0, 45000.0, 43000.0]

    # Create initial points with placeholder scores/zones
    points: list[PhasePoint] = []
    for idx, price in enumerate(prices):
        ts = datetime.fromtimestamp(base_ts + idx * 86_400, tz=timezone.utc)
        points.append(
            PhasePoint(
                timestamp=ts,
                btc_price=price,
                phase_score=0.0,  # placeholder
                zone="neutral",  # placeholder
            )
        )
    return points


def _load_points_from_provider() -> tuple[list[PhasePoint], list[float] | None]:
    """Construct PhasePoints (and optional LTH series) from the provider.

    The provider abstraction supplies BTC price and an optional LTH-like
    metric. Both are already domain-level series (datetime + float).
    """

    provider = get_market_data_provider()
    btc_series = provider.get_btc_price_series()
    lth_points = provider.get_lth_metric_series()

    points: list[PhasePoint] = []
    for pt in btc_series:
        points.append(
            PhasePoint(
                timestamp=pt.timestamp,
                btc_price=pt.value,
                phase_score=0.0,  # placeholder, will be filled by scoring
                zone="neutral",  # placeholder, will be set by zone classifier
            )
        )

    # For Story 1.4 MVP, assume provider returns aligned BTC and LTH series.
    # If no LTH data is available, this can be an empty sequence.
    if not lth_points:
        lth_series: list[float] | None = None
    else:
        # Use the same order/length as btc_series; provider is responsible for
        # alignment. If lengths diverge, compute_phase_score will raise.
        lth_series = [pt.value for pt in lth_points]

    return points, lth_series
def _build_chart_data(points: list[PhasePoint]) -> ChartData:
    btc_price_series: list[TimeValue] = []
    lsd_series: list[TimeValue] = []
    for p in points:
        ts = int(p.timestamp.timestamp())
        btc_price_series.append(TimeValue(time=ts, value=p.btc_price))
        # `phase_score` field now semantically holds the LSD value
        lsd_series.append(TimeValue(time=ts, value=p.phase_score))

    last_updated = datetime.now(timezone.utc)

    # Use the shared evaluation logic so dataQuality semantics are consistent
    # with the architecture and unit tests.
    dq_config = DataQualityConfig()
    data_quality = evaluate_data_quality(points, now=last_updated, config=dq_config)

    return ChartData(
        btc_price=btc_price_series,
        lsd=lsd_series,
        last_updated=last_updated,
        data_quality=data_quality,
    )


def main() -> None:
    """Entry point for `timing-terminal-pipeline` CLI.

    For Story 1.1 this used in-memory fixtures only.
    Story 1.3 added the scoring module; Story 1.4 introduces an optional
    provider-backed path for building PhasePoints.
    """

    mode = get_pipeline_mode()

    if mode == "provider":
        points, lth_series = _load_points_from_provider()
    else:
        # Default / fixture mode preserves existing behavior for tests and
        # local runs that do not configure a provider.
        points = _load_fixture_points()
        lth_series = None
    
    # Compute phase scores using scoring module
    scoring_config = get_scoring_config()
    phase_scores = compute_phase_score(points, scoring_config, lth_series=lth_series)
    
    # Enrich points with computed scores and zones
    enriched_points = enrich_phase_points_with_zones(points, phase_scores, scoring_config)
    
    # Build chart data from enriched points
    chart_data = _build_chart_data(enriched_points)

    out_dir = Path("pipeline/out")
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / "chart-data.json"

    payload = chart_data.to_json_dict()
    out_path.write_text(json.dumps(payload, indent=2), encoding="utf-8")

    # Enhanced output showing phase scores and zones
    print(
        f"Generated {len(chart_data.btc_price)} points to {out_path} "
        f"(dataQuality={chart_data.data_quality}, lastUpdated={payload['lastUpdated']})"
    )
    print(f"Sample phase scores: {phase_scores}")
    print(f"Sample zones: {[p.zone for p in enriched_points]}")
