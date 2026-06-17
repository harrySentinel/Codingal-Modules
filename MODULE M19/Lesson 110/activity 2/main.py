import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

df = sns.load_dataset('titanic')
df = df[['survived', 'pclass', 'age', 'fare', 'sex']].dropna()
df['sex'] = df['sex'].map({'male': 0, 'female': 1})

X = df[['pclass', 'age', 'fare', 'sex']]
y = df['survived']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LogisticRegression(max_iter=500)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
print("Logistic Regression on Titanic Dataset")
print("Accuracy:", round(accuracy_score(y_test, y_pred) * 100, 1), "%")
print()
print("Coefficients:")
for feature, coef in zip(X.columns, model.coef_[0]):
    print(f"  {feature}: {round(coef, 4)}")

pclass = int(input("\nPassenger class (1/2/3): "))
age = float(input("Age: "))
fare = float(input("Fare paid: "))
sex = input("Gender (male/female): ").strip().lower()
sex_enc = 0 if sex == 'male' else 1

prob = model.predict_proba([[pclass, age, fare, sex_enc]])[0][1]
print(f"Survival Probability: {round(prob * 100, 1)}%")
