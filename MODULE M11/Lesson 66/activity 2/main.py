def flip_bits(n):
    bits = bin(n)[2:]
    flipped = ''.join('1' if b == '0' else '0' for b in bits)
    return int(flipped, 2)

num = int(input("Enter a number: "))
result = flip_bits(num)
print("Original:", num, "->", bin(num))
print("Flipped: ", result, "->", bin(result))
