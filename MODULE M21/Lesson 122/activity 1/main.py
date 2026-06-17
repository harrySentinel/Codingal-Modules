from tensorflow import keras
from tensorflow.keras import layers

print("Layers in a CNN")
print()
print("Key CNN Layers:")
print("  Conv2D      - Detects features like edges, shapes")
print("  MaxPooling2 - Reduces image size, keeps important features")
print("  Flatten     - Converts 2D feature map to 1D vector")
print("  Dense       - Fully connected layer for classification")
print("  Dropout     - Prevents overfitting")
print()

model = keras.Sequential([
    layers.Conv2D(32, (3, 3), activation='relu', input_shape=(28, 28, 1)),
    layers.MaxPooling2D((2, 2)),

    layers.Conv2D(64, (3, 3), activation='relu'),
    layers.MaxPooling2D((2, 2)),

    layers.Flatten(),
    layers.Dense(64, activation='relu'),
    layers.Dropout(0.3),
    layers.Dense(10, activation='softmax')
])

model.summary()

print()
print("Total parameters:", model.count_params())
