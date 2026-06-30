scores = [72, 45, 88, 91, 60, 55, 78]

total = 0
for s in scores:
    total += s
mean = total / len(scores)
print("Array:", scores)
print("Mean:", mean)

sorted_scores = sorted(scores)
n = len(sorted_scores)
if n % 2 == 0:
    median = (sorted_scores[n // 2 - 1] + sorted_scores[n // 2]) / 2
else:
    median = sorted_scores[n // 2]
print("Sorted:", sorted_scores)
print("Median:", median)
