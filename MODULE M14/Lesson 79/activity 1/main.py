import numpy as np

scores = np.array([85, 42, 91, 67, 55, 78, 33, 96, 61, 74])

print("Original Scores:", scores)
print("Sorted Ascending:", np.sort(scores))
print("Sorted Descending:", np.sort(scores)[::-1])
print()
print("Min Score:", np.min(scores))
print("Max Score:", np.max(scores))
print("Average Score:", np.mean(scores))
print("Median Score:", np.median(scores))
