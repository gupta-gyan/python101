def func1(x):
    return x *2

print(func1(4))


func2 = lambda x: x * 2
print(func2(4))

print("multiply two numbers using lambda:", (lambda x,y: x*y)(3,4))

someList = [1,2,3,4,5,6,7,8,9,10]
print("Squares using lambda and map:", list(map(lambda x: x*x, someList)))

# return list of even numbers using lambda and filter
print("Even numbers using lambda and filter:", list(filter(lambda x: x % 2 == 0, someList)))


