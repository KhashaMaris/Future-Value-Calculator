def fv_annuity(p,r,n):
    """Future value of end-of-period contributions"""
    if n < 0:
        raise ValueError("Number of periods cannot be negative")
    if r == 0:
        return p * n
    
    interest = (((1+r) ** n) - 1) / r
    fv = p*interest
    return fv

def fv_lumpsum(lump,p,r,n):
    """Future value of a lump-sum plus end-of-period contributions"""
    lumpsum = lump * (1 + r) ** n
    contribution_value = fv_annuity(p,r,n)
    
    return lumpsum + contribution_value

def fv_monthly(lump,monthly_payment,annual_rate,periods_per_year,years):
    """Future value with monthly compounding and contributions"""
    if periods_per_year <= 0:
        raise ValueError("compounding periods must be greater than zero")
    
    monthly_rate = annual_rate/periods_per_year
    number_of_periods = periods_per_year * years
    
    return fv_lumpsum(lump,monthly_payment,monthly_rate,number_of_periods)
    
   