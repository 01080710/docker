# from airflow import DAG
# from airflow.providers.docker.operators.docker import DockerOperator
# from docker.types import Mount
# from datetime import datetime

# default_args = {
#     "owner": "airflow",
#     "depends_on_past": False,
# }

# with DAG(
#     dag_id="docker_calculater_safe",
#     default_args=default_args,
#     start_date=datetime(2026, 1, 19),  # 今天的日期就好
#     schedule_interval="* * * * *",     # 每分鐘觸發
#     catchup=False,
#     tags=["docker", "test"],
# ) as dag:

#     run_calculater = DockerOperator(
#         task_id="run_calculater_container",
#         image="calculater:latest",
#         api_version="auto",
#         auto_remove=True,
#         mount_tmp_dir=False,  # 避免 /tmp 被覆蓋
#         mounts=[
#             # container 內 /opt/airflow/data 會映射到 Windows host
#             Mount(source="/opt/airflow/data", target="/opt/airflow/data", type="bind")
#         ],
#         docker_url="unix://var/run/docker.sock",
#         network_mode="bridge",
#         command="python app.py",
#     )


# from airflow import DAG
# from airflow.providers.docker.operators.docker import DockerOperator
# from docker.types import Mount
# from datetime import datetime

# default_args = {
#     "owner": "airflow",
#     "depends_on_past": False,
# }

# with DAG(
#     dag_id="docker_calculater_test",
#     default_args=default_args,
#     start_date=datetime(2026, 1, 19),
#     schedule_interval=None,  # 單次測試
#     catchup=False,
#     tags=["docker", "test"],
# ) as dag:

#     test_hello = DockerOperator(
#         task_id="hello_world_container",
#         image="calculater:latest",
#         api_version="auto",
#         auto_remove=True,
#         mount_tmp_dir=False,
#         mounts=[
#             Mount(
#                 source="C:/Users/88696/Desktop/airflow-data", # 必須是 Host 的真實路徑
#                 target="/opt/airflow/data", 
#                 type="bind"
#             )
#         ],
#         docker_url="unix://var/run/docker.sock",
#         network_mode="bridge",
#         command='python app.py"'
#         # command='python -c "print(\'Hello World\')"'
#     )


from airflow import DAG
from airflow.providers.docker.operators.docker import DockerOperator
from docker.types import Mount
from datetime import datetime

default_args = {
    "owner": "airflow",
    "depends_on_past": False,
}

with DAG(
    dag_id="docker_calculater_every_minute",
    default_args=default_args,
    start_date=datetime(2026, 1, 19),
    schedule_interval="* * * * *",  # 每分鐘觸發
    catchup=False,
    tags=["docker", "test"],
) as dag:

    run_calculater = DockerOperator(
        task_id="run_calculater_container",
        image="calculater:latest",
        api_version="auto",
        auto_remove=True,
        mount_tmp_dir=False,
        mounts=[
            Mount(source="C:/Users/88696/Desktop/airflow-data", 
                  target="/opt/airflow/data", 
                  type="bind")
        ],
        docker_url="unix://var/run/docker.sock",
        network_mode="bridge",
        command="python app.py"  # container 內 WORKDIR=/app，app.py 已經在裡面
    )
