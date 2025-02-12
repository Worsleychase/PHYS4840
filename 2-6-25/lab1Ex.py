#! /usr/bin/python
import numpy as np
import matplotlib.pyplot as plt
from sklearn.mixture import GaussianMixture

filename = 'NGC6341.dat'

blueIn, greenIn, redIn = np.loadtxt(filename, usecols=(8, 14, 26), unpack=True)

quality_cut = (redIn <= 22) & (blueIn <= 25) & (greenIn <= 25)

blue = blueIn[quality_cut]
red = redIn[quality_cut]
green = greenIn[quality_cut]

magnitude = blue
color = blue - red

data = np.vstack([color, magnitude]).T
gmm = GaussianMixture(n_components=2, covariance_type="full", random_state=5)
gmm.fit(data)
probabilities = gmm.predict_proba(data)
cluster_probabilities = probabilities[:, 0]
membership_prob = cluster_probabilities * 100

fig, ax = plt.subplots(figsize=(5, 7))
sc = ax.scatter(color, magnitude, c=membership_prob, cmap="viridis", s=1)
ax.invert_yaxis()
ax.set_title('This is my super duper title')
ax.set_xlabel('Color: B-R')
ax.set_ylabel('Magnitude: B')
ax.set_ylim(25, 14)
ax.set_xlim(-2, 5)
cbar = plt.colorbar(sc)
cbar.set_label("Membership Probability")

plt.savefig('lab1.png')
plt.show()