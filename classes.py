# sample class definition
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        return f"Hello, my name is {self.name} and I am {self.age} years old."
    
# creating an instance of the Person class
person1 = Person("Alice", 30)   
print(person1.greet())  # Output: Hello, my name is Alice and I am 30 years old.
# sample class definition
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def get_info(self):
        return f"{self.year} {self.make} {self.model}"      
# creating an instance of the Car class
car1 = Car("Toyota", "Camry", 2020)
print(car1.get_info())  # Output: 2020 Toyota Camry 


class someclass():
    def __init__(self, num):
        self.var= num
    def display(self):
        print("The value of var is:", self.var)

obj = someclass(10)
obj.display()  # Output: The value of var is: 10
