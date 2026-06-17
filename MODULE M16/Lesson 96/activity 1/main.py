import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset('titanic')
df['age'].fillna(df['age'].median(), inplace=True)
df['embarked'].fillna(df['embarked'].mode()[0], inplace=True)

print("Dataset Info:")
print("Total Passengers:", len(df))
print("Survived:", df['survived'].sum())
print("Missing values after cleaning:")
print(df[['age', 'fare', 'embarked']].isnull().sum())
print()
print("Survival Rate:", f"{round(df['survived'].mean()*100, 1)}%")
print()
print("By Class:", df.groupby('pclass')['survived'].mean().apply(lambda x: f"{round(x*100,1)}%").to_dict())
print("By Gender:", df.groupby('sex')['survived'].mean().apply(lambda x: f"{round(x*100,1)}%").to_dict())

fig, axes = plt.subplots(2, 2, figsize=(12, 8))
fig.suptitle("Titanic - Exploratory Data Analysis", fontsize=14)

df['survived'].value_counts().plot(kind='bar', ax=axes[0, 0],
    color=['red', 'green'], rot=0)
axes[0, 0].set_title("Survival Count")
axes[0, 0].set_xticklabels(['Not Survived', 'Survived'])

axes[0, 1].hist(df['age'], bins=20, color='steelblue', edgecolor='black')
axes[0, 1].set_title("Age Distribution")
axes[0, 1].set_xlabel("Age")

sns.barplot(data=df, x='pclass', y='survived', ax=axes[1, 0], palette='Set2')
axes[1, 0].set_title("Survival Rate by Class")
axes[1, 0].set_xlabel("Passenger Class")

sns.barplot(data=df, x='sex', y='survived', ax=axes[1, 1], palette='Set1')
axes[1, 1].set_title("Survival Rate by Gender")

plt.tight_layout()
plt.savefig("titanic_eda.png")
plt.show()
