# Future Value Investment Calculator
This is a Python project that I made to leverage my knowledge in Python and Finance. It calculates and visualise the future vlaue of different investment strategies.

It compares:
- End-of-year recurring contributions
- An initial lump sum plus yearly contributions
- An initial lump sum plus monthly contributions

It was built as a practical exercise in applying finance formulas with Python, orgnising my codes into modules and exploring Matplotlib as this is my first time using it so I had to read alot of documentation and assistance from coding agents

## Features
- Calculates the future value of an ordinary annuity
- Calculates the future value of a lump sum plus recurring payments
- Supports annual and monthly contribution scenarios
- Handles a 0% rate in annuity calculation
- Prints resutls as a currency to two decimal places
- Plots growth over time

## Project structure
future-value-calculator/
├── main.py
├── investment_formulas.py
├── visualisation.py
├── requirements.txt
└── README.md

### File responsibilities
- main.py contains the investment assumptions, runs the entire calculations, prints results and prepares the chart
- investment_formulas.py contains the future-value calculation functions
- visualtion.py containss the Matplotlib chart functions

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

## Skills Demonstrated
- Translating financial formulas into Python
- Writing usable functions
- Organising codes into modules
- Importing functions between files
- Working with Numpy arrays and list comprehensions
- Creating and formatting Matplotlib visualisations
- Input validations and currency formatting

# Possible improvements
Additional features such as accepting user inputs from the command line or a floating text box could improve the userability of the program. 

Adjusting results for inflation would make the growth estimates more accurate. 

Build a graphical or web-based interface

# Disclaimer
This calculator was created for educational purposes. Its results are simplified projections and should not be treated as investment advice or a guarantee of future returns.