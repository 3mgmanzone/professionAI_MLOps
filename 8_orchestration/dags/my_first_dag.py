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

    @task.branch()
    def check_path(dataset_path):
        if dataset_path:
            return "training_ML_model"
        else:
            return "raise_error_dataset_path"

    check_path_task = check_path(load_dataset_task)

    @task(task_id = "training_ML_model")
    def training_ML_model(dataset_path):
        print(f"read dataset from {dataset_path}")
        print("dataset letto")
        print("modello addestrato")
        return "ML_flow_model_id"

    @task(task_id = "raise_error_dataset_path")
    def raise_error_dataset_path():
        raise Exception("Percorso del dataset nullo")

    raise_error_dataset_path_task = raise_error_dataset_path()

    training_ML_model_task = training_ML_model(load_dataset_task)

    inizio >> load_dataset_task >> check_path_task >> [ training_ML_model_task, raise_error_dataset_path_task ]