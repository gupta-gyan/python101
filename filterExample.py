# filter function examples
numbers = [1, 2, 3, 4, 5]
# example using filter to get even numbers
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print("Even Numbers using filter:", even_numbers)  # Output: [2, 4
# example using filter to get numbers greater than 3
greater_than_three = list(filter(lambda x: x > 3, numbers))
print("Numbers greater than 3 using filter:", greater_than_three)  # Output: [4, 5]
# example using filter with a predefined function
def is_odd(num):
    return num % 2 != 0 
odd_numbers = list(filter(is_odd, numbers))
print("Odd Numbers using filter and predefined function:", odd_numbers)  # Output: [1, 3, 5]
# example using filter to remove empty strings from a list  
strings = ["hello", "", "world", "", "python", "filter"]
non_empty_strings = list(filter(lambda s: s != "", strings))
print("Non-empty strings using filter:", non_empty_strings)  # Output: ['hello', 'world', 'python', 'filter']
# example using filter to get prime numbers from a list 
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True
primes = list(filter(is_prime, numbers))
print("Prime Numbers using filter:", primes)  # Output: [2, 3, 5]
# example using filter with multiple conditions
def is_even_and_greater_than_two(num):
    return num % 2 == 0 and num > 2 
even_and_gt_two = list(filter(is_even_and_greater_than_two, numbers))
print("Even Numbers greater than 2 using filter:", even_and_gt_two)  # Output: [4]