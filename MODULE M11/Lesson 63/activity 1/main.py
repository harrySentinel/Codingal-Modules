def find_unique(arr):
    result = 0
    for num in arr:
        result ^= num
    return result

arr = [2, 3, 5, 3, 2, 5, 7, 7, 9, 9, 4, 4, 6]
print("Array:", arr)
print("The number that appears once:", find_unique(arr))
