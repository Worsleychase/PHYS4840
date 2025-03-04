import numpy as np
from numpy import array,empty

A = np.array([ [2,1,4,1], 
			[3,4,-1,-1], 
			[1,-4,1,5], 
			[2,-2,1,3] ],float)

vector = np.array([-4,3,9,7],float)

## dimension 
N = len(vector)

for m in range(N):

	## first, divide by the diagonal element
	divisor = A[m,m]

	## divide every entry in row m by the divisor
	A[m,:] /= divisor

	## the above is shorthand for this operation:
	## A[m,:] = A[m,:]/divisor

	##anything we do to the matrix we must do to the vector:
	vector[m] /= divisor

	## now subtract multipls of the top row from the lower rows
	## to zero out rows 2,3 and 4
	for i in range(m+1, N): ## note that we start from the second row: m+1

		## because the first row now has 1 in the upper-left corner,
		## the factor by which we have to multiply the first row to subtract
		## it from the second is equal to the value in the first entry
		## of the second row
		multiplication_factor = A[i,m] 

		## now we must apply this operation to the entire row 
		## AND vector, as usual 
		A[i,:]    -= multiplication_factor*A[m,:]
		vector[i] -= multiplication_factor*vector[m] 


print('the upper diagonal version of A is: \n', A)

## Write the next part of this program:
##  how do we solve the system of equations now that we have
##  an upper-diagonal matrix?

## you may consult example 6.1 in your textbook if you need help
varArrTest = [0] * (N)
thing = 0
for i in range(N-1,-1,-1):
	for k in range(N-1):
		thing += A[i,i-k]*varArrTest[i]
		
	varArrTest[i] = (vector[i] - thing)/A[i,i]
	thing = 0

print(vector)

# 1x + 0.5y + 2z + 0.5w = vector[0]
# 0x + 1y -2.8z - 1w    = vector[1]     y = (vector[1]-coeff*z-coeff*w)/coeff
# 0x + 0y + 1z - 0w     = vector[2]     z = (vector[2]-coeff*w)/coeff
# 0x + 0y + 0z + 1w     = vector[3]     w = vector[3]/coeff

print(varArrTest)