from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
from extract import extract
from transform import transform_news
from load import upload_dataframe_to_mysql

# ✅ Default DAG arguments
default_args = {
    "owner": "airflow",
    "depends_on_past": False,
    "start_date": datetime(2024, 1, 1),
    "retries": 2,
    "retry_delay": timedelta(minutes=5),
}

# Define DAG
dag = DAG(
    "news_etl_pipeline",
    default_args=default_args,
    description="Automated ETL Pipeline for News Data",
    schedule="0 9 * * *",
    catchup=False,
)

# Define Task Functions
def extract():
    return extract()

def transform(ti):
    news_data = ti.xcom_pull(task_ids="extract_task")
    return transform_news(news_data)

def load(ti):
    transformed_data = ti.xcom_pull(task_ids="transform_task")
    upload_dataframe_to_mysql(transformed_data)

# Define Tasks
extract_task = PythonOperator(task_id="extract_task", python_callable=extract, dag=dag)
transform_task = PythonOperator(task_id="transform_task", python_callable=transform, dag=dag)
load_task = PythonOperator(task_id="load_task", python_callable=load, dag=dag)

# Task Order
extract_task >> transform_task >> load_task
