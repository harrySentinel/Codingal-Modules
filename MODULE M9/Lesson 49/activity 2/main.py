f = open("info.txt", "w")
f.write("Name: Aditya Srivastava\n")
f.write("Role: Software Engineer\n")
f.write("Company: Codingal\n")
f.close()

f = open("info.txt", "r")
print(f.read())
f.close()
