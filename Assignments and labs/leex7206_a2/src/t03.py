"""
-------------------------------------------------------
Assignment 2, Task 3
-------------------------------------------------------
Author: Kevin Lee
ID:     210872060
Email:  leex7206@mylaurier.ca
__updated__ = '2022-01-17'
-------------------------------------------------------
"""

from Food import Food
from Food_utilities import calories_by_origin

Food1 = Food('Apple', 0, True, 2)
Food2 = Food('Banana', 1, False, 2)
Food3 = Food('Orange', 2, True, 4)
Food4 = Food('Carrot', 2, True, 3)
Food5 = Food('Coleslaw', 7, False, 2)
Food6 = Food('Spinich', 8, True, 2)

list = [Food1, Food2, Food3, Food4, Food5, Food6]

print(calories_by_origin(list, 2))
    