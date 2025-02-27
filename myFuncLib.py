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
   #plt.show()
    plt.savefig(output)
    plt.close()

    return 