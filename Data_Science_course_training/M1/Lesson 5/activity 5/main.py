def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

num = 6
print("Factorial of", num, "is", factorial(num))
