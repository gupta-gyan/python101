# Static and Class Methods in Python
class MathOperations:
    @staticmethod
    def add(x, y):
        return x + y

    @classmethod
    def multiply(cls, x, y):
        return x * y    
# Using the static method
result_add = MathOperations.add(5, 10)  
print("Addition Result:", result_add)  # Output: Addition Result: 15
# Using the class method
result_multiply = MathOperations.multiply(5, 10)
print("Multiplication Result:", result_multiply)  # Output: Multiplication Result: 50
# Demonstrating the difference between static and class methods
class Example:
    class_variable = "I am a class variable"

    @staticmethod
    def static_method():
        return "I am a static method and cannot access class variables directly."

    @classmethod
    def class_method(somecls):
        return f"I am a class method and can access: {somecls.class_variable}"  
print(Example.static_method())  # Output: I am a static method and cannot access class variables directly.
print(Example.class_method())   # Output: I am a class method and can access: I am a class variable

