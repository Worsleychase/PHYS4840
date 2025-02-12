# prob1.py
# 2-12-25

import numpy as np
import matplotlib.pyplot as plt

ngcPath = 'NGC6341.dat'
mistPath = 'MIST_v1.2_feh_m1.75_afe_p0.0_vvcrit0.4_HST_WFPC2.iso.cmd'

ngcBlue, ngcRed = np.loadtxt(ngcPath, usecols=(8, 26), unpack=True)
ngcMag = ngcBlue
ngcColor = ngcBlue - ngcRed

newFile = []
with open(mistPath, 'r') as file:
    for line in file:
        if '#' in line:
            continue
        elif not line.strip():
            continue
        else:
            newFile.append(line)

newMist = "MIST.dat"
with open('MIST.dat', 'w') as file:
    for line in newFile:
        file.write(line)

mistBlue, mistRed = np.loadtxt(newMist, usecols=(12, 20), unpack=True)
mistMag = mistBlue
mistColor = mistBlue - mistRed

fig, ax = plt.subplots(figsize=(5, 7))
ax.scatter(ngcColor, ngcMag, c='k', s=1,label="NGC Data")
ax.scatter(mistColor, mistMag, c='b', s=1,label="MIST Data")
ax.invert_yaxis()
ax.set_title('This is my super duper title')
ax.set_xlabel('Color: B-R')
ax.set_ylabel('Magnitude: B')
ax.set_ylim(25, -10)
ax.set_xlim(1, 5)
ax.legend()

plt.savefig('prob1.png')
plt.show()
