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

from functions import matrix_stats

array = [[1, 2, 3],
         [4, 5, 6],
         [7, 8, 9]

         ]

highest, lowest, total, average = matrix_stats(array)

print(f'max: {highest}')
print('min:', lowest)
print('total:', total)
print('average:', average)

