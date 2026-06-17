with open("file1.txt", "w") as f:
    f.write("Hello from file 1.\n")
    f.write("Aditya Srivastava\n")

with open("file2.txt", "w") as f:
    f.write("Hello from file 2.\n")
    f.write("Codingal Instructor\n")

with open("merged.txt", "w") as output:
    for filename in ["file1.txt", "file2.txt"]:
        with open(filename, "r") as f:
            output.write(f.read())

with open("merged.txt", "r") as f:
    print(f.read())
