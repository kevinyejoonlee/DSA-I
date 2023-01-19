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
from Food import Food
from Food_utilities import write_foods

with open('new_foods.txt', 'w') as file_variable:
    
    Food1 = Food('Apple', 0, True, 3)
    Food2 = Food('Banana', 1, False, 2)
    Food3 = Food('Orange', 2, True, 5)
    
    list = [Food1, Food2, Food3]
    
    write_foods(file_variable, list)
    
    

    
    