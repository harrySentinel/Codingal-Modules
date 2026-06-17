class Parrot:
    species = "bird"

    def __init__(self, name, age):
        self.name = name
        self.age = age

parrot1 = Parrot("Mithu", 2)

print(parrot1.name, "is a", parrot1.species)
print("Age:", parrot1.age)
