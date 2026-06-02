from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

from etl.extract import extract
from etl.transform import transform
from etl.load import load

def pipeline():
    df = extract()
    df = transform(df)
    load(df)

default_args = {
    "start_date": datetime(2026, 1, 1)
}

dag = DAG(
    "bank_etl",
    schedule_interval="@daily",
    default_args=default_args,
    catchup=False
)

task = PythonOperator(
    task_id="run_etl",
    python_callable=pipeline,
    dag=dag
)