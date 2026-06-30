nums = [34, 7, 89, 12, 56, 3, 100, 45]

largest = second = float('-inf')

for n in nums:
    if n > largest:
        second = largest
        largest = n
    elif n > second and n != largest:
        second = n

print("Array:", nums)
print("Largest:", largest)
print("Second Largest:", second)
