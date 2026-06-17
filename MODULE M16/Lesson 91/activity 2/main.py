import seaborn as sns

df = sns.load_dataset('titanic')

print("Age Statistics:")
print("Mean Age:  ", round(df['age'].mean(), 2))
print("Median Age:", df['age'].median())
print("Mode Age:  ", df['age'].mode()[0])
print()
print("Fare Statistics:")
print("Mean Fare:  ", round(df['fare'].mean(), 2))
print("Median Fare:", df['fare'].median())
print("Min Fare:   ", df['fare'].min())
print("Max Fare:   ", df['fare'].max())
