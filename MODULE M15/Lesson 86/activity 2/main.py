import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-10, 10, 300)

y1 = x ** 2
y2 = 2 * x + 3
y3 = np.sin(x)

plt.figure(figsize=(12, 4))

plt.subplot(1, 3, 1)
plt.plot(x, y1, color='red')
plt.title("y = x²")
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)

plt.subplot(1, 3, 2)
plt.plot(x, y2, color='green')
plt.title("y = 2x + 3")
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)

plt.subplot(1, 3, 3)
plt.plot(x, y3, color='blue')
plt.title("y = sin(x)")
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)

plt.tight_layout()
plt.savefig("equations.png")
plt.show()
