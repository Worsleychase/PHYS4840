import numpy as np

def myFunc (inVec):
    a = inVec[0]
    b = inVec[1]
    c = inVec[2]

    return np.linalg.norm(inVec)

vec = [1,2,3,4]
print("Vector: " + str(vec))
print(myFunc(vec))