import matplotlib
matplotlib.use('TkAgg')

import numpy as np
import matplotlib.pyplot as plt

plt.ion()

G = 6.67408e-11
M_sun = 1.989e30
AU = 1.496e11

x = 0.9833 * AU
y = 0

vx = 0
vy = 30290

dt = 60 * 60 * 24

x_positions = []
y_positions = []

fig, ax = plt.subplots(figsize=(6, 6))

orbit, = ax.plot([], [], label="Earth's Orbit")

sun = ax.scatter(0, 0, color="orange", s=150, label="Sun")

earth = ax.scatter(x / AU, y / AU, color="blue", s=40, label="Earth")

ax.set_xlabel("x position (AU)")
ax.set_ylabel("y position (AU)")
ax.set_title("Earth's Orbit Around the Sun")

ax.set_xlim(-1.2, 1.2)
ax.set_ylim(-1.2, 1.2)

ax.set_aspect("equal")
ax.grid(True)
ax.legend(loc="upper right", fontsize=8)


for i in range(365):

    r = np.sqrt(x**2 + y**2)

    ax_acc = -G * M_sun * x / r**3
    ay_acc = -G * M_sun * y / r**3

    vx += ax_acc * dt
    vy += ay_acc * dt

    x += vx * dt
    y += vy * dt

    x_positions.append(x)
    y_positions.append(y)

    orbit.set_data(
        np.array(x_positions) / AU,
        np.array(y_positions) / AU
    )

    earth.set_offsets([[x / AU, y / AU]])

    plt.pause(0.02)


plt.ioff()
plt.show()