"""Create a class Engine and a class Car. Use composition by passing an 
Engine object to the Car class during initialization. Access a method of
the Engine class via the Car class"""

class Engine:
    def __init__(self, horsepower, fuel_type):
        self.horsepower = horsepower
        self.fuel_type = fuel_type

    def start(self):
        return f"The engine with {self.horsepower} horsepower running on {self.fuel_type} has started."

class Car:
    def __init__(self, make, model, engine):
        self.make = make
        self.model = model
        self.engine = engine  # Composition: Car has an Engine

    def start_car(self):
        # Accessing the Engine's method through the Car class
        return f"{self.make} {self.model}: {self.engine.start()}"

# Example usage
engine = Engine(horsepower=200, fuel_type="petrol")
car = Car(make="Toyota", model="Camry", engine=engine)

print(car.start_car())