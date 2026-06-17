f = open("marks.txt", "w")
f.write("Aditya 95\nRiya 42\nAman 78\nNeha 35\nRohan 88\n")
f.close()

f = open("marks.txt", "r")
lines = f.readlines()
f.close()

result = open("passed.txt", "w")
for line in lines:
    parts = line.strip().split()
    if int(parts[1]) >= 50:
        result.write(line)
result.close()

f = open("passed.txt", "r")
print(f.read())
f.close()
