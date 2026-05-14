import matplotlib.pyplot as plt
import numpy as np
class FallingObject:
    def __init__(self, mass, drag_coefficient, initial_height):
        self.mass = mass
        self.c = drag_coefficient
        self.y = initial_height
        self.v = 0.0
        self.g = 9.81
    def update_physics(self, dt):
        drag_force = self.c * self.v
        gravity_force = self.mass * self.g
        net_acceleration = (gravity_force - drag_force) / self.mass
        self.v += net_acceleration * dt
        self.y += self.v * dt
        if self.y < 0:
            self.y = 0
            self.v = 0
            
skydiver = FallingObject(mass=85, drag_coefficient=0.25, initial_height=500)

time_data = []
height_data = []
velocity_data = []
t = 0.0
dt = 0.1
while skydiver.y > 0:
    time_data.append(t)
    height_data.append(skydiver.y)
    velocity_data.append(skydiver.v)
    skydiver.update_physics(dt)
    t += dt

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8))
ax1.plot(time_data, height_data, color='blue')
ax1.set_title("Skydiver Trajectory")
ax1.set_ylabel("Height (meters)")
ax1.grid(True)

ax2.plot(time_data, velocity_data, color='red')
ax2.set_title("Velocity over Time")
ax2.set_xlabel("Time (seconds)")
ax2.set_ylabel("Velocity (m/s)")
ax2.grid(True)

plt.tight_layout()
plt.show()
