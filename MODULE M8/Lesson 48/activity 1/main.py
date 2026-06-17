class Cat:
    def sound(self):
        print("Cat says meow")

class Dog:
    def sound(self):
        print("Dog says woof")

animals = [Cat(), Dog()]

for animal in animals:
    animal.sound()
