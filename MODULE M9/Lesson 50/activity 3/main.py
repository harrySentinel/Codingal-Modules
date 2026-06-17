f = open("students.txt", "w")
f.write("Aditya\nRiya\nAman\nNeha\nRohan\n")
f.close()

f = open("students.txt", "r")
for line in f:
    name = line.strip()
    if name.startswith("A"):
        print(name)
f.close()
