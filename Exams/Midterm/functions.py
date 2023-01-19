"""
-------------------------------------------------------
Midterm Functions
-------------------------------------------------------
Author:  Kevin Lee
ID:      210872060
Email:   leex7206@mylaurier.ca
__updated__ = "2022-02-12"
-------------------------------------------------------
"""
# Imports
from Stack_array import Stack
from Priority_Queue_array import Priority_Queue
from importlib._bootstrap_external import SourcelessFileLoader

# Constants
OPERATORS = ('*', '/', '+', '-')


def pq_triage(source, key):
    """
    -------------------------------------------------------
    Removes all values from source that have a priority
    less than key.
    Use: pq_triage(source, key)
    -------------------------------------------------------
    Parameters:
        source - a priority queue (Priority_Queue)
        key - a key value (?)
    Returns​‌‌‌​​​​‌:
        None
    -------------------------------------------------------
    """
    
    list = []
    
    while not source.is_empty():
        removed = source.remove()
    
        if key >= removed:
            list.append(removed)
            
    # list is filled with values only that have greater
    # prio to be added into the PQ
    
    for i in list:
        source.insert(i)


        
def purge(source, key):
    """
    -------------------------------------------------------
    Finds and removes all values in source that match key.
    Use: purge(source, key)
    -------------------------------------------------------
    Parameters:
        source - a List of values (List)
        key - a data element (?)
    Returns​‌‌‌​​​​‌:
        None
    -------------------------------------------------------
    """
    list = []
    
    while not source.is_empty():
        removed = source.remove_front()
    
        if key != removed:
            list.append(removed)

    
    number = 0
    for value in list:
        source.insert(number, value)
        number +=1


def eval_expression(string):
    """
    -------------------------------------------------------
    Evaluates a postfix expression.
    Use: answer = eval_expression(string)
    -------------------------------------------------------
    Parameters:
        string - the space-separted postfix string to evaluate (str)
    Returns​‌‌‌​​​​‌:
        answer - the result of evaluating string (float)
    -------------------------------------------------------
    """
    stack = Stack()
    exp = string.split(" ")
    
    for item in exp:
        if item not in OPERATORS:
            stack.push(float(item))
        else:
            operand2 = stack.pop()
            operand1 = stack.pop()
            
            if item == "+":
                answer = operand1 + operand2
            elif item == "-":
                answer = operand1 - operand2
            elif item == "*":
                answer = operand1 * operand2
            else:
                answer = operand1 / operand2
            
            stack.push(answer)
            
    answer = stack.pop()
    
    return answer
