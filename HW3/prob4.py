import numpy as np
import matplotlib.pyplot as plt

def f(x):
    if abs(x) < 1e-10:
        return 1.0
    return (np.sin(x) / x) ** 2

def step(x1, x2, f1, f2, epsilon=1e-4):
    x = (x1 + x2) / 2
    fm = f(x)
    h = x2 - x1

    I1 = h * (f1 + f2) / 2  
    I2 = h * (f1 + 2*fm + f2) / 4 
    
    error = abs(I2 - I1)

    points.append(x)

    if error <= epsilon * h:
        return h * (f1 + 4*fm + f2) / 6
    else:
        left = step(x1, x, f1, fm, epsilon)
        right = step(x, x2, fm, f2, epsilon)
        return left + right
points = []

x1, x2 = 0.0, 10.0
result = step(x1, x2, f(x1), f(x2))

print(f"Integral value: {result:.6f}")

x = np.linspace(0, 10, 1000)
y = [f(xi) for xi in x]

plt.figure(figsize=(12, 6))
plt.plot(x, y, 'b-', label='Integrand')
plt.plot(points, [f(p) for p in points], 'r.', label='Slice points')
plt.xlabel('x')
plt.ylabel('sin²(x)/x²')
plt.title('Adaptive Integration Points')
plt.legend()
plt.grid(True)
plt.show()