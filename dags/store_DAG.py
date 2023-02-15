from airflow import DAG
from datetime import datetime, timedelta
from airflow.operators.bash_operator import BashOperator
from airflow.operators.mysql_operator import MySqlOperator

yesterday_data = datetime.strftime(datetime.now() - timedelta(1), "%Y-%m-%d")

default_args = {
    "owner": "Airflow",
    "start_date": datetime(2023, 2, 16),
    "retries": 1,
    "retry_delay": timedelta(seconds=5)
}

with DAG("store_dag", default_args=default_args, schedule_interval="@daily", template_searchpath=["/usr/local/airflow/sql_files"], catchup=True) as dag:

    t1 = BashOperator(
        task_id="check_file_exists",
        bash_command="shasum ~/store_files_airflow/raw_store_transactions.csv",
        retries=2,
        retry_delay=timedelta(seconds=15)
    )

    t2 = MySqlOperator(
        task_id="create_mysql_table", 
        mysql_conn_id="mysql_conn",
        sql="create_table.sql"
    )

    t1 >> t2