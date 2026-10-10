import numpy as np

from investment_formulas import fv_annuity, fv_lumpsum, fv_monthly
from visualisation import show_chart

def main():
    initial_lump = 1000
    annual_payment = 135
    monthly_payment = 135
    annual_rate = 0.10
    compounding_period_per_year = 12
    investment_years = 10
    
    recurring_only = fv_annuity(annual_payment,annual_rate,investment_years)
    recurring_lump = fv_lumpsum(initial_lump, annual_payment, annual_rate, investment_years)
    recurring_monthly = fv_monthly(initial_lump, monthly_payment, annual_rate, compounding_period_per_year, investment_years)

    print("Yearly contributions only:", f"${recurring_only:,.2f}")
    print("Initial lump sum + yearly contributions:", f"${recurring_lump:,.2f}")
    print("Initial lump sum + monthly contributions:", f"${recurring_monthly:,.2f}")

    years = np.arange(0, investment_years + 1)
    recurring_values = [fv_annuity(annual_payment,annual_rate,year) for year in years]
    lumpsum_values = [fv_lumpsum(initial_lump,annual_payment,annual_rate,year) for year in years]
    monthly_values = [fv_monthly(initial_lump,monthly_payment,annual_rate,compounding_period_per_year,year) for year in years]

    show_chart(years,recurring_values,lumpsum_values,monthly_values)

if __name__ == "__main__":
    main()