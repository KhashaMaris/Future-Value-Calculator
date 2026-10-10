# Future Value Investment Calculator

A small Python project that compares the projected future value of three investment strategies:

- Regular end-of-year contributions
- An initial lump sum plus end-of-year contributions
- An initial lump sum plus monthly contributions

It prints the final values and displays a chart of each strategy's growth over time.

## Requirements

- Python 3
- NumPy
- Matplotlib

## Setup and run

From the project directory, install the dependencies and run the calculator:

```powershell
py -m pip install -r requirements.txt
py main.py
```

On systems where the Python command is `python` rather than `py`, use:

```shell
python -m pip install -r requirements.txt
python main.py
```

## Customize the example

Edit the assumptions near the top of `main.py`:

```python
initial_lump = 1000
annual_payment = 135
monthly_payment = 135
annual_rate = 0.10
compounding_period_per_year = 12
investment_years = 10
```

The calculator assumes contributions are made at the end of each period. The monthly scenario divides the annual rate by the number of compounding periods per year.

## Project files

- `main.py` sets the example assumptions, calculates and prints results, and prepares the chart.
- `investment_formulas.py` contains the future-value calculation functions.
- `visualisation.py` plots the investment growth scenarios.
- `requirements.txt` lists the Python packages required to run the project.

## Disclaimer

This calculator is for educational purposes only. Its results are simplified projections, not investment advice or a guarantee of future returns.
