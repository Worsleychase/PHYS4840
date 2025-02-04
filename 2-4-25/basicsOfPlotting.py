#!/usr/bin/python
#####################################
#
# Class 5: Linear and Log + Plotting
# Author: M Joyce
#
#####################################
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(1, 100, 500)
y = x**2.0

## linear plot
plt.plot(x,y, linestyle='-', color='blue', linewidth=5)
plt.xlabel('My x-axis')
plt.ylabel('My y-axis')
plt.grid(True) ## turn on/off as needed
plt.show()
plt.close()

## log plot
plt.plot(x,y, linestyle='-', color='red', linewidth=5)
plt.xlabel('My x-axis')
plt.ylabel('My y-axis')
plt.xscale('log')  # Set x-axis to log scale
plt.yscale('log')  # Set y-axis to log scale
plt.grid(True) ## turn on/off as needed
plt.show()
plt.close()