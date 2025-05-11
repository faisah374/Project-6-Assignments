"""Create a class Employee with:

a public variable name,

a protected variable _salary, and

a private variable __ssn.

Try accessing all three variables from an object of the class and document what happens"""

class Employee:
    def __init__(self, name, salary, ssn):
        self.name = name  # public variable
        self._salary = salary  # protected variable
        self.__ssn = ssn  # private variable
        # The private variable is not accessible outside the class
        # but can be accessed using the name mangling technique
        # self.__ssn = ssn
    def get_ssn(self):
        return self.__ssn
    def set_ssn(self, ssn):
        self.__ssn = ssn
    def __str__(self):
        return f"Name: {self.name}, Salary: {self._salary}, SSN: {self.__ssn}"
detailes = Employee("Ahmed", 50000, "123-45-6789")
print(detailes.name)  # Accessing public variable
print(detailes._salary)  # Accessing protected variable
# print(detailes.__ssn)  # This will raise an AttributeError
# Accessing private variable using name mangling
print(detailes._Employee__ssn)  # Accessing private variable using name mangling


