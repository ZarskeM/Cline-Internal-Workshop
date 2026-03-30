"""Streamlit UI for the Excel raw data cleaner workshop starter app."""

import streamlit as st

from excel_utils import get_preview, list_sheet_names, load_worksheet


st.set_page_config(page_title="Excel Raw Data Cleaner Demo", layout="wide")

st.title("Excel Raw Data Cleaner Demo")
st.write(
    "Upload a messy `.xlsx` file and inspect the raw worksheet preview. "
    "This starter app is intentionally small for workshop extensions."
)

uploaded_file = st.file_uploader("Upload an Excel file (.xlsx)", type=["xlsx"])

if uploaded_file is None:
    st.info("Upload a workbook to begin.")
    st.stop()

file_bytes = uploaded_file.getvalue()

try:
    sheet_names = list_sheet_names(file_bytes)
except Exception as exc:  # pragma: no cover - streamlit display path
    st.error(f"Could not read the workbook: {exc}")
    st.stop()

if not sheet_names:
    st.warning("No worksheets were found in this workbook.")
    st.stop()

if len(sheet_names) > 1:
    selected_sheet = st.selectbox("Worksheet", sheet_names)
else:
    selected_sheet = sheet_names[0]
    st.caption(f"Worksheet: **{selected_sheet}**")

try:
    raw_df = load_worksheet(file_bytes, selected_sheet)
except Exception as exc:  # pragma: no cover - streamlit display path
    st.error(f"Could not load worksheet '{selected_sheet}': {exc}")
    st.stop()

if raw_df.empty:
    st.warning("The selected worksheet is empty.")
    st.stop()

st.subheader("Raw worksheet preview")
st.caption(
    "This is the worksheet exactly as loaded (no header-row correction yet)."
)
st.dataframe(get_preview(raw_df, max_rows=25), width="stretch")

rows, cols = raw_df.shape
left_col, right_col = st.columns(2)
left_col.metric("Rows", rows)
right_col.metric("Columns", cols)

st.caption(
    "Workshop starter scope only: Task 1 introduces header-row selection and header application."
)
