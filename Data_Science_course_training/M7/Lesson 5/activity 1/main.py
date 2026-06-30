arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

print("=== PART 1: Subarrays with Slices ===")
print("Array:", arr)
print("arr[0:3] =", arr[0:3], " sum =", sum(arr[0:3]))
print("arr[3:6] =", arr[3:6], " sum =", sum(arr[3:6]))
print("arr[2:7] =", arr[2:7], " sum =", sum(arr[2:7]))

print("\n=== PART 2: Running Sum with Reset ===")
running = 0
for x in arr:
    running += x
    if running < 0:
        running = 0
    print(f"  element={x:3}  running_sum={running}")

print("\n=== PART 3: Max Subarray Sum ===")
running = 0
best = float('-inf')
for x in arr:
    running += x
    best = max(best, running)
    if running < 0:
        running = 0
print("Max Subarray Sum:", best)

print("\n=== PART 4: Kadane on a Harder Array ===")
arr2 = [3, -4, 2, -3, 5, -2, 1, -6, 4, -1]
print("Array:", arr2)
running = 0
best = float('-inf')
for x in arr2:
    running += x
    best = max(best, running)
    if running < 0:
        running = 0
print("Max Subarray Sum:", best)
