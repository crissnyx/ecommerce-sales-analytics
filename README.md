# Ecommerce Analytics & Churn SaaS

A modern analytics and churn prediction dashboard for e-commerce businesses. This project helps teams identify customers at risk, monitor revenue exposure, and prioritize retention actions based on customer behavior and sales data.

## Overview

Ecommerce Analytics & Churn SaaS combines:
- customer churn risk scoring
- sales and revenue monitoring
- department-level insights
- CSV batch upload workflows
- SaaS-style analytics dashboards

## Features

- Batch CSV ingestion
- Customer churn probability scoring
- Risk segmentation (High / Medium / Low)
- Department-level risk analysis
- KPI dashboard
- Search and filtering by customer ID
- Interactive visualizations with Plotly
- Streamlit-based SaaS interface
- Modular project structure

## Tech Stack

- Python 3.11+
- Streamlit
- Pandas
- Plotly
- scikit-learn
- Docker

## Project Structure

```text
ecommerce-sales-analytics/
├── app/
│   ├── __init__.py
│   ├── config.py
│   ├── main.py
│   ├── data/
│   │   ├── __init__.py
│   │   ├── loader.py
│   │   ├── preprocess.py
│   │   └── schema.py
│   ├── models/
│   │   ├── __init__.py
│   │   ├── pipeline.py
│   │   ├── train.py
│   │   └── predict.py
│   ├── services/
│   │   ├── churn_service.py
│   │   └── reporting.py
│   └── utils/
│       ├── validation.py
│       └── formatting.py
├── data/
│   ├── raw/
│   ├── processed/
│   └── models/
├── tests/
│   ├── test_loader.py
│   └── test_preprocess.py
├── .env.example
├── Dockerfile
├── requirements.txt
├── README.md
├── run.py
└── .gitignore
```

## Quick Start

### 1) Clone

```bash
git clone https://github.com/crissnyx/ecommerce-sales-analytics.git
cd ecommerce-sales-analytics
```

### 2) Create and activate a virtual environment

```bash
python -m venv .venv
source .venv/bin/activate
```

Windows:

```bash
python -m venv .venv
.venv\Scripts\activate
```

### 3) Install dependencies

```bash
pip install -r requirements.txt
```

### 4) Run the app

```bash
streamlit run app/main.py
```

or:

```bash
python run.py
```

## Expected CSV Format

The app expects a CSV file with the following columns:

```csv
CUSTOMER ID,DEPARTMENT STORE,TOTAL SPEND,PURCHASES,AVG ORDER VALUE,TENURE DAYS,LAST PURCHASE DAYS,RETURNS,CANCELLATIONS
```

## Model Workflow

1. Load customer data from CSV
2. Validate required columns
3. Clean and normalize data
4. Build churn features
5. Train a risk model
6. Predict churn probability
7. Display results in the dashboard

## Roadmap

- [x] dashboard foundation
- [x] CSV upload flow
- [x] KPI and visualizations
- [x] modular project structure
- [ ] production data validation
- [ ] persistent storage
- [ ] authentication
- [ ] CI/CD and automated tests

## License

This project is licensed under the MIT License.
