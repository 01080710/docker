from confluent_kafka import Producer, Consumer
import threading ,time ,json ,random
from datetime import datetime



BOOTSTRAP_SERVERS = "localhost:9092"
TOPIC = "api.health.raw"
GROUP_ID = "api-monitor-group"

running = True

def producer_loop():
    producer = Producer({
        "bootstrap.servers": BOOTSTRAP_SERVERS
    })

    i = 0
    while running:
        message = {
            "source": "python-api-poller",
            "status": "OK",
            "status_code": 200,
            "latency_ms": random.randint(80, 500),
            "sequence": i,
            "created_at": datetime.now().isoformat()
        }

        producer.produce(
            TOPIC,
            key="python-api-poller",
            value=json.dumps(message).encode("utf-8")
        )

        producer.flush()

        print(f"[PRODUCER] sent: {message}")

        i += 1
        time.sleep(1)


def consumer_loop():
    consumer = Consumer({
        "bootstrap.servers": BOOTSTRAP_SERVERS,
        "group.id": GROUP_ID,
        "auto.offset.reset": "earliest",
        "enable.auto.commit": False
    })

    consumer.subscribe([TOPIC])
    print(f"[CONSUMER] listening topic={TOPIC}, group.id={GROUP_ID}")

    while running:
        msg = consumer.poll(1.0)

        if msg is None:
            continue
        if msg.error():
            print(f"[CONSUMER] error: {msg.error()}")
            continue

        data = json.loads(msg.value().decode("utf-8"))
        print(f"[CONSUMER] received: {data}")
        consumer.commit(msg)

    consumer.close()


if __name__ == "__main__":
    producer_thread = threading.Thread(target=producer_loop)
    consumer_thread = threading.Thread(target=consumer_loop)

    producer_thread.start()
    consumer_thread.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        running = False
        print("\nstop testing...")