import streamlit as st
import pandas as pd
from sqlalchemy import create_engine

engine = create_engine(
    "postgresql://postgres:password@localhost:5432/bankdb"
)

df = pd.read_sql("SELECT * FROM transaction", engine)

st.title("Banking Analytics Dashboard")

st.write(df)

st.bar_chart(df['amount'])