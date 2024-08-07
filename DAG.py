from airflow import DAG

default_arguments = {
  'owner': 'NadaH',
  'start_date': datetime(2023, 1, 14),
  'retries': 2
}

with DAG('example_etl', default_args=default_arguments) as etl_dag:
  pass
