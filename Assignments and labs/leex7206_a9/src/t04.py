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


from BST_linked import BST

SEP = "-" * 40

b = BST()
b.insert(3)
b.insert(4)
b.insert(2)
b.insert(7)
b.insert(8)
print(b.node_counts())
print(SEP)

print(5 in b)
print(3 in b)
print(8 in b)
print(SEP)

print(b.parent(2))
print(b.parent(3))
print(b.parent(8))
print(b.parent(7))
print(SEP)

print(b.parent_r(2))
print(b.parent_r(3))
print(b.parent_r(8))
print(b.parent_r(7))