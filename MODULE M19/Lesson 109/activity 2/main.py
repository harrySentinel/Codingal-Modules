import numpy as np
import matplotlib.pyplot as plt
from sklearn import svm
from sklearn.datasets import make_classification

X, y = make_classification(n_samples=50, n_features=2, n_redundant=0,
                            n_clusters_per_class=1, random_state=42)

model = svm.SVC(kernel='linear')
model.fit(X, y)

print("Maximum Margin Classifier - SVM")
print()
print("Support Vectors:", len(model.support_vectors_))
print("Classes:", model.classes_)
print()

w = model.coef_[0]
b = model.intercept_[0]
print("Decision Boundary: {:.2f}x1 + {:.2f}x2 + {:.2f} = 0".format(w[0], w[1], b))

plt.figure(figsize=(7, 5))
plt.scatter(X[y == 0][:, 0], X[y == 0][:, 1], color='blue', label='Class 0')
plt.scatter(X[y == 1][:, 0], X[y == 1][:, 1], color='red', label='Class 1')
plt.scatter(model.support_vectors_[:, 0], model.support_vectors_[:, 1],
            s=150, facecolors='none', edgecolors='black', label='Support Vectors')

x_vals = np.linspace(X[:, 0].min(), X[:, 0].max(), 100)
y_vals = -(w[0] * x_vals + b) / w[1]
plt.plot(x_vals, y_vals, 'k-', label='Decision Boundary')

plt.title("Maximum Margin Separating Hyperplane (SVM)")
plt.legend()
plt.savefig("svm_margin.png")
plt.show()
