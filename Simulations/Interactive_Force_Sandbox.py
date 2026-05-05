import matplotlib.pyplot as plt
import numpy as np
class PhysicsVector:
    def __init__(self, x, y, name, color):
        self.x = x
        self.y = y
        self.name = name
        self.color = color

    def display(self, ax):
        ax.quiver(0, 0, self.x, self.y, color=self.color,
                  angles='xy', scale_units='xy', scale=1,
                  label=f"{self.name} ({self.x}, {self.y})")
        
def get_user_vector():
    print("\n--- Create a New Force ---")
    try:
        name = input("Enter vector name(e.g., Tension): ")
        x = float(input(f"Enter {name}'s X component: "))
        y = float(input(f"Enter {name}'s Y component: "))
        color = input("Enter color (r,g,b, or orange): ")
        return PhysicsVector(x, y, name, color)
    except ValueError:
        print("❌ Error: Please enter numbers for the components!")
        return None
    
fig, ax = plt.subplots(figsize=(7,7))
active_vectors = []

for i in range(2):
    v = get_user_vector()
    if v:
        active_vectors.append(v)
        v.display(ax)

if len(active_vectors) == 2:
    res_x = active_vectors[0].x + active_vectors[1].x
    res_y = active_vectors[0].y + active_vectors[1].y
    ax.quiver(0, 0, res_x, res_y, color='gold',
              angles='xy', scale_units='xy', scale=1,
              label="RESULTANT", width=0.015)

ax.set_xlim(-15, 15)
ax.set_ylim(-15, 15)
ax.grid(True, linestyle=':')
ax.set_aspect('equal')
plt.legend()
plt.title("Interactive Force Sandbox")
plt.show()
            