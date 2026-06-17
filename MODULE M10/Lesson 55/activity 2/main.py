def count_iterations(n):
    count = 0
    for i in range(n):
        count += 1
    return count

def count_nested_iterations(n):
    count = 0
    for i in range(n):
        for j in range(n):
            count += 1
    return count

n = 5
print("Single loop iterations for n =", n, ":", count_iterations(n))
print("Nested loop iterations for n =", n, ":", count_nested_iterations(n))
