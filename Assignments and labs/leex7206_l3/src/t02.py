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
from utilities import array_to_queue, queue_to_array


q = Queue()

source = [11,22,33,44]

array_to_queue(q, source)


target = []

queue_to_array(q, target)

print(target)