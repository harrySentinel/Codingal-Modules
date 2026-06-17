class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def show_details(self):
        print("Student name:", self.name)
        print("Grade:", self.grade)

student1 = Student("Aditya Srivastava", 8)
student1.show_details()
