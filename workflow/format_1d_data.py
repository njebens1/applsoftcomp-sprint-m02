import pandas as pd

def format_1d_data():
    df = pd.read_csv("data/1d-data.csv")
    df = df.dropna()
    print("1D data formatted")

if __name__ == "__main__":
    format_1d_data()