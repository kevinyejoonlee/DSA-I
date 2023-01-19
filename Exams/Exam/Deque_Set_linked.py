"""
-------------------------------------------------------
Linked version of the Deque Set ADT.
-------------------------------------------------------
Author: Kevin Lee
ID:     210872060
Email:  leex7206@mylaurier.ca
__updated__ = "2022-04-06"
-------------------------------------------------------
"""
# pylint: disable=protected-access

# Imports
from copy import deepcopy


class _Deque_Set_Node:

    def __init__(self, value, _prev, _next):
        """
        -------------------------------------------------------
        Initializes a Deque_Set n.
        Use: n = _Deque_Set_Node(value, _prev, _next)
        -------------------------------------------------------
        Parameters:
            value - value value for n (?)
            _prev - another Deque_Set n (_Deque_Set_Node)
            _next - another Deque_Set n (_Deque_Set_Node)
        Returns‌‌​​​‌‌​:
            a new _Deque_Set_Node object (_Deque_Set_Node)

        -------------------------------------------------------
        """
        self._value = deepcopy(value)
        self._prev = _prev
        self._next = _next


class Deque_Set:

    def __init__(self):
        """
        -------------------------------------------------------
        Initializes an empty Deque_Set.
        Use: d = Deque_Set()
        -------------------------------------------------------
        Returns‌‌​​​‌‌​:
            a new Deque_Set object (Deque_Set)
        -------------------------------------------------------
        """
        self._front = None
        self._rear = None
        self._count = 0

    def _linear_search(self, key):
        """
        -------------------------------------------------------
        Private helper method.
        Searches for key in a Deque_Set.
        Use: curr = self._linear_search(key)
        -------------------------------------------------------
        Parameters:
            key - a partial data element (*)
        Returns‌‌​​​‌‌​:
            curr - pointer to n containing key, None if not found (_Deque_Set_Node)
        -------------------------------------------------------
        """
        t = False
        curr = self._front
        
        while curr is not None and not t:
            if curr._value == key:
                t = True
            else:
                curr = curr._next

        return curr


    def _move_front_to_rear(self, source):
        """
        -------------------------------------------------------
        Private helper method.
        Moves the front n from source to the rear of self.
        Does *not* validate that self is still a set.
        Use: self._move_front_to_rear(source)
        -------------------------------------------------------
        Parameters:
            source - a non-empty Deque_Set (Deque_Set)
        Returns‌‌​​​‌‌​:
            self contains the old front of source as its rear.
            source front is updated. The counts of self and source are updated.
        -------------------------------------------------------
        """
        assert source._front is not None, \
            "Cannot move the front of an empty Deque_Set"

        n = source._front
        source._front = n._next
        
        if source._front is not None:
            source._front._prev = None
            
        else:
            source._rear = None
        
        if self._rear is not None:
            self._rear._next = n
            
        else:
            self._front = n
        
        n._prev = self._rear
        n._next = None
        self._rear = n
        
        source._count -=1
        self._count += 1

        return

    def is_empty(self):
        """
        -------------------------------------------------------
        Determines if a Deque_Set is empty.
        Use: b = source.is_empty()
        -------------------------------------------------------
        Returns‌‌​​​‌‌​:
            True if source is empty, False otherwise.
        -------------------------------------------------------
        """
        return self._count == 0

    def __len__(self):
        """
        -------------------------------------------------------
        Returns the size of a Deque_Set.
        Use: n = len(source)
        -------------------------------------------------------
        Returns‌‌​​​‌‌​:
            the number of values in source (int)
        -------------------------------------------------------
        """

        return self._count

    def insert_front(self, value):
        """
        -------------------------------------------------------
        Inserts a copy of value into the front of a Deque_Set.
        value cannot already be in the Deque_Set.
        Updates _count appropriately.
        Use: source.insert_front(value)
        -------------------------------------------------------
        Parameters:
            value - a data element (*)
        Returns‌‌​​​‌‌​:
            x - True if value is added to front of source, False otherwise.
        -------------------------------------------------------
        """

        x = False
        if self._linear_search(value) is None:
            
            x = True
            n = _Deque_Set_Node(value, None, self._front)
            
            if self._front is not None:
                self._front._prev = n
                
            else:
                self._rear = n
                
            self._front = n
            self._count += 1
            
        return x


    def insert_rear(self, value):
        """
        -------------------------------------------------------
        Inserts a copy of value into the front of a Deque_Set.
        value cannot already be in the Deque_Set.
        Updates _count appropriately.
        Use: source.insert_rear(value)
        -------------------------------------------------------
        Parameters:
            value - a data element (*)
        Returns‌‌​​​‌‌​:
            x - True if value is added to rear of source, False otherwise.
        -------------------------------------------------------
        """


        x = False
        if self._linear_search(value) is None:
            
            x = True
            n = _Deque_Set_Node(value, self._rear, None)
            
            if self._rear is not None:
                self._rear._next = n
                
            else:
                self._front = n
                
            self._rear = n
            self._count += 1

        return x


    def remove_front(self):
        """
        -------------------------------------------------------
        Removes and returns value from the front of a Deque_Set.
        Updates _count appropriately.
        Use: v = source.remove_front()
        -------------------------------------------------------
        Returns‌‌​​​‌‌​:
            value - the value at the front of source (*)
        -------------------------------------------------------
        """
        assert self._front is not None, "Cannot remove from an empty Deque_Set"

        value = self._front._value
        self._front = self._front._next
        self._count -= 1
        
        if self._front is None:
            self._rear = None

        return value


    def remove_rear(self):
        """
        -------------------------------------------------------
        Removes and returns value from the rear of a Deque_Set.
        Updates _count appropriately.
        Use: v = source.remove_rear()
        -------------------------------------------------------
        Returns‌‌​​​‌‌​:
            value - the value at the rear of source (*)
        -------------------------------------------------------
        """
        assert self._rear is not None, "Cannot remove from an empty Deque_Set"

        value = self._rear._value
        self._rear = self._rear._prev
        self._count -= 1
        
        if self._rear is None:
            self._front = None

        return value


    def remove(self, key):
        """
        -------------------------------------------------------
        Finds, removes, and returns the x in source that matches key.
        Updates _count appropriately.
        Use: x = source.remove(key)
        -------------------------------------------------------
        Parameters:
            key - a partial data element (*)
        Returns‌‌​​​‌‌​:
            x - the full x matching key, otherwise None (*)
        -------------------------------------------------------
        """

        
        x = None
        n = self._linear_search(key)
        
        if n is not None:
            x = n._value
            prev_node = n._prev
            next_node = n._next
            
            if prev_node is not None:
                prev_node._next = next_node
            if next_node is not None:
                next_node._prev = prev_node
            if self._front == n:
                self._front = next_node
            if self._rear == n:
                self._rear = prev_node
            self._count -= 1


        return x

    def max(self):
        """
        -------------------------------------------------------
        Finds the maximum v in a Deque_Set.
        Use: v = source.max()
        -------------------------------------------------------
        Returns‌‌​​​‌‌​:
            a copy of the maximum v in source (?)
        -------------------------------------------------------
        """
        assert self._front is not None, "Cannot find maximum of an empty Deque_Set"

        v = self._front._value
        curr = self._front._next

        while curr is not None:
            if curr._value > v:
                v = curr._value
            curr = curr._next
        return deepcopy(v)

    def split_key(self, key):
        """
        -------------------------------------------------------
        Splits source so that target1 contains all values < key,
        and target2 contains all values >= key. source is empty
        when finished.
        Nodes are moved, values are not copied.
        Updates _count appropriately.
        Use: target1, target2 = source.split_key(key)
        -------------------------------------------------------
        Parameters:
            key - a key value to split source upon (?)
        Returns‌‌​​​‌‌​:
            target1 - a new Deque_Set of values < key (Deque_Set)
            target2 - a new Deque_Set of values >= key (Deque_Set)
        -------------------------------------------------------
        """
        
        target1 = Deque_Set()
        target2 = Deque_Set()

        while self._front is not None:
            
            if self._front._value < key:
                target1._move_front_to_rear(self)
                
            else:
                target2._move_front_to_rear(self)

        return target1, target2
   

    def combine(self, source1, source2):
        """
        -------------------------------------------------------
        Combines source1 and source2 into target.
        When finished, the contents of source1 and source2 are interlaced
        into target and source1 and source2 are empty.
        Order of source values is preserved.
        Values may appear only once in target.
        Nodes are moved, values are not copied.
        Updates _count appropriately.
        Use: target.combine(source1, source2)
        -------------------------------------------------------
        Parameters:
            source1 - a Deque_Set (Deque_Set)
            source2 - a Deque_Set (Deque_Set)
        Returns‌‌​​​‌‌​:
            None
        -------------------------------------------------------
        """
        assert self._front is None, "target must be empty"
                
        while source1._front is not None and source2._front is not None:
            if self._linear_search(source1._front._value) is None:
                self._move_front_to_rear(source1)
                
            else:
                source1._front = source1._front._next
                
            if self._linear_search(source2._front._value) is None:
                self._move_front_to_rear(source2)
                
            else:
                source2._front = source2._front._next
        
        while source1._front is not None:
            
            if self._linear_search(source1._front._value) is None:
                self._move_front_to_rear(source1)
                
            else:
                source1._front = source1._front._next
        
        while source2._front is not None:
        
            if self._linear_search(source2._front._value) is None:
                self._move_front_to_rear(source2)
                
            else:
                source2._front = source2._front._next
                
        source1._front, source1._rear, source2._front, source2._rear = None, None, None, None
        source1._count, source2._count = 0, 0

        
        return
