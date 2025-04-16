#####################################
#
# Class 23: PDEs I: 3D Laplace Solver
# Author: Adapted by M Joyce from Mark Newman
#
#####################################
import numpy as np
import matplotlib.pyplot as plt

# Constants
N = 30              # Grid size (cube of size N x N x N)
h = 1               # Grid spacing
V = 1.0             # Voltage on the top face (z = 0)
target = 1e-6       # Convergence criterion

# Initialize the potential arrays
phi = np.zeros((N+1, N+1, N+1), dtype=float)
phinew = np.empty_like(phi)

# Apply boundary condition: top face (z = 0) at V, others at 0
phi[:,:,0] = V

# Iterative solution using Gauss-Seidel-like update
delta = 1.0
iteration = 0
while delta > target:
    iteration += 1
    for i in range(1, N):
        for j in range(1, N):
            for k in range(1, N):
                phinew[i,j,k] = (phi[i+h,j,k] + phi[i-h,j,k] +
                                 phi[i,j+h,k] + phi[i,j-h,k] +
                                 phi[i,j,k+h] + phi[i,j,k-h]) / 6.0

    # Preserve boundary conditions
    phinew[:,:,0] = V
    phinew[:,:,N] = 0
    phinew[:,0,:] = 0
    phinew[:,N,:] = 0
    phinew[0,:,:] = 0
    phinew[N,:,:] = 0

    delta = np.max(np.abs(phi - phinew))
    phi, phinew = phinew, phi

    if iteration % 10 == 0:
        print(f"Iteration {iteration}, max delta = {delta:.2e}")

# Visualization: middle slice in z-direction
mid_z = N // 2
plt.figure(figsize=(6,5))
plt.imshow(phi[:,0,:], origin='lower', cmap='inferno')
plt.colorbar(label='Potential $\Phi$')
plt.title(f"Midplane slice at z = {mid_z}")
plt.xlabel('x')
plt.ylabel('y')
plt.tight_layout()
plt.show()


'''
a) 3rd dimension (z) adds two more terms

b) Iterations take way too long

c) It changes how accurate the answer is, it therefore takes more time (if you increase the accuracy) to reach an acceptable output

d) In 2D the boundaries are kept in phi but in 3D they are kept in phinew
'''

# Solve with mfl
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import myFuncLib as mfl

thing = mfl.laplacian_operator(phi, h,h,h)