import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset('titanic')
df['age'].fillna(df['age'].median(), inplace=True)

print("Average Age and Fare by Passenger Class:")
print(df.groupby('pclass')[['age', 'fare']].mean().round(2))
print()
print("Survival Rate by Class and Gender:")
print(df.groupby(['pclass', 'sex'])['survived'].mean().apply(lambda x: f"{round(x*100,1)}%"))

plt.figure(figsize=(7, 4))
sns.scatterplot(data=df, x='age', y='fare', hue='survived',
                palette={0: 'red', 1: 'green'}, alpha=0.6)
plt.title("Age vs Fare (Green = Survived)")
plt.xlabel("Age")
plt.ylabel("Fare")
plt.tight_layout()
plt.savefig("age_fare_scatter.png")
plt.show()
