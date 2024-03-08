# **********************************************************************
# Function Optimization using SLSQP ----
# SLSQP stands for Sequential Least Squares Programming
#
# Course Code: ME555
# Course Name: Design Optimization
# University of Michigan
# Semester Duration: 10th Jan 2024 to 29th April 2024
# 
# **********************************************************************
import math
import numpy as np
from scipy.optimize import minimize

# Objective function
def objective(x):
    return (1 * (x[0] ** -1.0) - 1 * (1 * (math.sin(x[1] / x[2])) ** 2/3 * 1 * (x[3]) ** 1/3) +
            (x[4]) ** 2 + 1 * (x[5]) + 1 * (x[6] - x[5]) +
            1 * (x[7] ** -1) - 1 * (x[8] ** -1))
# r = x[0]
# cw = x[1]
# t = x[2]
# ce = x[3]
# qs_stddev = x[4]
# qd = x[5]
# qs = x[6]
# mal = x[7]
# tal = x[8]

# ==== Constraint Bounds ====
bounds = [(0, 25000), (400, 5000), (3,3), (300, 9000), (0, 750), (0, 2500), (0, 2500), (800, 1500), (0, 15000)]

# ==== Constraint Functions ====
def g1(x):
    return x[7] - x[0]

def g2(x):
    return (math.sin(x[1] / x[2]) + x[3] - x[0])

def g3(x):
    return x[6] - x[5]

def g4(x):
    return x[4] - 1.15

def g5(x):
    return (0.15 / x[0]) - x[7]

# Constraints
constraints = [{'type': 'ineq', 'fun': g1},
               {'type': 'ineq', 'fun': g2},
               {'type': 'eq', 'fun': g3},
               {'type': 'ineq', 'fun': g4},
               {'type': 'ineq', 'fun': g5}]

# ==== Initialization ====
init = [2362.2061, 3776.6741, 3, 8548.9602, 669.9823, 191.6636, 946.5487, 1272.7085, 6384.6091]

# ==== Perform the Optimization ====
result = minimize(objective, init, method='SLSQP', bounds=bounds, constraints=constraints)

# ==== Print the Result ====
print("\n***Result***")
formatted_numbers = [f"{num:.2f}" for num in result.x]
print("Solution: ",formatted_numbers)
print(f"\nObjective value: {result.fun: .2f}")