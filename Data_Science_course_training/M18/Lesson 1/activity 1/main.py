import numpy as np
import matplotlib.pyplot as plt
from collections import Counter

data = {
    'acid_durability': [7, 7, 3, 1],
    'strength':        [7, 4, 4, 4],
    'label':           ['Bad', 'Bad', 'Good', 'Good']
}

new_tissue = [3, 7]
k = 3

print("Training Data:")
for i in range(len(data['label'])):
    print(f"  Acid Durability: {data['acid_durability'][i]}, Strength: {data['strength'][i]}, Label: {data['label'][i]}")

print(f"\nNew Tissue to Predict: Acid Durability={new_tissue[0]}, Strength={new_tissue[1]}")

distances = []
for i in range(len(data['label'])):
    d = np.sqrt((data['acid_durability'][i] - new_tissue[0])**2 +
                (data['strength'][i] - new_tissue[1])**2)
    distances.append((d, data['label'][i]))
    print(f"  Distance to point {i+1}: {d:.2f}")

distances.sort(key=lambda x: x[0])
k_nearest = [label for _, label in distances[:k]]
print(f"\n{k} Nearest Neighbors: {k_nearest}")

prediction = Counter(k_nearest).most_common(1)[0][0]
print(f"Prediction for new tissue: {prediction}")

colors = {'Good': 'green', 'Bad': 'red'}
for i in range(len(data['label'])):
    plt.scatter(data['acid_durability'][i], data['strength'][i],
                color=colors[data['label'][i]], s=100, zorder=5)
    plt.text(data['acid_durability'][i]+0.1, data['strength'][i], data['label'][i])

plt.scatter(new_tissue[0], new_tissue[1], color='blue', marker='*', s=200, label='New Tissue')
plt.xlabel('Acid Durability')
plt.ylabel('Strength')
plt.title('KNN - Paper Tissue Classification')
plt.legend()
plt.show()
