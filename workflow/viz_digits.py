import pandas as pd
import matplotlib.pyplot as plt
from sklearn.manifold import TSNE

def visualize_digits():

    df = pd.read_csv("data/digits-data.csv")

    # Features and labels
    X = df.iloc[:, :-1]
    y = df.iloc[:, -1]

    # Reduce to 2D using t-SNE
    tsne = TSNE(n_components=2, random_state=42)

    X_embedded = tsne.fit_transform(X)

    plt.figure(figsize=(8,6))

    scatter = plt.scatter(
        X_embedded[:,0],
        X_embedded[:,1],
        c=y,
        cmap="tab10",
        s=10
    )

    plt.title("Digits Visualization (t-SNE)")
    plt.xlabel("Component 1")
    plt.ylabel("Component 2")

    plt.colorbar(scatter)

    plt.tight_layout()

    plt.savefig("figs/fig-digits.png")

    plt.show()

if __name__ == "__main__":
    visualize_digits()