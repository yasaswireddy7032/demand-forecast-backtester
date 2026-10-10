# Demand Forecast Backtester

[![Tests](https://github.com/yasaswireddy7032/demand-forecast-backtester/actions/workflows/tests.yml/badge.svg)](https://github.com/yasaswireddy7032/demand-forecast-backtester/actions)

Expanding-window time-series evaluation comparing a ridge forecaster with a seasonal-naive baseline.

**Status:** runnable portfolio reference implementation. Uses synthetic or hand-authored demonstration data. No employer code, customer data, or production performance claims.

## Run

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python app.py
python -m unittest -v
```

The default command prints a reproducible JSON demonstration. See `app.py` for the reusable Python API. `example-output.json` records the locally executed demo; it is not an external benchmark.

## Architecture

Synthetic daily series → past-only lag features → expanding-window refits → one-step predictions → comparison with a seven-day seasonal baseline.

## Validation

Tests exercise failure cases and behavioral invariants, in addition to the executable demo. GitHub Actions runs the tests and demo on pushes and pull requests. See the Actions tab for current results.

## Limitations and next steps

Only one-step univariate forecasting with synthetic weekly seasonality. No promotion signals, hierarchy, prediction intervals, or multi-step planning. Extend with rolling-origin horizon evaluation and real demand data; report when the baseline wins.

## Container

```bash
docker build -t demand-forecast-backtester .
docker run --rm demand-forecast-backtester
```

The Docker recipe is provided; local validation uses Python, not Docker.

## Responsible use

Review the code and understand its assumptions before deploying. Keep credentials in environment variables and exclude private data from commits. This project is an educational engineering baseline, not a production-certified service.
