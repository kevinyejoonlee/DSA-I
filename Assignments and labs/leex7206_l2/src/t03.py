"""
-------------------------------------------------------
[Functions]
-------------------------------------------------------
Author: Kevin Lee
ID:     210872060
Email:  leex7206@mylaurier.ca
__updated__ = '2022-01-17'
-------------------------------------------------------
"""

from Stack_array import Stack
from utilities import stack_to_array


s = Stack()

l = [1,2,3]
target = []

for i in l:
    s.push(i)

# for i in s:
#     print(s.pop())


stack_to_array(s, target)

print(target)
