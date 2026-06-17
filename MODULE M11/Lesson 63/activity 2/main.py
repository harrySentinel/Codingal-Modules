def find_odd_occurring(arr):
    result = 0
    for num in arr:
        result ^= num
    return result

arr = [3, 3, 5, 7, 5, 7, 9]
print("Array:", arr)
print("Odd occurring number:", find_odd_occurring(arr))
