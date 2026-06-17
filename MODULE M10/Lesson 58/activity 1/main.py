def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def is_strong(n):
    digits = str(n)
    total = sum(factorial(int(d)) for d in digits)
    return total == n

print("Strong Numbers between 1 and 1000:")
for num in range(1, 1001):
    if is_strong(num):
        print(num)
