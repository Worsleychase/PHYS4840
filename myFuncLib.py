import numpy as np
import scipy as sp
import matplotlib.pyplot as plt

def myFunc (inVec):
    a = inVec[0]
    b = inVec[1]
    c = inVec[2]

    return np.linalg.norm(inVec)

def y(x):
    y = 2.0*x**3.0	
    return y