from airflow import dag
from datetime import datetime,timedelta
from airflow.operators import PythonOperator
from airflow.utils.dates import days_ago
from twitter_etl import twitter_etl

default_args = {
    'owner' : 'vishal',
    'depends_on_past' : False,
    'start_date' : datetime(2023,10,31),
    'retries' : 3,
    'retry_delay' : timedelta(minutes = 1)
}

with dag(
    'twitter_pipeline',
    default_args = default_args,
    decription = 'first twitter etl'
)as dag:
    run_etl = PythonOperator(
        task_id = 'twitter etl',
        python_callable = twitter_etl,
        dag = dag
    )

run_etl