def find_two_odd_occurring(arr):
    xor = 0
    for num in arr:
        xor ^= num

    set_bit = xor & (-xor)

    x, y = 0, 0
    for num in arr:
        if num & set_bit:
            x ^= num
        else:
            y ^= num

    return x, y

arr = [2, 4, 2, 5, 7, 4, 5, 9]
print("Array:", arr)
a, b = find_two_odd_occurring(arr)
print("Two odd occurring numbers:", a, "and", b)
