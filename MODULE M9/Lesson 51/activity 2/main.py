import os

filename = "temp.txt"

with open(filename, "w") as f:
    f.write("This is a temporary file.")

if os.path.exists(filename):
    print(filename, "exists. Deleting it...")
    os.remove(filename)
    print("File deleted.")
else:
    print("File not found.")
