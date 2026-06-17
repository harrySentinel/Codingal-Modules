import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_squared_error
import numpy as np

data = {
    "Experience_years": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    "Salary":           [30000, 38000, 45000, 52000, 60000, 68000, 75000, 83000, 90000, 98000]
}

df = pd.DataFrame(data)

X = df[["Experience_years"]]
y = df["Salary"]

model = LinearRegression()
model.fit(X, y)

print("Regression Analysis - Experience vs Salary")
print()
print("Slope (coefficient):", round(model.coef_[0], 2))
print("Intercept:          ", round(model.intercept_, 2))
print()
print(f"Formula: Salary = {round(model.coef_[0],2)} × Experience + {round(model.intercept_,2)}")
print()
print("R² Score:", round(r2_score(y, model.predict(X)), 3))
print("RMSE:    ", round(np.sqrt(mean_squared_error(y, model.predict(X))), 2))
print()

exp = float(input("Enter years of experience: "))
predicted = model.predict([[exp]])[0]
print(f"Predicted Salary: ₹{round(predicted, 2)}")

plt.scatter(df["Experience_years"], df["Salary"], color='blue', label='Actual')
plt.plot(df["Experience_years"], model.predict(X), color='red', label='Regression Line')
plt.title("Experience vs Salary")
plt.xlabel("Experience (years)")
plt.ylabel("Salary (₹)")
plt.legend()
plt.savefig("regression.png")
plt.show()
