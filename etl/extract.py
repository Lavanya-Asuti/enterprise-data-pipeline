import pandas as pd

def extract():
    df = pd.read_csv("data/raw/transaction.csv")
    print("Data extracted")
    return df