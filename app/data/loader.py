"""Data access helpers for CSV loading and validation."""
<<<<<<< HEAD
from __future__ import annotations
from pathlib import Path
from typing import Iterable
import pandas as pd

=======

from __future__ import annotations

from pathlib import Path
from typing import Iterable

import pandas as pd


>>>>>>> origin/feat/project-structure
def load_csv(file_path: str | Path) -> pd.DataFrame:
    """Load a CSV file into a pandas DataFrame."""
    return pd.read_csv(file_path)

<<<<<<< HEAD
=======

>>>>>>> origin/feat/project-structure
def validate_columns(df: pd.DataFrame, required_columns: Iterable[str]) -> None:
    """Raise a clear error when required columns are missing."""
    missing = sorted(set(required_columns) - set(df.columns))
    if missing:
<<<<<<< HEAD
        raise ValueError(f"Missing required columns: {missing}")
=======
        raise ValueError(f"Missing required columns: {missing}")
>>>>>>> origin/feat/project-structure
