print("=== PART 1: Peeling Off Digits ===")
num = 1234
temp = num
while temp > 0:
    digit = temp % 10
    print("Peeled digit:", digit)
    temp = temp // 10

print("\n=== PART 2: Reverse a Number ===")
def reverse_number(n, result=0):
    if n == 0:
        return result
    return reverse_number(n // 10, result * 10 + n % 10)

number = 5678
print("Original:", number)
print("Reversed:", reverse_number(number))

print("\n=== PART 3: Reverse a Word/Name ===")
def reverse_string(s):
    if len(s) == 0:
        return ""
    return reverse_string(s[1:]) + s[0]

name = "Aditya"
print("Original:", name)
print("Reversed:", reverse_string(name))

print("\n=== PART 4: Powers of 4 ===")
def is_power_of_4(n):
    if n == 1:
        return True
    if n < 1 or n % 4 != 0:
        return False
    return is_power_of_4(n // 4)

test_numbers = [1, 4, 16, 20, 64, 100, 256]
for n in test_numbers:
    print(n, "is power of 4:", is_power_of_4(n))

user_input = int(input("\nEnter a number to test: "))
print(user_input, "is power of 4:", is_power_of_4(user_input))
