from datetime import datetime
import random
import csv
import os


def generate_csv_report(task_name, time_str):
    rows = 20

    # 確保資料夾存在（Docker / 本機都安全）
    output_dir = "/opt/airflow/data"
    os.makedirs(output_dir, exist_ok=True)

    output_path = f"{output_dir}/{task_name}_{time_str}.csv"

    with open(output_path, mode="w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["id", "score"])
        for i in range(1, rows + 1):
            writer.writerow([i, random.randint(50, 100)])

    print(f"Successfully generated: {output_path}")
    return output_path


if __name__ == "__main__":
    today = datetime.now().strftime("%Y%m%d%H%M%S")
    generate_csv_report("test", today)
