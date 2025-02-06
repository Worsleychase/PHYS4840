#! /usr/bin/python
import numpy as np
import matplotlib.pyplot as plt

filename = 'NGC6341.dat'

blueIn, greenIn, redIn = np.loadtxt(filename,usecols=(8,14,26),unpack=True)

quality_cut = np.where((redIn > 10) &\
              (blueIn > 10) &\
              (greenIn > 10))

blue = np.delete(blueIn,quality_cut)
red = np.delete(redIn,quality_cut)
green = np.delete(greenIn,quality_cut)

magnitude = blue
color     = blue - red

fig, ax = plt.subplots( figsize=(10, 13) )

plt.plot(color, (magnitude), "ko",markersize=2)
plt.gca().invert_yaxis()
plt.ylim(24,14)
plt.xlim(-2,5)
plt.savefig('lab1.png')