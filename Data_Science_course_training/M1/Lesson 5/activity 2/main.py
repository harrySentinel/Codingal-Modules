def factorial(number):
    answer = 1

    for i in range(1, number + 1):
        answer = answer * i

    return answer

print("Factorial is", factorial(5))
