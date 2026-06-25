number = 17
is_prime = True

if number <= 1:
    is_prime = False
else:
    for i in range(2, number):
        if number % i == 0:
            is_prime = False
            break

if is_prime:
    print(number, "is a prime number")
else:
    print(number, "is not a prime number")
