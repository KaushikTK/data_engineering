from airflow import DAG
from datetime import datetime, timedelta
from airflow.operators.bash import BashOperator

default_args = {
    'owner': 'kaushik',
    'retries': 5,
    'retry_delay': timedelta(minutes=2)
}


with DAG(
    'our_first_dag_v2',
    default_args=default_args,
    description='this is our first dag using bash',
    schedule_interval='@daily',
    start_date=datetime.now(),
) as dag:
    task_1 = BashOperator(
        task_id="task_1",
        bash_command='echo "this is task 1.."'
    )

    task_2 = BashOperator(
        task_id="task_2",
        bash_command='echo "This is task 2"',
    )

    task_3 = BashOperator(
        task_id="task_3",
        bash_command='echo "This is task 3"',
    )

    # run task 1 and then run task 2 and task 3 parallely
    #task_1.set_downstream(task_2)
    #task_1.set_downstream(task_3)
    '''
    this can also be written as follows:
    task_1 >> [task_2, task_3]
    '''

    # run task 1 and then run task 2 and then run task 3
    #task_1.set_downstream(task_2)
    #task_2.set_downstream(task_3)
    '''
    this can also be written as follows:
    task_1 >> task_2 >> task_3
    '''

    task_1 >> task_2 >> task_3