import numpy as np
import matplotlib.pyplot as plt
from tensorflow import keras
from tensorflow.keras import layers

print("Introduction to CNN - Training a Model for Images")
print()
print("What is a CNN?")
print("  CNN = Convolutional Neural Network")
print("  It is specially designed to work with images.")
print()
print("How it sees an image:")
print("  - An image is a grid of pixels")
print("  - Each pixel has a value (0-255) for color intensity")
print("  - CNN learns patterns like edges, shapes, and textures")
print()

(X_train, y_train), (X_test, y_test) = keras.datasets.mnist.load_data()

X_train = X_train / 255.0
X_test  = X_test  / 255.0

print("Dataset: MNIST (Handwritten Digits)")
print("Training images:", X_train.shape)
print("Testing images: ", X_test.shape)
print("Classes: 0 to 9")
print()

plt.figure(figsize=(10, 2))
for i in range(10):
    plt.subplot(1, 10, i + 1)
    plt.imshow(X_train[i], cmap='gray')
    plt.title(str(y_train[i]))
    plt.axis('off')
plt.suptitle("Sample Training Images")
plt.savefig("mnist_samples.png")
plt.show()

print("Images loaded and ready for CNN training!")
