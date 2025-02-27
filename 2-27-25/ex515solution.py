import numpy as np
import matplotlib.pyplot as plt
from math  import tanh, cosh

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import myFuncLib as mfl

## compute the instantaneous derivatives
## using the central difference approximation
## over the interval -2 to 2

x_lower_bound = -2.0
x_upper_bound = 2.0

N_samples = 100

#####################
#
# Try different values of h
# What did we "prove" h should be
# for C = 10^(-16) in Python?
#
#######################
#h = (10**-16)**(1/3) ## what goes here?
h = [2,1,10**-16,((10**-16)**(1/3))]
xdata = np.linspace(x_lower_bound, x_upper_bound, N_samples)

central_diff_values = []
central_diff_values1 = []
central_diff_values2 = []
central_diff_values3 = []
for x in xdata:
    central_difference = ( mfl.f(x + 0.5*h[0]) - mfl.f(x - 0.5*h[0]) ) / h[0]
    central_difference1 = ( mfl.f(x + 0.5*h[1]) - mfl.f(x - 0.5*h[1]) ) / h[1]
    central_difference2 = ( mfl.f(x + 0.5*h[2]) - mfl.f(x - 0.5*h[2]) ) / h[2]
    central_difference3 = ( mfl.f(x + 0.5*h[3]) - mfl.f(x - 0.5*h[3]) ) / h[3]
    central_diff_values.append(central_difference)
    central_diff_values1.append(central_difference1)
    central_diff_values2.append(central_difference2)
    central_diff_values3.append(central_difference3)

## Add the analytical curve
## let's use the same xdata array we already made for our x values

analytical_values = []
for x in xdata:
	dfdx = mfl.df_dx_analytical(x)
	analytical_values.append(dfdx)


plt.plot(xdata, analytical_values, linestyle='-', color='black')
plt.plot(xdata, central_diff_values, "*", color="green", markersize=8, alpha=0.5, label="h=2")
plt.plot(xdata, central_diff_values1, "+", color="red", markersize=8, alpha=0.5, label="h=1")
plt.plot(xdata, central_diff_values2, "x", color="blue", markersize=8, alpha=0.5, label="h=10^-16")
plt.plot(xdata, central_diff_values3, "1", color="purple", markersize=8, alpha=0.5, label="h=(10^-16)^(1/3)")
plt.legend(loc='upper left')
plt.savefig('numerical_vs_analytic_derivatives.png')
plt.close()