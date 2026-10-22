from __future__ import annotations
<<<<<<< HEAD
import pandas as pd
from app.data.preprocess import clean_customer_data, create_features
from app.models.pipeline import build_model_pipeline

=======

import pandas as pd

from app.data.preprocess import clean_customer_data, create_features
from app.models.pipeline import build_model_pipeline


>>>>>>> origin/feat/project-structure
def predict_churn(model, df: pd.DataFrame) -> pd.DataFrame:
    """Apply the trained model to a dataset and add churn risk columns."""
    df = clean_customer_data(df)
    df = create_features(df)
<<<<<<< HEAD
    
=======

>>>>>>> origin/feat/project-structure
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
<<<<<<< HEAD
    X = df[feature_cols]
    probabilities = model.predict_proba(X)[:, 1]
    df["CHURN_PROBABILITY"] = probabilities
    df["RISK_LEVEL"] = df["CHURN_PROBABILITY"].apply(
        lambda p: "High Risk" if p >= 0.7 else "Medium Risk" if p >= 0.4 else "Low Risk"
    )
    return df
=======

    X = df[feature_cols]
    probabilities = model.predict_proba(X)[:, 1]
    df["CHURN_PROBABILITY"] = probabilities

    df["RISK_LEVEL"] = df["CHURN_PROBABILITY"].apply(
        lambda p: "High Risk" if p >= 0.7 else "Medium Risk" if p >= 0.4 else "Low Risk"
    )

    return df
>>>>>>> origin/feat/project-structure
