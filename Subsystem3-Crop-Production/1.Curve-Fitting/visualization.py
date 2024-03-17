# **********************************************************************
# Visualization Code ----
#
# Course Code: ME555
# Course Name: Design Optimization
# University of Michigan
# Semester Duration: 10th Jan 2024 to 29th April 2024
#
# Purpose ----
# To create a 3D visualization of the objective function.
# **********************************************************************

# Imports ----
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define the function for the objective
def objective_function(exp, mal, r=1, amp_w = 1, t_w = 1, tp_w = 1, phase_w = 1, vert_w = 1, acre = 1, c_w = 1, qe=1, ce = 1, qd = 1, qs = 1, tal = 1, vert = 1):
    return (
        0.2350747 * r ** (-1.0)
        + 0.4804318 * ((
            ((amp_w * np.sin((2 * np.pi) / t_w * (tp_w - phase_w)) + vert_w) * acre * c_w) ** 0.4) * 
            (qe * acre * ce) ** 0.6 )
        + 0.2811869 * qd
        - 0.9963252 * qs
        - 0.1230044 * (1)
        + 0.2777817 * tal ** (-1.0)
        + 1.1544897 * vert ** (-1.0)
        + 0.1500959 * exp ** (-1.0)
        + 0.1491099 * mal ** (-1.0)
        + 0.0004785
    )

# Create the grid of values
exp_values = np.linspace(0.1, 2, 100)  # Avoid division by zero by starting from 0.1
mal_values = np.linspace(0.1, 2, 100)  # Avoid division by zero by starting from 0.1
exp_grid, mal_grid = np.meshgrid(exp_values, mal_values)
z_values = objective_function(exp_grid, mal_grid)

# Plotting the 3D surface plot
fig = plt.figure(figsize=(14, 9))
ax = fig.add_subplot(111, projection='3d')

# Surface plot
surf = ax.plot_surface(exp_grid, mal_grid, z_values, cmap='jet')

# Labels and title
ax.set_xlabel('Export Fee (exp)')
ax.set_ylabel('Market Access Licence Fee (mal)')
ax.set_zlabel('Objective Function')
ax.set_title('Surface Plot of the Objective Function\'s \nMarket Access License Fee (mal) \nand the Export Fee (exp) \nWhile Holding all Other Variables at a Constant of 1')

# Color bar
fig.colorbar(surf, shrink=0.5, aspect=5)

# Show the plot
plt.show()
