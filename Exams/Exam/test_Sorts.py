"""
-------------------------------------------------------
Simple Radix String sort testing - Exam
-------------------------------------------------------
Author: Kevin Lee
ID:     210872060
Email:  leex7206@mylaurier.ca
__updated__ = "2022-04-06"
-------------------------------------------------------
"""
# Imports
from Sorts_array import Sorts

# Constants
SEP = '-' * 60
EMPTY = []
ONE = ['a']
LOWER_INORDER = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
LOWER_RANDOM = ['z', 'v', 'x', 'w', 'u', 'y', 's', 't']
LOWER_LONGER = ['w', 'yjjh', 'z', 't', 'xqt', 'dglk', 'ksr']
MIXED = ['ia', 'schEJ', 'f', 'rLF', 'BaWSs', 'p', 'YPDc', 'XCFP', 'u', 'u']
DATA = (EMPTY, ONE, LOWER_INORDER, LOWER_RANDOM, LOWER_LONGER, MIXED)

# Testing
print("Test Radix String Sort")
print()
print(SEP)

for values in DATA:
    print(f"Values: {values}")
    Sorts.radix_string_sort(values)
    print(f"Result: {values}")
    srtd = Sorts.is_sorted_alpha(values)
    print(f"Sorted: {srtd}")
    print(SEP)
