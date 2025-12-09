from datetime import datetime, timezone

from timing_terminal.models import ChartData, TimeValue


def test_chart_data_to_json_dict_structure():
    """ChartData.to_json_dict emits the expected JSON structure and types."""

    ts = int(datetime(2024, 1, 1).replace(tzinfo=timezone.utc).timestamp())
    btc_series = [TimeValue(time=ts, value=29000.5)]
    phase_series = [TimeValue(time=ts, value=45.2)]
    last_updated = datetime(2025, 12, 5, 8, 15, 0, tzinfo=timezone.utc)

    chart = ChartData(
        btc_price=btc_series,
        phase_score=phase_series,
        last_updated=last_updated,
        data_quality="complete",
    )

    payload = chart.to_json_dict()

    assert set(payload.keys()) == {"btcPrice", "phaseScore", "lastUpdated", "dataQuality"}

    assert payload["btcPrice"] == [{"time": ts, "value": 29000.5}]
    assert payload["phaseScore"] == [{"time": ts, "value": 45.2}]

    assert payload["lastUpdated"] == "2025-12-05T08:15:00Z"
    assert payload["dataQuality"] == "complete"