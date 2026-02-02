#import modules
import math
import myModule
#import some more built-in modules
import datetime
import random
import os
import sys
import functions
import write2File
import listAndTuple

from myModule import farewell, add, divide
#using functions from built-in modules
current_time = datetime.datetime.now()
print("Current Time:", current_time)
print("Square root of 16 is:", math.sqrt(16))



print("Value of pi is:", math.pi)   
myModule.greet("Alice")
myModule.farewell("Bob")
result_add = myModule.add(5, 3)
print("Addition Result:", result_add)
result_divide = myModule.divide(10, 2)
print("Division Result:", result_divide)
result_divide_by_zero = myModule.divide(10, 0)

print("Division by Zero Result:", result_divide_by_zero)


# Use other imported modules
random_number = random.randint(1, 100)
print("Random Number between 1 and 100:", random_number)
current_directory = os.getcwd()
print("Current Working Directory:", current_directory)
python_version = sys.version    
print("Python Version:", python_version)
# Use functions from functions module
functions.addTwo(10)
functions.multiplyByThree(7)
print("Add Two to 10:", functions.addTwo(10))          # 12
print("Multiply 7 by Three:", functions.multiplyByThree(7))  # 21
print("Use Farewell directly:", farewell("Charlie"))  # Using imported function directly
print("Use Add directly:", add(20, 30))               # Using imported function directly
print("Use Divide directly:", divide(15, 3))          # Using imported function directly
