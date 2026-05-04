import matplotlib.pyplot as plt 
import numpy as np 

fig, ax = plt.subplots()
x_start = [0,0,0,0]
y_start = [0,0,0,0]
u_dir = [5,6,3,4]
v_dir = [1,7,9,5]
colors = ['r','g','b', 'g']
ax.quiver(x_start, y_start, u_dir, v_dir, color=colors, angles = 'xy', scale_units = 'xy', scale = 1, label = 'Forces')
ax.set_xlim(-1,10)
ax.set_ylim(-1,10)
ax.set_aspect('equal')
ax.grid(True, linestyle='--')
plt.title("Vector Force Simulation")
ax.set_xlabel("Force X (Newtons)")
ax.set_ylabel("Force Y (Newtons)")
ax.axhline(0, color='black', lw=0.5)
ax.axvline(0, color='black', lw=0.5)
plt.show()

