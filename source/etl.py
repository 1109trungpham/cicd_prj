# source/etl.py
import pandas as pd

def run_etl():
    df = pd.read_csv("source/input.csv")
    df["total"] = df["quantity"] * df["price"]
    df.to_csv("output.csv", index=False)

if __name__ == "__main__":
    run_etl()
