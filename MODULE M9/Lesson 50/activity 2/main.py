f = open("data.txt", "w")
f.write("Apple\nBanana\nMango\nOrange\n")
f.close()

f = open("data.txt", "r")
lines = f.readlines()
f.close()

for line in lines:
    print(line.strip())
