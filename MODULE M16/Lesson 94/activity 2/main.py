import seaborn as sns

df = sns.load_dataset('titanic')

df['sex_encoded'] = df['sex'].map({'male': 0, 'female': 1})

print("Gender Encoding (male=0, female=1):")
print(df[['sex', 'sex_encoded']].head(10))
print()

df['age'].fillna(df['age'].median(), inplace=True)
print("Missing Age values after filling:", df['age'].isnull().sum())
print()

df['age_group'] = df['age'].apply(
    lambda x: 'Child' if x < 18 else ('Adult' if x < 60 else 'Senior')
)
print("Age Group Distribution:")
print(df['age_group'].value_counts())
