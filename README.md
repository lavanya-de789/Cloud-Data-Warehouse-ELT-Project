# Cloud Data Warehouse ETL Pipeline

## Overview

This project demonstrates an end-to-end cloud-based ELT (Extract, Load, Transform) pipeline using Amazon S3, Snowflake, dbt, Airflow, and Python. The platform ingests raw customer data into cloud object storage, loads it into a cloud data warehouse, applies transformations using dbt models, and orchestrates the workflow with Airflow.

The goal is to simulate a production-style Data Engineering architecture where scalable ingestion, transformation, and analytical modeling are performed using modern cloud-native tools.

---

## Architecture

```text
Raw CSV Files
      ↓
Amazon S3
      ↓
Snowflake
      ↓
dbt Models
      ↓
Data Marts
      ↓
Airflow Orchestration
```

---

## Repository Structure

```text
cloud-datawarehouse-etl/

├── docker-compose.yml
├── requirements.txt
├── README.md
│
├── ingestion/
│   └── upload_to_s3.py
│
├── warehouse/
│   └── load_snowflake.py
│
├── dbt/
│   ├── models/
│   │   ├── staging.sql
│   │   └── customer_metrics.sql
│   │
│   └── dbt_project.yml
│
├── airflow/
│   └── dags/
│       └── warehouse_pipeline.py
│
├── data/
│   └── customers.csv
│
└── docs/
    └── architecture.png
```

---

## Tech Stack

- Python
- Amazon S3
- Snowflake
- dbt
- Apache Airflow
- Docker
- Pandas

---

## Features

- Cloud object storage ingestion
- ELT workflow implementation
- Snowflake data warehouse loading
- dbt transformation models
- Automated orchestration using Airflow
- Dimensional analytics layer
- Scalable cloud architecture

---

## Dataset

Sample customer dataset:

```csv
customer_id,name,city,spend

1,John,Dallas,500
2,Edward,Austin,700
3,Sarah,Houston,200
4,Mike,Dallas,800
5,Jennifer,Chicago,900
```

---

## Pipeline Flow

### Step 1: Data Ingestion

Raw customer data is uploaded into Amazon S3.

Example:

```python
s3.upload_file(
'data/customers.csv',
'my-data-bucket',
'customers.csv'
)
```

Purpose:

- Centralized storage
- Decoupled ingestion
- Scalable file management

---

## Step 2: Snowflake Loading

Data is loaded from S3 into Snowflake.

Example:

```sql
COPY INTO customers

FROM @my_stage/customers.csv

FILE_FORMAT=(
TYPE=CSV
SKIP_HEADER=1
)
```

Purpose:

- Cloud warehouse ingestion
- High-performance querying
- Scalable compute and storage

---

## Step 3: dbt Transformations

Staging model:

```sql
select

customer_id,

name,

city,

spend

from customers
```

Business model:

```sql
select

city,

avg(spend) avg_spend,

count(*) total_customers

from {{ref('staging')}}

group by city
```

Purpose:

- Data cleansing
- Business logic implementation
- Data mart creation

---

## Sample Output

|City|Average Spend|Total Customers|
|---|---:|---:|
|Dallas|650|2|
|Austin|700|1|
|Houston|200|1|
|Chicago|900|1|

---

## Airflow DAG Workflow

```text
Upload S3
      ↓
Load Snowflake
      ↓
Run dbt Models
```

Task dependency:

```python
upload>>load>>transform
```

---

## Setup Instructions

### Clone repository

```bash
git clone <repository-url>
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Start services

```bash
docker-compose up -d
```

### Upload data

```bash
python ingestion/upload_to_s3.py
```

### Load into Snowflake

```bash
python warehouse/load_snowflake.py
```

### Run dbt models

```bash
dbt run
```

### Start Airflow

```bash
airflow standalone
```

---

## Future Enhancements

- Incremental dbt models
- CDC integration
- Apache Iceberg support
- Kubernetes deployment
- Great Expectations validation
- CI/CD using GitHub Actions
- Snowflake optimization
- Real-time ingestion with Kafka
- Monitoring with Prometheus and Grafana
