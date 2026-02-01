def addTwo(x):
    return x + 2

def multiplyByThree(x):
    return x * 3

def divideByFour(x=16):
    return x / 4

print("Add Two to 5:", addTwo(5))          # 7
print("Multiply 4 by Three:", multiplyByThree(4))  # 12
print("Divide 16 by Four:", divideByFour(16))      # 4.0
print("Divide default by Four:", divideByFour())      # 4.0
print("Divide 20 by Four:", divideByFour(20))      # 5.0

