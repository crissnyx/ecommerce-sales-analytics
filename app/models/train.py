from __future__ import annotations
<<<<<<< HEAD
from pathlib import Path
import joblib
import pandas as pd
from sklearn.model_selection import train_test_split
=======

from pathlib import Path

import joblib
import pandas as pd
from sklearn.model_selection import train_test_split

>>>>>>> origin/feat/project-structure
from app.config import MODELS_DIR
from app.data.preprocess import clean_customer_data, create_features
from app.models.pipeline import build_model_pipeline

<<<<<<< HEAD
def prepare_training_data(df: pd.DataFrame) -> tuple[pd.DataFrame, pd.Series]:
    df = clean_customer_data(df)
    df = create_features(df)
    if "CHURN_LABEL" not in df.columns:
        df["CHURN_LABEL"] = (df["CHURN_SCORE"] >= 70).astype(int)
    
=======

def prepare_training_data(df: pd.DataFrame) -> tuple[pd.DataFrame, pd.Series]:
    df = clean_customer_data(df)
    df = create_features(df)

    if "CHURN_LABEL" not in df.columns:
        df["CHURN_LABEL"] = (df["CHURN_SCORE"] >= 70).astype(int)

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
=======

>>>>>>> origin/feat/project-structure
    X = df[feature_cols]
    y = df["CHURN_LABEL"]
    return X, y

<<<<<<< HEAD
def train_churn_model(df: pd.DataFrame, model_path: str | Path | None = None):
    """Train a churn classification model and save it to disk."""
    X, y = prepare_training_data(df)
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )
    model = build_model_pipeline(X_train)
    model.fit(X_train, y_train)
    
    if model_path is None:
        MODELS_DIR.mkdir(parents=True, exist_ok=True)
        model_path = MODELS_DIR / "churn_model.pkl"
    joblib.dump(model, model_path)
    return model
=======

def train_churn_model(df: pd.DataFrame, model_path: str | Path | None = None):
    """Train a churn classification model and save it to disk."""
    X, y = prepare_training_data(df)

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )

    model = build_model_pipeline(X_train)
    model.fit(X_train, y_train)

    if model_path is None:
        MODELS_DIR.mkdir(parents=True, exist_ok=True)
        model_path = MODELS_DIR / "churn_model.pkl"

    joblib.dump(model, model_path)
    return model
>>>>>>> origin/feat/project-structure
