import numpy as np
import matplotlib.pyplot as plt
from tensorflow import keras
from tensorflow.keras import layers

(X_train, y_train), (X_test, y_test) = keras.datasets.cifar10.load_data()

class_names = ['Airplane', 'Car', 'Bird', 'Cat', 'Deer',
               'Dog', 'Frog', 'Horse', 'Ship', 'Truck']

X_train = X_train / 255.0
X_test  = X_test  / 255.0

print("Image Classifier - Part 1 (Data Preparation)")
print()
print("Dataset: CIFAR-10")
print("Training images:", X_train.shape)
print("Testing images: ", X_test.shape)
print("Classes:", class_names)
print()

plt.figure(figsize=(12, 2))
for i in range(10):
    plt.subplot(1, 10, i + 1)
    plt.imshow(X_train[i])
    plt.title(class_names[y_train[i][0]], fontsize=7)
    plt.axis('off')
plt.suptitle("CIFAR-10 Sample Images")
plt.tight_layout()
plt.savefig("cifar10_samples.png")
plt.show()

print("Data loaded. Building the model in Part 2...")
np.save("X_train_img.npy", X_train[:5000])
np.save("X_test_img.npy",  X_test[:1000])
np.save("y_train_img.npy", y_train[:5000])
np.save("y_test_img.npy",  y_test[:1000])
print("Data saved for Part 2.")
