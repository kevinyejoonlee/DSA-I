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


from functions import clean_list


values = [1, 2, 0, 1, 4, 1, 1, 2, 2, 5, 4,
          3, 1, 3, 3, 4, 2, 4, 3, 1, 3, 0, 3, 0, 0]

print(f'Values: {values}')
clean_list(values)
print(f'Cleaned: {values}')

