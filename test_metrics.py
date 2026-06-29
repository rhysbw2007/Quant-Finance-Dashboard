import pandas as pd

from app import compute_metrics, prepare_data


def test_compute_metrics_and_volatility_for_short_series():
    df = pd.DataFrame(
        {
            "date": pd.to_datetime([
                "2024-01-02",
                "2024-01-03",
                "2024-01-04",
                "2024-01-05",
                "2024-01-08",
                "2024-01-09",
            ]),
            "ticker": ["AAPL"] * 6,
            "close": [100.0, 101.0, 100.0, 102.0, 103.0, 104.0],
        }
    )

    prepared = prepare_data(df)
    metrics = compute_metrics(prepared, "AAPL")

    assert metrics[0] > 0
    assert metrics[1] > 0
    assert metrics[2] > 0
    assert prepared["vol_30d"].notna().any()
