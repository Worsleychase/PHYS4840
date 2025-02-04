#!/usr/bin/python

#### YOUR SHEBANG IS DIFFERENT THAN MINE
#### PS 227 LINUX USERS: USE THE SHEBAG
#!/usr/local/Anaconda2023/bin/...

#####################################
#
# Class 5: Linear and Log + Plotting
# Author: < YOUR NAME HERE > 
#
#####################################
import numpy as np
import matplotlib.pyplot as plt
import sys
sys.path.append('/home/chaserix/Documents/PHYS4840/')
## in your functions library, which should 
## be in a different file, define the function
#
# def y(x):
# 	y = 2.0*x**3.0
# 	return y
#
# and import your functions library

import myFuncLib as mfl

# define your x values
x = np.linspace(1, 100, 500)  # x values

y = mfl.y(x) # complete this statement using the
		# function you wrote in your functions library

# (1) make a linear plot of y vs x
plt.plot(x,y)
plt.grid()
plt.show()
plt.close()

# (2) make a log-log plot of y vs x
plt.plot(x,y)
plt.yscale('log')
plt.xscale('log')
plt.grid()
plt.show()
plt.close()

# (3) make a plot of log(x) vs log(y)
plt.plot(np.log10(x),np.log10(y))
plt.grid()
plt.show()
plt.close()
