"""
-------------------------------------------------------
[Functions]
-------------------------------------------------------
Author: Kevin Lee
ID:     210872060
Email:  leex7206@mylaurier.ca
__updated__ = '2022-01-17'
-------------------------------------------------------
"""

from copy import deepcopy
from Stack_array import Stack
from utilities import array_to_stack, stack_test
from Food_utilities import read_foods

file_variable = open("foods.txt", 'r')
foods = read_foods(file_variable)
source = deepcopy(foods)
stack_test(source)

file_variable.close()