import pandas as pd
import matplotlib.pyplot as plt

def visualize_multi_method():

    df = pd.read_csv("data/1d-multi-method-data.csv")

    # Print column names (helps debugging)
    print("Columns:", df.columns)

    # Assume first column is method, second is performance metric
    method_col = df.columns[0]
    score_col = df.columns[1]

    method_avg = df.groupby(method_col)[score_col].mean()

    plt.figure(figsize=(8,6))

    method_avg.plot(kind="bar")

    plt.title("Average Performance by Method")
    plt.xlabel("Method")
    plt.ylabel(score_col)

    plt.xticks(rotation=45)

    plt.tight_layout()

    plt.savefig("figs/fig-multi-method.png")

    plt.show()

if __name__ == "__main__":
    visualize_multi_method()