"""
-------------------------------------------------------
Assignment 2, Task 4
-------------------------------------------------------
Author: Kevin Lee
ID:     210872060
Email:  leex7206@mylaurier.ca
__updated__ = '2022-01-17'
-------------------------------------------------------
"""
from Food import Food
from Food_utilities import food_table

Food1 = Food('Apple', 0, True, 123)
Food2 = Food('Banana', 1, False, 2)
Food3 = Food('Orange', 2, True, 4)
Food4 = Food('Carrot', 2, True, 3)
Food5 = Food('Coleslaw', 7, False, 2)
Food6 = Food('Spinich', 8, True, 2)

list = [Food5, Food3 , Food2, Food4, Food1, Food6]

food_table(list)
