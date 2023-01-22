from airflow import DAG
from datetime import datetime, timedelta
from airflow.operators.bash import BashOperator

default_args = {
    'owner': 'kaushik',
    'retries': 5,
    'retry_delay': timedelta(minutes=2)
}

with DAG(
    'sample_catchup_and_backfill',
    default_args=default_args,
    description='sample catchup and backfill option in airflow',
    schedule_interval='@daily',
    start_date=datetime(2023,1,10), # start date is backdated
    catchup=True, # this will run the task for all the days missed and this is the default config
    #catchup=False, # this will skip for all the missed days and start fresh from the current day
) as dag:
    task_1 = BashOperator(
        task_id="task_1",
        bash_command='echo "this is task 1.."'
    )

    task_1