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
from Priority_Queue_array import Priority_Queue
from utilities import array_to_pq, pq_to_array


source = [1,2,3]

pq= Priority_Queue()

array_to_pq(pq, [1,2,3])

target = []


pq_to_array(pq,target)


print(target)