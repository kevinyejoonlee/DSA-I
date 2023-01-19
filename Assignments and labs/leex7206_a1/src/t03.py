"""
-------------------------------------------------------
[Functions]
-------------------------------------------------------
Author: Kevin Lee
ID:     210872060
Email:  leex7206@mylaurier.ca
__updated__ = "2022-01-05"
-------------------------------------------------------
"""

from functions import file_analyze

filename = 'kevin.txt'
fv = open('kevin.txt', 'r')
u, l, d, w, r = file_analyze(fv)
fv.close()

print(f"Uppercase characters: {u}")
print(f"Lowercase characters: {l}")
print(f"Digit characters: {d}")
print(f"White Space characters: {w}")
print(f"Remaining characters: {r}")