# DO NOT CHANGE CODE BELOW THIS LINE
# =======================================================================

    def peek_front(self):
        """
        -------------------------------------------------------
        Peeks at the front of a Deque_Set.
        Use: v = source.peek_front()
        -------------------------------------------------------
        Returns‌‌​​​‌‌​:
            a copy of the value at the front of source (?)
        -------------------------------------------------------
        """
        assert self._front is not None, "Cannot peek at an empty Deque_Set"

        return deepcopy(self._front._value)

    def peek_rear(self):
        """
        -------------------------------------------------------
        Peeks at the rear of a Deque_Set.
        Use: v = source.peek_rear()
        -------------------------------------------------------
        Returns‌‌​​​‌‌​:
            a copy of the value at the rear of source (?)
        -------------------------------------------------------
        """
        assert self._rear is not None, "Cannot peek at an empty Deque_Set"

        return deepcopy(self._rear._value)

    def __iter__(self):
        """
        USE FOR TESTING ONLY
        -------------------------------------------------------
        Generates a Python iterator. Iterates through the deque
        from front to rear.
        Use: for v in d:
        -------------------------------------------------------
        Returns‌‌​​​‌‌​:
            yields
            value - the next value in the deque (?)
        -------------------------------------------------------
        """
        current = self._front

        while current is not None:
            yield current._value
            current = current._next
