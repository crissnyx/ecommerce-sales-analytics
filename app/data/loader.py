"""Data access helpers for CSV loading and validation."""

from __future__ import annotations

from pathlib import Path
from typing import Iterable

import pandas as pd


def load_csv(file_path: str | Path) -> pd.DataFrame:
    """Load a CSV file into a pandas DataFrame."""
    return pd.read_csv(file_path)


def validate_columns(df: pd.DataFrame, required_columns: Iterable[str]) -> None:
    """Raise a clear error when required columns are missing."""
    missing = sorted(set(required_columns) - set(df.columns))
    if missing:
        raise ValueError(f"Missing required columns: {missing}")
