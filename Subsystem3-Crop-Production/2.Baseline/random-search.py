# **********************************************************************
# Baseline using Random Search ----
#
# Course Code: ME555
# Course Name: Design Optimization
# University of Michigan
# Semester Duration: 10th Jan 2024 to 29th April 2024
# 
# ==== Purpose ====
# Perform function optimization using a random search (a naive optimization
# algorithm) to obtain the baseline. The baseline will be used as a point
# of comparison for more sophisticated optimization algorithms.
# **********************************************************************

# ==== Imports ====
import math
import statistics
import numpy as np

# ==== Objective Function ====
def objective(r, cw, t, ce, qs_stddev, qs, qd, mal, tal):
    return (1 * (r ** -1.0) - 1 * (1 * (math.sin(cw / t)) ** 2/3 * 1 * (ce) ** 1/3) +
            (qs_stddev) ** 2 + 1 * (qd) + 1 * (qs - qd) +
            1 * (mal ** -1) - 1 * (tal ** -1))


# ==== Constraint Bounds ====
# TODO: Identify correct constraints through data collection
# For small-scale farmers
r_min, r_max = 0.0, 25000.0
cw_min, cw_max = 400.0, 5000.0
ce_min, ce_max = 300.0, 9000.0
qs_min, qs_max = 0.0, 2500.0
qd_min, qd_max = 0.0, 2500.0
mal_min, mal_max = 800.0, 1500.0
tal_min, tal_max = 1000.0, 15000.0


# ==== Constraint Functions ====
# g1: c(tal) - r <= 0
def g1(tal, r):
    return tal - r


# g2: 1 * (1 * (math.sin(cw / t)) + 1 * (ce)) - r <= 0
def g2(cw, ce, t, r):
    return ((math.sin(cw / t)) + 1 * (ce)) - r


# Compile the constraints in the format scipy.optimize.minimize expects
constraints = [
    {'type': 'ineq', 'fun': g1},
    {'type': 'ineq', 'fun': g2}
]

# ==== Parameters ====
t = 3
# TODO: Confirm if price p should be used in the supply and demand functions
p = 55

# ==== Design Space ====
# Generate random samples within the design space
r_design_space = r_min + np.random.rand(100) * (r_max - r_min)
cw_design_space = cw_min + np.random.rand(100) * (cw_max - cw_min)
ce_design_space = ce_min + np.random.rand(100) * (ce_max - ce_min)
qs_design_space = qs_min + np.random.rand(100) * (qs_max - qs_min)
qs_stddev = statistics.stdev(qs_design_space)
qd_design_space = qd_min + np.random.rand(100) * (qd_max - qd_min)
mal_design_space = mal_min + np.random.rand(100) * (mal_max - mal_min)
tal_design_space = tal_min + np.random.rand(100) * (tal_max - tal_min)

# ==== Range Space ====
# Evaluate the objective function for each sample
range_space = np.array([objective(r, cw, t, ce, qs_stddev, qs, qd, mal, tal)
                        for r, cw, ce, qs, qd, mal, tal in zip(r_design_space,
                                             cw_design_space, ce_design_space,
                                             qs_design_space,
                                             qd_design_space,
                                             mal_design_space,
                                             tal_design_space)])

# ==== Index of Optimal Result in the Range Space ====
optimum_index = np.argmin(range_space)

# ==== Print the Result ====
# To get the random search output in CSV format (manual runs)
# print('%.2f, %.2f, %.2f, %.2f, %.2f, %.2f, '
#       '%.2f, %.2f, %.2f' %
print('Optimum: f(r=%.2f, cw=%.2f, ce=%.2f, qs_stddev=%.2f, qs=%.2f, qd=%.2f, '
      'mal=%.2f, tal=%.2f) = %.2f' %
      (r_design_space[optimum_index], cw_design_space[optimum_index], 
       ce_design_space[optimum_index], qs_stddev,
       qs_design_space[optimum_index], qd_design_space[optimum_index],
       mal_design_space[optimum_index], tal_design_space[optimum_index],
       range_space[optimum_index]))