import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from shapes import shapes_data

# Gravitational constant
G = 9.81  # m/s^2


# Class to represent an object
class Object:
    def __init__(self, shape_id, position, velocity):
        self.shape_id = shape_id
        self.position = np.array(position, dtype=float)
        self.velocity = np.array(velocity, dtype=float)


# Function to calculate acceleration due to gravity
def gravity_acceleration(obj):
    return np.array([0, -G])


# Function for calculating air resistance
def air_resistance(obj):
    shape = shapes_data[obj.shape_id]
    drag_force = 0.5 * shape.drag_coefficient * obj.velocity**2
    drag_direction = -np.sign(obj.velocity)
    return drag_force * drag_direction


# Function to update the position and speed of the object
def update_object(obj, dt):
    obj.velocity += (gravity_acceleration(obj) + air_resistance(obj)) * dt
    obj.position += obj.velocity * dt

    # Rebound control
    if obj.position[1] <= 0:
        obj.position[1] = 0
        # Reverses and reduces vertical speed
        obj.velocity[1] = -obj.velocity[1] * restitution_coefficient


# Animation initialisation function
def init():
    line1.set_data([], [])
    line2.set_data([], [])
    return line1, line2


# Function to update animation
def animate(i):
    update_object(obj1, dt)
    update_object(obj2, dt)
    line1.set_data([obj1.position[0]], [obj1.position[1]])
    line2.set_data([obj2.position[0]], [obj2.position[1]])
    return line1, line2


# Choice of object shape
print("Choose the shape of the object 1: ")
for shape_id, shape in shapes_data.items():
    print(f"{shape_id}: {shape.name}")
obj1_shape_id = None
while True:
    try:
        obj1_shape_id = int(
            input(
                "Enter the number corresponding to the desired shape (between 1 and 9): "
            )
        )
        if obj1_shape_id not in shapes_data:
            raise ValueError
        break
    except ValueError:
        continue

print("Choose the shape of the object 2: ")
for shape_id, shape in shapes_data.items():
    print(f"{shape_id}: {shape.name}")
obj2_shape_id = None
while True:
    try:
        obj2_shape_id = int(
            input(
                "Enter the number corresponding to the desired shape (between 1 and 9): "
            )
        )
        if obj2_shape_id not in shapes_data:
            raise ValueError
        break
    except ValueError:
        continue

while True:
    try:
        restitution_coefficient = float(
            input("Enter coefficient of restitution (between 0 and 1): ")
        )
        if 0 <= restitution_coefficient <= 1:
            break
        else:
            raise ValueError
    except ValueError:
        continue


obj1 = Object(obj1_shape_id, [0, 10], [0, 0])
obj2 = Object(obj2_shape_id, [2, 10], [0, 0])


# Settings for animation
dt = 0.02  # Time interval
fig, ax = plt.subplots()
ax.set_xlim(-1, 3)
ax.set_ylim(0, 11)
# Line style for the first object
line_style1 = shapes_data[obj1_shape_id].line_style
(line1,) = ax.plot([], [], line_style1, markersize=50)

# Line style for the second object
line_style2 = shapes_data[obj2_shape_id].line_style
(line2,) = ax.plot([], [], line_style2, markersize=50)

# Animation creation
ani = animation.FuncAnimation(
    fig, animate, frames=range(1000), init_func=init, blit=True, interval=16.6
)

plt.xlabel("Axis X (m)")
plt.ylabel("Axis Y (m)")
plt.title("Simulation of two falling objects")

plt.show()
