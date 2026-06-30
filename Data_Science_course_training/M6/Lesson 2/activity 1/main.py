print("=== PART 1: Linear Recursion ===")
def linear(n):
    if n == 0:
        return
    print("Linear call:", n)
    linear(n - 1)

linear(5)

print("\n=== PART 2: Tail Recursion (Numbers Going Down) ===")
def tail(n):
    if n == 0:
        return
    print(n)
    tail(n - 1)

tail(5)

print("\n=== PART 3: Head Recursion (Numbers Going Up) ===")
def head(n):
    if n == 0:
        return
    head(n - 1)
    print(n)

head(5)

print("\n=== PART 4: Increasing-Decreasing Pattern ===")
def inc_dec(n):
    if n == 0:
        print(0)
        return
    print(n)
    inc_dec(n - 1)
    print(n)

inc_dec(4)

print("\n=== PART 5: Tree Recursion (Two Calls Per Level) ===")
def tree(n):
    if n == 0:
        print("leaf")
        return
    print("branching at level", n)
    tree(n - 1)
    tree(n - 1)

tree(3)
