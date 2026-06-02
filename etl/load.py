from sqlalchemy import create_engine

def load(df):

    engine = create_engine(
        "postgresql://postgres:postgres@bank-postgres:5432/banking"
    )

    df.to_sql(
        "transaction",
        engine,
        if_exists="replace",
        index=False
    )

    print("Loaded into SQL")