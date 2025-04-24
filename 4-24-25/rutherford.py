#####################################
#
# Class 26: Oddball integration
# Author: Mark Newman, modified by M Joyce
#
#####################################

from math import sqrt,log,cos,sin,pi
from random import random

Z = 79 # Element being decayed
e = 1.602e-19 # elementary charge
E = 7.7e6*e # KE of radiation particle
epsilon0 = 8.854e-12 # permittivity of something or other
a0 = 5.292e-11 # nuclear cross section
sigma = a0/100

N = int(1e9) # Number of particles

# Gaussian function
def gaussian():
    r = sqrt(-2*sigma*sigma*log(1-random()))
    theta = 2*pi*random()
    x = r*cos(theta)
    y = r*sin(theta)
    return x,y

# Init count to be 0
count = 0

# Plug constants into equations
for i in range(N):
    x,y = gaussian()
    b = sqrt(x*x+y*y)
    if b<Z*e*e/(2*pi*epsilon0*E):
        count += 1

# Print result
print(count,"particles were reflected out of",N)