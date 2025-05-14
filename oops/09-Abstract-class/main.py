"""Use the abc module to create an abstract class Shape with an abstract method area(). 
Inherit a class Rectangle that implements area()."""
from abc import ABC, abstractmethod
class Shape(ABC):
    """Abstract class for shapes."""

    @abstractmethod
    def area(self):
        """Calculate the area of the shape."""
        pass
class Rectangle(Shape):
    """Class for rectangles."""

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        """Calculate the area of the rectangle."""
        return self.width * self.height

area1 = Rectangle(5, 10)
area2 = Rectangle(3, 4)
print(f"Area of rectangle 1: {area1.area()}")
print(f"Area of rectangle 2: {area2.area()}")    
