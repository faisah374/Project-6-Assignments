"""Create a class Product with a private attribute _price. 
Use @property to get the price, @price.setter to update it, and @price.deleter to delete it."""

class Product:
    def __init__(self, price):
        self._price = price

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Price cannot be negative.")
        self._price = value

    @price.deleter
    def price(self):
        del self._price
        print("Price deleted.")
# Example usage
product = Product(100)
print(product.price)
product.price = 150
print(product.price)
del product.price
# print(product.price)  # This will raise an AttributeError since price has been deleted
# product.price = -50  # This will raise a ValueError since price cannot be negative



