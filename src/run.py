
import pandas as pd
from pathlib import Path
import matplotlib.pyplot as plt

DATA = Path(__file__).resolve().parents[1] / "data" / "sample_tickets.csv"
DOCS = Path(__file__).resolve().parents[1] / "docs"
DOCS.mkdir(parents=True, exist_ok=True)

def main():
    df = pd.read_csv(DATA, parse_dates=["opened_ts","closed_ts"])
    df["ttt_seconds"] = (df["closed_ts"] - df["opened_ts"]).dt.total_seconds()
    avg_ttt = df["ttt_seconds"].mean()
    coverage = (df["is_correctly_triaged"].sum() / len(df)) * 100.0

    metric_path = DOCS / "metric.txt"
    with metric_path.open("w") as f:
        f.write(f"Average time-to-triage (seconds) = {avg_ttt:.2f}\n")
        f.write(f"Correct triage coverage (%) = {coverage:.2f}\n")

    plt.figure()
    df["ttt_seconds"].plot(kind="hist", bins=10, title="Time-to-Triage (seconds)")
    plt.xlabel("seconds")
    fig_path = DOCS / "chart.png"
    plt.savefig(fig_path, bbox_inches="tight")
    plt.close()

    print(f"MTTT={avg_ttt:.0f}s; Coverage={coverage:.1f}% -> wrote {metric_path.name} and {fig_path.name} in docs/")

if __name__ == "__main__":
    main()
