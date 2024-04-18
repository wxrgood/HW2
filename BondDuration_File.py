import numpy as np

def getBondDuration(y, face, couponRate, m, ppy=1):
    periods = np.arange(1, m + 1)
    coupon_payment = face * couponRate / ppy
    discount_factors = (1 + y / ppy) ** periods
    present_values = coupon_payment / discount_factors
    present_values[-1] += face / discount_factors[-1] 
    bond_price = np.sum(present_values)
    duration = np.sum(periods * present_values) / bond_price
    return duration
