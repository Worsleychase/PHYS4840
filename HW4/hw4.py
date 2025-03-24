import numpy as np

# Problem 2
# Part a) ------------------------------------------------------------------------------------------------------------
def trapezoidal_rule(f, a, b, N):
    """
    Approximates the integral using the trapezoidal rule with a loop.

    Parameters:
        f (function or array-like): A function, it's evaluated at N+1 points.
                                    
        a (float): Lower bound of integration.
        b (float): Upper bound of integration.
        N (int): Number of intervals (trapezoids).

    Returns:
        float: The approximated integral.
    """
    
    h = (b-a)/N

    integral = (1/2) * (f(a) + f(b)) * h  # Matches the first & last term in the sum

    # Loop through k=1 to N-1 to sum the middle terms
    for k in range(1, N):
        xk = a + k * h  # Compute x_k explicitly (matches the formula)
        integral += f(xk) * h  # Normal weight (multiplied by h directly)

    return integral

def adaptiveTrapezoidal(f, a, b, tol):
    n = 1
    integral_old = trapezoidal_rule(f, a, b, n)
    error = tol + 1

    while error > tol:
        n *= 2
        integral_new = trapezoidal_rule(f, a, b, n)
        error = np.abs(integral_new - integral_old) / 3
        integral_old = integral_new

    return integral_new, n

def func1(x):
    return (np.sin(np.sqrt(100*x)))**2

a = 0
b = 1
tolerance = 1e-6

integral, intervals = adaptiveTrapezoidal(func1, a, b, tolerance)
print(f"Estimated integral: {integral}")
print(f"Number of intervals used: {intervals}")

# Part b) ------------------------------------------------------------------------------------------------------------
print("Doing romberg now")

def adaptiveRomberg(f, a, b, tol):
    R = [[(b - a) * (f(a) + f(b)) / 2]] 
    m = 1 
    error = tol + 1 

    while error > tol:
        m_old = m
        m *= 2
        h = (b - a) / m
        T_new = 0.5 * R[-1][0] + h * sum(f(a + (k + 0.5) * ((b - a) / m_old)) for k in range(m_old))
        R.append([T_new])

        i = len(R) - 1
        for j in range(1, i + 1):
            extrapolated = (4**j * R[i][j-1] - R[i-1][j-1]) / (4**j - 1)
            R[i].append(extrapolated)

        if i > 0:
            error = abs(R[i][i] - R[i-1][i-1])
        else:
            error = tol + 1

    return R[-1][-1], R

def rombergTable(R):
    for i, row in enumerate(R):
        print("R[{}]: {}".format(i, "\t".join(f"{val:.10f}" for val in row)))
        
a = 0
b = 1
tolerance = 1e-6

result, R = adaptiveRomberg(func1, a, b, tolerance)
rombergTable(R)
print(f"Integral: {result}")

# -----------------------------------------------------------------------------------------------------------------------
# Problem 3
# Part 1)
# See pdf

# Part 2)
print("\n----------- Problem 3 -----------\n")
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import myFuncLib as mfl

A = np.array([ [1, 0, 0, 0],\
			   [0,1,1,-1], 
			   [0,2,4,0],
               [0,2,-1,2] ],float)
N = len(A)

L = np.array([[1.0 if i == j else 0.0 for j in range(N)] for i in range(N)])
U = A.copy()
for m in range(N):
    for i in range(m+1, N):        
        L[i, m] = U[i, m] / U[m, m]
        U[i, :] -= L[i, m] * U[m, :]

print('The lower triangular matrix L is:\n', L)
print('The upper triangular matrix U is:\n', U)

vector = np.array([0,294.3,392.4,196.2],float)

Q, R = mfl.qr_decomposition(A)

print("Matrix Q:\n", Q)
print("Matrix R:\n", R)

# Part 3)
is_orthogonal = np.allclose(np.dot(Q.T, Q), np.eye(Q.shape[1]))
print("Is Q orthogonal? (Q^T Q = I):", is_orthogonal)

def isUpper(matrix):
    rows, cols = matrix.shape
    for i in range(1, rows):
        for j in range(i):
            if matrix[i, j] != 0:
                return False

    return True

print("Upper diagonality for Q?:", isUpper(Q))
print("Upper diagonality for R?:", isUpper(R))