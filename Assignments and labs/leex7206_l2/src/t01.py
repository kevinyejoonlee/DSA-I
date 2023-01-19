"""
-------------------------------------------------------
stack array testing
-------------------------------------------------------
Author: Kevin Lee
ID:     210872060
Email:  leex7206@mylaurier.ca
__updated__ = '2022-01-17'
-------------------------------------------------------
"""
from Stack_array import Stack

stack = Stack()


for i in 'kevin is the best':
    stack.push(i)
    



print(stack.is_empty())

print(stack.peek())

