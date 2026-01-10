import random  ,csv


def generate_csv_report(task_name, time_str, **context):
    """
    業務邏輯層：專注於如何產生 CSV
    execution_date: 由 Airflow 傳入的邏輯時間，確保重跑時結果一致
    """
    rows = 20
    # 使用 Airflow 的時間標記，而不是 datetime.now()
    output_path = f"/opt/airflow/data/{task_name}_{time_str}.csv"

    with open(output_path, mode="w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["id", "score"])
        for i in range(1, rows + 1):
            writer.writerow([i, random.randint(50, 100)])

    print(f"Successfully generated: {output_path}")
    return output_path  