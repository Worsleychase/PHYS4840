# prob2.py
# 2-12-25

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-100,100,10000)
y = x**4

fig, ax = plt.subplots(1, 3, figsize=(15, 5))

ax[0].plot(x, y, 'r-', label=r'$y = x^4$')
ax[0].set_title('Linear Plot', fontsize=12)
ax[0].set_xlabel('x', fontsize=10)
ax[0].set_ylabel('y', fontsize=10)
ax[0].set_xlim(-100,100)
ax[0].grid(True)
ax[0].legend()

ax[1].plot(x, y, 'b-', label=r'Log-Log $y = x^4$')
ax[1].set_xscale('log')
ax[1].set_yscale('log')
ax[1].set_title('Log-Log Plot', fontsize=12)
ax[1].set_xlabel('log(x)', fontsize=10)
ax[1].set_ylabel('log(y)', fontsize=10)
ax[1].set_xlim(-100,100)
ax[1].grid(True,which='both', linestyle='--')
ax[1].legend()

ax[2].plot(x, np.log10(y), 'g-', label=r'$\log_{10}(y)$')
ax[2].set_title('Log(y) on Linear Grid', fontsize=12)
ax[2].set_xlabel('x', fontsize=10)
ax[2].set_ylabel(r'$\log_{10}(y)$', fontsize=10)
ax[2].set_xlim(-100,100)
ax[2].grid(True)
ax[2].legend()

plt.tight_layout()
plt.savefig('prob2.png')
plt.show()
