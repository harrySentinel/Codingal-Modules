def check_odd_even(n):
    if n & 1:
        return "Odd"
    else:
        return "Even"

numbers = [4, 7, 12, 19, 3, 100]
for num in numbers:
    print(num, "->", check_odd_even(num))
