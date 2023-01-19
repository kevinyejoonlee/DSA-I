"""
-------------------------------------------------------
Food class definition.
-------------------------------------------------------
Author: Kevin Lee
ID:     210872060
Email:  leex7206@mylaurier.ca
Section: CP164 Winter 2022
__updated__ = '2022-01-15'
-------------------------------------------------------
"""

from Food_utilities import read_foods

with open('food.txt', 'r') as file_variable:
    print(read_foods(file_variable))
    

    
    