import matplotlib.pyplot as plt
import numpy as np
class PhysicsVector:
    def __init__(self, x_comp, y_comp, name="Force", color="green"):
        self.x = x_comp
        self.y = y_comp
        self.name = name
        self.color = color
    def get_magnitude(self):
            return np.sqrt(self.x**2 + self.y**2)
    def display(self,ax):
            ax.quiver(0,0, self.x, self.y, color=self.color,
                      angles = 'xy', scale_units='xy', scale=1, label=self.name)
fig, ax = plt.subplots(figsize=(6,6))
f1 = PhysicsVector(35, 67, "Tension", "red")
f2 = PhysicsVector(-83, 25, "Friction", "green")
f3 = PhysicsVector(f1.x + f2.x, f1.y + f2.y, "Resultant", "blue")

print(f"The {f1.name} magnitude is: {f1.get_magnitude():.2f}")
f1.display(ax)
f2.display(ax)
f3.display(ax)
ax.set_xlim(-100, 100)
ax.set_ylim(-100, 100)
ax.grid(True)
ax.set_aspect('equal')
plt.legend()
ax.set_xticks(np.arange(-100, 101, 10))
ax.set_yticks(np.arange(-100, 101, 10))
plt.show()

