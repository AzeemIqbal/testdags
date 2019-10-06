from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.contrib.operators.kubernetes_pod_operator import KubernetesPodOperator
from datetime import datetime, timedelta


default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2019,10,2),
    'email': ['airflow@example .com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
    # 'queue': 'bash_queue',
    # 'pool': 'backfill',
    # 'priority_weight': 10,
    # 'end_date': datetime(2016, 1, 1),
}



dag =  DAG('BradPittDags',
	default_args = default_args,
	schedule_interval = '0 * * * *',
	concurrency=1,
	max_active_runs = 1
	)

gif = KubernetesPodOperator(namespace='airflow', image='slackdag:latest', cmds = ['python'], arguments=['/dags/slacktestBAD.py'],
	dag=dag, name='gif', task_id='gif', get_logs=True)
# gif = PythonOperator(task_id='motherfucking_dags', python_callable=post_slack_msg, provide_context=False, dag=dag)
