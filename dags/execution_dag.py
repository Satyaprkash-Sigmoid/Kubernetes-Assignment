from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.operators.dummy_operator import DummyOperator
from datetime import datetime, timedelta
from airflow.operators.bash_operator import BashOperator
# from utils import fetch_and_store_execution_dag_run

import psycopg2


def fetch_and_store_execution_dag_run():
    try:
        conn = psycopg2.connect(host="postgres-service-db", database="airflow", user="airflow", password="airflow", port='5432')
        cursor = conn.cursor()
        drop_table = """drop table IF EXISTS execution_table"""
        cursor.execute(drop_table)
        conn.commit()
        create_query = """create table execution_table as select dag_id, execution_date from dag_run order by execution_date;"""
        cursor.execute(create_query)
        conn.commit()
        cursor.execute('select * from execution_table')
        data = cursor.fetchall()
        print("This is Data Execution time for every DAG runs :- ")
        for i in data:
            print(i)

    except Exception as e:
        print(e)
    finally:
        conn.close()

default_args = {
    "owner": "Satyaprakash",
    "depends_on_past": False,
    "start_date": datetime(2022, 3, 30),
    "email": ["airflow@airflow.com"],
    "email_on_failure": False,
    "email_on_retry": False,
    "retries": 1,
    "retry_delay": timedelta(minutes=5),
    # 'queue': 'bash_queue',
    # 'pool': 'backfill',
    # 'priority_weight': 10,
    # 'end_date': datetime(2016, 1, 1),
}

dag = DAG("Kubernetes_assignment", default_args=default_args, schedule_interval=timedelta(1))

t1 = BashOperator(task_id="Welcome", bash_command="echo Hi This is Satyaprakash From Sigmoid", dag=dag)

t2 = PythonOperator(task_id="fetch_execution_data_and_store", python_callable=fetch_and_store_execution_dag_run, dag=dag)

t1 >> t2
