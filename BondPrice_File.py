
import numpy as np

def getBondPrice(y, face, couponRate, m, ppy=1):
    periods = np.arange(1, m + 1)
    coupon_payment = face * couponRate / ppy
    discount_factors = 1 / (1 + y / ppy) ** periods
    bond_price = np.sum(coupon_payment * discount_factors)
    bond_price += face * discount_factors[-1]
    return bond_price