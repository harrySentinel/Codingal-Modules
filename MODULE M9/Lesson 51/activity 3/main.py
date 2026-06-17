with open("original.txt", "w") as f:
    f.write("Python\nJava\nPython\nC++\nJava\nPython\n")

with open("original.txt", "r") as f:
    lines = f.readlines()

seen = set()
with open("no_duplicates.txt", "w") as f:
    for line in lines:
        if line not in seen:
            seen.add(line)
            f.write(line)

with open("no_duplicates.txt", "r") as f:
    print(f.read())
