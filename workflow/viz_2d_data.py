import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def visualize_2d_data():

    df = pd.read_csv("data/2d-data.csv")

    plt.figure(figsize=(8,6))

    sns.heatmap(df, cmap="viridis")

    plt.title("2D Data Heatmap")

    plt.savefig("figs/fig-2d-data.png")

    plt.show()

if __name__ == "__main__":
    visualize_2d_data()