from collections import namedtuple
# namedtuple examples
# example 1: creating a simple namedtuple
Person = namedtuple('Person', 'name age city')
some_person = Person("Alice",30,"New York")
print("Person namedtuple:", some_person)  # Output: Person(name='Alice', age=30, city='New York')
print("Name:", some_person.name)  # Output: Alice   
print("Age:", some_person.age)    # Output: 30
print("City:", some_person.city)  # Output: New York

# example 2: using namedtuple specifying field names as a list
Point = namedtuple('Point', ['x', 'y'])         
Car = namedtuple('Car', 'make model year color')
my_point = Point(10, 20)
my_car = Car("Toyota", "Camry", 2020, "Blue")
print("Point namedtuple:", my_point)  # Output: Point(x=10, y=20)   
print("Car namedtuple:", my_car)      # Output: Car(make='Toyota', model='Camry', year=2020, color='Blue')
print("Point coordinates:", my_point.x, my_point.y)  # Output: 10 20
print("Car details:", my_car.make, my_car.model, my_car.year, my_car.color)  # Output: Toyota Camry 2020 Blue

