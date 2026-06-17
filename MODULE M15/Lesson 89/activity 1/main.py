import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

data = {
    "Area_sqft": [500, 750, 1000, 1200, 1500, 800, 950, 1100, 1300, 600,
                  700, 1400, 900, 1050, 1600],
    "Bedrooms": [1, 2, 3, 3, 4, 2, 2, 3, 3, 1, 2, 4, 2, 3, 4],
    "Rent": [12000, 18000, 30000, 26000, 50000, 16000, 21000, 33000, 28000, 11000,
             15000, 45000, 20000, 29000, 52000]
}

df = pd.DataFrame(data)

X = df[["Area_sqft", "Bedrooms"]]
y = df["Rent"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

print("Model Performance:")
print("R² Score:", round(r2_score(y_test, y_pred), 3))
print("RMSE:", round(np.sqrt(mean_squared_error(y_test, y_pred)), 2))

area = int(input("\nEnter area (sqft): "))
beds = int(input("Enter number of bedrooms: "))
predicted = model.predict([[area, beds]])[0]
print(f"Predicted Rent: ₹{round(predicted, 2)}")

plt.figure(figsize=(10, 4))

plt.subplot(1, 2, 1)
plt.scatter(df["Area_sqft"], df["Rent"], color='blue', label='Actual')
plt.title("Area vs Rent")
plt.xlabel("Area (sqft)")
plt.ylabel("Rent (₹)")
plt.legend()

plt.subplot(1, 2, 2)
plt.scatter(y_test, y_pred, color='green')
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'r--')
plt.title("Actual vs Predicted Rent")
plt.xlabel("Actual Rent")
plt.ylabel("Predicted Rent")

plt.tight_layout()
plt.savefig("rent_prediction.png")
plt.show()
