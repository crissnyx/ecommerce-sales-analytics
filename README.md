# Ecommerce Analytics & Churn SaaS

A modern analytics and churn prediction dashboard for e-commerce businesses. This project helps teams identify customers at risk, monitor revenue exposure, and prioritize retention actions based on customer behavior and sales data.

## Overview

Ecommerce Analytics & Churn SaaS combines:
* customer churn risk scoring
* sales and revenue monitoring
* department-level insights
* CSV batch upload workflows
* SaaS-style analytics dashboards

## Features

* Batch CSV ingestion
* Customer churn probability scoring
* Risk segmentation (High / Medium / Low)
* Department-level risk analysis
* KPI dashboard
* Search and filtering by customer ID
* Interactive visualizations with Plotly
* Streamlit-based SaaS interface
* Modular project structure

## Tech Stack

* Python 3.11+
* Streamlit
* Pandas
* Plotly
* scikit-learn
* Docker

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
│   │   ├── predict.py
│   │   └── train.py
│   ├── services/
│   │   ├── churn_service.py
│   │   └── reporting.py
│   └── utils/
│       ├── formatting.py
│       └── validation.py
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
└── run.py