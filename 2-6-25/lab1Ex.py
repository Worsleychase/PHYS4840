#! /usr/bin/python
import numpy as np
import matplotlib.pyplot as plt

filename = 'NGC6341.dat'

blueIn, greenIn, redIn = np.loadtxt(filename,usecols=(8,14,26),unpack=True)

quality_cut = np.where((redIn > 20) &\
                       (blueIn > 30) &\
                       (greenIn > 60))

blue = np.delete(blueIn,quality_cut)
red = np.delete(redIn,quality_cut)
green = np.delete(greenIn,quality_cut)

magnitude = blue
color     = blue - red

fig, ax = plt.subplots( figsize=(5, 7) )

plt.plot(color, (magnitude), "k.",markersize=0.3)
plt.gca().invert_yaxis()
plt.title('This is my super duper title')
plt.xlabel('Color: B-R')
plt.ylabel('Magnitude: B')
plt.ylim(25,14)
plt.xlim(-2,5)
plt.savefig('lab1.png')