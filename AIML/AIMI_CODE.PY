import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

# data

n_A , conv_A = 1000,52
n_B, conv_B = 1000,68

rate_A = conv_A / n_A
rate_B = conv_B / n_B

print(f'Version A conversion rate: {rate_A*100: .1f}%')
print(f'Version B conversion rate: {rate_B*100: .1f}%')
print(f'Improvement: {(rate_B-rate_A) / rate_A*100: .1f}%')

# chi-value
#chi- square test for statistical significance
table = [[conv_A,n_A-conv_A],[conv_B, n_B-conv_B]]
chi2, p_value, dof, expected = stats.chi2_contingency(table)

print(f'Chi-square: {chi2: .4f}')
print(f'P-value: {p_value: .4f}')
print('Result:','significant - B is better!' if p_value<0.05 else 'Not significant- could be rndom')

