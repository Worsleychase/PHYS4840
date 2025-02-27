import numpy as np
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import myFuncLib as mfl
import matplotlib.pyplot as plt

def f(x):
    return 1+(1/2)*np.tanh(2*x)

hArr = [10**-5,10**-6,10**-7,10**-8,10**-9,10**-10,10**-11,10**-12,10**-13]
errArr = []
for h in hArr:
    intApprox = mfl.centDiffInt(f,0, h)
    errArr.append(abs(1-intApprox))

bestH = hArr[np.argmin(errArr)]
print(bestH)
print(mfl.centDiffInt(f,0,bestH))