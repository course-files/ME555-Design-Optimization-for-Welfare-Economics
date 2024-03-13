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


# Objective Function ----
def objective(x):
    """
    This is the objective function to be minimized.
    r = x[0]
    cw = x[1]
    tw = x[2]
    ce = x[3]
    qs_stddev = x[4]
    qd = x[5]
    qs = x[6]
    ts = x[7]
    tal = x[8]
    mal = x[9]
    """
    # Model without parameter values
    # return (1 * (x[0] ** -1.0) - 1 * ((np.sin(x[1] / x[2])) * (x[3])) +
    #         (x[4]) ** 1 + 1 * (x[5]) ** -1.0 + 1 * ((np.sin(x[6] / x[7])) - x[5]) -
    #         1 * (x[8] ** -1)) - (x[9] ** -1.0)

    # Small-Scale Farmer Model with Parameter Values ----
    return (1000 * (x[0] ** -1.0) + 0.0006389 * (-(np.sin(x[1] / x[2])) * -(x[3])) +
            (x[4]) ** 0.6384 + 1000 * (x[5]) ** -1.0 + 0.01999 * ((np.sin(x[6] / x[7])) - x[5]) +
            0.001 * -(x[8] ** -1)) - (x[9] ** -1.0) + 269.2


# Bounds for the variables
lower_bounds = np.array([46700, 20, 3, 2000, 0, 720, 720, 5, 5000, 50])
upper_bounds = np.array([70049, 5000, 3, 10000, 180, 1080, 1080, 5, 20000, 500])


# Adjusted function to plot with x[6] and x[9], fixing the rest of the variables
def adjusted_objective_for_x6_x9(x6, x9, fixed_x):
    x = fixed_x.copy()
    x[6], x[9] = x6, x9
    return objective(x)


# Midpoints for variables not being varied in the plot
fixed_x = (lower_bounds + upper_bounds) / 2

# Ranges for variables x[6] and x[9] to be varied in the plot
x6_range = np.linspace(lower_bounds[6], upper_bounds[6], 50)
x9_range = np.linspace(lower_bounds[9], upper_bounds[9], 50)

# Create meshgrid for x[6] and x[9]
X6, X9 = np.meshgrid(x6_range, x9_range)
Z = np.zeros(X6.shape)

# Calculate Z values using the adjusted objective function
for i in range(X6.shape[0]):
    for j in range(X6.shape[1]):
        Z[i, j] = adjusted_objective_for_x6_x9(X6[i, j], X9[i, j], fixed_x)

# Plotting
fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')
surf = ax.plot_surface(X6, X9, Z, cmap='jet', edgecolor='none')
fig.colorbar(surf, ax=ax, shrink=0.5, aspect=5)
ax.set_xlabel('x[6]')
ax.set_ylabel('x[9]')
ax.set_zlabel('Objective Function Value')
ax.set_title('3D Plot of the Small-Scale Farmers\' Objective Function with '
             'Variables x[6] (Quantity Supplied) and '
             'x[9] (Market Access License Fee)')
plt.show()
