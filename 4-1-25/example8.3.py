import numpy as np
import matplotlib.pyplot as plt

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import myFuncLib as mfl

def f(x,t):
    return -x**3+np.sin(t)

a = 0.0
b = 10.0
N1 = 10
h1 = (b-a)/N1
N2 = 20
h2 = (b-a)/N2
N3 = 50
h3 = (b-a)/N3
N4 = 100
h4 = (b-a)/N4

tpoints1 = np.arange(a,b,h1)
xpoints1 = []
tpoints2 = np.arange(a,b,h2)
xpoints2 = []
tpoints3 = np.arange(a,b,h3)
xpoints3 = []
tpoints4 = np.arange(a,b,h4)
xpoints4 = []

x = 0.0
for t in tpoints1:
    xpoints1.append(x)
    k1 = h1*f(x,t)
    k2 = h1*f(x+0.5*k1, t+0.5*h1)
    k3 = h1*f(x+0.5*k2, t+0.5*h1)
    k4 = h1*f(x+k3, t+h1)
    x += (k1+2*k2+2*k3+k4)/6

x = 0.0
for t in tpoints2:
    xpoints2.append(x)
    k1 = h2*f(x,t)
    k2 = h2*f(x+0.5*k1, t+0.5*h2)
    k3 = h2*f(x+0.5*k2, t+0.5*h2)
    k4 = h2*f(x+k3, t+h2)
    x += (k1+2*k2+2*k3+k4)/6

x = 0.0
for t in tpoints3:
    xpoints3.append(x)
    k1 = h3*f(x,t)
    k2 = h3*f(x+0.5*k1, t+0.5*h3)
    k3 = h3*f(x+0.5*k2, t+0.5*h3)
    k4 = h3*f(x+k3, t+h3)
    x += (k1+2*k2+2*k3+k4)/6

x = 0.0
for t in tpoints4:
    xpoints4.append(x)
    k1 = h4*f(x,t)
    k2 = h4*f(x+0.5*k1, t+0.5*h4)
    k3 = h4*f(x+0.5*k2, t+0.5*h4)
    k4 = h4*f(x+k3, t+h4)
    x += (k1+2*k2+2*k3+k4)/6

plt.plot(tpoints1,xpoints1, label =f"N = {N1}")
plt.plot(tpoints2,xpoints2, label =f"N = {N2}")
plt.plot(tpoints3,xpoints3, label =f"N = {N3}")
plt.plot(tpoints4,xpoints4, label =f"N = {N4}")
plt.legend()
plt.show()