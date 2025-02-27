# prob3.py

# Note: I will not be using NumPy because it hides the core logic.

# Part a
def funcA(xData):
    s = 0
    for i in xData:
        s += i**2
    return s

# Part b
def funcB(xData):
    xSum = 0
    for i in xData:
        xSum += i
    return xSum/len(xData)

# Part c
def funcC(n):
    fact = 1
    for i in range(1,n+1):
        fact *= i
    return fact

xData = [1,2,3,5,24,53,35677,12335,1234,1237,4,8,43]
n = 6

print(f'Part A: {funcA(xData)}')
print(f'Part B: {funcB(xData)}')
print(f'Part C (N = {n}): {funcC(n)}')