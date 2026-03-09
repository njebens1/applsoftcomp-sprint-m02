import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def visualize_1d_data():
    df = pd.read_csv("data/1d-data.csv")
    df = df.dropna()

    # assume: first column = value, second column = group (cases/control)
    value_col = df.columns[0]
    group_col = df.columns[1]

    plt.figure(figsize=(8,6))
    sns.boxplot(data=df, x=group_col, y=value_col)

    plt.title("1D Data: Cases vs Control")
    plt.xlabel("Group")
    plt.ylabel(value_col)

    plt.tight_layout()
    plt.savefig("figs/fig-1d-data.png")
    plt.show()

if __name__ == "__main__":
    visualize_1d_data()