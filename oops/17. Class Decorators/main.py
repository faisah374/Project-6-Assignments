""""Create a class decorator add_greeting that 
modifies a class to add a greet() method returning "Hello from Decorator!". 
Apply it to a class Person."""

def add_greeting(cls):
    """Class decorator that adds a greet method to the class."""
    def greet(self):
        return "Hello from Decorator!"
    
    # Add the greet method to the class
    cls.greet = greet
    return cls

@add_greeting
class Person:
    pass

# Example usage
person = Person()
print(person.greet())  # Output: Hello from Decorator!
