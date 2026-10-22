<<<<<<< HEAD
from __future__ import annotations
=======
"""Machine learning pipeline definition for churn prediction."""

from __future__ import annotations

>>>>>>> origin/feat/project-structure
from sklearn.compose import ColumnTransformer
from sklearn.ensemble import RandomForestClassifier
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder

<<<<<<< HEAD
def build_model_pipeline(X):
    """Create a preprocessing & model pipeline."""
    categorical_cols = X.select_dtypes(include=["object"]).columns.tolist()
    numeric_cols = X.select_dtypes(exclude=["object"]).columns.tolist()
    
=======

def build_model_pipeline(X):
    """Create a preprocessing + model pipeline."""
    categorical_cols = X.select_dtypes(include=["object"]).columns.tolist()
    numeric_cols = X.select_dtypes(exclude=["object"]).columns.tolist()

>>>>>>> origin/feat/project-structure
    preprocessor = ColumnTransformer(
        transformers=[
            (
                "num",
                Pipeline([("imputer", SimpleImputer(strategy="median"))]),
                numeric_cols,
            ),
            (
                "cat",
                Pipeline(
                    [
                        ("imputer", SimpleImputer(strategy="most_frequent")),
                        ("encoder", OneHotEncoder(handle_unknown="ignore")),
                    ]
                ),
                categorical_cols,
            ),
        ]
    )
<<<<<<< HEAD
    
=======

>>>>>>> origin/feat/project-structure
    model = Pipeline(
        steps=[
            ("preprocessor", preprocessor),
            (
                "classifier",
                RandomForestClassifier(
                    n_estimators=200,
                    random_state=42,
                    class_weight="balanced",
                ),
            ),
        ]
    )
<<<<<<< HEAD
    return model
=======

    return model
>>>>>>> origin/feat/project-structure
