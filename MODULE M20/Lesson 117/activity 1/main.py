import numpy as np

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def relu(x):
    return np.maximum(0, x)

print("Forward Propagation - Step by Step")
print()

inputs = np.array([0.5, 0.8, 0.3])
print("Input Layer:", inputs)
print()

W1 = np.array([[0.2, 0.4], [0.5, 0.1], [0.3, 0.7]])
b1 = np.array([0.1, 0.2])
z1 = np.dot(inputs, W1) + b1
a1 = relu(z1)
print("Hidden Layer:")
print("  Weighted sum (z1):", np.round(z1, 4))
print("  After ReLU  (a1):", np.round(a1, 4))
print()

W2 = np.array([[0.6, 0.9], [0.3, 0.4]])
b2 = np.array([0.05, 0.1])
z2 = np.dot(a1, W2) + b2
a2 = sigmoid(z2)
print("Output Layer:")
print("  Weighted sum (z2):", np.round(z2, 4))
print("  After Sigmoid (a2):", np.round(a2, 4))
print()
print("Final Output (prediction):", np.round(a2, 4))
print("Predicted class:", np.argmax(a2))
