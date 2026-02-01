# write a bunch of functions in this module
def greet(name):
    return "Hello, " + name + "!"
def farewell(name):
    return "Goodbye, " + name + "!"

#some basic maths functions
def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b
def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: Division by zero"
    