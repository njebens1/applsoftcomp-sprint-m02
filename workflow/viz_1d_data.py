import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def visualize_1d_data():

    # Load the dataset
    df = pd.read_csv("data/1d-data.csv")

    # Remove missing values
    df = df.dropna()

    # Identify columns
    value_col = df.columns[0]
    group_col = df.columns[1]

    # Create visualization
    plt.figure(figsize=(8,6))
    sns.boxplot(data=df, x=group_col, y=value_col)

    plt.title("Distribution of Values: Cases vs Control")
    plt.xlabel("Group")
    plt.ylabel("Value")

    plt.tight_layout()

    # Save figure
    plt.savefig("figs/fig-1d-data.png")

    # Show graph
    plt.show()

    print("Visualization saved to figs/fig-1d-data.png")

if __name__ == "__main__":
    visualize_1d_data()