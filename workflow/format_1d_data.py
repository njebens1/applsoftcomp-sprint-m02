import pandas as pd

def format_1d_data():
    # Load original data
    df = pd.read_csv("data/1d-data.csv")

    # Remove missing values
    df = df.dropna()

    # Save cleaned version
    df.to_csv("data/1d-data-clean.csv", index=False)

    print("1D data formatted and saved.")

if __name__ == "__main__":
    format_1d_data()