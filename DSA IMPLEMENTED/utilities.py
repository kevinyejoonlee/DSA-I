"""
-------------------------------------------------------
utilities- stack
-------------------------------------------------------
Author: Kevin Lee
ID:     210872060
Email:  leex7206@mylaurier.ca
__updated__ = '2022-01-17'
-------------------------------------------------------
"""

from Stack_array import Stack
from Queue_array import Queue
from Priority_Queue_array import Priority_Queue
from List_array import List
#utilities

# =====2
def array_to_stack(stack, source):
    """
    -------------------------------------------------------
    Pushes contents of source onto stack. At finish, source is empty.
    Last value in source is at bottom of stack,
    first value in source is on top of stack.
    Use: array_to_stack(stack, source)
    -------------------------------------------------------
    Parameters:
        stack - a Stack object (Stack)
        source - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """
    
    while len(source) > 0:
        stack.push(source.pop())
        

# ===== 3
def stack_to_array(stack, target):
    """
    -------------------------------------------------------
    Pops contents of stack into target. At finish, stack is empty.
    Top value of stack is at end of target,
    bottom value of stack is at beginning of target.
    Use: stack_to_array(stack, target)
    -------------------------------------------------------
    Parameters:
        stack - a Stack object (Stack)
        target - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """
    
    while not stack.is_empty():
        target.insert(0, stack.pop())
    return
    
    
    

# ===== 4
def stack_test(source):
    """
    -------------------------------------------------------
    Tests the methods of Stack for empty and
    non-empty stacks using the data in source:
    is_empty, push, pop, peek
    (Testing pop and peek while empty throws exceptions)
    Use: stack_test(source)
    -------------------------------------------------------
    Parameters:
        source - list of data (list of ?)
    Returns:
        None
    -------------------------------------------------------
    """
    
    
    
    stack = Stack()
    
    empty = stack.is_empty()
    print(f"is_empty on empty stack: {empty}")
    
    if len(source) > 0:
        stack.push(source[0])
        empty_with_data = stack.is_empty()
        print(f"is_empty on stack with data: {empty_with_data}")
        
        top_item = stack.peek()
        print(f"peek on stack with data: {top_item}")
        
        popped_item = stack.pop()
        print(f"pop on stack with data: {popped_item}")
    
    return
    
# ===== 5

# ========================= Queue

def array_to_queue(queue, source):
    """
    -------------------------------------------------------
    Inserts contents of source into queue. At finish, source is empty.
    Last value in source is at rear of queue,
    first value in source is at front of queue.
    Use: array_to_queue(queue, source)
    -------------------------------------------------------
    Parameters:
        queue - a Queue object (Queue)
        source - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """
    
    while len(source) > 0:
        queue.insert(source.pop(0))

def queue_to_array(queue, target):
    """
    -------------------------------------------------------
    Removes contents of queue into target. At finish, queue is empty.
    Front value of queue is at front of target,
    rear value of queue is at end of target.
    Use: queue_to_array(queue, target)
    -------------------------------------------------------
    Parameters:
        queue - a Queue object (Queue)
        target - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """

    while not queue.is_empty():
        target.append(queue.remove())
        
        
def queue_test(a):
    """
    -------------------------------------------------------
    Tests queue implementation.
  Tests the methods of Queue are tested for both empty and
  non-empty queues using the data in a:
        is_empty, insert, remove, peek, len
    Use: queue_test(a)
    -------------------------------------------------------
    Parameters:
        a - list of data (list of ?)
    Returns:
        None
    -------------------------------------------------------
    """
    a = Queue()

    # tests for the queue methods go here
    # print the results of the method calls and verify by hand
    
    print(f'Queue is_empty: {a.is_empty}')
    
    if not a.is_empty():
        
        print(f'Queue len: {len(a)}')
        print(f'Queue insert: {a.insert()}')
        print(f'Queue remove: {a.remove()}')
        print(f'Queue peek: {a.peek()}')
    return

# ========================= Stack

#-------------------Priority Queue

def array_to_pq(pq, source):
    """
    -------------------------------------------------------
    Inserts contents of source into pq. At finish, source is empty.
    Last value in source is at rear of pq,
    first value in source is at front of pq.
    Use: array_to_pq(pq, source)
    -------------------------------------------------------
    Parameters:
        pq - a Priority_Queue object (Priority_Queue)
        source - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """
    
    while len(source)>0:
        pq.insert(source.pop(0))

def pq_to_array(pq, target):
    """
    -------------------------------------------------------
    Removes contents of pq into target. At finish, pq is empty.
    Highest priority value in pq is at front of target,
    lowest priority value in pq is at end of target.
    Use: pq_to_array(pq, target)
    -------------------------------------------------------
    Parameters:
        pq - a Priority_Queue object (Priority_Queue)
        target - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """
    while not pq.is_empty():
        target.append(pq.remove())

def priority_queue_test(a):
    """
    -------------------------------------------------------
    Tests priority queue implementation.
    Test the methods of Priority_Queue are tested for both empty and
    non-empty priority queues using the data in a:
        is_empty, insert, remove, peek
    Use: priority_queue_test(a)
    -------------------------------------------------------
    Parameters:
        a - list of data (list of ?)
    Returns:
        None
    -------------------------------------------------------
    """
    a = Priority_Queue()

    
    # tests for the queue methods go here
    # print the results of the method calls and verify by hand
    
    print(f'Queue is_empty: {a.is_empty}')
    
    if not a.is_empty():
        
        print(f'Queue len: {len(a)}')
        print(f'Queue insert: {a.insert()}')
        print(f'Queue remove: {a.remove()}')
        print(f'Queue peek: {a.peek()}')
    return

# -------------------------------------------------------- list
def array_to_list(llist, source):
    """
    -------------------------------------------------------
    Appends contests of source to llist. At finish, source is empty.
    Last element in source is at rear of llist,
    first element in source is at front of llist.
    Use: array_to_list(llist, source)
    -------------------------------------------------------
    Parameters:
        llist - a List object (List)
        source - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """
    while len(source) != 0:
        value = source.pop(0)
        
        llist.insert(len(llist), value)
        
    return

def list_to_array(llist, target):
    """
    -------------------------------------------------------
    Removes contents of llist into target. At finish, llist is empty.
    Front element of llist is at front of target,
    rear element of llist is at rear of target.
    Use: list_to_array(llist, target)
    -------------------------------------------------------
    Parameters:
        llist - a List object (List)
        target - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """
    while len(llist) != 0:
        value = llist.pop(0)
        
        target.append(value)
    
def list_test(source):
    """
    -------------------------------------------------------
    Tests List implementation.
    The methods of List are tested for both empty and
    non-empty lists using the data in source
    Use: list_test(source)
    -------------------------------------------------------
    Parameters:
        source - list of data (list of ?)
    Returns:
        None
    -------------------------------------------------------
    """
    lst = List()

    for i in range(len(source)):
        lst.append(source[i])
        
    lst.insert(len(lst), source[i])
        
    while not lst.is_empty():
        _max = lst.max()
        _min = lst.min()
        
        print(f"Max value:\n{_max}")
        print()
        print(f"Min value:\n{_min}")
        print()
        
        val = lst.peek()
        lst.remove(val)
        
        print(f"Removed:\n{val}")
        print()
        
        if lst.count(val):
            val = lst.find(val)
            idx = lst.index(val)
            
            print(f"Found:\n{val}\nAt index: {idx}")
            print()
            
        print("\n\n")

    return
