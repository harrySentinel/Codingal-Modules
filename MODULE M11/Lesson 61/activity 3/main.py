def count_set_bits(n):
    count = 0
    while n:
        count += n & 1
        n >>= 1
    return count

numbers = [5, 7, 13, 255, 1024]
for num in numbers:
    print(f"{num} in binary: {bin(num)} -> Set bits: {count_set_bits(num)}")
