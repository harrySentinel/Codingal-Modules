num = 153
digits = len(str(num))
total = sum(int(d) ** digits for d in str(num))

if total == num:
    print(num, "is an Armstrong number")
else:
    print(num, "is not an Armstrong number")
