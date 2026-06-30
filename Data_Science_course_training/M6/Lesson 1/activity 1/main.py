import sys

print("=== PART 1: The Two Rules of Recursion ===")
print("Rule 1 - Base Case: the condition that stops the recursion")
print("Rule 2 - Recursive Case: the function calls itself with a smaller input")

print("\n=== PART 2: Count Up from 1 to 10 (No Loop) ===")
def count_up(n):
    if n > 10:
        return
    print(n)
    count_up(n + 1)

count_up(1)

print("\n=== PART 3: Countdown — Build and Unwind ===")
def countdown(n):
    if n == 0:
        print("Go!")
        return
    print("Building...", n)
    countdown(n - 1)
    print("Unwinding...", n)

countdown(4)

print("\n=== PART 4: Factorial (Multiplies on the Way Back Up) ===")
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

print("5! =", factorial(5))
print("6! =", factorial(6))

print("\n=== PART 5: Stack Overflow — Missing Base Case ===")
sys.setrecursionlimit(50)

def no_base(n):
    print("Calling with", n)
    no_base(n + 1)

try:
    no_base(1)
except RecursionError:
    print("RecursionError: Maximum recursion depth exceeded!")
    print("This is what happens when you forget the base case.")
