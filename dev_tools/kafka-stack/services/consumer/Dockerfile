# 使用輕量級 Python 環境
FROM python:3.9-slim

# 設定工作目錄
WORKDIR /app

# 複製依賴檔並安裝
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 複製你的 Consumer 程式碼
COPY consumer.py .

# 暴露 Prometheus 監控用的 Port
EXPOSE 8000

# 執行程式
CMD ["python", "consumer.py"]