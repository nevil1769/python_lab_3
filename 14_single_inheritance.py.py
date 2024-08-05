
class Company:
    def __init__(self, name, city, mobile_no):
        self.name = name
        self.city = city
        self.mobile_no = mobile_no

    def display_company_details(self):
        print(f"Company Name: {self.name}")
        print(f"City: {self.city}")
        print(f"Mobile No: {self.mobile_no}")


class Employee(Company):
    def __init__(self, name, city, mobile_no, emp_name, designation, salary):
        super().__init__(name, city, mobile_no)
        self.emp_name = emp_name
        self.designation = designation
        self.salary = salary

    def display_employee_details(self):
        self.display_company_details()
        print(f"Employee Name: {self.emp_name}")
        print(f"Designation: {self.designation}")
        print(f"Salary: {self.salary}")

employee1 = Employee("Tech Solutions", "rajkot", "9589569859", "nevil", "Developer", 85000)

employee1.display_employee_details()
