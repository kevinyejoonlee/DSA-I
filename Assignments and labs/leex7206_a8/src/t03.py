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

from Letter import Letter
from BST_linked import BST
from functions import do_comparisons, comparison_total, letter_table

DATA1 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
DATA2 = "MFTCJPWADHKNRUYBEIGLOQSVXZ"
DATA3 = "ETAOINSHRDLUCMPFYWGBVKJXZQ"

def create_bst(s):
    new_tree = BST()
    for i in s:
        new_tree.insert(Letter(i))
    return new_tree

bst1 = create_bst(DATA1)
bst2 = create_bst(DATA2)
bst3 = create_bst(DATA3)

# file_variable = open("gibbon.txt", "r")
# do_comparisons(file_variable, bst1)
# file_variable.close()
#
# letter_table(bst1)

# file_variable = open("gibbon.txt", "r")
# do_comparisons(file_variable, bst2)
# file_variable.close()
#
# letter_table(bst2)

file_variable = open("gibbon.txt", "r")
do_comparisons(file_variable, bst3)
file_variable.close()

letter_table(bst3)