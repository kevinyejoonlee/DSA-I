"""
-------------------------------------------------------
Simple midterm function testing
-------------------------------------------------------
Author:  Kevin Lee
ID:      210872060
Email:   leex7206@mylaurier.ca
__updated__ = "2022-02-12"
-------------------------------------------------------
"""
# pylint: disable=protected-access

# Imports
from List_array import List
from Priority_Queue_array import Priority_Queue
from functions import pq_triage, purge, eval_expression

# Constants
SEP = "-" * 60


def test_pq_triage():
    """
    Simple tests for the pq_triage function.
    """
    CASES = (
        ([], 999, []), ([1, 2, 3], 999, [1, 2, 3]),
        ([1, 2, 3], 0, []), ([1, 2, 3], 2, [1, 2]),
    )
    print(SEP)
    print('Testing pq_triage')
    for case in CASES:
        source = Priority_Queue()

        for v in case[0]:
            source.insert(v)
        print(f'source._values: {case[0]}')
        pq_triage(source, case[1])
        print(f'pq_triage(source, {case[1]}): {case[2]}')
        values = []
        for v in source:
            values.append(v)
        print(f'    actual result - source._values: {values}')
    return


def test_purge():
    """
    Simple tests for the purge function.
    """
    CASES = (
        ([], 999, []), ([1, 2, 3], 999, [1, 2, 3]),
        ([1, 2, 3], 2, [1, 3]), ([2, 2, 2], 2, []),
    )
    print(SEP)
    print('Testing purge')
    print()
    for case in CASES:
        source = List()

        for v in case[0]:
            source.append(v)
        print(f'source._values: {case[0]}')
        purge(source, case[1])
        print(f'purge(source, {case[1]}): {case[2]}')
        values = []
        for v in source:
            values.append(v)
        print(f'    actual result - source._values: {values}')
    return


def test_eval_expression():
    """
    Simple tests for the eval_expression function.
    """
    CASES = (
        ("0", 0.0), ("1 2 +", 3.0), ("3 2 -", 1.0), ("2.5 3 *", 7.5),
    )
    print(SEP)
    print('Testing eval_expression')
    print()
    for case in CASES:
        print(f'eval_expression("{case[0]}") : {case[1]}')
        result = eval_expression(case[0])
        print(f'    actual result: {result}')
    return


# Main code
# Add or remove commenting as appropriate
test_pq_triage()
test_purge()
test_eval_expression()
