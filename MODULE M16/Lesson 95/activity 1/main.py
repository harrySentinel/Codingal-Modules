import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset('titanic')
df['age'].fillna(df['age'].median(), inplace=True)

corr = df[['survived', 'pclass', 'age', 'fare', 'sibsp', 'parch']].corr()

print("Correlation Table:")
print(corr)

plt.figure(figsize=(7, 5))
sns.heatmap(corr, annot=True, cmap='coolwarm', fmt='.2f')
plt.title("Correlation Between Variables")
plt.tight_layout()
plt.savefig("correlation.png")
plt.show()
