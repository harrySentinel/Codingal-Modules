import seaborn as sns
import pandas as pd

df = sns.load_dataset('titanic')

print("Titanic Dataset - First 5 rows:")
print(df.head())
print()
print("Shape:", df.shape)
print()
print("Columns:", list(df.columns))
print()
print("Survival Count:")
print(df['survived'].value_counts())
print()
print("0 = Did not survive, 1 = Survived")
