'''
steps to follow:
1. go to localhost:8080 and select connections under admin section.
2. create a new record with both login and pw as airflow and 5432 as port and host as 'postgres' or 'host.docker.internal'
'''

from airflow import DAG
from datetime import datetime, timedelta
from airflow.providers.postgres.operators.postgres import PostgresOperator

default_args = {
    'owner': 'kaushik',
    'retries': 5,
    'retry_delay': timedelta(minutes=2)
}

with DAG(
    'dag_with_postgres_connection',
    default_args=default_args,
    description='sample dag with postgres connection',
    schedule_interval='@daily',
    start_date=datetime.now(),
) as dag:

    task_1 = PostgresOperator(
        task_id="create_table",
        postgres_conn_id = 'postgres_localhost',
        sql='''
        create table if not exists dag_runs(
            dt date,
            dag_id character varying,
            primary key (dt, dag_id)
        )
        '''
    )

    task_3 = PostgresOperator(
        task_id="delete_data",
        postgres_conn_id = 'postgres_localhost',
        sql='''
        delete from dag_runs where dt = '{{ ds }}' and dag_id = '{{ dag.dag_id }}';
        '''
    )

    task_2 = PostgresOperator(
        task_id="insert_data",
        postgres_conn_id = 'postgres_localhost',
        sql='''
        insert into dag_runs values ('{{ ds }}','{{ dag.dag_id }}');
        '''
    )

    task_1 >> task_3 >> task_2