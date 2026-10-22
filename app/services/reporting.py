"""Reporting utilities for dashboards."""
<<<<<<< HEAD
from __future__ import annotations
import pandas as pd

=======

from __future__ import annotations

import pandas as pd


>>>>>>> origin/feat/project-structure
def summarize_risk(df: pd.DataFrame) -> dict:
    counts = df["RISK_LEVEL"].value_counts().to_dict()
    return {
        "High Risk": counts.get("High Risk", 0),
        "Medium Risk": counts.get("Medium Risk", 0),
        "Low Risk": counts.get("Low Risk", 0),
<<<<<<< HEAD
    }
=======
    }
>>>>>>> origin/feat/project-structure
