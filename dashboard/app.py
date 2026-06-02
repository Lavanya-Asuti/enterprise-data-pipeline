from sqlalchemy import create_engine
import pandas as pd
import streamlit as st

engine = create_engine(
    "postgresql://postgres:postgres@host.docker.internal:5432/banking"
)

df = pd.read_sql(
    'SELECT * FROM "transaction"',
    engine
)

st.title("Banking ETL Dashboard")

st.dataframe(df)

st.metric(
    "Total Transactions",
    len(df)
)