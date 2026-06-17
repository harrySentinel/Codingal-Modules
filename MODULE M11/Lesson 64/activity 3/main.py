def power(base, exp):
    result = 1
    while exp > 0:
        if exp & 1:
            result *= base
        base *= base
        exp >>= 1
    return result

base = int(input("Enter base: "))
exp = int(input("Enter exponent: "))
print(f"{base} ^ {exp} = {power(base, exp)}")
