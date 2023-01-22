'''
This is same as that of the 'dag_using_python.py' but this uses the decorators api to reduce the complexity of the code..
'''

from airflow.decorators import dag, task
from datetime import datetime, timedelta

default_args = {
    'owner': 'kaushik',
    'retries': 5,
    'retry_delay': timedelta(minutes=2)
}

@dag(dag_id='python-dag-with-taskflow-api',
    default_args=default_args,
    description='sample dag using python operator',
    schedule_interval='@daily',
    start_date=datetime.now())


def _main():
    @task(multiple_outputs=True)
    def greet(name,age):
        print(f'Hello {name}!! You are {age} years old..')
        return {'age': age}

    @task()
    def major_or_not(age):
        if(age>18): return True
        return False

    @task()
    def display_message(flag):
        if(flag): print('You are a major!!')
        else: print('You are a minor!!')

    data = greet('kaushik', 21)
    major_flag = major_or_not(data['age'])
    display_message(major_flag)

sample_dag = _main()