from sqlalchemy import create_engine

def load(df):
    df.to_csv("output.csv", index=False)
    print("Data loaded successfully")

    df.to_sql(
        "transaction",
        engine,
        if_exists="replace",
        index=False
    )

    print("Loaded into SQL")