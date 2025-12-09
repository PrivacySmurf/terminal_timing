from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path

from .models import ChartData, PhasePoint, TimeValue


_EXPECTED_POINT_COUNT = 4


def _load_fixture_points() -> list[PhasePoint]:
    """Return a tiny, deterministic set of PhasePoints from in-memory fixtures.

    This keeps Story 1.1 self-contained without real external providers.

    Tests can monkeypatch this function to simulate missing or stale fixture data
    in order to drive `dataQuality` away from "complete".
    """

    base_ts = int(datetime(2024, 1, 1, tzinfo=timezone.utc).timestamp())
    prices = [40000.0, 42000.0, 45000.0, 43000.0]
    raw_scores = [10.0, 30.0, 70.0, 85.0]

    points: list[PhasePoint] = []
    for idx, (price, score) in enumerate(zip(prices, raw_scores, strict=True)):
        ts = datetime.fromtimestamp(base_ts + idx * 86_400, tz=timezone.utc)
        if score <= 20:
            zone: str = "retention"
        elif score >= 80:
            zone = "distribution"
        else:
            zone = "neutral"
        points.append(PhasePoint(timestamp=ts, btc_price=price, phase_score=score, zone=zone))
    return points


def _infer_data_quality(points: list[PhasePoint]) -> str:
    """Infer a simple dataQuality flag from the available points.

    - No points      → "stale" (nothing to emit)
    - Some but < N   → "partial" (fixtures incomplete)
    - N or more     → "complete"
    """

    if not points:
        return "stale"
    if len(points) < _EXPECTED_POINT_COUNT:
        return "partial"
    return "complete"


def _build_chart_data(points: list[PhasePoint]) -> ChartData:
    btc_price_series: list[TimeValue] = []
    phase_series: list[TimeValue] = []
    for p in points:
        ts = int(p.timestamp.timestamp())
        btc_price_series.append(TimeValue(time=ts, value=p.btc_price))
        phase_series.append(TimeValue(time=ts, value=p.phase_score))

    last_updated = datetime.now(timezone.utc)
    data_quality: str = _infer_data_quality(points)
    return ChartData(
        btc_price=btc_price_series,
        phase_score=phase_series,
        last_updated=last_updated,
        data_quality=data_quality,
    )


def main() -> None:
    """Entry point for `timing-terminal-pipeline` CLI.

    For Story 1.1 this uses in-memory fixtures only.
    """

    points = _load_fixture_points()
    chart_data = _build_chart_data(points)

    out_dir = Path("pipeline/out")
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / "chart-data.json"

    payload = chart_data.to_json_dict()
    out_path.write_text(json.dumps(payload, indent=2), encoding="utf-8")

    print(
        f"Generated {len(chart_data.btc_price)} points to {out_path} "
        f"(dataQuality={chart_data.data_quality}, lastUpdated={payload['lastUpdated']})"
    )