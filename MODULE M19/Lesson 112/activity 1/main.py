from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report

iris = load_iris()
X = iris.data
y = iris.target

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LogisticRegression(max_iter=200)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

print("Multi-class Classification - Iris Species Predictor")
print("Classes:", list(iris.target_names))
print()
print("Accuracy:", round(accuracy_score(y_test, y_pred) * 100, 1), "%")
print()
print(classification_report(y_test, y_pred, target_names=iris.target_names))

print("Enter flower measurements:")
sl = float(input("Sepal Length (cm): "))
sw = float(input("Sepal Width (cm): "))
pl = float(input("Petal Length (cm): "))
pw = float(input("Petal Width (cm): "))

prediction = model.predict([[sl, sw, pl, pw]])[0]
print("Predicted Species:", iris.target_names[prediction])
