class Student:
    def __init__(self, name):
        self.name = name
        print(self.name, "object is created")

    def __del__(self):
        print(self.name, "object is deleted")

student1 = Student("Aditya")

print("Student object is being used")

del student1
