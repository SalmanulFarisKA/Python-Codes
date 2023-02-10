import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

# Define the physical constants
G = 6.67430e-11
M_sun = 1.9885e30
M_earth = 5.9722e24
AU = 1.49597870700e11

# Define the initial conditions
x0 = 1.0 * AU
y0 = 0.0
vx0 = 0.0
vy0 = 2 * np.pi

# Define the simulation parameters
dt = 3600.0
T = 1.0 * 365 * 24 * 3600

# Compute the position of the Earth at n evenly spaced time steps
n = int(T/dt)
x = np.zeros(n)
y = np.zeros(n)
vx = np.zeros(n)
vy = np.zeros(n)
x[0] = x0
y[0] = y0
vx[0] = vx0
vy[0] = vy0

for i in range(1, n):
    r = np.sqrt(x[i-1]**2 + y[i-1]**2)
    ax = -G * M_sun * x[i-1] / r**3
    ay = -G * M_sun * y[i-1] / r**3
    x[i] = x[i-1] + vx[i-1] * dt + 0.5 * ax * dt**2
    y[i] = y[i-1] + vy[i-1] * dt + 0.5 * ay * dt**2
    vx[i] = vx[i-1] + ax * dt
    vy[i] = vy[i-1] + ay * dt

# Define the update function for the animation
def update(frame):
    plt.clf()
    plt.plot(x[:frame], y[:frame], '-b')
    plt.plot(0, 0, 'yo', markersize=10)
    plt.plot(x[frame], y[frame], 'ro', markersize=5)
    plt.xlim(-1.5 * AU, 1.5 * AU)
    plt.ylim(-1.5 * AU, 1.5 * AU)
    plt.xlabel('x (m)')
    plt.ylabel('y (m)')
    plt.title('Orbit of the Earth')

# Create the animation
ani = animation.FuncAnimation(plt.gcf(), update, frames=n, interval=20)
plt.show()
