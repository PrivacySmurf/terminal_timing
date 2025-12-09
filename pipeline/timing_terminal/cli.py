from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path

from .models import ChartData, PhasePoint, TimeValue
from .quality import DataQualityConfig, evaluate_data_quality
from .config import get_scoring_config
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
def _build_chart_data(points: list[PhasePoint]) -> ChartData:
    btc_price_series: list[TimeValue] = []
    phase_series: list[TimeValue] = []
    for p in points:
        ts = int(p.timestamp.timestamp())
        btc_price_series.append(TimeValue(time=ts, value=p.btc_price))
        phase_series.append(TimeValue(time=ts, value=p.phase_score))

    last_updated = datetime.now(timezone.utc)

    # Use the shared evaluation logic so dataQuality semantics are consistent
    # with the architecture and unit tests.
    dq_config = DataQualityConfig()
    data_quality = evaluate_data_quality(points, now=last_updated, config=dq_config)

    return ChartData(
        btc_price=btc_price_series,
        phase_score=phase_series,
        last_updated=last_updated,
        data_quality=data_quality,
    )


def main() -> None:
    """Entry point for `timing-terminal-pipeline` CLI.

    For Story 1.1 this uses in-memory fixtures only.
    Updated in Story 1.3 to compute phase scores using scoring module.
    """

    # Load fixture points with placeholder scores
    points = _load_fixture_points()
    
    # Compute phase scores using scoring module
    scoring_config = get_scoring_config()
    phase_scores = compute_phase_score(points, scoring_config)
    
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
