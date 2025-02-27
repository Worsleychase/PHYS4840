import numpy as np
import time
import matplotlib.pyplot as plt

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

# Function to integrate
def function(x):
    return x * np.exp(-x)

# Precompute data for fair comparisons
x_data = np.linspace(0, 1, 100000000)  # High-resolution x values
y_data = function(x_data)

# Testing parameters
N = 1# Number of intervals
max_order = 2# Romberg's accuracy level

# Measure timing for custom methods
trap_time, trap_result = timing_function(trapezoidal, x_data, y_data, N)
simp_time, simp_result = timing_function(simpsons, x_data, y_data, N)
romb_time, romb_result = timing_function(romberg, x_data, y_data, max_order)

# True integral value
true_value = 0.26424111765711535680895245967707826510837773793646433098432639660507700851

# Compute errors
trap_error = abs(trap_result - true_value)
simp_error = abs(simp_result - true_value)
romb_error = abs(romb_result - true_value)

# Print results with error analysis
print("\nIntegration Method Comparison")
print("=" * 80) # why 80? https://peps.python.org/pep-0008/
print(f"{'Method':<25}{'Result':<20}{'Error':<20}{'Time (sec)':<15}")
print("-" * 80)
print(f"{'Custom Trapezoidal':<25}{trap_result:<20.8f}{trap_error:<20.8e}{trap_time:<15.6f}")
print(f"{'Custom Simpson\'s':<25}{simp_result:<20.8f}{simp_error:<20.8e}{simp_time:<15.6f}")
print(f"{'Custom Romberg':<25}{romb_result:<20.8f}{romb_error:<20.8e}{romb_time:<15.6f}")
print("=" * 80)

trapErrArr = []
simpErrArr = []
rombErrArr = []
trapTimeArr = []
simpTimeArr = []
rombTimeArr = []


nArr = np.arange(1,20,1)
for N in nArr:
    trap_time, trap_result = timing_function(trapezoidal, x_data, y_data, N)
    trapTimeArr.append(trap_time)
    trapErrArr.append(abs(trap_result-true_value))
    simp_time, simp_result = timing_function(simpsons, x_data, y_data, N)
    simpTimeArr.append(simp_time)
    simpErrArr.append(abs(simp_result-true_value))
    romb_time, romb_result = timing_function(romberg, x_data, y_data, N)
    rombTimeArr.append(romb_time)
    rombErrArr.append(abs(romb_result-true_value))


fig, ax = plt.subplots(3,1,figsize=(10,18))

ax[0].scatter(nArr, trapErrArr, color='blue', marker='x', s=30, label='Trap')
ax[0].scatter(nArr, rombErrArr, color='red', marker='o', s=30, label='Romb')
ax[0].scatter(nArr, simpErrArr, color='green', marker='1', s=30, label='Simp')
ax[0].plot(nArr, trapErrArr, color='blue', label='Trap')
ax[0].plot(nArr, rombErrArr, color='red', label='Romb')
ax[0].plot(nArr, simpErrArr, color='green', label='Simp')
ax[0].set_yscale('linear')
ax[0].set_xscale('linear')
ax[0].set_xlabel('N')
ax[0].set_ylabel('Error of Method')
ax[0].set_xlim(0,20)
ax[0].legend()

ax[1].scatter(nArr, trapTimeArr, color='blue', marker='x', s=30, label='Trap')
ax[1].scatter(nArr, rombTimeArr, color='red', marker='o', s=30, label='Romb')
ax[1].scatter(nArr, simpTimeArr, color='green', marker='1', s=30, label='Simp')
ax[1].plot(nArr, trapTimeArr, color='blue', label='Trap')
ax[1].plot(nArr, rombTimeArr, color='red', label='Romb')
ax[1].plot(nArr, simpTimeArr, color='green',label='Simp')
ax[1].set_yscale('linear')
ax[1].set_xscale('linear')
ax[1].set_xlabel('N')
ax[1].set_xlim(0,20)
ax[1].set_ylabel('Time Taken')
ax[1].legend(loc='upper left')

computeTimeTrap = []
computeTimeSimp = []
computeTimeRomb = []
for i in range(len(trapTimeArr)):
    computeTimeTrap.append(trapTimeArr[i]*trapErrArr[i])
    computeTimeSimp.append(simpTimeArr[i]*simpErrArr[i])
    computeTimeRomb.append(rombTimeArr[i]*rombErrArr[i])

ax[2].scatter(nArr, computeTimeTrap, color='blue', marker='x', s=30, label='Trap')
ax[2].scatter(nArr, computeTimeRomb, color='red', marker='o', s=30, label='Romb')
ax[2].scatter(nArr, computeTimeSimp, color='green', marker='1', s=30, label='Simp')
ax[2].plot(nArr, computeTimeTrap, color='blue', label='Trap')
ax[2].plot(nArr, computeTimeRomb, color='red', label='Romb')
ax[2].plot(nArr, computeTimeSimp, color='green', label='Simp')
ax[2].set_xlabel('N')
ax[2].set_xlim(0,20)
ax[2].set_ylabel('Compute Time \n(Time*Error)')
ax[2].legend()

plt.tight_layout()
plt.show()
fig.savefig('plot.png')
