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


from Hash_Set_array import Hash_Set

h = Hash_Set(2)
for i in range(10):
    h.insert("No"*i)
    h.insert("yes"*i)
    h.insert("lol what"*i)
    h.insert("NAH"*i)
    h.insert("what"*i)
h.debug()