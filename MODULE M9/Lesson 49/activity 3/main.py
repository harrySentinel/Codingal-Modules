f = open("lines.txt", "w")
f.write("Line 1: Python is fun\n")
f.write("Line 2: File handling is easy\n")
f.write("Line 3: Aditya teaches Python\n")
f.close()

f = open("lines.txt", "r")
for line in f:
    print(line.strip())
f.close()
