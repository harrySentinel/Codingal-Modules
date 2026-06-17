f = open("sample.txt", "w")
f.write("Hello, my name is Aditya Srivastava.")
f.write("\nI am a coding instructor at Codingal.")
f.close()

f = open("sample.txt", "r")
content = f.read()
f.close()

print(content)
