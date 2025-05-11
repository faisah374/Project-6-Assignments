"""Create a class Car with a public variable brand and a public method start(). 
Instantiate the class and access both from outside the class"""
class Car:
    def __init__(self, brand):
        self.brand = brand  # Public variable

    def start(self):  # Public method
        print(f"The {self.brand} car has started.")

toyta= Car("Toyota")  # Instantiate the class
toyta.start()  # Call the public method 
print(toyta.brand)  # Access the public variable
# Output:
# The Toyota car has started.
