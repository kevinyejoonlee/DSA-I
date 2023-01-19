"""
-------------------------------------------------------
Set_linked.py
Linked version of the Set ADT
-------------------------------------------------------
Author: Kevin Lee
ID:     210872060
Email:  leex7206@mylaurier.ca
__updated__ = '2022-01-15'
-------------------------------------------------------
"""

# Imports
from copy import deepcopy

class _Set_Node:
    
    def __init__(self, value, next_):
        """
        -------------------------------------------------------
        Initializes a Set node that contains a copy of value
        and a link to another Set node.
        Use: node = _Set_Node(value, next_)
        -------------------------------------------------------
        Parameters:
        value - value for node (?)
        next_ - another Set node (_Set_Node)
        Returns:
        a new _Set_Node object (_Set_Node)
        -------------------------------------------------------
        """
        self._value = deepcopy(value)
        self._next = next_

class Set:
    
    def __init__(self):

        """
        -------------------------------------------------------
        Efficiency: O(*)
        -------------------------------------------------------
        Initializes an empty Set.
        Use: set = Set()
        -------------------------------------------------------
        Returns:
        A new Set object (Set)
        -------------------------------------------------------
        """
        self._front = None
        self._count = 0
        
    def is_empty(self):
        """
        -------------------------------------------------------
        Efficiency: O(n^2)
        -------------------------------------------------------
        Determines if source is empty.
        Use: empty = source.is_empty()
        -------------------------------------------------------
        Returns:
        True if source is empty, False otherwise.
        -------------------------------------------------------
        """
        return self._count == 0
    
    def __len__(self):
        """
        -------------------------------------------------------
        Efficiency: O(n^2)
        -------------------------------------------------------
        Returns the number of values in source.
        Use: n = len(source)
        -------------------------------------------------------
        Returns:
        the number of values in source.
        -------------------------------------------------------
        """
        return self._count
    
    def _linear_search(self, key):
        """
        -------------------------------------------------------
        Efficiency: O(n)
        -------------------------------------------------------
        Searches for the first occurrence of key in self.
        (Private helper method.)
        Use: prev, curr = self._linear_search(key)
        -------------------------------------------------------
        Parameters:
        key - a partial data element (?)
        Returns:
        prev - pointer to node prev to the node containing key
           
        (_Set_Node)
        curr - pointer to node containing key, None if not
        found (_Set_Node)
        -------------------------------------------------------
        """
        prev = None
        curr = self._front
        i = 0
        
        while curr is not None and curr._value != key:
            prev = curr
            curr = curr._next
            i += 1
        
        if curr is None:
            curr = None
            
        return prev, curr      
    
    def add(self, value):
        """
        -------------------------------------------------------
        Efficiency: O(n)
        ---------------------------------------------------------
        Adds value to end of source, allows only one copy of
        value.
        Use: added = source.add(value)
        -------------------------------------------------------
        Parameters:
        value - a comparable data element (?)
        Returns:
        added - True if value is added to source, False
        otherwise (boolean)
        -------------------------------------------------------
        """
        self._values.append(deepcopy(value))
        
        if value in self._values:
            added = True
        else:
            added = False
        
        return added
    
    def remove(self, key):
        """
        -------------------------------------------------------
        Efficiency: O(n)
        -------------------------------------------------------
        Finds, removes, and returns value in source that matches
        key.
        Returns None if no matching value.
        Use: value = source.remove(key)
        -------------------------------------------------------
        Parameters:
        key - a partial data element (?)
        Returns:
        value - the value matching key, otherwise None (?)
        -------------------------------------------------------
        """
        prev, curr = self._linear_search(key)
        
        if curr is None:
            value = None
        else:
            value = curr._value
            self._count -= 1
        
            if prev is None:
                self._front = self._front._next
            else:
                prev._next = curr._next
        
        return value

    def find(self, key):
        """
        -------------------------------------------------------
        Efficiency: O(n)
        -------------------------------------------------------
        Finds and returns a copy of value in source that matches
        key.
        Use: value = source.find(key)
        -------------------------------------------------------
        Parameters:
        key - a partial data element (?)
        Returns:
        value - a copy of value matching key, otherwise None
        (?)
        -------------------------------------------------------
        """
        value = None
        
        _, curr = self._linear_search(key)
        
        if curr != None:
            value = curr._value
        
        return value
    
    def __contains__(self, key):
        """
        -------------------------------------------------------
        Efficiency: O(n log n)
        ---------------------------------------------------------
        Determines if source contains a value matching key.
        Use: b = key in source
        -------------------------------------------------------
        Parameters:
        key - a partial data element (?)
        Returns:
        True if source contains key, False otherwise.
        (boolean)
        -------------------------------------------------------
        """
        _, curr = self._linear_search(key)
        
        return curr is not None
    
    def max(self):
        """
        -------------------------------------------------------
        Efficiency: O(log n)
        -------------------------------------------------------
        Returns a copy of maximum value in source.
        Use: value = source.max()
        -------------------------------------------------------
        Returns:
        value - a copy of maximum value in source (?)
        -------------------------------------------------------
        """
        assert self._count > 0, "Cannot find maximum of an empty set"
        
        value = self._front._value
        current = self._front._next
        
        while current is not None:
            if value < current._value:
                value = current._value
            current = current._next
        value = deepcopy(value)
        
        return value
    
    def min(self):
        """
        -------------------------------------------------------
        Efficiency: O(n)
        -------------------------------------------------------
        Returns a copy of minimum value in source.
        Use: value = source.min()
        -------------------------------------------------------
        Returns:
        value - a copy of minimum value in source (?)
        -------------------------------------------------------
        """
        assert self._count > 0, "Cannot find minimum of an empty set"
        
        value = self._front._value
        current = self._front._next
        
        while current is not None:
            if value > current._value:
                value = current._value
            current = current._next
    
    
        return deepcopy(value)
    
    def split_th(self):
        """
        -------------------------------------------------------
        Efficiency: O(log n)
        -------------------------------------------------------
        Splits source into two parts. target1 contains the first
        half,
        target2 the second half. source becomes empty.
        Uses Tortoise/Hare algorithm.
        Use: target1, target2 = source.split_th()
        -------------------------------------------------------
        Returns:
        target1 - a new set with >= 50% of the original set
        (Set)
        target2 - a new set with <= 50% of the original set
        (Set)
        -------------------------------------------------------
        """
        target1 = Set()
        target2 = Set()
        
        if len(self) % 2 == 0:
            target1._value = self._value[:len(self._value) // 2]
            target2._value = self._value[len(self._value) // 2:]
        else:
            target1._value = self._value[:len(self._value) // 2 + 1]
            target2._value = self._value[len(self._value) // 2 + 1:]
        
        self._value = []
        
        return target1, target2

    def intersection(self, source):
        """
        -------------------------------------------------------
        Efficiency: O(n log n)
        -------------------------------------------------------
        Returns a new set with only the values that appear in both
        self and source.
        Resulting order is not guaranteed.
        Use: target = self.intersection(source)
         -------------------------------------------------------
        Parameters:
        source - a set (Set)
        Returns:
        target - a set containing one copy of all the values
        that appear in both self and source (Set)
        -------------------------------------------------------
        Examples:
        (1,2,3) intersection (3,2,1) is (1,2,3)
        (1,2,3) intersection (4,5,6) is ()
        (1,2,3,4,5,6) intersection (0,2,4,6,8) is (2,4,6)
        -------------------------------------------------------
        """
        target = []
        for values in source._value:
            if values in self._value:
                target.append(deepcopy(values))
        
        return target
    
    def union(self, source):
        """
        -------------------------------------------------------
        Efficiency: O(n log n)
        -------------------------------------------------------
        Returns a new set with copies of all values from self and
        source.
        Values may appear in target only once.
        Resulting order is not guaranteed.
        Use: target = self.union(source)
        -------------------------------------------------------
        Parameters:
        source - a set (Set)
        Returns:
        target - a set containing one copy of all the values
        of self and source (Set)
        -------------------------------------------------------
        Examples:
        (1,2,3) union (3,2,1) is (1,2,3)
        (1,2,3) union (4,5,6) is (1,2,3,4,5,6)
        (1,2,3,4,5,6) union (8,2,4,6,0) is (1,2,3,4,5,6,8,0)
        -------------------------------------------------------
        """
        target = []
        for values in source._value:
            if values not in target:
                target.append(deepcopy(values))
                
        for values in self._value:
            if values not in target:
                target.append(deepcopy(values))
        
        return target
    
    def difference(self, source):
        """
        -------------------------------------------------------
        Efficiency: O(n^2)
        -------------------------------------------------------
        Returns a set that contains the items that exist only in
        self and not in source.
        Resulting order is not guaranteed.
        Use: target = self.difference(source)
        -------------------------------------------------------
        Parameters:
        source - a set (Set)
        Returns:
        target - a set containing one copy of all the values
        in self that are not in source (Set)
        -------------------------------------------------------
        Examples:
        (1,2,3) difference (3,2,1) is ()
        (1,2,3) difference (4,5,6) is (1,2,3)
        (1,2,3,4,5,6) difference (0,2,4,6,8) is (1,3,5)
        -------------------------------------------------------
        """
        target = []
        
        for values in self._value:
            if values not in source._value:
                target.append(deepcopy(values))
        
        return target

    def symmetric_difference(self, source):
        """
        -------------------------------------------------------
        Efficiency: O(n log n)
        -------------------------------------------------------
        Returns a set that contains the items that exist in
        self or source, but not in both.
        Resulting order is not guaranteed.
        Use: target = self.symmetric_difference(source)
        ------------------------------------------------------- 
        
        Parameters:
        source - a set (Set)
        Returns:
        target - a set containing one copy of all the values
        in self and source but not in both (Set)
        -------------------------------------------------------
        Examples:
        (1,2,3) symetric_difference (3,2,1) is ()
        (1,2,3) symetric_difference (4,5,6) is (1,2,3,4,5,6)
        (1,2,3,4,5,6) symetric_difference (0,2,4,6,8) is
        (0,1,3,5,8)
        -------------------------------------------------------
        """
        target = []
        for values in source._value:
            if values not in self._value:
                target.append(deepcopy(values))
            
        for values in self._value:
            if values not in source._value:
                target.append(deepcopy(values))
        
        return target 
      
    def issubset(self, source):
        """
        -------------------------------------------------------
        Efficiency: O(n)
        -------------------------------------------------------
        Determines if self is a subset of source. self is a subset
        of source
        if self contains all the values in source.
        Use: same = self.issubset(source)
        -------------------------------------------------------
        Parameters:
        source - a set (Set)
        Returns:
        subset - True if self contains all the values in
        source,
        otherwise False (boolean)
        -------------------------------------------------------
        Examples:
        () issubset (3,2,1) is True
        (1,2,3) issubset (3,2,1) is True
        (1,2,3) issubset (4,5,6) is False
        (2,4,6) issubset (0,2,4,6,8) is True
        ------------------------------------------------------- 
         """

        for values in self._value:
            if values not in source._value:
                subset = False
            elif values == source._value:
                subset = True
        
        return subset   
    
    def isdisjoint(self, source):
        """
        -------------------------------------------------------
        Efficiency: O(n)
        -------------------------------------------------------
        Determines if self is disjoint with source. self is
        disjoint with source
        if self and source have not values in common.
        Use: same = self.isdisjoint(source)
        -------------------------------------------------------
        Parameters:
        source - a set (Set)
        Returns:
        disjoint - True if self and source have not values in
        common,
        otherwise False (boolean)
        -------------------------------------------------------
        Examples:
        () isdisjoint (3,2,1) is True
        (1,2,3) isdisjoint (3,2,1) is True
        (1,2,3) isdisjoint (4,5,6) is False
        (2,4,6) isdisjoint (0,2,4,6,8) is True
        -------------------------------------------------------
        """
        for values in self._value:
            if values not in source._value:
                disjoint = True
            elif values == source._value:
                disjoint = False   
            
        return disjoint
    
    def __iter__(self):
        """
        USE FOR TESTING ONLY
        -------------------------------------------------------
        Generates a Python iterator. Iterates through the set
        from first to last items.
        Use: for v in set:
        -------------------------------------------------------
        Returns:
        yields
        value - the next value in the set (?)
        -------------------------------------------------------
        """
        curr = self._front
        
        while curr is not None:
            yield curr._value
            curr = curr._next
 
 
 
 