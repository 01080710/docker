import time
import datetime
import random

# 模擬一個會自動檢查並輸出的程式
def my_monitoring_app():
    print(f"[{datetime.datetime.now()}] 🚀 告警監控程式已啟動...", flush=True)

    status_codes = [200, 200, 200, 404, 500, 200] # 模擬不同的執行結果

    while True:
        now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        code = random.choice(status_codes)

        if code == 200:
            # 正常執行時的輸出
            print(f"{now} INFO: 程式執行正常。狀態碼: {code}", flush=True)
        elif code == 404:
            # 警告訊息
            print(f"{now} WARN: 找不到目標資源！狀態碼: {code}", flush=True)
        else:
            # 錯誤訊息 (這是我們之後要過濾的重點)
            print(f"{now} ERROR: 系統發生致命錯誤！請立即檢查程式邏輯。", flush=True)

        # 每 5 秒執行一次
        time.sleep(5)

if __name__ == "__main__":
    my_monitoring_app()