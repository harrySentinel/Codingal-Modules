import matplotlib.pyplot as plt

def compute_cost(m, b, X, y):
    total = sum((y[i] - (m * X[i] + b)) ** 2 for i in range(len(X)))
    return total / len(X)

def gradient_descent(X, y, learning_rate=0.01, iterations=500):
    m, b = 0, 0
    n = len(X)
    cost_history = []

    for _ in range(iterations):
        y_pred = [m * x + b for x in X]
        dm = (-2/n) * sum(X[i] * (y[i] - y_pred[i]) for i in range(n))
        db = (-2/n) * sum(y[i] - y_pred[i] for i in range(n))
        m -= learning_rate * dm
        b -= learning_rate * db
        cost_history.append(compute_cost(m, b, X, y))

    return m, b, cost_history

X = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y = [30000, 38000, 45000, 52000, 60000, 68000, 75000, 83000, 90000, 98000]

X_norm = [x / 10 for x in X]
y_norm = [val / 100000 for val in y]

m, b, cost_history = gradient_descent(X_norm, y_norm)

print("Gradient Descent Results:")
print("Final Slope (m):    ", round(m, 4))
print("Final Intercept (b):", round(b, 4))
print("Final Cost:         ", round(cost_history[-1], 6))

plt.plot(cost_history, color='red')
plt.title("Gradient Descent - Cost over Iterations")
plt.xlabel("Iterations")
plt.ylabel("Cost")
plt.grid(True)
plt.savefig("gradient_descent.png")
plt.show()
