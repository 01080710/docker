from report_project.scripts.csv_generator import generate_csv_report
from datetime import datetime, timedelta
from airflow.operators.python import PythonOperator
from airflow import DAG




default_args = {
    "owner": "Vantage",
    "retries": 1,
    "retry_delay": timedelta(minutes=5),
}


with DAG(
    dag_id="Report_Workflow",
    default_args=default_args,
    start_date=datetime(2024, 1, 1),
    schedule_interval="*/1 * * * *",  # 每分鐘
    catchup=False,
    tags=["Project", "FreshReport"]
) as dag:
    
    # 這裡我們可以用迴圈動態產生任務
    tasks = []
    for i in range(1, 4):
        t = PythonOperator(
            task_id=f"generate_task_{i}",
            python_callable=generate_csv_report,
            # op_kwargs 會傳給 function
            # {{ logical_date }} 是 Airflow 的模板變數，代表這一批次應該執行的時間
            op_kwargs={
                "task_name": f"report_v{i}",
                "time_str": "{{ logical_date.strftime('%Y%m%d_%H%M%S') }}" 
            }
        )
        tasks.append(t)

    # 設定依賴關係：1 -> 2 -> 3
    tasks[0] >> tasks[1] >> tasks[2]