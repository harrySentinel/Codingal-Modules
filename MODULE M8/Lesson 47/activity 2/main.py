class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Student(Person):
    def __init__(self, name, age, grade):
        super().__init__(name, age)
        self.grade = grade

    def show_details(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Grade:", self.grade)

student1 = Student("Aditya Srivastava", 14, 8)
student1.show_details()
