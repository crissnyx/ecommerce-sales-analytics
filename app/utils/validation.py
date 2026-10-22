"""Validation helpers for app input flows."""
<<<<<<< HEAD
from __future__ import annotations

=======

from __future__ import annotations


>>>>>>> origin/feat/project-structure
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
<<<<<<< HEAD
    return required.issubset(set(df.columns))
=======
    return required.issubset(set(df.columns))
>>>>>>> origin/feat/project-structure
