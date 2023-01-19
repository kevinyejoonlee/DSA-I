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

# Imports
import random
from Number import Number
from Sorts_array import Sorts

# Constants
SIZE = 100  # Size of array to sort.
XRANGE = 1000  # Range of values in random arrays to sort.
TESTS = 100  # Number of random arrays to generate.

SORTS = (
    ('Bubble Sort', Sorts.bubble_sort),
    ('Insertion Sort', Sorts.insertion_sort),
    ('Merge Sort', Sorts.merge_sort),
    ('Quick Sort', Sorts.quick_sort),
    ('Selection Sort', Sorts.selection_sort),
    ('Bin. Ins. Sort', Sorts.binary_insert_sort),
    ('BST Sort', Sorts.bst_sort),
    ('Cocktail Sort', Sorts.cocktail_sort),
    ('Comb Sort', Sorts.comb_sort),
    ('Heap Sort', Sorts.heap_sort),
    ('Shell Sort', Sorts.shell_sort)
)


def create_sorted():
    """
    -------------------------------------------------------
    Creates a sorted list of SIZE Number objects with values
    from 0 up to SIZE-1.
    Use: values = create_sorted()
    -------------------------------------------------------
    Returns:
        values - a sorted list of SIZE Number objects (list of Number)
    -------------------------------------------------------
    """
    values = []
    
    for i in range(SIZE):
        values.append(Number(i))

    return values


def create_reversed():
    """
    -------------------------------------------------------
    Create a reversed list of SIZE Number objects with values
    from SIZE-1 down to 0.
    Use: values = create_reversed()
    -------------------------------------------------------
    Returns:
        values - a reversed list of SIZE Number objects (list of Number)
    -------------------------------------------------------
    """
    values = []
    
    for i in range(SIZE-1, -1, -1):
        values.append(Number(i))

    return values


def create_randoms():
    """
    -------------------------------------------------------
    Create a 2D list of Number objects with TESTS rows and
    SIZE columns of values between 0 and XRANGE.
    Use: lists = create_randoms()
    -------------------------------------------------------
    Returns:
        arrays - TESTS lists of SIZE Number objects containing
            values between 0 and XRANGE (list of list of Number)
    -------------------------------------------------------
    """
    arrays = []

    for _ in range(TESTS):
        arr = []
        for _ in range(SIZE):
            val = random.randint(0, XRANGE)
            arr.append(Number(val))
            
        arrays.append(arr)

    return arrays


def test_sort(title, func):
    """
    -------------------------------------------------------
    Test a sort function with Number data and prints the number 
    of comparisons necessary to sort an array:
    in order, in reverse order, and a list of arrays in random order.
    Use: test_sort(title, func)
    -------------------------------------------------------
    Parameters:
        title - name of the sorting function to call (str)
        func - the actual sorting function to call (function)
    Returns:
        None
    -------------------------------------------------------
    """
    inorder_arr = create_sorted()
    reversed_arr = create_reversed()
    random_arrs = create_randoms()
    
    func(inorder_arr)
    inorder_swaps = Sorts.swaps
    inorder_comparisons = Number.comparisons
    
    Sorts.swaps = 0
    Number.comparisons = 0
    
    func(reversed_arr)
    reversed_swaps = Sorts.swaps
    reversed_comparisons = Number.comparisons
    
    Sorts.swaps = 0
    Number.comparisons = 0
    
    for arr in random_arrs:
        func(arr)
    
    random_swaps = Sorts.swaps/TESTS
    random_comparisons = Number.comparisons/TESTS
    
    Sorts.swaps = 0
    Number.comparisons = 0
    
    print(f"{title:14s} {inorder_comparisons:8d} {reversed_comparisons:8d} {random_comparisons:>8.0f} {inorder_swaps:8.0f} {reversed_swaps:8.0f} {random_swaps:>8.0f}")
    
    return


print(f"n: {SIZE:5d}       |      Comparisons       | |         Swaps          |")
print(f"Algorithm       In Order Reversed   Random In Order Reversed   Random")
print("-------------- -------- -------- -------- -------- -------- --------")
for sort in SORTS:
    test_sort(sort[0], sort[1])