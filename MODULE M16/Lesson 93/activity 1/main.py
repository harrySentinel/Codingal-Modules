import seaborn as sns
import numpy as np

df = sns.load_dataset('titanic')
age = df['age'].dropna()

q1 = age.quantile(0.25)
q2 = age.quantile(0.50)
q3 = age.quantile(0.75)

print("Titanic - Age Quartiles:")
print("Q1 (25%):", q1)
print("Q2 (50% - Median):", q2)
print("Q3 (75%):", q3)
print()
print("Quantiles:")
print("10th percentile:", age.quantile(0.10))
print("90th percentile:", age.quantile(0.90))
