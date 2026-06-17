import seaborn as sns

df = sns.load_dataset('titanic')

print("Passenger Class Count:")
print(df['pclass'].value_counts())
print()
print("Gender Count:")
print(df['sex'].value_counts())
print()
print("Embarked (Port) Count:")
print(df['embarked'].value_counts())
print()
print("Survival by Gender:")
print(df.groupby('sex')['survived'].mean().apply(lambda x: f"{round(x*100, 1)}%"))
