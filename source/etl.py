import pandas as pd

def run_etl(input_path="data/sales.csv", output_path="output/aggregated.csv"):
    df = pd.read_csv(input_path)
    df = df.dropna(subset=["Country", "Revenue"])
    df["Revenue"] = pd.to_numeric(df["Revenue"], errors="coerce")
    df = df.dropna(subset=["Revenue"])
    aggregated = df.groupby("Country")["Revenue"].sum().reset_index()
    aggregated.to_csv(output_path, index=False)
