import numpy as np
import scipy
import matplotlib.pyplot as plt

def myFunc (inVec):
    a = inVec[0]
    b = inVec[1]
    c = inVec[2]

    return np.linalg.norm(inVec)

# mu = 5log_10(d/10) = m-M
def distMod(x):
    return 5*np.log10(x/10)

def centDiffInt(f,a,h):
    return (f(a+h)-f(a-h))/(2*h)

def f(x):
    return 1.0 + 0.5*np.tanh(2.0*x)

def df_dx_analytical(x):
    return 1.0/(np.cosh(2.0*x)**2.0)

def derivProb5_15(x):
    return ((2*np.exp(2*x))/(np.exp(4*x)-1))**2

def show_data(x_gaia, y_gaia,x_vega, y_vega, output = 'test.png'):

    #savename = kwargs.get('output_png', 'test.png')

    plt.figure(figsize=(10, 5))
    plt.plot(x_gaia, y_gaia, label="GAIA")
    plt.plot(x_vega, y_vega, label="Vega")
    plt.xlabel("Wavelength")
    plt.ylabel("Flux")
    plt.title("GAIA and Vega Data")
    plt.legend()
    plt.savefig(output)
    plt.close()

    return 

def qr_decomposition(A):
    ## Computes the QR decomposition of matrix A using
    ## Gram-Schmidt orthogonalization.
    m, n = A.shape
    Q = np.zeros((m, n))
    R = np.zeros((n, n))

    for j in range(n):
        v = A[:, j]  # Take column j of A
        for i in range(j):  # Subtract projections onto previous Q columns
            R[i, j] = np.dot(Q[:, i], A[:, j])
            v = v - R[i, j] * Q[:, i]
        R[j, j] = np.linalg.norm(v)  # Compute norm
        Q[:, j] = v / R[j, j]  # Normalize

    return Q, R

def euler_method(f, x0, t0, t_end, dt):
    t_values = np.arange(t0, t_end + dt, dt) # makes a numpy array starting at t0 going to t_end+dt, in increments of dt
    x_values = np.zeros(len(t_values)) # makes an array with same length of t_values, fills with 0's
    x_values[0] = x0 # sets first value in x_values to x0

    for i in range(1, len(t_values)): # iterate through array going from 1 to length of t_values
        x_values[i] = x_values[i - 1] + dt * f(x_values[i-1], t_values[i-1]) # sets x_value[i] where i is the current index to the previous x_value (i-1) + dt * f(x,t)

    return t_values, x_values # returns t_values and x_values

def laplacian_operator(Phi, dx, dy, dz):
    """
    Compute the Laplacian of a scalar field Phi (i.e., apply the Poisson operator)
    using central finite differences on a 3D uniform grid.

    Parameters:
    - Phi : 3D numpy array of shape (nx, ny, nz)
    - dx, dy, dz : grid spacings in x, y, z directions

    Returns:
    - laplacian : 3D numpy array of the same shape as Phi
    """

    laplacian = (
        (np.roll(Phi, -1, axis=0) - 2*Phi + np.roll(Phi, 1, axis=0)) / dx**2 +
        (np.roll(Phi, -1, axis=1) - 2*Phi + np.roll(Phi, 1, axis=1)) / dy**2 +
        (np.roll(Phi, -1, axis=2) - 2*Phi + np.roll(Phi, 1, axis=2)) / dz**2
    )

    return laplacian