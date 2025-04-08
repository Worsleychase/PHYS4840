import numpy as np
import matplotlib.pyplot as plt

t,x = np.loadtxt("rk2_results.dat", unpack=True, skiprows = 1)
t2, x2 = np.loadtxt("rk2_results2.dat", unpack=True, skiprows = 1)
t3, x3 = np.loadtxt("rk4_results2.dat", unpack=True, skiprows= 1)

plt.plot(t,x)
plt.plot(t2,x2)
plt.plot(t3,x3)
plt.xlim(0,10)
plt.show()