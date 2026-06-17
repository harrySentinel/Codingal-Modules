def divide(dividend, divisor):
    sign = -1 if (dividend < 0) ^ (divisor < 0) else 1
    dividend, divisor = abs(dividend), abs(divisor)
    quotient = 0
    while dividend >= divisor:
        temp = divisor
        multiple = 1
        while dividend >= (temp << 1):
            temp <<= 1
            multiple <<= 1
        dividend -= temp
        quotient += multiple
    return sign * quotient

a = int(input("Enter dividend: "))
b = int(input("Enter divisor: "))
print(f"{a} / {b} = {divide(a, b)}")
