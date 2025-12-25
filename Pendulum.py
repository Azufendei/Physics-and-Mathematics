import numpy as np
import math
import matplotlib.pyplot as plt
from scipy.integrate import odeint


# defining the function to solve the ode
def odes(theta, t, b, g, l, m):
    theta1 = theta[0]
    theta2 = theta[1]
    dtheta1dt = theta2
    dtheta2dt = -(b / m) * theta2 - (g / l) * math.sin(theta1)
    dthetadt = [dtheta1dt, dtheta2dt]
    return dthetadt


# Input variables
b = 0.05
g = 9.81
l = 1
m = 1

# Initial conditions
theta0 = [0, 3]

t = np.linspace(0, 20, 200)

# Solving the ode
theta = odeint(odes, theta0, t, args=(b, g, l, m))

# Determining the origin of pendulum
x0 = 0
y0 = 0

plt.figure()
plt.plot(t, theta[:, 0], \'r\')
plt.plot(t, theta[:, 1], \'b\')
plt.savefig(\'angvt.png\')

ct = 0
for i in theta[:, 0]:
# Determining the place of the pendulum at each time step
    x1 = (1 * math.sin(i))
y1 = (-1 * math.cos(i))

# Plotting the pendulum and saving at each time step
filename = str(ct) + \'.png\'
ct = ct + 1
plt.figure()
plt.plot([-1, 1], [0, 0], \'r\', linewidth=3)
plt.plot([x0, x1], [y0, y1])
plt.plot(x1, y1, \'o\', markersize = 20)
plt.xlim([-1.5, 1.5])
plt.ylim([-1.5, 0.5])
plt.grid(bool)
plt.savefig(filename)
