# The Basics

Airflow Commands:
- astro dev init: initiate a project
- astro dev start: start airflow
- astro dev ps: check containers
- astro dev stop && astro dev start: restart airflow

localhost:8080 -> admin painel

## Define your DAG: the right way
- scheduler will read the files from the dag folder if they contain the words `dag` or `airflow`
    - change this with core.DAG_DISCOVERY_SAFE_MODE=False - will try to parse all
- .airflowignore -> add files into this files to not parse/read this type of files

### Dag Arguments:
- dag_id: if you have the same dag with the same id - will not report error, will get randomly one of the dags. STRING
- description: best practice. STRING
- start_date: date at which tasks start being scheduled, give error if not specified. DATETIME OBJECT
- schedule_interval: interval of time. ex. @daily, cron or timedelta object
- dagrun_time: recomended so dag dont overlap
- tags: helps to identify and categorize
- catchup:  to disable untriggered dags from the past or while the dag is paused
    - setup in config scheduler.catchup_by_default=False
    - will still have one running dag when enabling the dag

```python
from airflow import DAG
from datetime import datetime, timedelta

with DAG(dag_id='101my_dag',
         description='',
         start_date=datetime(2021,1,1),
         schedule_interval='@daily',
         dagrun_timeout=timedelta(minutes=10),
         tags=['data_science', 'customer'],
         catchup=False
         ) as dag:
         None
```

## DAG Scheduling 101

### Important Parameters:
- start_date: Date at which tasks start being scheduled
- schedule_interval: interval of time from the min(start_date) as which the DAG is triggered

The DAG [X] starts being scheduled from the start_date and will be triggered after every schedule_interval

If start_date is 10:00 AM and schedule interval every 10 minute.
Execute_date will be 10:00AM, start_date will be 10:10AM and DagRun #1

## Cron vs Timedelta
- timedelta is statefull, related to start_date
- cron expression is stateless, not related
    - usefull for jobs that have exactly X days between them

ex:
schedule_interval = "@daily" -> 0 0 ***

    1. 01/01 00:00
    2. 01/02 00:00

start_date = 01/01 10:00 AM and schedule_interval=timedelta(days=1)

    1. 01/01 10:00 AM - triggered on 01/02 10:00 AM
    2. 01/02 10:00 AM - triggered on 01/03 10:00 AM

## Task idempotence and determinism

- Determinism: Execute your task with an input. For the same input, you will always get the same output.
    Example: create table -> can only execute 1 time
- Idempotence: Execute multiple times your task, your task will always produce the same side effect.
    Example: create table if not exists

## Backfilling

- if catchup=True: will trigger all dagruns from the start_date to the current date
- airflow dags backfill -s 2020-01-01 -e 2021-01-01 dag_name
- max_active_runs=1 avoid to run more than 1 dag at a time
- in the interface can rerun by clearing the selected dagruns