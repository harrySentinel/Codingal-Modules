print("=== PART 1: Reverse a List In Place (Two-Pointer) ===")
arr = [1, 2, 3, 4, 5, 6]
print("Before:", arr)
start, end = 0, len(arr) - 1
while start < end:
    arr[start], arr[end] = arr[end], arr[start]
    start += 1
    end -= 1
print("After:", arr)

print("\n=== PART 2: Reverse in Groups of 3 ===")
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
k = 3
print("Before:", arr)
i = 0
while i < len(arr):
    start = i
    end = min(i + k - 1, len(arr) - 1)
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1
    i += k
print("After:", arr)

print("\n=== PART 3: Left Rotate by n Positions ===")
arr = [1, 2, 3, 4, 5]
n = 2
print("Before:", arr)
for _ in range(n):
    temp = arr[0]
    for j in range(len(arr) - 1):
        arr[j] = arr[j + 1]
    arr[-1] = temp
print(f"After rotating left by {n}:", arr)

print("\n=== PART 4: Leaders in an Array ===")
arr = [16, 17, 4, 3, 5, 2]
print("Array:", arr)
leaders = []
max_right = arr[-1]
leaders.append(max_right)
for i in range(len(arr) - 2, -1, -1):
    if arr[i] > max_right:
        max_right = arr[i]
        leaders.append(arr[i])
print("Leaders:", leaders[::-1])
