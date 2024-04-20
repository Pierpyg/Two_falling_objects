# Simulation of two falling objects
#### Description:

This project involves a Python program that simulates the fall of two objects subject to gravity and air resistance. The objective is to display an animation representing the movement of these two objects during the fall.

#### Contents of the files

This project consists of two files:

#### gravity.py

This file contains the main code for simulating the fall of objects. Here's how it is structured:

Firstly, the numpy and matplotlib libraries are imported. The first one is a library for scientific computing in Python, used for performing calculations. The second one is a library used for creating plots, employed here to generate the animation graph of the two falling objects. 'shapes' is the second file I created, I'll discuss it later.

Next, the gravitational acceleration of Earth is defined, with a constant value of 9.81 meters per second squared.

Then, we define the 'Object' class, which is used to represent an object within the simulation of falling objects.

The function "gravity_acceleration" calculates the acceleration due to gravity for a given object. The body of the function computes and returns the gravitational acceleration as a numpy array, which consists of two elements: 0 for the acceleration along the x-axis and -G along the y-axis. Since the object is in free fall, its position along the x-axis remains unchanged, while along the y-axis, it changes, and the value is negative because gravity acts downwards.

The function "air_resistance" calculates the air resistance on a specific object during its fall. Firstly, it takes information about the shape of the object "shape_id" from which we obtain the value of the "drag_coefficient" that changes depending on the shape. Then, it calculates the "drag_force" and the "drag_direction" and returns the product of the two.

Now, onto the "update_object" function, which is responsible for updating the position and velocity of an object during the simulation of its fall. The velocity is given by the sum of gravitational acceleration and air resistance multiplied by time, while the displacement is given by the product of velocity and time. The second part of the function is used to bounce the object based on the "restitution_coefficient" provided by the user. The program takes the center of the object as a reference point, and when it reaches the ground, it bounces. The center was chosen instead of the base for simplicity, as the object can have different shapes, and modifying the code for each case would be cumbersome.


The init function initializes the animation, where line1 and line2 represent the two objects that will fall, initially without any data to display.

The animate function is used to update the animation. Particularly, update_object updates the position and velocity of the two objects over time. The subsequent lines update the data of the visualization points of the two objects based on their position, ensuring that the objects are displayed correctly in the animation at their updated positions.

Following that, questions are defined to be asked to the user, namely choosing the shapes of the objects and the restitution_coefficient. The first two must be integers ranging from 1 to 9, and the last one a float ranging from 0 to 1.

The lines obj1 and obj2 create the two objects and define their positions on the graph, with the same height (10m), positioned 2m apart, and initial velocity set to zero for both.

#### shapes.py

This is the second file, which contains the shapes that the various objects can assume.

Here, the class 'Shape' is defined, representing a geometric shape. It has three attributes:

"name": the name of the shape.
"drag_coefficient": the coefficient of air resistance associated with the shape.
"line_style": the line style used to visualize the simulation object.

Finally, we have the 'shapes_data' dictionary where the names of the 9 objects, the resistance coefficient, and the marker used to represent them are defined. For simplicity, I used markers already defined in matplotlib, although they do not exactly correspond to the name of the figure.

#### requirements.txt

This file contains instructions on how to install the necessary libraries to make the program work.
