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

from numpy.random import rand


# Objective Function
def objective(x):
    return x ** 2.0


# Constraints
x_min, x_max = -5.0, 5.0

# Design Space
sample = x_min + rand(100) * (x_max - x_min)

# Range Space
sample_eval = objective(sample)

# Minimum Value in Range Space
optimum_ix = 0
for i in range(len(sample)):
    if sample_eval[i] < sample_eval[optimum_ix]:
        optimum_ix = i

# Print the Result
print('Optimum: f(%.5f) = %.5f' % (sample[optimum_ix], sample_eval[optimum_ix]))