# TaskFlow Api
## Templating
- templated params are defined in the Operator template_fields, template_ext
- for Python Operator they are: templates_dict, op_args and op_kwargs
- for PostgresOperator they are sql and the .sq extenson
- syntax: param: '{{ templated_param}}' or param: 'path/to_file.ext'

## XCOMS
- share data between tasks
- push XCOM -> store in metadata database -> pull XCOM
- ti.xcom_push(key="partner_name", value=partner_name)
    - OR just return in

## TaskFlow API

- Decorators
    - Help you create dags easier
    - @task.python: on top of your python function
    - @task.virtualenv
    - @task_group: multiple task
    - @dag
    - just add decorators in front of the functions
- XCOM Args
    - Tasks that have dependency (inplicity)
    - Automatically create explicit dependencies
    - Returned params can be directly used and they will be passed through XCOMs
- The task name will be the function name
- The dag id will be the funtion name anotated with @dag
- At the end you need to run the main function and store it in a variable
- for multiple xcom values
    - add multiple_outputs=True for multiple XCOMs - will also push dictionary
        - prevent push dictionary with do_xcom_push=False
    - or put -> Dict[str, str] - with this doesn't seem to work for separate xcoms

## Group Tasks

- Subdags
    - pretty complicated, needs some specific associations
    - behind the scene it is a Sensor in Airflow 2.0, so it waits for the tasks to complete
        - can use poke_interval
        - can use mode='reschedule'
    - have to put task_concurrency within each task in subdag
- Tasks Groups
    - easy to use
    - can import a task group from other file