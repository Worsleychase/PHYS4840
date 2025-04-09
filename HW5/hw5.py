import numpy as np
import matplotlib.pyplot as plt
import time 

# Problem 1 -----------------------------------------------------------------------------

def func(t):
    if (np.ceil(t*2)%2 == 0):
        return 1
    else:
        return -1
    
rc = [0.01,0.1,1.0]
h = 0.01
t = np.arange(0.0,10.0+h,h)
vout = np.zeros((len(t),len(rc)))

for i in range(len(rc)):
    for j in range(len(t)-1):
        k1 = h*(func(t[j]) - vout[j,i])/rc[i]
        k2 = h*(func(t[j]+0.5*h) - (vout[j,i]+0.5*k1))/rc[i]
        k3 = h*(func(t[j]+0.5*h) - (vout[j,i]+0.5*k2))/rc[i]
        k4 = h*(func(t[j]+h) - (vout[j,i]+k3))/rc[i]
        vout[j+1,i] = vout[j,i]+(k1+2*k2+2*k3+k4)/6

plt.plot(t, vout[:,0], label='RC = 0.01')
plt.plot(t, vout[:,1], label='RC = 0.1')
plt.plot(t, vout[:,2], label='RC = 1.0')
plt.xlabel('t')
plt.ylabel(r'$V_{out}(t)$')
plt.legend(framealpha=1)
plt.title(r'$V_{out}$ vs $t$ ')
plt.savefig('prob1.png')
plt.close()

# Problem 2 -----------------------------------------------------------------------------

def func(x,t):
    return -1*(x**(3))+np.sin(t)

a = 0.0
b = 10.0
N = 1000
h = (b-a)/N

tpoints = np.arange(a,b,h)
xpoints = []

x = 1.0
for t in tpoints:
    xpoints.append(x)
    k1 = h*func(x,t)
    k2 = h*func(x+0.5*k1, t+0.5*h)
    x += k2

a1 = 0.0
b1 = 10000.0
N1 = 1000
h1 = (b1-a1)/N1

tpoints1 = np.arange(a1,b1,h1)
xpoints1 = []

x1 = 1.0
for t1 in tpoints1:
    xpoints1.append(x1)
    k1 = h1*func(x1,t1)
    k2 = h1*func(x1+0.5*k1, t1+0.5*h1)
    x1 += k2

tFort,xFort = np.loadtxt("prob2-1.dat", unpack=True, skiprows = 1)
tFort1,xFort1 = np.loadtxt("prob2-2.dat", unpack=True, skiprows = 1)

fig, ax = plt.subplots(2, 1, figsize=(8, 6))

ax[0].plot(tpoints, xpoints, label="Python RK2", linewidth = 5)
ax[0].plot(tFort, xFort, label="Fortran RK2")
ax[0].set_xlim(0, 10)
ax[0].set_ylabel("x(t)")
ax[0].legend()
ax[0].set_title(f"[0,10] | N = {N}")

ax[1].plot(tpoints1, xpoints1, label="Python RK2", linewidth = 5)
ax[1].plot(tFort1, xFort1, label="Fortran RK2")
ax[1].set_xlim(0, 35)
ax[1].set_xlabel("t")
ax[1].set_ylabel("x(t)")
ax[1].legend()
ax[1].set_title(f"[0,10000] | N = {N1}")

plt.tight_layout()
plt.savefig("prob2.png")
plt.close()

# Problems 3 and 4 -----------------------------------------------------------------------------

def func(x,t):
    return -1*(x**(3))+np.sin(t)

a = 0.0
b = 10.0
N = 1000
h = (b-a)/N

tpoints = np.arange(a,b,h)
xpoints = []

x = 1.0
for t in tpoints:
    xpoints.append(x)
    k1 = h*func(x,t)
    k2 = h*func(x+0.5*k1, t+0.5*h)
    k3 = h*func(x+0.5*k2, t+0.5*h)
    k4 = h*func(x+k3, t+h)
    x += (k1+2*k2+2*k3+k4)/6

start = time.time()
a1 = 0.0
b1 = 10000.0
N1 = 1000
h1 = (b1-a1)/N1

tpoints1 = np.arange(a1,b1,h1)
xpoints1 = []

x1 = 1.0
for t1 in tpoints1:
    xpoints1.append(x1)
    k1 = h1*func(x1,t1)
    k2 = h1*func(x1+0.5*k1, t1+0.5*h1)
    k3 = h1*func(x1+0.5*k2, t1+0.5*h1)
    k4 = h1*func(x1+k3, t1+h1)
    x1 += (k1+2*k2+2*k3+k4)/6
stop = time.time()
total = stop-start

print(f"Python took {total} seconds to run")

tFort4,xFort4 = np.loadtxt("prob3-1.dat", unpack=True, skiprows = 1)
tFort14,xFort14 = np.loadtxt("prob3-2.dat", unpack=True, skiprows = 1)

plt.plot(tpoints, xpoints, label="Python RK4 | [0,10]", linewidth = 5)
plt.plot(tFort4, xFort4, label="Fortran RK4 | [0,10]")
plt.plot(tpoints1, xpoints1, label="Python RK4 | [0,10000]", linewidth = 5)
plt.plot(tFort14, xFort14, label="Fortran RK4 | [0,10000]")
plt.xlim(0, 10)
plt.ylim(-1,1)
plt.ylabel("x(t)")
plt.legend()
plt.title(f"[0,10] | N = {N}")

plt.tight_layout()
plt.savefig("prob3.png")
plt.close()
