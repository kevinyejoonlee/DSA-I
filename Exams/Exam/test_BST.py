"""
-------------------------------------------------------
Simple BST testing - Exam
-------------------------------------------------------
Author: Kevin Lee
ID:     210872060
Email:  leex7206@mylaurier.ca
__updated__ = "2022-04-06"
-------------------------------------------------------
"""
# pylint: disable=protected-access

# Imports
from BST_linked import BST

# Constants
SEP = '-' * 60
# These values match the sample BST diagram on the exam web page:
# https://bohr.wlu.ca/cp164/exam
values = [11, 7, 6, 9, 8, 15, 12, 18]
print("BST Testing")
print()
print(SEP)
print("Test reverse")
print()
print(f"Create a BST with {values}")
bst = BST()

for v in values:
    bst.insert(v)

a = bst.preorder()
print(f"  Preorder: {a}")
a = bst.inorder()
print(f"  Inorder: {a}")
print("Reverse the tree")
bst.reverse()
a = bst.preorder()
print(f"  Preorder: {a}")
a = bst.inorder()
print(f"  Inorder: {a}")
print(SEP)
print("Test _shift_left")
print()
print(f"Create a BST with {values}")
bst = BST()

for v in values:
    bst.insert(v)

a = bst.preorder()
print(f"  Preorder: {a}")
a = bst.inorder()
print(f"  Inorder: {a}")
print("Shift Left the root")
bst._root = bst._shift_left(bst._root)
a = bst.preorder()
print(f"  Preorder: {a}")
a = bst.inorder()
print(f"  Inorder: {a}")
print(SEP)
