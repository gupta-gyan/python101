# List vs tuple usecases
# | Scenario                             | Use     |
# | ------------------------------------ | ------- |
# | Collection changes over time         | `list`  |
# | Fixed configuration / constants      | `tuple` |
# | Return multiple values from function | `tuple` |
# | Dictionary key                       | `tuple` |
# | Large read-only data                 | `tuple` |



#using lists
fruits = ["apple", "banana", "cherry", "date", "elderberry" ]
print(fruits)
fruits.append("fig")
print("After appending fig:", fruits)
print("First fruit:", fruits[0])
fruits[1] = 4
print("After changing second fruit:", fruits)
# print type
print("Type of fruits:", type(fruits))

for fruit in fruits:
    print("Fruit:", fruit)

# methods on lists
print("Length of fruits list:", len(fruits))
print("Index of 'cherry':", fruits.index("cherry")) 
print("Count of 'apple':", fruits.count("apple"))   



#using tuples
coordinates = (10.0, 20.0)
print("Coordinates:", coordinates)  
print("Type of coordinates:", type(coordinates))

#methods on tuples
print("Length of coordinates tuple:", len(coordinates))
print("Index of 20.0:", coordinates.index(20.0))    
print("Count of 10.0:", coordinates.count(10.0))    
for coord in coordinates:
    print("Coordinate:", coord) 
# unpacking tuples
x, y = coordinates      
print("X:", x)
print("Y:", y)
# trying to change tuple value (will raise an error)
# coordinates[0] = 15.0  # Uncommenting this line will raise a TypeError

