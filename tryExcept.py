age = input("Please enter your age: ")
try:
    age = int(age)
    if age < 0:
        print("Age cannot be negative.")
    else:
        print(f"You are {age} years old.")
except:
    print("Invalid input. Please enter a valid number for your age.")