# Homework 3
## Problem 0:
See `2-18-25` and `2-20-25`

## Problem 1:
### a)
See `HW3`. Console Output:

GAIA Integrals:

  Trapezoidal: 3173.239426967372
  
  Simpson's: 3173.239438707639
  
  Romberg: 3173.2394426934334
  
VEGA Integrals:

  Trapezoidal: 2.952078067128259e-05
  
  Simpson's: 2.930695653336045e-05
  
  Romberg: 2.9748014434874256e-05
  
  Interpolated Trapezoidal: 3.0262648840886888e-05
  
  Interpolated Simpson's: 3.0108478412524078e-05
  
  Interpolated Romb: 3.027323129476018e-05
  
### b)
For the VEGA data, both the Simpson and Romberg integration technique assumes that the data is equally spaced (relative to x), so one would need to interpolate the data to ensure equal data points. I used SciPy's interpolate function to do it and we can see that the integral is evaluated to around the same value as the un-interpolated values. This means that the interpolation was likely unnecessary, so the un-interpolated values should be considered over the interpolated.

## Problem 2:
A common integration problem is a Gaussian/Normal shaped curve with evenly spaced data points (again in terms of x). For example, if you had a radiation measuring device (as a function of time), it yields a gaussian curve. For this, I would want to use Romberg's method because it is perfect for high precision, near continuous/smooth functions. However, if the data points were not evenly spread across x, I would want to use a very high N value of trapezoidal integration. This also works really well for Gaussian functions because their geometry is relatively simple. In short:

Romberg with high max order for evenly spaced data and little to no time constraints.
Trapezoidal with extremely high N for unevenly spaced data, irrelevant time constraints.

Obviously you would want to change the max order or N depending on time, but trapezoidal would be "good enough" for a Gaussian.

## Problem 3:
See `prob3.py`.

## Problem 4:
See `prob4.py`.
