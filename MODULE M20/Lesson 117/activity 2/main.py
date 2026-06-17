import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-5, 5, 100)

sigmoid  = 1 / (1 + np.exp(-x))
relu     = np.maximum(0, x)
tanh     = np.tanh(x)
leaky    = np.where(x > 0, x, 0.1 * x)

fig, axes = plt.subplots(2, 2, figsize=(10, 7))
fig.suptitle("Activation Functions in Neural Networks", fontsize=13)

axes[0, 0].plot(x, sigmoid, color='blue')
axes[0, 0].set_title("Sigmoid  →  output: 0 to 1")
axes[0, 0].axhline(0, color='k', linewidth=0.5)
axes[0, 0].grid(True)

axes[0, 1].plot(x, relu, color='green')
axes[0, 1].set_title("ReLU  →  output: 0 or positive")
axes[0, 1].axhline(0, color='k', linewidth=0.5)
axes[0, 1].grid(True)

axes[1, 0].plot(x, tanh, color='red')
axes[1, 0].set_title("Tanh  →  output: -1 to 1")
axes[1, 0].axhline(0, color='k', linewidth=0.5)
axes[1, 0].grid(True)

axes[1, 1].plot(x, leaky, color='purple')
axes[1, 1].set_title("Leaky ReLU  →  allows small negatives")
axes[1, 1].axhline(0, color='k', linewidth=0.5)
axes[1, 1].grid(True)

plt.tight_layout()
plt.savefig("activation_functions.png")
plt.show()

print("Activation Function Summary:")
print("  Sigmoid    - Used in output layer for binary classification")
print("  ReLU       - Most popular for hidden layers")
print("  Tanh       - Similar to sigmoid but outputs -1 to 1")
print("  Leaky ReLU - Fixes dying ReLU problem")
