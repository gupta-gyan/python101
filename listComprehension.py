# list comprehension equivalent of map examples
numbers = [1, 2, 3, 4, 5]
numbers1 = [1, 2, 3]
numbers2 = [4, 5, 6]
strings = ["1", "2", "3", "4", "5"]
celsius_temps = [0, 10, 20, 30, 40]
people = [
    {"name": "Alice", "age": 30},
    {"name": "Bob", "age": 25},
    {"name": "Charlie", "age": 35}
]
words = ["hello", "world", "python", "map"]
squared_numbers_comp = [x * x for x in numbers] 
print("Squared Numbers with list comprehension:", squared_numbers_comp)  # Output: [1, 4, 9, 16, 25]
summed_numbers_comp = [x + y for x, y in zip(numbers1, numbers2)]
print("Summed Numbers with list comprehension:", summed_numbers_comp)  # Output: [5, 7, 9]
integers_comp = [int(s) for s in strings]   
print("Converted to integers with list comprehension:", integers_comp)  # Output: [1, 2, 3, 4, 5]
fahrenheit_temps_comp = [(c * 9/5) + 32 for c in celsius_temps]
print("Temperatures in Fahrenheit with list comprehension:", fahrenheit_temps_comp)  # Output: [32.0, 50.0, 68.0, 86.0, 104.0]
names_comp = [person["name"] for person in people]
print("Names extracted with list comprehension:", names_comp)  # Output: ['Alice', 'Bob', 'Charlie']
uppercased_words_comp = [word.upper() for word in words]
print("Uppercased words with list comprehension:", uppercased_words_comp)  # Output: ['HELLO', 'WORLD', 'PYTHON', 'MAP']
lengths_comp = [len(word) for word in words]    
print("Lengths of strings with list comprehension:", lengths_comp)  # Output: [5, 5, 6, 3]
# filter even numbers using list comprehension
even_numbers_comp = [x for x in numbers if x % 2 == 0]  
print("Even Numbers with list comprehension:", even_numbers_comp)  # Output: [2, 4]