def paren(s, l, r, p, n):
    if p < 0 or l > n or r > n:
        return
    if l == n and r == n:
        print(s)
        return
    paren(s + "{", l + 1, r, p + 1, n)
    paren(s + "}", l, r + 1, p - 1, n)

n = 3
print(f"All valid combinations of {n} balanced pairs:\n")
paren("", 0, 0, 0, n)
