import numpy as np
import matplotlib.pyplot as plt
from tensorflow import keras
from sklearn.metrics import classification_report, confusion_matrix
import seaborn as sns

model = keras.models.load_model("digit_recognizer.h5")
X_test = np.load("X_test_digits.npy")
y_test = np.load("y_test_digits.npy")

print("Digit Recognizer using CNN - Part 2")
print()

loss, acc = model.evaluate(X_test, y_test, verbose=0)
print("Test Accuracy:", round(acc * 100, 2), "%")
print()

y_pred = np.argmax(model.predict(X_test, verbose=0), axis=1)
y_true = np.argmax(y_test, axis=1)

print("Classification Report:")
print(classification_report(y_true, y_pred))

plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
cm = confusion_matrix(y_true, y_pred)
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues')
plt.title("Confusion Matrix")
plt.xlabel("Predicted")
plt.ylabel("Actual")

plt.subplot(1, 2, 2)
for i in range(10):
    plt.subplot(2, 5, i + 1)
    plt.imshow(X_test[i].reshape(28, 28), cmap='gray')
    plt.title(f"P:{y_pred[i]} A:{y_true[i]}", fontsize=8)
    plt.axis('off')

plt.suptitle("Predictions vs Actual")
plt.tight_layout()
plt.savefig("digit_recognizer_results.png")
plt.show()
