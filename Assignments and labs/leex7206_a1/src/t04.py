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


from functions import is_leap_year

year = int(input('Enter year: '))
leap_year = is_leap_year(year)

print(leap_year)