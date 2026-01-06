"""
my first dag for airflow
"""

import pendulum
from airflow.decorators import task
from airflow.models.dag import DAG
from airflow.operators.empty import EmptyOperator

with DAG(
    dag_id = "my_first_dag",
    start_date = pendolum.datetime(2026,4,1),
    catchup = False,
    schedule = None
) as dag:
    inizio = EmptyOperator( task_id = "inizio" )


    @task()
    def load_dataset():
        print("loading dataset ....")
        print("dataset loaded")
        return "path/to/dataset.parquet"
    
    load_dataset_task = load_dataset()

    @task()
    def training_ML_model(dataset_path):
        print(f"read dataset from {dataset_path}")
        print("dataset letto")
        print("modello addestrato")
        return "ML_flow_model_id"

    training_ML_model_task = training_ML_model(load_dataset_task)

    inizio >> load_dataset_task >> training_ML_model_task