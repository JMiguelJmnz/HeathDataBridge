🏥 HealthDataBridge: Healthcare ETL Pipeline to FHIR
📌 Project Overview
HealthDataBridge is an ETL pipeline that ingests structured healthcare datasets (e.g., CMS beneficiaries), transforms them into standardized FHIR resources, and streams them via Kafka for downstream processing.

This project demonstrates how to bridge legacy healthcare formats with modern interoperability standards like HL7 FHIR R4, leveraging streaming technologies for scalable, fault-tolerant pipelines.

🛠️ Tech Stack
Python

Pandas

FHIR.resources (FHIR R4 Models)

Confluent Kafka (via Docker Compose)

Docker Desktop (Zookeeper & Kafka Broker)

📂 Project Structure
```
HealthDataBridge/
├── output/fhir/           # FHIR-compliant JSON output<br>
├── scripts/<br>
│   ├── beneficiary_mapper.py    # Maps CSV data to FHIR Patient
│   ├── consumer_fhir.py         # Kafka consumer: JSON to FHIR output
│   ├── producer_csv.py          # CSV producer: sends to Kafka
│   ├── validator.py             # Validates FHIR resources
│   └── writer.py                # Handles FHIR JSON output
├── docker/docker-compose.yml    # Zookeeper & Kafka services
├── requirements.txt
└── README.md
```

🔄 Pipeline Flow

[CSV Files (CMS Beneficiaries)]
         │
         ▼
 [Kafka Producer] 
   └─ Read rows
   └─ Convert to JSON
   └─ Send to Kafka topic
         │
         ▼
    [Kafka Topic]
         │
         ▼
 [Kafka Consumer]
   └─ Convert JSON to FHIR Patient
   └─ Validate resource
   └─ Write FHIR JSON output


🚀 Running the Project

1️⃣ Start Kafka + Zookeeper (via Docker)
<pre>```
cd docker
docker-compose up -d
```<pre>
2️⃣ Run Kafka Consumer
# From project root, with virtualenv activated
<pre>```python -m scripts.consumer_fhir```<pre>
3️⃣ Run Kafka Producer (sends CSV data)
<pre>```
python -m scripts.producer_csv
```<pre>
4️⃣ Output:
FHIR-compliant JSON files written to:
<pre>```
/output/fhir/patient_<id>.json
```<pre>


✅ Features
Decoupled ETL pipeline via Kafka

Structured output as valid FHIR Patient R4 JSON

Extensible for additional datasets (inpatient, outpatient)

Validation layer for schema compliance

📈 Future Improvements (Planned):
Integrate additional healthcare datasets (e.g., HL7 v2, CDA)

Connect output to Neo4j Knowledge Graph

Integrate with LLMs for enrichment/analysis

Orchestrate with Airflow / Dagster
