# **********************************************************************
# Baseline using Random Search ----
#
# Course Code: ME555
# Course Name: Design Optimization
# University of Michigan
# Semester Duration: 10th Jan 2024 to 29th April 2024
# 
## Purpose: ----
# Perform function optimization using a random search (a naive optimization
# algorithm) to obtain the baseline. The baseline will be used as a point
# of comparison for more sophisticated optimization algorithms.
# **********************************************************************

import math
import statistics
import numpy as np


# Objective Function
def objective(r, cw, t, ce, mal, tal):
    return 1 * (r ** -1.0) - 1 * (1 * (math.sin(cw / t)) + 1 * (ce)) + 1 * (mal ** -1) - 1 * (tal ** -1)


# Constraints
# For small-scale farmers
r_min, r_max = 0.0, 25000.0
cw_min, cw_max = 400.0, 5000.0
ce_min, ce_max = 300.0, 9000.0
mal_min, mal_max = 800.0, 1500.0
tal_min, tal_max = 1000.0, 15000.0

# Parameters
t = 3
p = 55

# Design Space
# Generate random samples within the design space
r_design_space = r_min + np.random.rand(100) * (r_max - r_min)
cw_design_space = cw_min + np.random.rand(100) * (cw_max - cw_min)
ce_design_space = ce_min + np.random.rand(100) * (ce_max - ce_min)
mal_design_space = mal_min + np.random.rand(100) * (mal_max - mal_min)
tal_design_space = tal_min + np.random.rand(100) * (tal_max - tal_min)

# Range Space
# Evaluate the objective function for each sample
range_space = np.array([objective(r, cw, t, ce, mal, tal)
                        for r, cw, ce, mal, tal in zip(r_design_space,
                                             cw_design_space, ce_design_space,
                                              mal_design_space,
                                              tal_design_space)])

# Identify the index of the optimum result
optimum_index = np.argmin(range_space)

# Print the Result
print('Optimum: f(r=%.4f, cw=%.4f, ce=%.4f, mal=%.4f, tal=%.4f) = %.4f' % 
      (r_design_space[optimum_index], cw_design_space[optimum_index], 
       ce_design_space[optimum_index], mal_design_space[optimum_index],
       tal_design_space[optimum_index],
       range_space[optimum_index]))