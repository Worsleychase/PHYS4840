import numpy as np
import scipy
import matplotlib.pyplot as plt

def myFunc (inVec):
    a = inVec[0]
    b = inVec[1]
    c = inVec[2]

    return np.linalg.norm(inVec)

def y(x):
    y = 2.0*x**3.0	
    return y

# mu = 5log_10(d/10) = m-M
def distMod(x):
    return 5*np.log10(x/10)

