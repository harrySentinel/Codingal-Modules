f = open("notes.txt", "w")
f.write("Python is a great language.\n")
f.close()

f = open("notes.txt", "a")
f.write("File handling helps store data.\n")
f.write("Aditya Srivastava loves coding.\n")
f.close()

f = open("notes.txt", "r")
print(f.read())
f.close()
