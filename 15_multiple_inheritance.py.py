class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def display_personal_details(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Gender: {self.gender}")

class EmployeeDetails:
    def __init__(self, employee_id, department, salary):
        self.employee_id = employee_id
        self.department = department
        self.salary = salary

    def display_employee_details(self):
        print(f"Employee ID: {self.employee_id}")
        print(f"Department: {self.department}")
        print(f"Salary: {self.salary}")

class Employee(Person, EmployeeDetails):
    def __init__(self, name, age, gender, employee_id, department, salary):
        Person.__init__(self, name, age, gender)
        EmployeeDetails.__init__(self, employee_id, department, salary)

    def display_full_details(self):
        self.display_personal_details()
        self.display_employee_details()


employee1 = Employee("nevil", 20, "Male", "E123", "IT", 70000)

employee1.display_full_details()
