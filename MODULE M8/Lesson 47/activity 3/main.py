class Animal:
    def sound(self):
        print("Animals make different sounds")

class Dog(Animal):
    def bark(self):
        print("Dog says woof")

dog1 = Dog()
dog1.sound()
dog1.bark()
