details = {
    "name": "Aditya Srivastava",
    "role": "Software Engineer",
    "company": "Codingal"
}

def get_name(d):
    return d["name"]

def get_role(d):
    return d["role"]

print(get_name(details))
print(get_role(details))
print("Both operations are O(1) - constant time regardless of dictionary size.")
