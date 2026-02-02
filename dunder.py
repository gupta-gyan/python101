# sample code using dunder (double underscore) methods in Python
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y)
        return NotImplemented

    def __sub__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x - other.x, self.y - other.y)
        return NotImplemented

    def __mul__(self, scalar):
        if isinstance(scalar, (int, float)):
            return Vector(self.x * scalar, self.y * scalar)
        return NotImplemented

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"

    def __eq__(self, other):
        if isinstance(other, Vector):
            return self.x == other.x and self.y == other.y
        return NotImplemented   
    def __len__(self):
        return int((self.x**2 + self.y**2)**0.5)    
    def __neg__(self):
        return Vector(-self.x, -self.y)
    def __getitem__(self, index):
        if index == 0:
            return self.x
        elif index == 1:
            return self.y
        else:
            raise IndexError("Index out of range")  
# Example usage
v1 = Vector(2, 3)   
v2 = Vector(4, 5)
print("v1:", v1)  # Output: Vector(2, 3)
print("v2:", v2)  # Output: Vector(4, 5)
v3 = v1 + v2
print("v1 + v2:", v3)  # Output: Vector(6, 8)
v4 = v2 - v1    
print("v2 - v1:", v4)  # Output: Vector(2, 2)
v5 = v1 * 3
print("v1 * 3:", v5)  # Output: Vector(6, 9)
print("v1 == v2:", v1 == v2)  # Output: False
print("Length of v1:", len(v1))  # Output: 3
v6 = -v1
print("Negation of v1:", v6)  # Output: Vector(-2, -3)
print("v1[0]:", v1[0])  # Output: 2
print("v1[1]:", v1[1])  # Output: 3     
try:
    print("v1[2]:", v1[2])  # This will raise an IndexError 
except IndexError as e:
    print("Error:", e)
    