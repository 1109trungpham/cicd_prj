from source.etl import run_etl
import pandas as pd
import os

def test_run_etl(tmp_path):
    input_path = tmp_path / "sales.csv"
    output_path = tmp_path / "aggregated.csv"

    # sample test data
    df = pd.DataFrame({
        "Country": ["US", "UK", "US", None],
        "Revenue": [100, 200, 300, 400]
    })
    df.to_csv(input_path, index=False)

    run_etl(input_path, output_path)
    result = pd.read_csv(output_path)

    assert "Country" in result.columns
    assert "Revenue" in result.columns
    assert result.shape[0] == 2
    assert result["Revenue"].sum() == 600
