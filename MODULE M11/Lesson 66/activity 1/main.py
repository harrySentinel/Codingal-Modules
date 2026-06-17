def power_set(arr):
    n = len(arr)
    total = 1 << n
    subsets = []
    for i in range(total):
        subset = []
        for j in range(n):
            if i & (1 << j):
                subset.append(arr[j])
        subsets.append(subset)
    return subsets

arr = [1, 2, 3]
print("Array:", arr)
print("Power Set:")
for subset in power_set(arr):
    print(subset)
