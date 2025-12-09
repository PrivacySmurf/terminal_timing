import json
from datetime import datetime, timedelta, timezone
from pathlib import Path

import timing_terminal.cli as cli
from timing_terminal.models import PhasePoint


def test_cli_generates_chart_data_json(tmp_path, monkeypatch):
    """CLI should generate a valid chart-data.json in the expected location.

    Uses in-memory fixtures only (no external HTTP).
    """

    out_root = tmp_path / "pipeline" / "out"

    def _fake_out_dir() -> Path:
        return out_root

    # Monkeypatch Path used inside CLI if needed by redirecting CWD
    monkeypatch.chdir(tmp_path)

    cli.main()

    out_path = tmp_path / "pipeline" / "out" / "chart-data.json"
    assert out_path.exists(), "chart-data.json was not generated"

    data = json.loads(out_path.read_text(encoding="utf-8"))

    # Basic schema checks
    assert set(data.keys()) == {"btcPrice", "phaseScore", "lastUpdated", "dataQuality"}

    assert isinstance(data["btcPrice"], list) and data["btcPrice"], "btcPrice should be non-empty list"
    assert isinstance(data["phaseScore"], list) and data["phaseScore"], "phaseScore should be non-empty list"

    # Time alignment: lengths must match and times correspond
    assert len(data["btcPrice"]) == len(data["phaseScore"])
    for p_entry, s_entry in zip(data["btcPrice"], data["phaseScore"], strict=True):
        assert p_entry["time"] == s_entry["time"]

    assert data["dataQuality"] in {"complete", "partial", "stale"}

    # lastUpdated must be a non-empty ISO-like string ending with Z
    assert isinstance(data["lastUpdated"], str)
    assert data["lastUpdated"].endswith("Z")


def test_cli_can_emit_partial_data_quality(tmp_path, monkeypatch):
    """CLI should be able to emit a non-complete dataQuality value.

    We simulate missing fixture data by monkeypatching the internal
    `_load_fixture_points` helper to return fewer points than expected,
    which should drive `dataQuality` to "partial".
    """

    out_root = tmp_path / "pipeline" / "out"

    def _partial_points() -> list[PhasePoint]:
        # Use recent timestamps so data is fresh enough to avoid "stale" and
        # exercise the "partial" path based on insufficient point count.
        now = datetime.now(timezone.utc)
        prices = [40000.0, 42000.0]
        scores = [10.0, 30.0]
        points: list[PhasePoint] = []
        for idx, (price, score) in enumerate(zip(prices, scores, strict=True)):
            ts = now - timedelta(hours=idx + 1)
            zone = "retention" if score <= 20 else "neutral"
            points.append(PhasePoint(timestamp=ts, btc_price=price, phase_score=score, zone=zone))
        return points

    monkeypatch.chdir(tmp_path)
    monkeypatch.setattr(cli, "_load_fixture_points", _partial_points)

    cli.main()

    out_path = out_root / "chart-data.json"
    assert out_path.exists(), "chart-data.json was not generated for partial scenario"

    data = json.loads(out_path.read_text(encoding="utf-8"))
    assert data["dataQuality"] == "partial"


def test_cli_can_emit_stale_data_quality(tmp_path, monkeypatch):
    """CLI should be able to emit a stale dataQuality value.

    We simulate stale data by returning points whose timestamps are well
    outside the freshness window. This should drive `dataQuality` to "stale".
    """

    out_root = tmp_path / "pipeline" / "out"

    def _stale_points() -> list[PhasePoint]:
        # Far in the past relative to "now" inside the CLI
        base_ts = datetime(2020, 1, 1, tzinfo=timezone.utc)
        points: list[PhasePoint] = []
        for days in (10, 9, 8):
            ts = base_ts - timedelta(days=days)
            points.append(PhasePoint(timestamp=ts, btc_price=40000.0, phase_score=50.0, zone="neutral"))
        return points

    monkeypatch.chdir(tmp_path)
    monkeypatch.setattr(cli, "_load_fixture_points", _stale_points)

    cli.main()

    out_path = out_root / "chart-data.json"
    assert out_path.exists(), "chart-data.json was not generated for stale scenario"

    data = json.loads(out_path.read_text(encoding="utf-8"))
    assert data["dataQuality"] == "stale"
