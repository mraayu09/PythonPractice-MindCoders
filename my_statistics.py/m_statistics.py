import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats 

salaries = [22,28,35,42,38,55,48,60,72,85,30,45,60,72,85,30,45,52,65,28,34,41,58,75,90]  #employee salaries

mean = np.mean(salaries)                               # Average
median = np.median(salaries)                           #middle value when sorted
mode = stats.mode(salaries,keepdims=True).mode[0]      # most frequent

print(f'Mean (Average):  Rs.{mean:.1f}K')
print(f'Median (Middle value):  Rs.{median}K')
print(f'Mode (Most common):  Rs.{mode}K')

# spread- how varied is the data
std = np.std(salaries)   # standard daviation
var = np.var(salaries)   # variance(std squared)
rng = max(salaries)-min(salaries) # range
q1 = np.percentile(salaries,25)  # 25th percentile tak k log
q3 = np.percentile(salaries,75)  #75th percentile tak k log
iqr = q3-q1      # interquartile Range

print(f'Std Daviation: {std:.2f}K  (most important spread measure)')
print(f'IQR:  {iqr}K  (Q1={q1},  Q3={q3})')


# outlier detection using Iqr ( interquartile range)
lower = q1 - 1.5*iqr
upper = q3 + 1.5*iqr
outliers = [x for x in salaries if x < lower or x > upper]
print(f'Outliers: {outliers}')
