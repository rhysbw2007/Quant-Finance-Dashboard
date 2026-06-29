# Quant Finance Dashboard

A compact Streamlit-based dashboard for exploring financial time series, risk metrics, and portfolio performance. It ships with a small sample dataset and utilities for running quick analyses and tests.

## Features

- Interactive charts of price series and returns
- Volatility and risk metric calculations (rolling volatility, drawdowns, etc.)
- Simple, local-first Streamlit app for rapid prototyping
- Test suite for core metric functions


## Run (explicit steps)

These exact commands have been tested on macOS / Linux. Run them from the workspace root (the folder that contains `quant_finance_dashboard`).

1. Change into the project folder

```bash
cd quant_finance_dashboard
```

2a. If the project already has a virtualenv, activate it (recommended)

```bash
source .venv/bin/activate
```

2b. If you don't have a virtualenv yet, create and activate one

```bash
python3 -m venv .venv
source .venv/bin/activate
```

3. Install project dependencies

```bash
pip install -r requirements.txt
```

4. Run the Streamlit app

```bash
streamlit run app.py
```

Notes and alternatives

- If you prefer not to activate the virtualenv, run Streamlit using the venv binary explicitly:

```bash
.venv/bin/streamlit run app.py
```

- If you see `ModuleNotFoundError: No module named 'streamlit'` or similar, ensure you installed the requirements into the correct virtualenv (`.venv/bin/python3 -m pip install -r requirements.txt`).
- If `streamlit` is already installed but the command isn't found after activation, try the explicit binary above.
- The app reads its sample data from the `data/prices.csv` file. If you add your own CSV files, keep the date column named `date` and price column named `close`, and include a `ticker` column.

Open the URL printed by Streamlit (usually http://localhost:8501) to view the dashboard.

## Data

Place CSV time-series data in the `data/` folder. The included sample is `data/prices.csv` and expects a date column plus one or more price series. The app reads CSV files using pandas; adapt column names as needed in `app.py`.

## Tests

Run the unit tests with pytest:

```bash
pytest -q
```

The test suite lives in the `tests/` folder and covers metric calculations used by the dashboard.

## Project structure

- `app.py` — Streamlit dashboard entry point
- `requirements.txt` — Python dependencies
- `data/` — example datasets (e.g., `prices.csv`)
- `tests/` — pytest tests for core functions

## Development notes

- Use the virtual environment to keep dependencies isolated.
- To add new metrics, implement functions in a module and add tests under `tests/
