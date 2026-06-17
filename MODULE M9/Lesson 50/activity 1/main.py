f = open("sample.txt", "w")
f.write("Aditya Srivastava is a Python developer.")
f.close()

f = open("sample.txt", "r")
print(f.read(6))
print(f.read(10))
f.close()
