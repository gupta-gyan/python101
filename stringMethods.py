# string methods
text = "Hello, World!"
print(text.lower())          # hello, world!
print(text.upper())          # HELLO, WORLD!    
print(text.capitalize())     # Hello, world!
print(text.title())          # Hello, World!    
print(text.strip("!"))      # Hello, World
print(text.replace("World", "Python"))  # Hello, Python!    
print(text.split(", "))     # ['Hello', 'World!']
print(text.find("World"))   # 7         
print(text.startswith("Hello"))  # True
print(text.endswith("!"))        # True
print("Type of text:", type(text))  # <class 'str'> 
for char in text:
    print("Character:", char)
print("Length of text:", len(text))  # 13   
print("Index of 'o':", text.index("o"))  # 4
print("Count of 'l':", text.count("l"))  # 3
print("Is alphanumeric?:", text.isalnum())  # False
print("Is alphabetic?:", text.isalpha())    # False
print("Is digit?:", text.isdigit())          # False
print("Is lowercase?:", text.islower())      # False
print("Is uppercase?:", text.isupper())      # False
