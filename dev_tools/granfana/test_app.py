import json
import time
import datetime
import random

# 模擬的監控服務設定
REGULATORS = ["ASIC", "VFSC"]
STAGES = ["authentication", "regulator_switching", "data_collection"]
SERVICE_NAME = "CrmMonitoring"
LOGGER_NAME = "CrmMonitoring.AccTransAudit"

# 模擬交易摘要生成
def generate_summary():
    categories = [
        "Trade—Trade", "Trade—Rebate", "Rebate—Trade", "Rebate—Rebate",
        "Rebate—Trade(IB Transfer)", "Rebate—Rebate(IB Transfer)",
        "Trade—Wallet", "Wallet—Trade", "CPA Rebate—Trade"
    ]
    summary = {}
    for cat in categories:
        summary[cat] = {
            "Submitted": random.randint(0, 50),
            "Completed": random.randint(0, 2000),
            "Rejected": random.randint(0, 10),
            "Fail": random.randint(0, 5),
            "Processing": random.randint(0, 5),
            "Reversed": random.randint(0, 5),
            "Audit": random.randint(0, 5),
            "Risk Audit": random.randint(0, 5)
        }
    return summary

def log_event(level, stage, message, regulator, summary=None):
    log_entry = {
        "timestamp": datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S%z"),
        "level": level,
        "service": SERVICE_NAME,
        "logger": LOGGER_NAME,
        "stage": stage,
        "status": "ok",
        "message": message,
        "regulator": regulator
    }
    if summary:
        log_entry["summary"] = summary
    # print(json.dumps(log_entry), flush=True)
    # 改成
    import sys
    sys.stdout.write(json.dumps(log_entry) + "\n")
    sys.stdout.flush()

def crm_monitoring_simulator():
    while True:
        for regulator in REGULATORS:
            # Authentication
            log_event("INFO", "authentication", f"Starting authentication: {regulator}", regulator)
            time.sleep(0.5)
            log_event("INFO", "authentication", f"Success authentication: {regulator}", regulator)
            time.sleep(0.5)

            # Regulator switching
            log_event("INFO", "regulator_switching", f"Starting Switching: {regulator}", regulator)
            time.sleep(0.5)
            log_event("INFO", "regulator_switching", f"Successful switching: {regulator}", regulator)
            time.sleep(0.5)

            # Data collection
            log_event("INFO", "data_collection", f"Starting Data Collection: {regulator}", regulator)
            time.sleep(0.5)
            summary = generate_summary()
            log_event("INFO", "data_collection", f"Success Data collection: {regulator}", regulator, summary)
            time.sleep(0.5)

if __name__ == "__main__":
    crm_monitoring_simulator()