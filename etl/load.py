def load(df):
    df.to_csv("output.csv", index=False)
    print("Data loaded successfully")