import pandas as pd

def format_multi_method():

    df = pd.read_csv("data/1d-multi-method-data.csv")

    df = df.dropna()

    df.to_csv("data/1d-multi-method-clean.csv", index=False)

    print("Multi-method data formatted")

if __name__ == "__main__":
    format_multi_method()