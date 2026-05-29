import json
import time
import random
from kafka import KafkaProducer

# 初始化 Producer
producer = KafkaProducer(
    bootstrap_servers=['localhost:9092'],
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

# 模擬 CRM 可能發生的幾種業務行為
actions = ["lead_created", "status_updated", "email_sent", "meeting_booked"]
regulators = ["FCA","ASIC","VFSC1","VFSC2"]

print("🚀 模擬 CRM 業務行為 API 已啟動...")

while True:
    # 模擬隨機產生的業務數據
    
    log_record = {
        "event_id": f"evt_{random.randint(10000, 99999)}",
        "regulator":random.choices(regulators),
        "action": random.choice(actions),  # 隨機抽取行為
        "value": random.randint(1, 100),   # 隨機產生業務數值 (例如成交金額)
        "timestamp": time.time()
    }
    
    # 發送至 Kafka
    producer.send('crm-topic', value=log_record)
    print(f"📦 發送業務數據: {log_record['action']} (Val: {log_record['value']})")
    
    # 模擬不規則的進線頻率 (5 ~ 10 秒隨機間隔)
    time.sleep(random.uniform(2.1, 2.2))