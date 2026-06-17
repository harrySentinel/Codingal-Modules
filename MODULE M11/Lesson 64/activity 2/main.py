def is_power_of_four(n):
    if n <= 0:
        return False
    if (n & (n - 1)) != 0:
        return False
    return (n & 0xAAAAAAAA) == 0

numbers = [1, 4, 8, 16, 32, 64, 100, 256]
for num in numbers:
    if is_power_of_four(num):
        print(num, "is a power of 4")
    else:
        print(num, "is NOT a power of 4")
