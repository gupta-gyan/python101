# counter examples
from collections import Counter

# different counter examples
# example 1: counting elements in a list
data = ['apple', 'banana', 'orange', 'apple', 'orange', 'banana', 'apple']
counter1 = Counter(data)    
print("Counter Example 1:", counter1)  # Output: Counter({'apple': 3, 'banana': 2, 'orange': 2})    
# example 2: counting characters in a string
text = "hello world"    
counter2 = Counter(text)
print("Counter Example 2:", counter2)  # Output: Counter({'l': 3, 'o': 2, 'h': 1, 'e': 1, ' ': 1, 'w': 1, 'r': 1, 'd': 1})
# example 3: counting words in a sentence
sentence = "this is a test this is only a test"
words = sentence.split()    
counter3 = Counter(words)
print("Counter Example 3:", counter3)  # Output: Counter({'this': 2, 'is': 2, 'a': 2, 'test': 2, 'only': 1})
# example 4: using most_common method
most_common_two = counter1.most_common(2)
print("Most common two elements in counter1:", most_common_two)  # Output: [('apple', 3), ('banana', 2)]
# example 5: updating a counter with more data
more_data = ['banana', 'kiwi', 'apple', 'kiwi', 'kiwi']
counter1.update(more_data)  
print("Counter after update:", counter1)  # Output: Counter({'apple': 4, 'kiwi': 3, 'banana': 3, 'orange': 2})
# example 6: subtracting counts using another counter
counter4 = Counter({'apple': 2, 'banana': 1})
counter1.subtract(counter4)
print("Counter after subtraction:", counter1)  # Output: Counter({'apple': 2, 'kiwi': 3, 'banana': 2, 'orange': 2})
# example 7: converting counter to a dictionary
counter_dict = dict(counter1)
print("Counter as dictionary:", counter_dict)  # Output: {'apple': 2, 'banana': 2, 'orange': 2, 'kiwi': 3}
# example 8: total count of all elements    
total_count = sum(counter1.values())
print("Total count of all elements in counter1:", total_count)  # Output: 9
# example 9: clearing a counter
counter1.clear()