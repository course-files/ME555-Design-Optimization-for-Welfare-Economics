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
    The variables and parameters have been coded as follows:
    x[0] = r
    x[1] = amp_w
    x[2] = t_w
    x[3] = tp_w
    x[4] = phase_w
    x[5] = vert_w
    x[6] = acre
    x[7] = c_w
    x[8] = qe
    x[9] = ce
    x[10] = qd
    x[11] = qs
    x[12] = amp_s
    x[13] = t_s
    x[14] = tp_s
    x[15] = phase_s
    x[16] = vert_s
    x[17] = tal
    x[18] = exp
    x[19] = mal
    """
    # Model without parameter values
    # return (1 * (x[0] ** -1.0) - 1 * ((np.sin(x[1] / x[2])) * (x[3])) +
    #         (x[4]) ** 1 + 1 * (x[5]) ** -1.0 + 1 * ((np.sin(x[6] / x[7])) - x[5]) -
    #         1 * (x[8] ** -1)) - (x[9] ** -1.0)

    # return ((10 * (x[0] ** -1.0) - 0.00001159 * ((np.sin(x[1] / x[2])) * (x[3])) -
    #         6.029 * (x[4]) + 10 * (x[5]) ** -1.0 - 4.03 * ((np.sin(x[6] / x[7])) - x[5]) -
    #         10 * -(x[8] ** -1)) - (x[9] ** -1.0) - 10)
    return (
        0.2350747 * x[0] ** (-1.0)
        + 0.4804318 * (
            (((x[1] * np.sin((2 * np.pi) / x[2] * (x[3] - x[4])) + x[5]) * x[6] * x[7]) ** 0.4) * 
            (x[8] * x[6] * x[9]) ** 0.6 
        )
        + 0.2811869 * x[10]
        - 0.9963252 * x[11]
        - 0.1230044 * ((x[12] * np.sin((2 * np.pi) / x[13] * (x[14] - x[15])) + x[16]) - x[10])
        + 0.2777817 * x[17] ** (-1.0)
        + 1.1544897 * x[16] ** (-1.0)
        + 0.1500959 * x[18] ** (-1.0)
        + 0.1491099 * x[19] ** (-1.0)
        + 0.0004785
    )


# Constraint Functions ----
def g1(x):
    return x[17] - x[0]


def g2(x):
    return ((x[1] * np.sin((2 * np.pi) / x[2] * (x[3] - x[4])) + x[5]) * x[6] * x[7]) - x[0]


def g3(x):
    return (x[8] * x[6] * x[9]) - x[0]


def g4(x):
    return x[10] + 1000 - (x[12] * np.sin((2 * np.pi) / x[13] * (x[14] - x[15])) + x[16])


def g5(x):
    return x[0] - (x[18] + x[19])


def g6(x):
    return x[10] - x[11] - 1000


def g7(x):
    return x[11] - x[10] - 1000


def g8(x):
    return x[19] - x[17]


def g9(x):
    return x[18] - x[19]


# Constraint Bounds ----
lower_bounds = np.array([34.58, 10000, 6, 6, 4.5, 26305.14, 0.1, 0.00044, 5,
                         1.49, 720, 720, 180, 6, 6, 4.5, 720, 37, 0.37, 0.37])
upper_bounds = np.array([345.58, 10000, 6, 6, 4.5, 26305.14, 20, 0.00044, 100,
                         1.49, 3600, 3600, 675, 6, 6, 4.5, 2700, 7400, 148,
                         444.42])


# Function to check if a solution is feasible
def is_feasible(x):
    return all([
        g1(x) <= 0,
        g2(x) <= 0,
        g3(x) <= 0,
        # Tolerance Level
        # The tolerance checks whether the absolute value of the constraint
        # function is within a range of -1e3 to 1e3. This is a form of relaxed
        # constraint, allowing solutions where the constraint deviates
        # from zero, up to 0.001 units in either direction.
        # abs(g4(x)) <= 1e-3, # Tolerance level
        g4(x) <= 0,
        g5(x) <= 0,
        g6(x) <= 0,
        g7(x) <= 0,
        g8(x) <= 0,
        g9(x) <= 0
    ])


# Perform a Random Search for a Feasible Solution ----
num_samples = 100000  # Increase if needed to find a feasible solution
best_f = float('inf')
best_x = None

for _ in range(num_samples):
    # Generate a random sample within the bounds
    x = lower_bounds + np.random.rand(20) * (upper_bounds - lower_bounds)
    
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
    x_opt_formatted = ", ".join([f"{x:.8f}" for x in best_x])
    print(f"Best feasible random solution found: [{x_opt_formatted}], "
          f"with minimum value: {best_f:.8f}")
else:
    print("No feasible solution found within the given number of samples. "
          "Consider increasing the number of samples or revising the constraints.")
