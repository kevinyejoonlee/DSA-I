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

from List_linked import List
from Number import Number
from Sorts_List_linked import Sorts

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
)


def create_sorted():
    """
    -------------------------------------------------------
    Creates a sorted List of Number objects.
    Use: values = create_sorted()
    -------------------------------------------------------
    Returns:
        values - a sorted list of SIZE Number objects (List of Number)
    -------------------------------------------------------
    """
    values = List()
    
    for i in range(SIZE):
        values.append(Number(i))

    return values


def create_reversed():
    """
    -------------------------------------------------------
    Create a reversed List of Number objects.
    Use: values = create_reversed()
    -------------------------------------------------------
    Returns:
        values - a reversed list of SIZE Number objects (List of Number)
    -------------------------------------------------------
    """
    values = List()
    
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
        lists - TESTS lists of SIZE Number objects containing
            values between 0 and XRANGE (list of List of Number)
    -------------------------------------------------------
    """
    lists = []

    for _ in range(TESTS):
        list_ = List()
        for _ in range(SIZE):
            val = random.randint(0, XRANGE)
            list_.append(Number(val))
            
        lists.append(list_)

    return lists


def test_sort(title, func):
    """
    -------------------------------------------------------
    Tests a sort function with Number data and prints the number 
    of comparisons necessary to sort an array:
    in order, in reverse order, and a list of Lists in random order.
    Use: test_sort(title, func)
    -------------------------------------------------------
    Parameters:
        title - name of the sorting function to call (str)
        func - the actual sorting function to call (function)
    Returns:
        None
    -------------------------------------------------------
    """
    inord_lst = create_sorted()
    rev_lst = create_reversed()
    rand_lsts = create_randoms()
    
    func(inord_lst)
    inord_swp = Sorts.swaps
    inord_cmp = Number.comparisons
    
    Sorts.swaps = 0
    Number.comparisons = 0
    
    func(rev_lst)
    rev_swp = Sorts.swaps
    rev_cmp = Number.comparisons
    
    Sorts.swaps = 0
    Number.comparisons = 0
    
    for lst in rand_lsts:
        func(lst)
    
    rand_swp = Sorts.swaps/TESTS
    rand_cmp = Number.comparisons/TESTS
    
    Sorts.swaps = 0
    Number.comparisons = 0
    
    print(f"{title:14s} {inord_cmp:8d} {rev_cmp:8d} {rand_cmp:>8.0f} {inord_swp:8.0f} {rev_swp:8.0f} {rand_swp:>8.0f}")
    
    return


print(f"n: {SIZE:5d}       |      Comparisons       | |         Swaps          |")
print(f"Algorithm      In Order Reversed   Random In Order Reversed   Random")
print("-------------- -------- -------- -------- -------- -------- --------")
for sort in SORTS:
    test_sort(sort[0], sort[1])