from confluent_kafka import Producer

conf = {
    'bootstrap.servers': 'localhost:9092'
}

producer = Producer(conf)

def delivery_report(err, msg):
    if err is not None:
        print(f"Delivery failed: {err}")
    else:
        print(f"Message delivered to {msg.topic()}" [{msg.partition()}""])

topic = "test-topic"
producer.produce(topic, key="key", value="Hello from Miguel!", callback=delivery_report)
producer.flush()