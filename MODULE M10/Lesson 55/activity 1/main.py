numbers = [3, 1, 4, 1, 5, 9, 2, 6]

def find_max_v1(arr):
    sorted_arr = sorted(arr)
    return sorted_arr[-1]

def find_max_v2(arr):
    max_val = arr[0]
    for num in arr:
        if num > max_val:
            max_val = num
    return max_val

def find_max_v3(arr):
    return max(arr)

print("Version 1 (Sort):", find_max_v1(numbers))
print("Version 2 (Loop):", find_max_v2(numbers))
print("Version 3 (Built-in):", find_max_v3(numbers))
