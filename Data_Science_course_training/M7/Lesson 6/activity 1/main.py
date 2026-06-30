print("=== PART 1: Equilibrium Point Setup ===")
arr = [1, 7, 3, 6, 5, 6]
print("Array:", arr)
total = sum(arr)
print("Total Sum:", total)

print("\n=== PART 2: Left Sum Scan ===")
left_sum = 0
for i in range(len(arr)):
    print(f"  index={i}  left_sum={left_sum}  right_sum={total - left_sum - arr[i]}")
    left_sum += arr[i]

print("\n=== PART 3: Finding Equilibrium Index ===")
left_sum = 0
eq_index = -1
for i in range(len(arr)):
    right_sum = total - left_sum - arr[i]
    if left_sum == right_sum:
        eq_index = i
        break
    left_sum += arr[i]
print("Equilibrium Index:", eq_index)

print("\n=== PART 4: Subarray with Target Sum ===")
arr2 = [1, 4, 20, 3, 10, 5]
target = 33
print("Array:", arr2, " Target:", target)

found = False
for i in range(len(arr2)):
    total2 = 0
    for j in range(i, len(arr2)):
        total2 += arr2[j]
        if total2 == target:
            print(f"Subarray found from index {i} to {j}:", arr2[i:j+1])
            found = True
            break
    if found:
        break

print("\n=== PART 5: Early Exit Confirmed ===")
if found:
    print("Target", target, "matched — loop exited early.")
else:
    print("No subarray found with target", target)
