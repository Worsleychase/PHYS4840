# prob3.py
# 2-12-25

import numpy as np
import matplotlib.pyplot as plt

month, spotCount = np.loadtxt('sunspots.txt', usecols=(0, 1), unpack=True)
fig, ax = plt.subplots(3, 1, figsize=(10, 10))

# part a
ax[0].plot(month, spotCount, 'r-')
ax[0].set_title('Part A Plot', fontsize=12)
ax[0].set_xlabel('Month', fontsize=10)
ax[0].set_ylabel('Spot Count', fontsize=10)
ax[0].set_xlim(0,3200)
ax[0].set_ylim(0,260)
ax[0].grid(True)

# part b
ax[1].plot(month, spotCount, 'b-')
ax[1].set_title('Part B Plot', fontsize=12)
ax[1].set_xlabel('Month', fontsize=10)
ax[1].set_ylabel('Spot Count', fontsize=10)
ax[1].set_xlim(0,1000)
ax[1].set_ylim(0,260)
ax[1].grid(True)

# part c
sum = np.cumsum(np.insert(spotCount,0,0))
avg = (sum[5:] - sum[:-5])/5
monthTrim = month[4:]

ax[2].plot(month, spotCount, 'k-',alpha = 0.3, label = "Dataset")
ax[2].scatter(monthTrim, avg, c='c', s=20, label = "Running average")
ax[2].set_title('Part C Plot', fontsize=12)
ax[2].set_xlabel('Month', fontsize=10)
ax[2].set_ylabel('Spot Count', fontsize=10)
ax[2].set_xlim(0,1000)
ax[2].set_ylim(0,260)
ax[2].grid(True)
ax[2].legend()

plt.tight_layout()
plt.savefig('prob3.png')
plt.show()