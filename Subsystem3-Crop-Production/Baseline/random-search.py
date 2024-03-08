# **********************************************************************
# Baseline using Random Search ----
#
# Course Code: ME555
# Course Name: Design Optimization
# Semester Duration: 10th Jan 2024 to 29th April 2024
# University of Michigan
# 
## Purpose: ----
# Perform function optimization using a random search (a naive optimization
# algorithm) to obtain the baseline. The baseline will be used as a point
# of comparison for more sophisticated optimization algorithms.
# **********************************************************************

import math
import numpy as np


# Objective Function
def objective(r, cw, T):
    return r ** -1.0 - math.sin(cw / T)


# Constraints
r_min, r_max = 0.0, 25000.0
cw_min, cw_max = 400.0, 5000.0

# Parameters
T = 3

# Design Space
# Generate random samples within the design space
r_design_space = r_min + np.random.rand(100) * (r_max - r_min)
cw_design_space = cw_min + np.random.rand(100) * (cw_max - cw_min)

# Range Space
# Evaluate the objective function for each sample
range_space = np.array([objective(r, cw, T) 
                        for r, cw in zip(r_design_space, cw_design_space)])

# Identify the index of the optimum result
optimum_index = np.argmin(range_space)

# Print the Result
print('Optimum: f(r=%.5f, cw=%.5f) = %.5f' % 
      (r_design_space[optimum_index], cw_design_space[optimum_index], 
       range_space[optimum_index]))