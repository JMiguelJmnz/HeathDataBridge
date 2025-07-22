import pandas as pd
from confluent_kafka import Producer

producer = Producer({'bootstrap.servers': "localhost:9092"})

def delivery_report(err, msg):
    if err is not None:
        print(f"Delivery failed: {err}")
    else:
        print(f"Message sent: {msg.value()}")

df = pd.read_csv('datasets/cms/DE1_0_2008_Beneficiary_Summary_File_Sample_1.csv', dtype=str)

for _, row in df.iterrows():
    message = row.to_json()
    producer.produce('cms-topic', value=message, callback=delivery_report)

producer.flush()