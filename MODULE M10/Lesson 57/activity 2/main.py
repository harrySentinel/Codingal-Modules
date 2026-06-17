def sum_list(arr):
    total = 0
    for num in arr:
        total += num
    return total

def sum_with_copy(arr):
    copy = arr[:]
    return sum(copy)

numbers = [1, 2, 3, 4, 5]

print("Sum:", sum_list(numbers))
print("sum_list uses O(1) space - only one variable.")
print()
print("Sum with copy:", sum_with_copy(numbers))
print("sum_with_copy uses O(n) space - creates a new list.")
