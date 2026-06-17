import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix

data = {
    "Age":    [22, 25, 47, 52, 46, 56, 55, 60, 62, 61, 18, 28, 35, 42, 48],
    "Salary": [25000, 30000, 52000, 65000, 58000, 72000, 68000, 80000, 85000, 90000,
               20000, 35000, 45000, 55000, 62000],
    "Bought": [0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1]
}

df = pd.DataFrame(data)
print("Binary Classification - Purchased Product?")
print(df)
print()

X = df[["Age", "Salary"]]
y = df["Bought"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LogisticRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
print("Accuracy:", round(accuracy_score(y_test, y_pred) * 100, 1), "%")
print()
print("Confusion Matrix:")
print(confusion_matrix(y_test, y_pred))

age = float(input("\nEnter Age: "))
salary = float(input("Enter Salary: "))
result = model.predict([[age, salary]])[0]
print("Will buy product?", "YES" if result == 1 else "NO")
