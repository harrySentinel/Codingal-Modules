import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

data = {
    "Hours_Studied": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    "Attendance": [40, 50, 55, 60, 70, 75, 80, 85, 90, 95],
    "Pass": [0, 0, 0, 0, 1, 1, 1, 1, 1, 1]
}

df = pd.DataFrame(data)
print("Training Data:")
print(df)
print()

X = df[["Hours_Studied", "Attendance"]]
y = df["Pass"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = KNeighborsClassifier(n_neighbors=3)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
print("Predictions:", y_pred.tolist())
print("Accuracy:", round(accuracy_score(y_test, y_pred) * 100, 1), "%")
print()

hours = float(input("Enter hours studied: "))
attendance = float(input("Enter attendance %: "))
result = model.predict([[hours, attendance]])[0]
print("Result:", "PASS" if result == 1 else "FAIL")
