import math as m
import numpy as np
from scipy import optimize

coupon = 8
c = coupon / 2

def f0(x):
    return 97.5*m.exp(x*0.25) - 100


zr0 = optimize.newton(f0, 0)
zr0_percentage = f"{zr0:.3%}"
print("zero rate =", zr0_percentage)

def f1(x):
    return 94.9*m.exp(x*0.5) - 100


zr1 = optimize.newton(f1, 0)
zr1_percentage = f"{zr1:.3%}"
print("zero rate =", zr1_percentage)

def f2(x):
    return 90.0*m.exp(x) - 100


zr2 = optimize.newton(f2, 0)
zr2_percentage = f"{zr2:.3%}"
print("zero rate =", zr2_percentage)

def f3(x):
    return 4 * np.exp(-zr1 * 0.5) + 4 * np.exp(-zr2) + 104 * np.exp(-x * 1.5) - 96


zr3 = optimize.newton(f3, 0)
zr3_percentage = f"{zr3:.3%}"
print("zero rate =", zr3_percentage)

def f4(x):
    return 6 * np.exp(-zr1 * 0.5) + 6 * np.exp(-zr2) + 6 * np.exp(-zr3 * 1.5) + 106 * np.exp(-x * 2) - 101.6


zr4 = optimize.newton(f4, 0)
zr4_percentage = f"{zr4:.3%}"
print("zero rate =", zr4_percentage)

# test fields
pay = 100 * (1+zr4)**2
print(pay, "annually compounding")
pay = 100 * m.exp(2*zr4)
print(pay, "continuous compounding")

# Forward rate