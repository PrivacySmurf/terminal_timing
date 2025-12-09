import json
from pathlib import Path

from timing_terminal.cli import main


def test_cli_generates_chart_data_json(tmp_path, monkeypatch):
    """CLI should generate a valid chart-data.json in the expected location.

    Uses in-memory fixtures only (no external HTTP).
    """

    out_root = tmp_path / "pipeline" / "out"

    def _fake_out_dir() -> Path:
        return out_root

    # Monkeypatch Path used inside CLI if needed by redirecting CWD
    monkeypatch.chdir(tmp_path)

    main()

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