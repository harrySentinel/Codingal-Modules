import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report

data = {
    "Hours_Studied": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 2, 4, 6, 8, 3],
    "Mock_Score":    [30, 40, 45, 55, 60, 70, 75, 80, 88, 95, 35, 50, 65, 82, 48],
    "Pass":          [0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 0]
}

df = pd.DataFrame(data)
print("Dataset:")
print(df)
print()

X = df[["Hours_Studied", "Mock_Score"]]
y = df["Pass"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LogisticRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
print("Accuracy:", round(accuracy_score(y_test, y_pred) * 100, 1), "%")
print()
print(classification_report(y_test, y_pred, target_names=["Fail", "Pass"]))

hours = float(input("Hours studied: "))
score = float(input("Mock score: "))
result = model.predict([[hours, score]])[0]
prob = model.predict_proba([[hours, score]])[0][1]
print("Prediction:", "PASS" if result == 1 else "FAIL")
print("Pass Probability:", round(prob * 100, 1), "%")
