def count_ones_zeros(n):
    binary = bin(n)[2:]
    ones = binary.count('1')
    zeros = binary.count('0')
    return ones, zeros

num = int(input("Enter a number: "))
ones, zeros = count_ones_zeros(num)
print("Binary representation:", bin(num))
print("Number of 1s:", ones)
print("Number of 0s:", zeros)
