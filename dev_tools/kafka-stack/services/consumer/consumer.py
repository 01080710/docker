from prometheus_client import start_http_server, Counter, Gauge, Histogram
from kafka import KafkaConsumer
import json


#  1. 額外指標定義 ---> parameter1:metric name / parameter2 : description content / parameter3:dimension column
# LOG_STATUS_COUNTER = Counter('crm_logs_status_total', 'Count of processed logs by status', ['action', 'status']) # 1.1 錯誤監控 (增加 status 標籤，用來監控失敗率)
# TOTAL_VALUE_COUNTER = Counter('crm_total_value_sum', 'Cumulative sum of value', ['action'])                      # 1.2 總金額累加器 (這比 Gauge 更適合統計總營收，因為不會被 set 覆蓋)
# PROCESS_LATENCY = Histogram('crm_process_latency_seconds', 'Time spent processing log', ['action'])              # 1.3 處理耗時 (Histogram 是監控「效能」的神器，幫你抓出哪種動作處理最慢)
LOG_COUNTER = Counter('crm_logs_total', 'Total CRM logs processed', ['regulator','action'])                                  # 1.4 計算累計log value共多少 
LOG_VALUE_GAUGE = Gauge('crm_log_value', 'Last CRM log value', ['regulator','action'])                                       # 1.5 計算當下log value為多少

# 2. 啟動 Prometheus HTTP 服務 (Port: 8050)，讓 Prometheus 定期來這裡「拉」數據
start_http_server(8000)
print("📊 Metrics 網頁已啟動，請查看：http://localhost:8000/metrics")

# 3. 初始化 Kafka Consumer，訂閱 'crm-topic'
consumer = KafkaConsumer(
    'crm-topic',
    bootstrap_servers=['kafka:29092'], # 這裡要改成你在 docker-compose 定義的 service 名稱
    group_id='crm-consumer-group',
    auto_offset_reset='earliest',
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))
)
print(" Consumer 開始監聽...")
for message in consumer:
    log_data = message.value
    # action_type = log_data.get('action', 'unknown')
    value = log_data.get('value', 0) # 拿到這個數值了！
    
    # 統計次數
    LOG_COUNTER.labels(
        regulator=log_data['regulator'],
        action=log_data['action']
        ).inc(value)
    LOG_VALUE_GAUGE.labels(
        regulator=log_data['regulator'],
        action=log_data['action']
        ).set(value)
    
    print(f"📥 收到 Regulator: {log_data['regulator']},收到 Action: {log_data['action']} ,Value: {value}")