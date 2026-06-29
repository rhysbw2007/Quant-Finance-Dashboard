# Quant-Finance-Dashboard

A compact Streamlit-based dashboard for exploring financial time series, risk metrics, and portfolio performance. It ships with a small sample dataset and utilities for running quick analyses and tests.

## Features

- Interactive charts of price series and returns
- Volatility and risk metric calculations (rolling volatility, drawdowns, etc.)
- Simple, local-first Streamlit app for rapid prototyping
- Test suite for core metric functions

## Quickstart (local)

Prerequisites: Python 3.10+ recommended.

1. Create and activate a virtual environment

```bash
python3 -m venv .venv
source .venv/bin/activate
```

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Run the dashboard

```bash
streamlit run app.py
```

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
- To add new metrics, implement functions in a module and add tests under `tests/`.
