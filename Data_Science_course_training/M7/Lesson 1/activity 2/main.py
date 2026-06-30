nums = [34, 7, 89, 12, 56, 3, 100, 45]

max_val = nums[0]
min_val = nums[0]

for n in nums:
    if n > max_val:
        max_val = n
    if n < min_val:
        min_val = n

print("Array:", nums)
print("Maximum:", max_val)
print("Minimum:", min_val)
