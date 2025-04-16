# --------------------------------------------------------------------------
# Problem 0
# --------------------------------------------------------------------------
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.collections import LineCollection

def genDoublePend(fileName,theta1,theta2,omega1,omega2,g=9.81,l=1,m=1):
    # Initial conditions
    # State vector r = [theta1, theta2, omega1, omega2]
    r0 = np.array([theta1, theta2, omega1, omega2])  

    # Time parameters
    dt = 0.01  # Time step
    t_max = 10  # Simulation duration: sets number of TIME STEPS
    t = np.arange(0, t_max, dt)

    # Equations of motion for the double pendulum
    def equations(r):
        ## assign the four variables we need to evolve to ONE vector r 
        ## that holds them all
        theta1, theta2, omega1, omega2 = r
        delta_theta = theta2 - theta1

        # Define the four equations for the system
        ftheta1 = omega1
        ftheta2 = omega2

        ## HINT: the expressions for fomega1, fomega2 are quite long,
        ## so create smaller expressions to hold the denominators

        denom1 = (2 * m * l ** 2)
        denom2 = (m * l ** 2)

        fomega1 = (-g * (2 * m) * np.sin(theta1) - m * g * np.sin(theta1 - 2 * theta2) - 
                    2 * np.sin(delta_theta) * m *\
                    (omega2 ** 2 * l + omega1 ** 2 * l * np.cos(delta_theta))) / denom1

        fomega2 = (2 * np.sin(delta_theta) * (omega1 ** 2 * l * m + g * m * np.cos(theta1) + 
                    omega2 ** 2 * l * m * np.cos(delta_theta))) / denom2

        return np.array([ftheta1, ftheta2, fomega1, fomega2])

    # Runge-Kutta 4th order method

    def rk4_step(r, dt):
        k1 = dt * equations(r)
        k2 = dt * equations(r + 0.5 * k1)
        k3 = dt * equations(r + 0.5 * k2)
        k4 = dt * equations(r + k3)
        return r + (k1 + 2 * k2 + 2 * k3 + k4) / 6

    ## this is a CLEVER way to hold all of your data in one object
    ## R is a vector of lenght t (time steps) that will hold the evolution
    ## of all FOUR of your variables
    ## r0 is a VECTOR initialized to r0 = [0,0,0,0]
    R = np.zeros((len(t), 4))
    R[0] = r0

    # Integrate equations and save data
    ## remember: numerical integration --> for loop
    for i in range(1, len(t)):
        R[i] = rk4_step(R[i - 1], dt)

    # Extract angles and angular velocities
    theta1_vals, theta2_vals, omega1_vals, omega2_vals = R.T

    # Convert to Cartesian coordinates for visualization
    x1 = l * np.sin(theta1_vals)
    y1 = -l * np.cos(theta1_vals)
    x2 = x1 + l * np.sin(theta2_vals)
    y2 = y1 - l * np.cos(theta2_vals)

    # Save data
    np.savetxt(fileName, np.column_stack([t, x1, y1, x2, y2]),
            header="time x1 y1 x2 y2", comments="")
    
    print(f"Data saved to {fileName}")

name1 = "doublePend1.txt"
name2 = "doublePend2.txt"
name3 = "doublePend3.txt"

genDoublePend(name1, theta1=np.radians(90), theta2=np.radians(90), omega1=0,omega2=0)
genDoublePend(name2, theta1=np.radians(90), theta2=np.radians(90), omega1=0.1,omega2=0)
genDoublePend(name3, theta1=np.radians(90), theta2=np.radians(90), omega1=0,omega2=0.1)

dataFiles = [name1, name2, name3]
dataSets = [np.loadtxt(fname, skiprows=1).T for fname in dataFiles]
timeArray = dataSets[0][0]

fig, axes = plt.subplots(1, 3, figsize=(18, 6), sharex=True, sharey=True)
for ax in axes:
    ax.set_xlim(-2.5, 2.5)
    ax.set_ylim(-2.5, 2.5)
    ax.set_xlabel("X position (m)")
axes[0].set_ylabel("Y position (m)")
fig.suptitle("Double Pendulum Simulation")

