"""
Create a class TemperatureConverter with a static 
method celsius_to_fahrenheit(c) that returns the Fahrenheit value."""

class TemperatureConverter:
    @staticmethod
    def celusius_to_farhrehetic(c):
        return (c *9/5)+ 32 
    
celesius=32 
farhreenheit =TemperatureConverter.celusius_to_farhrehetic
print(f" {celesius} is equal {farhreenheit} f ")
resul=TemperatureConverter.celusius_to_farhrehetic(32)    
