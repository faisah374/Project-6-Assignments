"""Create a class Multiplier with an __init__() to set a factor. 
Define a __call__() method that multiplies an input by the factor. 
Test it with callable() and by calling the object like a function."""

class Multiplier:
    def __init__(self, factor):
        self.factor = factor

    def __call__(self, x):
        return x * self.factor

# Test the Multiplier class
double = Multiplier(2)
print(callable(double))  # True
print(double(5))         # 10

print(double(10))        # 20
triple = Multiplier(3)
print(triple(5))        # 15
