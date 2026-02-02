# Collections module examples
import collections
# example using namedtuple
Point = collections.namedtuple('Point', ['x', 'y']) 
p = Point(10, 20)
print("Namedtuple Point:", p)  # Output: Point(x=10, y=20)
print("Point coordinates:", p.x, p.y)  # Output: 10 20
# example using deque
dq = collections.deque([1, 2, 3])
dq.append(4)    
dq.appendleft(0)
print("Deque after appends:", dq)  # Output: deque([0, 1, 2, 3, 4])
dq.pop()
dq.popleft()
print("Deque after pops:", dq)  # Output: deque([1, 2, 3])
# example using Counter
data = ['apple', 'banana', 'orange', 'apple', 'orange', 'banana', 'apple']
counter = collections.Counter(data) 
print("Counter of fruits:", counter)  # Output: Counter({'apple': 3, 'banana': 2, 'orange': 2})
print("Most common fruit:", counter.most_common(1))  # Output: [('apple', 3)]
# example using OrderedDict
od = collections.OrderedDict()
od['a'] = 1
od['b'] = 2
od['c'] = 3
print("OrderedDict items:", od.items())  # Output: odict_items([('a', 1), ('b', 2), ('c', 3)])
# example using defaultdict
dd = collections.defaultdict(int)
dd['a'] += 1
dd['b'] += 2
print("Defaultdict contents:", dd)  # Output: defaultdict(<class 'int'>, {'a': 1, 'b': 2})
# example using ChainMap
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}
chain = collections.ChainMap(dict1, dict2)
print("ChainMap contents:", chain)  # Output: ChainMap({'a': 1, 'b': 2}, {'b': 3, 'c': 4})
print("Value for 'b' in ChainMap:", chain['b'])  # Output: 2
# example using frozenset
fs = frozenset([1, 2, 3, 4])    
print("Frozenset contents:", fs)  # Output: frozenset({1, 2, 3, 4})
# example using UserDict
class MyDict(collections.UserDict):
    def __setitem__(self, key, value):
        print(f"Setting {key} to {value}")
        super().__setitem__(key, value)
my_dict = MyDict()
my_dict['x'] = 10
my_dict['y'] = 20
print("UserDict contents:", my_dict)  # Output: {'x': 10, 'y': 20}
