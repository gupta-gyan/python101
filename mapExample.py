# example without using map
def square(num):
    return num * num    
numbers = [1, 2, 3, 4, 5]
squared_numbers = []    
for number in numbers:
    squared_numbers.append(square(number))  
print("Squared Numbers without map:", squared_numbers)  # Output: [1, 4, 9, 16, 25] 

# example using map
def square(num):
    return num * num    
numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(square, numbers))    
print("Squared Numbers with map:", squared_numbers)  # Output: [1, 4, 9, 16, 25]
print("Test without list", map(square, numbers))  # Output: <map object at ...>
# example using lambda with map
numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x * x, numbers))
print("Squared Numbers with map and lambda:", squared_numbers)  # Output: [1, 4, 9, 16, 25]
# example using map with multiple iterables
numbers1 = [1, 2, 3]
numbers2 = [4, 5, 6]    
summed_numbers = list(map(lambda x, y: x + y, numbers1, numbers2))
print("Summed Numbers with map and multiple iterables:", summed_numbers)  # Output: [5, 7, 9]
# example using map with built-in functions
strings = ["1", "2", "3", "4", "5"]
integers = list(map(int, strings))
print("Converted to integers using map and int():", integers)  # Output: [1, 2, 3, 4, 5]
# example using map to convert temperatures from Celsius to Fahrenheit
celsius_temps = [0, 10, 20, 30, 40]
fahrenheit_temps = list(map(lambda c: (c * 9/5) + 32, celsius_temps))
print("Temperatures in Fahrenheit using map:", fahrenheit_temps)  # Output: [32.0, 50.0, 68.0, 86.0, 104.0]
# example using map to extract specific fields from a list of dictionaries
people = [
    {"name": "Alice", "age": 30},
    {"name": "Bob", "age": 25},
    {"name": "Charlie", "age": 35}
]   
names = list(map(lambda person: person["name"], people))
print("Names extracted using map:", names)  # Output: ['Alice', 'Bob', 'Charlie']
ages = list(map(lambda person: person["age"], people))
print("Ages extracted using map:", ages)  # Output: [30, 25, 35]
# example using map to uppercase strings in a list
words = ["hello", "world", "python", "map"]
uppercased_words = list(map(lambda word: word.upper(), words))
print("Uppercased words using map:", uppercased_words)  # Output: ['HELLO', 'WORLD', 'PYTHON', 'MAP']
# example using map to calculate lengths of strings in a list
lengths = list(map(len, words))
print("Lengths of strings using map:", lengths)  # Output: [5, 5, 6, 3] 
# example using map to flatten a list of lists
list_of_lists = [[1, 2], [3, 4], [5]]   
flattened_list = list(map(lambda x: x, [item for sublist in list_of_lists for item in sublist]))
print("Flattened list using map:", flattened_list)  # Output: [1, 2, 3, 4, 5]
# example using map to format strings   
names = ["alice", "bob", "charlie"]
formatted_names = list(map(lambda name: name.capitalize(), names))  
print("Formatted names using map:", formatted_names)  # Output: ['Alice', 'Bob', 'Charlie']
# example using map to calculate factorials 
import math 
numbers = [1, 2, 3, 4, 5]
factorials = list(map(math.factorial, numbers)) 
print("Factorials using map:", factorials)  # Output: [1, 2, 6, 24, 120]
# example using map to convert strings to booleans  
string_bools = ["True", "False", "True", "False"]
bools = list(map(lambda x: x == "True", string_bools))  
print("Converted to booleans using map:", bools)  # Output: [True, False, True, False]
# example using map to round floating-point numbers
float_numbers = [1.2, 2.5, 3.7, 4.4, 5.9]
rounded_numbers = list(map(round, float_numbers))   
print("Rounded numbers using map:", rounded_numbers)  # Output: [1, 3, 4, 4, 6]
# example using map to convert temperatures from Fahrenheit to Celsius  
fahrenheit_temps = [32, 50, 68, 86, 104]
celsius_temps = list(map(lambda f: (f - 32) * 5/9, fahrenheit_temps))
print("Temperatures in Celsius using map:", celsius_temps)  # Output: [0.0, 10.0, 20.0, 30.0, 40.0]
# example using map to extract domains from email addresses 
emails = ["alice@gmail.com", "bob@yahoo.com", "charlie@outlook.com"]    
domains = list(map(lambda email: email.split('@')[1], emails))
print("Extracted domains using map:", domains)  # Output: ['gmail.com', 'yahoo.com', 'outlook.com']
