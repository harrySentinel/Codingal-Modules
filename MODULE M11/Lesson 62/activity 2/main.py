def is_nth_bit_set(num, n):
    if num & (1 << n):
        return True
    return False

num = int(input("Enter a number: "))
n = int(input("Enter bit position (0-indexed): "))

if is_nth_bit_set(num, n):
    print(f"Bit {n} of {num} is SET (1)")
else:
    print(f"Bit {n} of {num} is NOT SET (0)")

print("Binary:", bin(num))
