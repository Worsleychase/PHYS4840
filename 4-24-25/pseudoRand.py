#####################################
#
# Class 26: pseudo-random algorithms
# Author: M Joyce
#
#####################################

import numpy as np
import matplotlib.pyplot as plt

seeds = np.arange(0, 1000, 1)
rng1_vals = []
rng2_vals = []
rng3_vals = []
rng4_vals = []

for seed in seeds:
    # Mersenne Twister (legacy)
    rng1 = np.random.default_rng(np.random.MT19937(seed))
    rng1_vals.append(rng1.random())

    # PCG64 (NumPy default)
    rng2 = np.random.default_rng(seed)
    rng2_vals.append(rng2.random())

    # Philox (counter-based PRNG)
    rng3 = np.random.Generator(np.random.Philox(seed))
    rng3_vals.append(rng3.random())

    # SFC64
    rng4 = np.random.Generator(np.random.SFC64(seed))
    rng4_vals.append(rng4.random())

plt.figure(figsize=(12, 6))
plt.plot(seeds, rng1_vals, label="Mersenne Twister (MT19937)")
plt.plot(seeds, rng2_vals, label="PCG64")
plt.plot(seeds, rng3_vals, label="Philox")
plt.plot(seeds, rng4_vals, label="SFC64")
plt.xlabel("Seed")
plt.ylabel("Random Value")
plt.title("Random Number Generators Comparison")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
