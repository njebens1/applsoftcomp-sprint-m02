import pandas as pd
import matplotlib.pyplot as plt

def visualize_1d_data():
    # Load cleaned data
    df = pd.read_csv("data/1d-data.csv")
    df = df.dropna()

    # Create figure
    plt.figure()
    plt.plot(df.iloc[:, 0], df.iloc[:, 1])
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.title("1D Data Visualization")

    # Save figure
    plt.savefig("figs/fig-1d-data.png")
    plt.close()

    print("Figure saved to figs/fig-1d-data.png")

if __name__ == "__main__":
    visualize_1d_data()