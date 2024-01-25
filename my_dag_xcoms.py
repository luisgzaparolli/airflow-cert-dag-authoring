from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.decorators import task, dag
from airflow.operators.subdag import SubDagOperator
from airflow.utils.task_group import TaskGroup
from datetime import datetime, timedelta
from typing import Dict
from subdag.subdag_factory import subdag_factory
from groups.process_task import process_task

@task.python(task_id="extract_partners", do_xcom_push=False, multiple_outputs=True)
def extract() -> Dict[str, str]:
    partner_name = "netflix"
    partner_path = "/partners/netflix"
    return {"partner_name": partner_name, "partner_path": partner_path}

@task.python
def process_a(partner_name, partner_path):
    print(partner_name)
    print(partner_path)

@task.python
def process_b(partner_name, partner_path):
    print(partner_name)
    print(partner_path)

@task.python
def process_c(partner_name, partner_path):
    print(partner_name)
    print(partner_path)

default_args = {
     "start_date": datetime(2021, 1, 1)
}

@dag(description="DAG in charge of processing custom data",
        default_args=default_args,
        schedule_interval='@daily',
        dagrun_timeout=timedelta(minutes=10),
        tags=['data_science', 'customer'],
        catchup=False,
        max_active_runs=1
         )

def my_dag():

    partner_settings = extract()

    process_task(partner_settings)
             
        
            

dag = my_dag()