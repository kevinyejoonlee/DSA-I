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

from Food import Food
from List_array import List
from utilities import list_test
from Food_utilities import read_food

file_variable = open("foods.txt", "r")
foods = read_food(file_variable)
file_variable.close()

list_test(foods)
