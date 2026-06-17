from tensorflow import keras
from tensorflow.keras import layers
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
import numpy as np

iris = load_iris()
X = iris.data
y = keras.utils.to_categorical(iris.target, 3)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

print("Trying Different Layer Configurations on Iris Dataset")
print()

configs = [
    ("Simple  (1 hidden layer)", [8]),
    ("Medium  (2 hidden layers)", [16, 8]),
    ("Deep    (3 hidden layers)", [32, 16, 8])
]

for name, units in configs:
    model = keras.Sequential()
    model.add(layers.Dense(units[0], activation='relu', input_shape=(4,)))
    for u in units[1:]:
        model.add(layers.Dense(u, activation='relu'))
    model.add(layers.Dense(3, activation='softmax'))

    model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
    model.fit(X_train, y_train, epochs=30, verbose=0)

    loss, acc = model.evaluate(X_test, y_test, verbose=0)
    print(f"{name} -> Accuracy: {round(acc * 100, 1)}%")