lines1, lines2, masses1, masses2 = [], [], [], []
trailSegments1, trailSegments2 = [], []
trailLines1, trailLines2 = [], []

trailLength = 100
def getTrailLine(ax, cmap):
    return ax.add_collection(LineCollection([], linewidths=2, cmap=cmap, alpha=0.6))

for i in range(3):
    ax = axes[i]
    if i == 0:
        ax.set_title(fr"{i+1}: $\theta_1 = 90^\circ$, $\theta_2 = 90^\circ$, $\omega_1 = 0$, $\omega_2 = 0$")
    elif i == 1:
        ax.set_title(fr"{i+1}: $\theta_1 = 90^\circ$, $\theta_2 = 90^\circ$, $\omega_1 = 0.1$, $\omega_2 = 0$")
    else:
        ax.set_title(fr"{i+1}: $\theta_1 = 90^\circ$, $\theta_2 = 90^\circ$, $\omega_1 = 0$, $\omega_2 = 0.1$")
    ax.plot(0, 0, 'ko')

    line1Color = 'b'
    line2Color = 'r'
    mass1Color = 'bo'
    mass2Color = 'ro'
    trailCmap1 = plt.get_cmap('winter')
    trailCmap2 = plt.get_cmap('autumn')

    line1, = ax.plot([], [], color=line1Color, linestyle='-')
    line2, = ax.plot([], [], color=line2Color, linestyle='-')
    mass1, = ax.plot([], [], mass1Color, markersize=8)
    mass2, = ax.plot([], [], mass2Color, markersize=8)

    trail1 = getTrailLine(ax, trailCmap1)
    trail2 = getTrailLine(ax, trailCmap2)

    lines1.append(line1)
    lines2.append(line2)
    masses1.append(mass1)
    masses2.append(mass2)
    trailLines1.append(trail1)
    trailLines2.append(trail2)
    trailSegments1.append([])
    trailSegments2.append([])

def init():
    for i in range(3):
        lines1[i].set_data([], [])
        lines2[i].set_data([], [])
        masses1[i].set_data([], [])
        masses2[i].set_data([], [])
        trailLines1[i].set_segments([])
        trailLines2[i].set_segments([])
    return lines1 + lines2 + masses1 + masses2 + trailLines1 + trailLines2

def update(frame):
    for i in range(3):
        _, x1, y1, x2, y2 = dataSets[i]
        x1f, y1f = x1[frame], y1[frame]
        x2f, y2f = x2[frame], y2[frame]

        lines1[i].set_data([0, x1f], [0, y1f])
        lines2[i].set_data([x1f, x2f], [y1f, y2f])

        masses1[i].set_data([x1f], [y1f])
        masses2[i].set_data([x2f], [y2f])

        if frame > 0:
            trailSegments1[i].append([[x1[frame-1], y1[frame-1]], [x1f, y1f]])
            trailSegments2[i].append([[x2[frame-1], y2[frame-1]], [x2f, y2f]])

            if len(trailSegments1[i]) > trailLength:
                trailSegments1[i].pop(0)
                trailSegments2[i].pop(0)

            n = len(trailSegments1[i])
            alphas = np.linspace(0.0, 1.0, n)
            trailLines1[i].set_segments(trailSegments1[i])
            trailLines1[i].set_array(alphas)

            trailLines2[i].set_segments(trailSegments2[i])
            trailLines2[i].set_array(alphas)

    return lines1 + lines2 + masses1 + masses2 + trailLines1 + trailLines2

intervalMs = 10
fps = 1000 // intervalMs
ani = animation.FuncAnimation(fig, update, frames=len(timeArray), init_func=init, blit=True, interval=intervalMs)

ani.save('tripleDoublePendulum.mp4', writer='ffmpeg', fps=fps)

'''
The first two pendulums stay relatively the same until around 6 seconds in. But the 3rd pendulum goes chaotic right at the beginning.
'''


# --------------------------------------------------------------------------
# Problem 1 - Finished, see 4-8-25 and 4-10-25
# --------------------------------------------------------------------------


# --------------------------------------------------------------------------
# Problem 2 - See the README for part a, and I guess I have already done part c above
# --------------------------------------------------------------------------

# part b)
