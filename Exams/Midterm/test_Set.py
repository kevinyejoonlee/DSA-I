"""
-------------------------------------------------------
Simple Set testing
-------------------------------------------------------
Author:  Kevin Lee
ID:      210872060
Email:   leex7206@mylaurier.ca
__updated__ = "2022-02-12"
-------------------------------------------------------
"""
# pylint: disable=protected-access

# Imports
from Set_array import Set

# Constants
SEP = "-" * 60

# Testing
source = Set()
print("Empty Set:")
source.print_set()
print(SEP)

for i in range(6):
    source.insert(i)

print("Value of _first:")
print("Expected: 6, Actual:", source._first)

source.print_set()
print("Values in set:")
for v in source:
    print(v)
print(SEP)

print()
print("delete 3")
deleted = source.delete(3)
print("deleted:", deleted)
print("Value of _first:")
print("Expected: 3, Actual:", source._first)
source.print_set()
print("Values in set:")

for v in source:
    print(v)
print(SEP)

print()
print("Test _linear_search")
print("Search 5")
i = source._linear_search(5)
print("Expected: 5, Actual:", i)
print("Search 5")
i = source._linear_search(3)
print("Expected -1, Actual", i)
print("Insert 99")
source.insert(99)
print("Value of _first:")
print("Expected: 6, Actual:", source._first)
print("Search 99")
i = source._linear_search(99)
print("Expected 3, Actual", i)
print(SEP)
source.print_set()
