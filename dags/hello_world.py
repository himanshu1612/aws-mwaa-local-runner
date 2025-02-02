import datetime

from airflow import models
from airflow.operators import bash

YESTERDAY = datetime.datetime.now() - datetime.timedelta(days=1)

default_args = {
    'owner': 'Himanshu - Druva',
    'depends_on_past': False,
    'email': [''],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': datetime.timedelta(minutes=5),
    'start_date': YESTERDAY,
}

with models.DAG(
        'hello_world',
        catchup=False,
        default_args=default_args,
        schedule_interval=datetime.timedelta(days=1)) as dag:

    # Print the dag_run id from the Airflow logs
    print_dag_run_conf = bash.BashOperator(
        task_id='hello_world', bash_command='echo "Hello World!"')