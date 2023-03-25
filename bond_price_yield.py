import math as m
import numpy as np
from scipy import optimize

for cupon in range(1, 11):
    c = 0.5*cupon
    bprice = c * m.exp(-0.05 * 0.5) + c * m.exp(-0.058) + c * m.exp(-0.064 * 1.5) + (100 + c) * m.exp(-0.068 * 2)
    def f(x):
        return c * np.exp(-x*0.5) + c*np.exp(-x) + c*np.exp(-x*1.5) + (100 + c)*np.exp(-2*x) - bprice
    byield = optimize.newton(f, 0.1)
    byield_percentage = f"{byield:.3%}"
    print("cupon = ", cupon, end="\t\t" )
    print("bond price =", bprice, end="\t\t")
    print("bond yield =", byield_percentage)