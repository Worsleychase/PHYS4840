import numpy as np
import matplotlib.pyplot as plt

L = 0.01
D = 4.25e-6
N = 100
a = L/N
h = 1e-4
epsilon = h/1000

Tlo = 0.0
Tmid = 20.0
Thi = 50.0

t1 = 0.01
t2 = 0.1
t3 = 0.4
t4 = 1.0
t5 = 10.0
tend = t5 + epsilon

T = np.empty(N+1,float)
T[0] = Thi
T[N] = Tlo
T[1:N] = Tmid
Tp = np.empty(N+1,float)
Tp[0] = Thi
Tp[N] = Tlo

t = 0.0
c = h*D/(a*a)

while t < tend:
    for i in range(1,N):
        Tp[i] = T[i] + c*(T[i+1]+T[i-1]-2*T[i])
    T,Tp = Tp, T
    t += h

    x = np.arange(0,len(T))
    if abs(t-t1) < epsilon:
        plt.plot(x,T, label=f"t={t1}")
    if abs(t-t2) < epsilon:
        plt.plot(x,T, label=f"t={t2}")
    if abs(t-t3) < epsilon:
        plt.plot(x,T, label=f"t={t3}")
    if abs(t-t4) < epsilon:
        plt.plot(x,T, label=f"t={t4}")
    if abs(t-t5) < epsilon:
        plt.plot(x,T, label=f"t={t5}")
    
plt.xlabel('x')
plt.ylabel('T')
plt.legend(framealpha=1)
plt.show()