# Excel Raw Data Cleaner Demo

A small Streamlit workshop starter app for cleaning messy Excel raw data.

This initial version keeps the scope intentionally simple:

- upload an `.xlsx` file
- choose a worksheet (if multiple sheets are present)
- preview the raw table as loaded
- view basic summary information (row count, column count, column names)

> Note: Header-row handling is intentionally **not** implemented in this baseline. It is the first workshop extension task.

The repository is designed for workshop participants to extend with Cline in later tasks.

It includes the workshop dataset and background material:

- `sample_data/Tab.S1_Sample_overview.xlsx` (supplemental Excel table used for cleaning tasks)
- `sample_data/s12864-024-10014-w.pdf` (paper context)

## Setup

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Run the app

```bash
cd excel-raw-data-cleaner-demo
streamlit run app.py
```

## Run tests

```bash
cd excel-raw-data-cleaner-demo
pytest
```

## Workshop context

This is an educational demo repository. Participants will gradually add new cleaning features during exercises, guided by `TASKS.md`.
