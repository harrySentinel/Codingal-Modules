import numpy as np
import matplotlib.pyplot as plt
from tensorflow import keras
from tensorflow.keras import layers

(X_train, y_train), (X_test, y_test) = keras.datasets.mnist.load_data()

X_train = X_train.reshape(-1, 28, 28, 1) / 255.0
X_test  = X_test.reshape(-1, 28, 28, 1)  / 255.0

y_train = keras.utils.to_categorical(y_train, 10)
y_test  = keras.utils.to_categorical(y_test, 10)

print("Digit Recognizer using CNN - Part 1")
print()
print("Dataset: MNIST")
print("Training samples:", X_train.shape[0])
print("Image size: 28x28 pixels, Grayscale")
print()

model = keras.Sequential([
    layers.Conv2D(32, (3, 3), activation='relu', input_shape=(28, 28, 1)),
    layers.MaxPooling2D((2, 2)),
    layers.Conv2D(64, (3, 3), activation='relu'),
    layers.MaxPooling2D((2, 2)),
    layers.Flatten(),
    layers.Dense(64, activation='relu'),
    layers.Dense(10, activation='softmax')
])

model.summary()
print()

model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
history = model.fit(X_train, y_train, epochs=5, batch_size=128,
                    validation_split=0.1, verbose=1)

model.save("digit_recognizer.h5")
print()
print("Model saved as digit_recognizer.h5")

np.save("X_test_digits.npy", X_test)
np.save("y_test_digits.npy", y_test)
print("Test data saved for Part 2.")
