from airflow import DAG

default_arguments = {
  'owner': 'NadaH',
  'start_date': datetime(2023, 1, 14),
  'retries': 2
}

with DAG('example_etl', default_args=default_arguments) as etl_dag:
  pass
# how to schedule a DAG 
default_args = {
  'owner': 'Engineering',
  'start_date': datetime(2023, 11, 1),
  'email': ['airflowresults@datacamp.com'],
  'email_on_failure': False,
  'email_on_retry': False,
  'retries': 3,
  'retry_delay': timedelta(minutes=20)
}

dag = DAG('update_dataflows', default_args=default_args, schedule_interval='30 12 * * 3')
