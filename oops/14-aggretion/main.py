""""Create a class Department and a class Employee.
 Use aggregation by having a Department object store a reference
   to an Employee object that exists independently of it"""

class Employee:
    def __init__(self, emp_id, name, position):
        self.emp_id = emp_id
        self.name = name
        self.position = position

    def __str__(self):
        return f"Employee[ID={self.emp_id}, Name={self.name}, Position={self.position}]"


class Department:
    def __init__(self, dept_name):
        self.dept_name = dept_name
        self.employees = []  # List to hold references to Employee objects

    def add_employee(self, employee):
        self.employees.append(employee)

    def __str__(self):
        employee_details = "\n".join([str(emp) for emp in self.employees])
        return f"Department: {self.dept_name}\nEmployees:\n{employee_details}"


# Creating Employee objects
emp1 = Employee(101, "Alice", "Software Engineer")
emp2 = Employee(102, "Bob", "Data Scientist")

# Creating Department object
dept = Department("IT Department")

# Adding Employees to the Department
dept.add_employee(emp1)
dept.add_employee(emp2)

# Printing the Department and Employees
print(dept)



