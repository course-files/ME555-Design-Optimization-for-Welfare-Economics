# **********************************************************************
# Sequential Least Squares Programming (SLSQP) ----
#
# Course Code: ME555
# Course Name: Design Optimization
# University of Michigan
# Semester Duration: 10th Jan 2024 to 29th April 2024
# 
# Purpose ----
# Perform function optimization using the Sequential Least Squares 
# Programming (SLSQP) algorithm.
# **********************************************************************

# Imports ----
import nlopt
import numpy as np


# Objective Function ----
def objective_function(x, grad):
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
def g1(x, grad):
    return x[17] - x[0]


def g2(x, grad):
    return ((x[1] * np.sin((2 * np.pi) / x[2] * (x[3] - x[4])) + x[5]) * x[6] * x[7]) - x[0]


def g3(x, grad):
    return (x[8] * x[6] * x[9]) - x[0]


def g4(x, grad):
    return x[10] + 1000 - (x[12] * np.sin((2 * np.pi) / x[13] * (x[14] - x[15])) + x[16])


def g5(x, grad):
    return x[0] - (x[18] + x[19])


def g6(x, grad):
    return x[10] - x[11] - 1000


def g7(x, grad):
    return x[11] - x[10] - 1000


def g8(x, grad):
    return x[19] - x[17]


def g9(x, grad):
    return x[18] - x[19]


# Constraint Bounds ----
lower_bounds = np.array([34.58, 10000, 6, 6, 4.5, 26305.14, 0.1, 0.00044, 5,
                         1.49, 720, 720, 180, 6, 6, 4.5, 720, 37, 0.37, 0.37])
upper_bounds = np.array([345.58, 10000, 6, 6, 4.5, 26305.14, 20, 0.00044, 100,
                         1.49, 3600, 3600, 675, 6, 6, 4.5, 2700, 7400, 148, 444.42])

# Optimizer Object ----
# Create an optimizer object with 20 dimensions for COBYLA
opt = nlopt.opt(nlopt.LD_SLSQP, 20)

# Set the objective function
opt.set_min_objective(objective_function)

# Add the inequality constraints
# with a tolerance for how closely they must be met
opt.add_inequality_constraint(g1, 1e-3)
opt.add_inequality_constraint(g2, 1e-3)
opt.add_inequality_constraint(g3, 1e-3)
opt.add_inequality_constraint(g4, 1e-3)
opt.add_inequality_constraint(g5, 1e-3)
opt.add_inequality_constraint(g6, 1e-3)
opt.add_inequality_constraint(g7, 1e-3)
opt.add_inequality_constraint(g8, 1e-3)
opt.add_inequality_constraint(g9, 1e-3)

# Add the equality constraints
# with a tolerance for how closely they must be met
# opt.add_equality_constraint(h1, 1e-2)

# Set the lower bounds and upper bounds
opt.set_lower_bounds(lower_bounds)
opt.set_upper_bounds(upper_bounds)

# Set stopping criteria
opt.set_xtol_rel(1e-3)
opt.set_maxeval(100000)

# Perform the Optimization ----
# Initialization point
x_opt = opt.optimize([190.08, 10000, 6, 6, 4.5, 26305.14, 10.05, 0.00044, 52.5,
                      1.49, 2160, 2160, 427.5, 6, 6, 4.5, 1710, 3718.5, 74.185,
                      222.395])
min_f = opt.last_optimum_value()

# print(f"Optimal solution found: {x_opt}, with minimum value: {min_f}")

x_opt_formatted = ", ".join([f"{x:.8f}" for x in x_opt])
print(f"Optimal solution found: [{x_opt_formatted}], with minimum value: {min_f:.8f}")
