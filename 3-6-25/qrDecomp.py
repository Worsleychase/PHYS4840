import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import myFuncLib as mfl

import numpy as np

'''
by importing and using the QR decomposition 
algorithm in my_functions_lib.py:
1) Find Q and R
2) Confirm that Q is orthogonal
3) Confirm that R is upper triangular
4) Confirm that the matrix A introduced in eigenvalues.py
can indeed be reconstructed by the dot product 
of matrices Q and R
'''

A = np.array([ [2, -1, 3,],\
			   [-1, 4, 5], 
			   [3,  5, 6] ],float)

Q, R = mfl.qr_decomposition(A)

print("Matrix Q:\n", Q)
print("Matrix R:\n", R)

# Check if Q is orthogonal
is_orthogonal = np.allclose(np.dot(Q.T, Q), np.eye(Q.shape[1]))
print("Is Q orthogonal? (Q^T Q = I):", is_orthogonal)

# Check if QR reconstructs A
reconstruction_check = np.allclose(np.dot(Q, R), A)
print("Does QR reconstruct A?:", reconstruction_check)