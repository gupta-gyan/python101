# type of objects in Python
a = 42
b = 3.14    
c = "Hello, World!"
d = [1, 2, 3, 4, 5]
e = (10, 20, 30)
f = { 'name': 'Alice', 'age': 30 }
g = True
print(type(a))  # int
print(type(b))  # float
print(type(c))  # str
print(type(d))  # list
print(type(e))  # tuple
print(type(f))  # dict
print(type(g))  # bool


# Basic operations on different object types
# Integer operations
sum_ab = a + 10
print("Sum of a and 10:", sum_ab)
# String operations
greeting = c + " How are you?"
print(greeting)
# List operations
d.append(6)
print("Updated list d:", d)
# Dictionary operations
f['city'] = 'New York'
print("Updated dictionary f:", f)

# bool methods
h = False
print("Boolean value of h:", bool(h))

print("Boolean value of empty string:", bool(""))
print("Boolean value of non-empty list:", bool(d))

