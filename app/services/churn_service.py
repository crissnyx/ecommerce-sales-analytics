"""Service layer for churn analytics tasks."""
<<<<<<< HEAD
from __future__ import annotations
from app.data.loader import validate_columns
from app.data.preprocess import clean_customer_data, create_features

=======

from __future__ import annotations

from app.data.loader import validate_columns
from app.data.preprocess import clean_customer_data, create_features


>>>>>>> origin/feat/project-structure
def build_customer_dataset(raw_df):
    """Validate and normalize raw customer data before prediction."""
    required = {
        "CUSTOMER ID",
        "DEPARTMENT STORE",
        "TOTAL SPEND",
        "PURCHASES",
        "AVG ORDER VALUE",
        "TENURE DAYS",
        "LAST PURCHASE DAYS",
        "RETURNS",
        "CANCELLATIONS",
    }
    validate_columns(raw_df, required)
    cleaned = clean_customer_data(raw_df)
<<<<<<< HEAD
    return create_features(cleaned)
=======
    return create_features(cleaned)
>>>>>>> origin/feat/project-structure
