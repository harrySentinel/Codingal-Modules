class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def show_details(self):
        print("Employee name:", self.name)
        print("Salary:", self.salary)

employee1 = Employee("Aditya", 50000)
employee1.show_details()
