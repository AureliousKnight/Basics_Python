import matplotlib.pyplot as plt
import numpy as np
class PhysicsVector:
    def __init__(self, x, y, name="Force", color="blue"):
        self.x = x
        self.y = y
        self.name = name
        self.color = color
    def display(self, ax):
        ax.quiver(0, 0, self.x, self.y, color=self.color, 
                  angles='xy', scale_units='xy', scale=1, 
                  label=f"{self.name} ({self.x}, {self.y})", width=0.01)
class PhysicsWorld:
    def __init__(self):
        self.vectors = []
    def add_vector(self, v):
        self.vectors.append(v)
    def transform_world(self, scalar):
        for v in self.vectors:
            v.x *= scalar
            v.y *= scalar
        print(f"🌍 World transformed by a factor of {scalar}")
    
    def render(self):
        if not self.vectors:
           print("World is Empty!")
           return
        
        fig, ax = plt.subplots(figsize=(7,7))

        for v in self.vectors:
            v.display(ax)

        res_x = sum(v.x for v in self.vectors)
        res_y = sum(v.y for v in self.vectors)
        ax.quiver(0, 0, res_x, res_y, color='gold', label="Net Force", width=0.012)
        all_vals = [v.x for v in self.vectors] + [v.y for v in self.vectors] + [res_x, res_y]
        limit = max(np.abs(all_vals)) + 2 if all_vals else 10

        ax.set_xlim(-limit, limit)
        ax.set_ylim(-limit, limit)
        ax.grid(True, linestyle=':')
        ax.set_aspect('equal')
        plt.legend()
        plt.show()

my_world = PhysicsWorld()
my_world.add_vector(PhysicsVector(6, 2, "ForceA", "red"))
my_world.add_vector(PhysicsVector(-7, 3, "Force B", "blue"))

my_world.transform_world(5.5)
my_world.render()




