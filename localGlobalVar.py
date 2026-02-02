#local and global variable example
x = "global x"
def my_function():
    x = "local x"
    print(x)
my_function()
print(x)    

# use of global keyword
y = "global y"
def my_other_function():
    global y
    y = "modified global y"
    print(y)

my_other_function()
print(y)    
