with open("profile.txt", "w") as f:
    f.write("Aditya Srivastava,28,Codingal,Python\n")
    f.write("Riya Sharma,22,Google,Java\n")

with open("profile.txt", "r") as f:
    for line in f:
        parts = line.strip().split(",")
        print("Name:", parts[0])
        print("Age:", parts[1])
        print("Company:", parts[2])
        print("Language:", parts[3])
        print()
