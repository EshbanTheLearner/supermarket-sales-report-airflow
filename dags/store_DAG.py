from airflow import DAG
from datetime import dateime, timedelta
from airflow.operators.bash_operator import BashOperator
from airflow.operators.mysql_operator import MySqlOperator