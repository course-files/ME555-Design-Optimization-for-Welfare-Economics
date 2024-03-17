from math import pi


T = 6  # Total duration of the cycle in months
B = 2 * pi / T  # B value based on the period T


# Target month for the peak is month 6
target_peak_month = 6


# Solving for phase
phase = target_peak_month - (pi/2) / B


print("Phase = ", phase)