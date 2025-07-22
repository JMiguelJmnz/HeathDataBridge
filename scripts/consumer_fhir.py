from confluent_kafka import Consumer
import json
from scripts.beneficiary_mapper import map_row_to_patient
from scripts.validator import validate_resource
from scripts.writer import write_resource
import pandas as pd

consumer = Consumer({
    'bootstrap.servers': 'localhost:9092',
    'group.id': 'fhir-pipeline',
    'auto.offset.reset': 'earliest'
})

consumer.subscribe(['cms-topic'])

print("Waiting for CSV messages...")

while True:
    msg = consumer.poll(1.0)
    if msg is None:
        continue
    if msg.error():
        print(f"Consumer error: {msg.error()}")
        continue

    row_dict = json.loads(msg.value())
    row_series = pd.Series(row_dict)

    patient = map_row_to_patient(row_series)
    is_valid, error = validate_resource(patient)
    if is_valid:
        filename = f"output/fhir/patient_{patient.id}.json"
        write_resource(patient, filename)
        print(f"✅ Wrote: {filename}")
    else:
        print(f"❌ Validation error for patient {patient.id}: {error}")

consumer.close()