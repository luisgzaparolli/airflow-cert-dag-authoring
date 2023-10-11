from airflow import DAG

with DAG("my_dag", description="DAG in charge of processing customer data", 
         start_date=datetime(2021, 1, 1),
         schedule_interval='@daily',
         dagrun_timeout=timedelta(minutes=10),
         tags=["data_science", "customers"],
         catchupe=False) as dag:
    None

