from __future__ import annotations
import pandas as pd
from app.data.preprocess import clean_customer_data, create_features
from app.models.pipeline import build_model_pipeline

def predict_churn(model, df: pd.DataFrame) -> pd.DataFrame:
    """Apply the trained model to a dataset and add churn risk columns."""
    df = clean_customer_data(df)
    df = create_features(df)
    
    feature_cols = [
        "TOTAL SPEND",
        "PURCHASES",
        "AVG ORDER VALUE",
        "TENURE DAYS",
        "LAST PURCHASE DAYS",
        "RETURNS",
        "CANCELLATIONS",
        "DEPARTMENT STORE",
    ]
    X = df[feature_cols]
    probabilities = model.predict_proba(X)[:, 1]
    df["CHURN_PROBABILITY"] = probabilities
    df["RISK_LEVEL"] = df["CHURN_PROBABILITY"].apply(
        lambda p: "High Risk" if p >= 0.7 else "Medium Risk" if p >= 0.4 else "Low Risk"
    )
    return df