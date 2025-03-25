import numpy as np
import matplotlib.pyplot as plt

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import myFuncLib as mfl

def differential_eq(x, t):
    expression = x**2-x
    return expression

# Initial conditions
x0 = 0.5
t0 = 0
t_end = 10.0
dt = 0.0001 ## try two other step sizes

# Solve using Euler method
t_values, x_values = mfl.euler_method(differential_eq, x0, t0, t_end, dt)

# Plotting the solution
plt.figure(figsize=(8, 5))
plt.plot(t_values, x_values, label="Euler Approximation", color="b")
plt.xlabel("t")
plt.ylabel("x(t)")
plt.title(r"Euler Method Solution for dx/dt = $x^2-x$")
plt.grid(True)
plt.legend()
plt.show()