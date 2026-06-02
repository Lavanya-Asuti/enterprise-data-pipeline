from sqlalchemy import create_engine

def load(df):

    engine = create_engine(
        "postgresql://postgres:password@localhost:5432/bankdb"
    )

    df.to_sql(
        "transaction",
        engine,
        if_exists="replace",
        index=False
    )

    print("Loaded into SQL")