# **********************************************************************
# Baseline using Random Search ----
#
# Course Code: ME555
# Course Name: Design Optimization
# University of Michigan
# Semester Duration: 10th Jan 2024 to 29th April 2024
# 
# Purpose ----
# Perform function optimization using a random search (a naive optimization
# algorithm) to obtain the baseline. The baseline will be used as a point
# of comparison for more sophisticated optimization algorithms.
# **********************************************************************

# Imports ----
import numpy as np


# Objective Function ----
def objective_function(x):
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


# Constraint Functions ----
def g1(x):
    return x[8] - x[0]


def g2(x):
    return np.sin(x[1] / x[2]) + x[3] - x[0]


def g3(x):
    return (0.1 / x[6]) - x[4]


def g4(x):
    return x[9] - (0.15 / x[0])


def h1(x):
    return x[6] - x[5]


def h2(x):
    return x[2] - 3


def h3(x):
    return 5 - x[7]


# Function to check if a solution is feasible
def is_feasible(x):
    return all([
        g1(x) <= 0,
        g2(x) <= 0,
        g3(x) <= 0,
        abs(g4(x)) <= 1e3, # Tolerance level
        abs(h1(x)) <= 1e0,
        h2(x) == 0,
        h3(x) == 0
    ])


# Constraint Bounds ----
lower_bounds = np.array([46700, 20, 3, 2000, 0, 720, 720, 5, 5000, 50])
upper_bounds = np.array([70049, 5000, 3, 10000, 180, 1080, 1080, 5, 20000, 500])

# Perform a Random Search for a Feasible Solution ----
num_samples = 1000  # Increase if needed to find a feasible solution
best_f = float('inf')
best_x = None

for _ in range(num_samples):
    # Generate a random sample within the bounds
    x = lower_bounds + np.random.rand(10) * (upper_bounds - lower_bounds)
    
    # Check if the solution is feasible
    if is_feasible(x):
        # Evaluate the objective function
        f = objective_function(x)
        
        # Check if this is the best solution found so far
        if f < best_f:
            best_f = f
            best_x = x

# Check if a solution was found
if best_x is not None:
    x_opt_formatted = ", ".join([f"{x:.2f}" for x in best_x])
    print(f"Best feasible random solution found: [{x_opt_formatted}], "
          f"with minimum value: {best_f:.2f}")
else:
    print("No feasible solution found within the given number of samples. "
          "Consider increasing the number of samples or revising the constraints.")
