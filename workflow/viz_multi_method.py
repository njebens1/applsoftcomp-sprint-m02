import pandas as pd
import matplotlib.pyplot as plt

def visualize_multi_method():

    df = pd.read_csv("data/1d-multi-method-data.csv")

    method_col = df.columns[0]
    score_col = df.columns[1]

    method_avg = df.groupby(method_col)[score_col].mean()

    # Set colors
    colors = []
    for method in method_avg.index:
        if "proposed" in method.lower():
            colors.append("red")     # highlight proposed method
        else:
            colors.append("gray")    # baseline methods

    plt.figure(figsize=(8,6))

    method_avg.plot(kind="bar", color=colors)

    plt.title("Comparison of Methods")
    plt.xlabel("Method")
    plt.ylabel(score_col)

    plt.xticks(rotation=45)

    plt.tight_layout()

    plt.savefig("figs/fig-multi-method.png")

    plt.show()

if __name__ == "__main__":
    visualize_multi_method()