"""Data normalization and feature creation for churn analysis."""
<<<<<<< HEAD
from __future__ import annotations
import pandas as pd

=======

from __future__ import annotations

import pandas as pd


>>>>>>> origin/feat/project-structure
def normalize_columns(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df.columns = [str(col).strip().upper() for col in df.columns]
    return df

<<<<<<< HEAD
=======

>>>>>>> origin/feat/project-structure
def clean_customer_data(df: pd.DataFrame) -> pd.DataFrame:
    """Apply basic cleaning to raw customer data."""
    df = normalize_columns(df)
    df = df.drop_duplicates()
    df = df.replace({None: pd.NA})
<<<<<<< HEAD
    
=======

>>>>>>> origin/feat/project-structure
    numeric_cols = [
        "TOTAL SPEND",
        "PURCHASES",
        "AVG ORDER VALUE",
        "TENURE DAYS",
        "LAST PURCHASE DAYS",
        "RETURNS",
        "CANCELLATIONS",
    ]
<<<<<<< HEAD
    for col in numeric_cols:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors="coerce")
            
    numeric_columns = df.select_dtypes(include=["number"]).columns
    df[numeric_columns] = df[numeric_columns].fillna(0)
    return df

=======

    for col in numeric_cols:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors="coerce")

    numeric_columns = df.select_dtypes(include=["number"]).columns
    df[numeric_columns] = df[numeric_columns].fillna(0)

    return df


>>>>>>> origin/feat/project-structure
def classify_risk(score: float) -> str:
    if score >= 70:
        return "High Risk"
    if score >= 40:
        return "Medium Risk"
    return "Low Risk"

<<<<<<< HEAD
def create_features(df: pd.DataFrame) -> pd.DataFrame:
    """Build churn-related features for scoring."""
    df = df.copy()
=======

def create_features(df: pd.DataFrame) -> pd.DataFrame:
    """Build churn-related features for scoring."""
    df = df.copy()

    spend = df.get("TOTAL SPEND", 0)
    purchases = df.get("PURCHASES", 0)
    avg_order = df.get("AVG ORDER VALUE", 0)
>>>>>>> origin/feat/project-structure
    tenure = df.get("TENURE DAYS", 0)
    recency = df.get("LAST PURCHASE DAYS", 0)
    returns = df.get("RETURNS", 0)
    cancellations = df.get("CANCELLATIONS", 0)
<<<<<<< HEAD
    purchases = df.get("PURCHASES", 0)
    
=======

>>>>>>> origin/feat/project-structure
    df["CHURN_SCORE"] = (
        (recency / 30) * 0.35
        + (1 / (tenure + 1)) * 100 * 0.20
        + (returns * 1.5) * 0.15
        + (cancellations * 2.0) * 0.30
        + (0 if purchases else 10)
    )
<<<<<<< HEAD
    df["RISK_LEVEL"] = df["CHURN_SCORE"].apply(classify_risk)
    return df
=======

    df["RISK_LEVEL"] = df["CHURN_SCORE"].apply(classify_risk)
    return df
>>>>>>> origin/feat/project-structure
