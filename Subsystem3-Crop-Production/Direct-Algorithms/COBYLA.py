# **********************************************************************
# ==== Constrained Optimization BY Linear Approximations (COBYLA) ====
#
# Course Code: ME555
# Course Name: Design Optimization
# University of Michigan
# Semester Duration: 10th Jan 2024 to 29th April 2024
# 
# ==== Purpose ====
# Perform function optimization using the Constrained Optimization BY Linear
# Approximations (COBYLA) algorithm.
# **********************************************************************

# ==== Imports ====
import nlopt
import numpy as np


# ==== Objective Function ====
def objective_function(x, grad):
    """
    This is the objective function to be minimized.
    Parameter 'grad' is for gradient, which we don't use with DIRECT, but it's part of the function signature.
    r = x[0]
    cw = x[1]
    t = x[2]
    ce = x[3]
    qs_stddev = x[4]
    qd = x[5]
    qs = x[6]
    mal = x[7]
    tal = x[8]
    """
    return (1 * (x[0] ** -1.0) - 1 * (1 * (np.sin(x[1] / x[2])) ** 2/3 * 1 * (x[3]) ** 1/3) +
            (x[4]) ** 2 + 1 * (x[5]) + 1 * (x[6] - x[5]) +
            1 * (x[7] ** -1) - 1 * (x[8] ** -1))


# ==== Constraint Functions ====
# Inequality constraint function in the form g(x) <= 0
def g1(x, grad):
    return x[7] - x[0]


# Inequality constraint function in the form g(x) <= 0
def g2(x, grad):
    return np.sin(x[1] / x[2]) + x[3] - x[0]


# Equality constraint function in the form h(x) = 0
def h1(x, grad):
    return x[6] - x[5]


# ==== Constraint Bounds ====
lower_bounds = [1, 400, 3, 300, 1, 1, 1, 800, 1]
upper_bounds = [25000, 5000, 3, 9000, 750, 2500, 2500, 1500, 15000]

# ==== Optimizer Object ====
# Create an optimizer object with 9 dimensions for COBYLA
opt = nlopt.opt(nlopt.LN_COBYLA, 9)

# Set the objective function
opt.set_min_objective(objective_function)

# Add the inequality constraints with a tolerance for how closely it must be met
opt.add_inequality_constraint(g1, 1e0)
opt.add_inequality_constraint(g2, 1e0)

# Add the equality constraint.
opt.add_equality_constraint(h1, 1e0)

# Set the lower bounds and upper bounds
opt.set_lower_bounds(lower_bounds)
opt.set_upper_bounds(upper_bounds)

# Set stopping criteria
opt.set_xtol_rel(1e-4)
opt.set_maxeval(1000)

# ==== Perform the Optimization ====
# Initialization point
x_opt = opt.optimize([1, 400, 3, 300, 1, 1, 1, 800, 1])
min_f = opt.last_optimum_value()

print(f"Optimal solution found: {x_opt}, with minimum value: {min_f}")
