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
from utilities import array_to_stack


#last value in source is at bottom of stack
s = Stack()
source = ['water','car','table']


array_to_stack(s, source)

for i in s:
    print(s.pop())
