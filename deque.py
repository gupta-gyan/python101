# deque example
from collections import deque
# Use deque over list for efficient appends and pops from both ends
# Use lists for fast random access and iteration
# example 1: creating a deque and appending elements
dq = deque([1, 2, 3])
dq.append(4)
dq.appendleft(0)
print("Deque after appends:", dq)  # Output: deque([0, 1, 2, 3, 4])
# example 2: popping elements from both ends
dq.pop()
dq.popleft()    
print("Deque after pops:", dq)  # Output: deque([1, 2, 3])
# example 3: extending deque with multiple elements 
dq.extend([4, 5, 6])
dq.extendleft([-1, -2])
print("Deque after extends:", dq)  # Output: deque([-2, -1, 1, 2, 3, 4, 5, 6])
# example 4: rotating the deque
dq.rotate(2)    
print("Deque after rotating right by 2:", dq)  # Output: deque([5, 6, -2, -1, 1, 2, 3, 4])
dq.rotate(-3)   
print("Deque after rotating left by 3:", dq)  # Output: deque([-1, 1, 2, 3, 4, 5, 6, -2])
# example 5: accessing elements by index
first_element = dq[0]
last_element = dq[-1]
print("First element:", first_element)  # Output: -1
print("Last element:", last_element)    # Output: -2
# example 6: getting the length of the deque
length = len(dq)
print("Length of deque:", length)  # Output: 8
# example 7: clearing the deque
dq.clear()
print("Deque after clearing:", dq)  # Output: deque([])
