import pandas as pd

def format_2d_data():
    df = pd.read_csv("data/2d-data.csv")
    df = df.dropna()
    print("2D data formatted")

if __name__ == "__main__":
    format_2d_data()