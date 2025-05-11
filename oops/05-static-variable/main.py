""""Create a class MathUtils with a static method add(a, b) that returns the sum. 
No class or instance variables should be used."""
class MathUtils:
    @staticmethod
    def add(a, b):
        return a + b
# Test the MathUtils class
if __name__ == "__main__":
    print(MathUtils.add(5, 3))  
    print(MathUtils.add(-8, 1))  
    print(MathUtils.add(0, 0))   
    print(MathUtils.add(2.5, 3.5))









     