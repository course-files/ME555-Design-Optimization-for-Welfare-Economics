# **********************************************************************
# Genetic Algorithm (GA) ----
#
# Course Code: ME555
# Course Name: Design Optimization
# University of Michigan
# Semester Duration: 10th Jan 2024 to 29th April 2024
# 
# Purpose ----
# Perform function optimization using the Genetic Algorithm (GA)
# algorithm.
# **********************************************************************

# Imports ----
import numpy as np
import random
from deap import base, creator, tools, algorithms


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


# Objective Function
def objective(individual):
    x = np.array(individual)
    return objective_function(x, None),  # Note: grad is not used


# Constraint Functions as penalty
def constraint_penalty(individual):
    x = np.array(individual)
    penalties = sum([
        max(0, g1(x, None)),
        max(0, g2(x, None)),
        max(0, g3(x, None)),
        max(0, g4(x, None)),
        max(0, g5(x, None)),
        max(0, g6(x, None)),
        max(0, g7(x, None)),
        max(0, g8(x, None)),
        max(0, g9(x, None)),
    ])
    return penalties,


# Modify the individual if it violates the bounds
def checkBounds(mins, maxs):
    def decorator(func):
        def wrapper(*args, **kargs):
            offspring = func(*args, **kargs)
            for child in offspring:
                for i in range(len(child)):
                    if child[i] > maxs[i]:
                        child[i] = maxs[i]
                    elif child[i] < mins[i]:
                        child[i] = mins[i]
            return offspring
        return wrapper
    return decorator

creator.create("FitnessMin", base.Fitness, weights=(-1.0,))
creator.create("Individual", list, fitness=creator.FitnessMin)

toolbox = base.Toolbox()
toolbox.register("attr_float", random.uniform, lower_bounds[0], upper_bounds[0])
toolbox.register("individual", tools.initRepeat, creator.Individual,
                 toolbox.attr_float, n=len(lower_bounds))
toolbox.register("population", tools.initRepeat, list, toolbox.individual)

toolbox.register("evaluate", objective)
toolbox.decorate("evaluate", tools.DeltaPenalty(constraint_penalty, 1000))
toolbox.register("mate", tools.cxBlend, alpha=0.5)
toolbox.register("mutate", tools.mutGaussian, mu=0, sigma=1, indpb=0.1)
toolbox.register("select", tools.selTournament, tournsize=3)
toolbox.decorate("mate", checkBounds(lower_bounds, upper_bounds))
toolbox.decorate("mutate", checkBounds(lower_bounds, upper_bounds))

population_size = 50
crossover_probability = 0.7
mutation_probability = 0.2
number_of_generations = 100

pop = toolbox.population(n=population_size)
hof = tools.HallOfFame(1)
stats = tools.Statistics(lambda ind: ind.fitness.values)
stats.register("avg", np.mean)
stats.register("min", min)
stats.register("max", max)

result, log = algorithms.eaSimple(pop, toolbox, cxpb=crossover_probability, mutpb=mutation_probability,
                                   ngen=number_of_generations, stats=stats, halloffame=hof, verbose=True)

print("Best individual is:", hof[0], "with fitness:", hof[0].fitness.values)
