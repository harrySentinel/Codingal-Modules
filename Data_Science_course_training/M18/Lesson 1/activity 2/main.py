import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

X, y = make_classification(n_samples=200, n_features=2, n_informative=2,
                            n_redundant=0, random_state=42)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

k_values = range(1, 21)
accuracies = []

for k in k_values:
    knn = KNeighborsClassifier(n_neighbors=k)
    knn.fit(X_train, y_train)
    y_pred = knn.predict(X_test)
    accuracies.append(accuracy_score(y_test, y_pred))
    print(f"K={k:2d}  Accuracy: {accuracy_score(y_test, y_pred)*100:.2f}%")

best_k = k_values[np.argmax(accuracies)]
print(f"\nBest K: {best_k} with accuracy {max(accuracies)*100:.2f}%")

plt.plot(k_values, accuracies, marker='o', color='blue')
plt.xlabel('K Value')
plt.ylabel('Accuracy')
plt.title('KNN Accuracy for Different K Values')
plt.xticks(k_values)
plt.grid(True)
plt.show()
