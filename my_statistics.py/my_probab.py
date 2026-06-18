import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm    # normal distribution calculator

#normal distribution the bell curve
#normal distribution with mean 165cm and standard daviation 7cm
mean_h, std_h = 165, 7

#probability of being taller than 175 cm
prob = 1 - norm.cdf(175, mean_h, std_h)      #cumulative distriution function
print(f'P(height>175cm) = {prob: .4f} = {prob*100: .1f}%')

#the 98-95-99.7 rule
print(f'68% of people: {mean_h - std_h: .0f}cm to {mean_h + std_h: .0f}cm')
print(f'95% of people: {mean_h - 2*std_h: .0f}cm to {mean_h + 2*std_h: .0f}cm')
print(f'99.7% of people: {mean_h - 3*std_h: .0f}cm to {mean_h + 3*std_h: .0f}cm')
