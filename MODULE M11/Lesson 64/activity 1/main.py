def is_power_of_two(n):
    if n <= 0:
        return False
    return (n & (n - 1)) == 0

numbers = [1, 2, 3, 4, 5, 8, 16, 18, 32, 100]
for num in numbers:
    if is_power_of_two(num):
        print(num, "is a power of 2")
    else:
        print(num, "is NOT a power of 2")
