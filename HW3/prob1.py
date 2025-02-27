import numpy as np
import time
import matplotlib.pyplot as plt
from scipy import interpolate

# Example usage with array data
def trapezoidal(y_values, x_values, N):
    """
    Approximates the integral using trapezoidal rule for given y_values at given x_values.
    
    Parameters:
        y_values (array-like): The function values at given x points.
        x_values (array-like): The x values corresponding to y_values.
        N (int): Number of intervals.

    Returns:
        float: The approximated integral.
    """
    a = x_values[0]
    b = x_values[-1]
    h = (b-a)/N

    integral = (1/2) * (y_values[0] + y_values[-1]) * h  # First and last terms

    for k in range(1, N):
        xk = a + k * h  # Compute x_k explicitly
        yk = np.interp(xk, x_values, y_values)  # Interpolate y at x_k manually in loop
        integral += yk * h

    return integral

# Simpson's rule for array data
def simpsons(y_values, x_values, N):
    """
    Approximates the integral using Simpson's rule for given y_values at given x_values.

    Parameters:
        y_values (array-like): The function values at given x points.
        x_values (array-like): The x values corresponding to y_values.
        N (int): Number of intervals (must be even).

    Returns:
        float: The approximated integral.
    """

    a = x_values[0]
    b = x_values[-1]
    h = (b-a)/N

    integral = y_values[0] + y_values[-1] # First and last y_value terms

    for k in range(1, N, 2):  # Odd indices (weight 4)
        xk = a + k * h
        yk = np.interp(xk, x_values, y_values)
        integral += 4 * yk

    for k in range(2, N, 2):  # Even indices (weight 2)
        xk = a + k * h
        yk = np.interp(xk, x_values, y_values)
        integral += 2 * yk

    return (h / 3) * integral  # Final scaling

# Romberg integration for array data
def romberg(y_values, x_values, max_order):
    """
    Approximates the integral using Romberg's method for given y_values at given x_values.

    Parameters:
        y_values (array-like): The function values at given x points.
        x_values (array-like): The x values corresponding to y_values.
        max_order (int): Maximum order (controls accuracy).

    Returns:
        float: The approximated integral.
    """
    R = np.zeros((max_order, max_order))
    a = x_values[0]
    b = x_values[-1]
    N = 0
    h = (b - a)

    # First trapezoidal estimate
    R[0, 0] = (h / 2) * (y_values[0] + y_values[-1])

    for i in range(1, max_order):
        N =  2**i#Remember: we are recomputing the integral with different N (and therefore h)
        h =  (b-a)/(2**i)#Look at the github derivation for richardson extrapolation

        sum_new_points = sum(np.interp(a + k * h, x_values, y_values) for k in range(1, N, 2))
        R[i, 0] = 0.5 * R[i - 1, 0] + h * sum_new_points

        for j in range(1, i + 1):
            R[i, j] = R[i, j - 1] + (R[i, j - 1] - R[i - 1, j - 1]) / (4**j - 1)

    return R[max_order - 1, max_order - 1]

def timing_function(integration_method, x_values, y_values, integral_arg):
    """
    Times the execution of an integration method.

    Parameters:
        integration_method (function): The numerical integration function.
        x_values (array-like): The x values.
        y_values (array-like): The corresponding y values.
        integral_arg (int, optional): EITHER Number of intervals to use (Simpson/Trapz) OR the maximum order of extrapolation (Romberg).

    Returns:
        tuple: (execution_time, integration_result)
    """
    start_time = time.time()
    result = integration_method(y_values, x_values, integral_arg)
    end_time = time.time()
    
    return end_time - start_time, result

def gaussLeg(f,N):
    roots, weights = np.polynomial.legendre.leggauss(n)

    sum = 0
    for i in range(N):
        root = roots[i]
        weight = weights[i]
        eval = weight*f(root)
        sum += eval

    integral_approx = sum


gaiaWave, gaiaFlux = np.loadtxt("GAIA_G.csv",delimiter=",", dtype=float, unpack=True)
vegaWave, vegaFlux = np.loadtxt("vega_SED.csv",delimiter=",", dtype=float, unpack=True, skiprows=1, usecols=(0,1))

fig, ax = plt.subplots(2,1,figsize=(5,9))

N = 10000

gaiaTrap = trapezoidal(gaiaFlux, gaiaWave, N)
gaiaSimp = simpsons(gaiaFlux, gaiaWave, N)
gaiaRomb = romberg(gaiaFlux, gaiaWave, 20)

vegaTrap = trapezoidal(vegaFlux, vegaWave, N)
vegaSimp = simpsons(vegaFlux, vegaWave, N)
vegaRomb = romberg(vegaFlux, vegaWave, 20)

interp_func = interpolate.interp1d(vegaWave, vegaFlux, kind='linear', fill_value='extrapolate')
new_vegaWave = np.linspace(min(vegaWave), max(vegaWave), len(vegaWave))
new_vegaFlux = interp_func(new_vegaWave)

newVegaTrap = trapezoidal(new_vegaFlux, new_vegaWave, N)
newVegaSimp = simpsons(new_vegaFlux, new_vegaWave, N)
newVegaRomb = romberg(new_vegaFlux, new_vegaWave, 20)

print(f"GAIA Integrals:")
print(f"  Trapezoidal: {gaiaTrap}")
print(f"  Simpson's: {gaiaSimp}")
print(f"  Romberg: {gaiaRomb}")

print(f"VEGA Integrals:")
print(f"  Trapezoidal: {vegaTrap}")
print(f"  Simpson's: {vegaSimp}")
print(f"  Romberg: {vegaRomb}")
print(f"  Interpolated Trapezoidal: {newVegaTrap}")
print(f"  Interpolated Simpson's: {newVegaSimp}")
print(f"  Interpolated Romb: {newVegaRomb}")

'''
ax[0].scatter(gaiaWave,gaiaFlux)

ax[1].scatter(vegaWave,vegaFlux)

plt.tight_layout()
plt.show()
fig.savefig('plot.png')
'''