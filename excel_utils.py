"""Helper utilities for reading and preparing Excel data for the Streamlit UI."""

from __future__ import annotations

from io import BytesIO
from pathlib import Path
from typing import Union

import pandas as pd

ExcelSource = Union[str, Path, bytes, bytearray, BytesIO]


def _normalize_source(source: ExcelSource):
    """Return a pandas-compatible source object."""
    if isinstance(source, (bytes, bytearray)):
        return BytesIO(source)
    return source


def list_sheet_names(source: ExcelSource) -> list[str]:
    """List worksheet names from an Excel workbook."""
    workbook = pd.ExcelFile(_normalize_source(source), engine="openpyxl")
    return workbook.sheet_names


def load_worksheet(source: ExcelSource, sheet_name: str | int = 0) -> pd.DataFrame:
    """Load a worksheet as a raw DataFrame without applying headers."""
    return pd.read_excel(
        _normalize_source(source),
        sheet_name=sheet_name,
        header=None,
        engine="openpyxl",
        dtype=object,
    )


def get_preview(df: pd.DataFrame, max_rows: int = 20) -> pd.DataFrame:
    """Return a small preview dataframe for UI display."""
    return df.head(max_rows).copy()
