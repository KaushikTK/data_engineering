# https://crontab.guru/

'''
Let us say that we want to schedule the run on weekends every week. For this we can use the website shared above to generate the cron schedule expression
'''

from airflow import DAG
from datetime import datetime, timedelta
from airflow.operators.bash import BashOperator

default_args = {
    'owner': 'kaushik',
    'retries': 5,
    'retry_delay': timedelta(minutes=2)
}

with DAG(
    'dag_with_cron_expression',
    default_args=default_args,
    description='this is a dag using the cron expression',
    schedule_interval='0 3 * * sat,sun', # '05 12 * * mon-fri,sun' means “At 12:05 on every day-of-week from Monday through Friday and Sunday.” 
    start_date=datetime.now(),
) as dag:
    task_1 = BashOperator(
        task_id="task_1",
        bash_command='echo "this is task 1.."'
    )

    task_1