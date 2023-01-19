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
from functions import insert_words, comparison_total

h = Hash_Set(20)

fv = open("otoos610.txt", "r")
insert_words(fv, h)
fv.close()

total, max_word = comparison_total(h)

print("Using array-based list Hash_Set")
print()
print(f"Total Comparisons: {total:,d}")
print(f"Word with maximum comparisons '{max_word.word}': {max_word.comparisons:,d}")
