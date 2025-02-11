#! /usr/bin/python
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import gaussian_kde

filename = 'NGC6341.dat'

blueIn, greenIn, redIn = np.loadtxt(filename, usecols=(8, 14, 26), unpack=True)

quality_cut = np.where((redIn > 20) &
                       (blueIn > 30) &
                       (greenIn > 60))

blue = np.delete(blueIn, quality_cut)
red = np.delete(redIn, quality_cut)
green = np.delete(greenIn, quality_cut)

magnitude = blue
color = blue - red

fig, ax = plt.subplots(figsize=(5, 7))
xy = np.vstack([color, magnitude])
z = gaussian_kde(xy)(xy)

ax.scatter(color, magnitude, c=z, s=1)
ax.invert_yaxis()
ax.set_title('This is my super duper title')
ax.set_xlabel('Color: B-R')
ax.set_ylabel('Magnitude: B')
ax.set_ylim(25, 14)
ax.set_xlim(-2, 5)

plt.savefig('lab1.png')
plt.show()