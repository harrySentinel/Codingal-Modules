import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset('titanic')
fare = df['fare'].dropna()

q1 = fare.quantile(0.25)
q3 = fare.quantile(0.75)
iqr = q3 - q1

lower = q1 - 1.5 * iqr
upper = q3 + 1.5 * iqr

outliers = fare[(fare < lower) | (fare > upper)]

print("Fare IQR Analysis:")
print("Q1:", round(q1, 2))
print("Q3:", round(q3, 2))
print("IQR:", round(iqr, 2))
print("Lower Bound:", round(lower, 2))
print("Upper Bound:", round(upper, 2))
print("Number of Outliers:", len(outliers))

plt.figure(figsize=(6, 4))
plt.boxplot(fare, vert=False)
plt.title("Fare Distribution - Boxplot")
plt.xlabel("Fare")
plt.tight_layout()
plt.savefig("fare_boxplot.png")
plt.show()
