import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from tensorflow import keras
from tensorflow.keras import layers
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

data = {
    "Area":     [500, 750, 1000, 1200, 1500, 800, 950, 1100, 1300, 600,
                 700, 1400, 900, 1050, 1600, 850, 1250, 650, 1150, 1350],
    "Rooms":    [1, 2, 3, 3, 4, 2, 2, 3, 3, 1, 2, 4, 2, 3, 4, 2, 3, 1, 3, 4],
    "Age":      [5, 10, 3, 8, 2, 15, 6, 4, 7, 12, 9, 1, 11, 5, 3, 7, 6, 14, 4, 2],
    "Price":    [2500000, 3800000, 5500000, 6200000, 8500000, 3200000, 4100000,
                 5900000, 6800000, 2200000, 3000000, 8000000, 3700000, 5600000,
                 9000000, 3400000, 7000000, 2400000, 6000000, 7500000]
}

df = pd.DataFrame(data)

X = df[["Area", "Rooms", "Age"]].values
y = df["Price"].values / 1000000

scaler = StandardScaler()
X = scaler.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = keras.Sequential([
    layers.Dense(32, activation='relu', input_shape=(3,)),
    layers.Dense(16, activation='relu'),
    layers.Dense(1)
])

model.compile(optimizer='adam', loss='mse', metrics=['mae'])
history = model.fit(X_train, y_train, epochs=100, verbose=0, validation_split=0.1)

loss, mae = model.evaluate(X_test, y_test, verbose=0)
print("House Price Prediction using Keras")
print("Mean Absolute Error:", round(mae, 4), "million ₹")

plt.plot(history.history['loss'], label='Train Loss')
plt.plot(history.history['val_loss'], label='Val Loss')
plt.title("Training Loss - House Price Model")
plt.xlabel("Epochs")
plt.ylabel("Loss")
plt.legend()
plt.savefig("house_price_keras.png")
plt.show()

area  = float(input("\nArea (sqft): "))
rooms = float(input("Number of rooms: "))
age   = float(input("Age of house (years): "))
inp = scaler.transform([[area, rooms, age]])
price = model.predict(inp, verbose=0)[0][0]
print(f"Predicted Price: ₹{round(price, 2)} million")
