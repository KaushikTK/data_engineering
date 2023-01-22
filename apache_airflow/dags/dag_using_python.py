from airflow import DAG
from datetime import datetime, timedelta
from airflow.operators.python import PythonOperator

default_args = {
    'owner': 'kaushik',
    'retries': 5,
    'retry_delay': timedelta(minutes=2)
}

'''
task 1 - this runs the greet function and pushes some data to the xcom which can be used by the other tasks
task 2 - this runs the major_or_not function which uses the age variable set by task 1 in xcom and returns a boolean (true/false)
task 3 - this runs the display_message function which uses the boolean returned by task 2 to print some message

Note - max xcom size is 48KB and hence do not use it to share huge volume of data
'''


def greet(name,age,ti):
    print(f'Hello {name}!! You are {age} years old..')
    ti.xcom_push(key='age', value=age)

def major_or_not(ti):
    age = ti.xcom_pull(task_ids='task_1',key='age')
    if(age>18): return True
    return False

def display_message(ti):
    flag = ti.xcom_pull(task_ids='task_2')
    if(flag): print('You are a major!!')
    else: print('You are a minor!!')

with DAG(
    'python-dag',
    default_args=default_args,
    description='sample dag using python operator',
    schedule_interval='@daily',
    start_date=datetime.now(),
) as dag:
    task_1 = PythonOperator(
        task_id="task_1",
        python_callable=greet,
        op_kwargs={
            'name':'kaushik',
            'age':21
        }
    )

    task_2 = PythonOperator(
        task_id = 'task_2',
        python_callable = major_or_not,
    )

    task_3 = PythonOperator(
        task_id = 'task_3',
        python_callable = display_message,
    )

    task_1 >> task_2 >> task_3