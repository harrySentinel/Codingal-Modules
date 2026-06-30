print("=== PART 1: Streak Counter in Real Time ===")
arr = [1, 1, 0, 1, 1, 1, 0, 1]
print("Array:", arr)
streak = 0
for x in arr:
    if x == 1:
        streak += 1
    else:
        streak = 0
    print(f"  element={x}  streak={streak}")

print("\n=== PART 2: Maximum Consecutive 1s ===")
streak = 0
best = 0
for x in arr:
    if x == 1:
        streak += 1
        best = max(best, streak)
    else:
        streak = 0
print("Max Consecutive 1s:", best)

print("\n=== PART 3: Move Zeros to End ===")
arr2 = [0, 1, 0, 3, 12, 0, 5]
print("Before:", arr2)
write = 0
for i in range(len(arr2)):
    if arr2[i] != 0:
        arr2[write], arr2[i] = arr2[i], arr2[write]
        write += 1
print("After: ", arr2)

print("\n=== PART 4: Non-Zero and Zero Count ===")
print("Non-zero elements:", write)
print("Zero elements:", len(arr2) - write)
