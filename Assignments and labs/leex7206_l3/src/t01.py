"""
-------------------------------------------------------
functions
-------------------------------------------------------
Author: Kevin Lee
ID:     210872060
Email:  leex7206@mylaurier.ca
__updated__ = '2022-01-15'
-------------------------------------------------------
"""


from Queue_array import Queue
from utilities import array_to_queue

q = Queue()

source = [1,2,3,4,5]

for i in source:
    q.insert(i)
    
    
#1,2,3,4,5

for i in q:
    print(i)