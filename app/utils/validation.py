"""Validation helpers for app input flows."""
from __future__ import annotations

def is_valid_churn_dataset(df) -> bool:
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
    return required.issubset(set(df.columns))