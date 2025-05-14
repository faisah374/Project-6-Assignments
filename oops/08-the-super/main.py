"""Create a class Person with a constructor that sets the name.
 Inherit a class Teacher from it, add a subject field, 
 and use super() to call the base class constructor"""


class Person:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Person: {self.name}"
class Teacher(Person):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject

    def __str__(self):
        return f"Teacher: {self.name}, Subject: {self.subject}"
    

person= Person("Hameed")

Teacher1=("hameed",'python')

teacher= Teacher(*Teacher1)
print(person)
print(teacher)
print(teacher.subject)
print(teacher.name)
print(teacher.__str__())
print(teacher.__dict__)
print(teacher.__class__)
print(teacher.__module__)
print(teacher.__class__.__name__)
print(teacher.__class__.__bases__)



 