import matplotlib.pyplot as plt
import numpy as np

class AnimatedCar:
    def __init__(self):
        self.x = 0.0
        self.v = 0.0
        self.a = 0.0  

    def update_engine(self, dt):
        if self.v < 15.0:
            self.a = 4.0
        elif self.v < 28.0:
            self.a = 1.5
        else:                   
            self.a = 0.0        

        self.v += self.a * dt
        self.x += self.v * dt

car = AnimatedCar()
time_data = []
position_data = []
velocity_data = []

t = 0.0
dt = 0.1

plt.ion()
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 6))

while t <= 15.0:
    time_data.append(t)
    position_data.append(car.x)
    velocity_data.append(car.v)
    car.update_engine(dt)
    t += dt

    ax1.clear()
    ax2.clear()

    ax1.plot(time_data, position_data, color='blue', lw=2)
    ax1.scatter(t, car.x, color='black', s=50) 
    ax1.set_title("Live Journey Tracking")
    ax1.set_ylabel("Distance (meters)")
    ax1.grid(True, linestyle=':')
    ax2.plot(time_data, velocity_data, color='red', lw=2)
    ax2.scatter(t, car.v, color='black', s=50)
    ax2.set_xlabel("Time (seconds)")
    ax2.set_ylabel("Speed (m/s)")
    ax2.grid(True, linestyle=':')

    plt.tight_layout()
    
    plt.pause(0.01) 

plt.ioff()
plt.show()
