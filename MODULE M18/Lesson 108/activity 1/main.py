import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score, mean_squared_error

data = {
    "Experience": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 3, 5, 7],
    "Age":        [22, 24, 25, 27, 28, 30, 32, 34, 35, 37, 26, 29, 31],
    "Skills":     [3, 4, 5, 6, 7, 8, 8, 9, 9, 10, 5, 7, 8],
    "Salary":     [30000, 38000, 45000, 53000, 61000, 69000, 76000, 84000, 91000, 99000,
                   44000, 60000, 75000]
}

df = pd.DataFrame(data)
print("Dataset:")
print(df)
print()

X = df[["Experience", "Age", "Skills"]]
y = df["Salary"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)

print("Coefficients:")
for feature, coef in zip(X.columns, model.coef_):
    print(f"  {feature}: {round(coef, 2)}")
print("Intercept:", round(model.intercept_, 2))
print()

y_pred = model.predict(X_test)
print("R² Score:", round(r2_score(y_test, y_pred), 3))
print("RMSE:    ", round(np.sqrt(mean_squared_error(y_test, y_pred)), 2))
print()

exp = float(input("Experience (years): "))
age = float(input("Age: "))
skills = float(input("Skill score (1-10): "))
salary = model.predict([[exp, age, skills]])[0]
print(f"Predicted Salary: ₹{round(salary, 2)}")

plt.scatter(y_test, y_pred, color='green')
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'r--')
plt.title("Actual vs Predicted Salary")
plt.xlabel("Actual Salary")
plt.ylabel("Predicted Salary")
plt.savefig("multiple_regression.png")
plt.show()
