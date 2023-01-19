"""
-------------------------------------------------------
Linked version of the Sorted_List ADT.
-------------------------------------------------------
Author:  David Brown
ID:      999999999
Email:   dbrown@wlu.ca
Term:    Spring 2021
__updated__ = "2022-02-09"
-------------------------------------------------------
"""

# pylint: disable=W0212

# Imports
from copy import deepcopy


class _SL_Node:

    def __init__(self, value, next_):
        """
        -------------------------------------------------------
        Initializes a sorted list node.
        Use: node = _SL_Node(value, _next)
        -------------------------------------------------------
        Parameters:
            value - value value for node (?)
            next_ - another sorted list node (_ListNode)
        Returns:
            Initializes a list node that contains a copy of value
            and a link to the next node in the list.
        -------------------------------------------------------
        """
        self._value = deepcopy(value)
        self._next = next_
        return


class Sorted_List:

    def __init__(self):
        """
        -------------------------------------------------------
        Initializes an empty Sorted_List.
        Use: sl = Sorted_List()
        -------------------------------------------------------
        Returns:
            a Sorted_List object (Sorted_List)
        -------------------------------------------------------
        """
        self._front = None
        self._rear = None
        self._count = 0

    def is_empty(self):
        """
        -------------------------------------------------------
        Determines if the list is empty.
        Use: b = sl.is_empty()
        -------------------------------------------------------
        Returns:
            True if the list is empty, False otherwise.
        -------------------------------------------------------
        """
        return self._front is None

    def __len__(self):
        """
        -------------------------------------------------------
        Returns the size of the list.
        Use: n = len(l)
        -------------------------------------------------------
        Returns:
            Returns the number of values in the list.
        -------------------------------------------------------
        """
        return self._count

    def insert(self, value):
        """
        -------------------------------------------------------
        Inserts value at the proper place in the sorted list.
        Must be a stable insertion, i.e. consecutive insertions
        of the same value must keep their order preserved.
        Use: sl.insert(value)
        -------------------------------------------------------
        Parameters:
            value - a data element (?)
        Returns:
            None
        -------------------------------------------------------
        """
        if self._front is None:
            # sorted list is empty
            node = _SL_Node(value, None)
            self._front = node
            self._rear = node
        elif value < self._front._value:
            # New value has lowest value
            self._front = _SL_Node(value, self._front)
        elif value >= self._rear._value:
            # New value has highest value
            node = _SL_Node(value, None)
            self._rear._next = node
            self._rear = node
        else:
            # Find the proper position for value.
            prev = None
            curr = self._front

            while value >= curr._value:
                prev = curr
                curr = curr._next

            # Create the new node and link it to curr.
            # The previous node is linked to the new node.
            prev._next = _SL_Node(value, curr)
        # Increment the sorted list size.
        self._count += 1
        return

    def _linear_search(self, key):
        """
        Cannot do a (simple) binary search on a linked structure.
        -------------------------------------------------------
        Searches for the first occurrence of key in the sorted list.
        Performs a stable search.
        Private helper method - used only by other ADT methods.
        Use: i = self._linear_search(key)
        -------------------------------------------------------
        Parameters:
            key - a partial data element (?)
        Returns:
            previous - pointer to the node previous to the node containing key (_ListNode)
            current - pointer to the node containing key (_ListNode)
            index - index of the node containing key, -1 if key not found (int)
        -------------------------------------------------------
        """
        previous = None
        current = self._front
        index = 0

        while current is not None and current._value < key:
            # Take advantaged of fact the list is sorted.
            previous = current
            current = current._next
            index += 1

        if current is None or current._value != key:
            index = -1

        return previous, current, index

    def remove(self, key):
        """
        -------------------------------------------------------
        Finds, removes, and returns the value in the sorted list that matches key.
        Use: value = sl.remove( key )
        -------------------------------------------------------
        Parameters:
            key - a partial data element (?)
        Returns:
            value - the full value matching key, otherwise None (?)
        -------------------------------------------------------
        """
        # search list for key.
        previous, current, index = self._linear_search(key)

        if index == -1:
            # Key is not found.
            value = None
        else:
            value = current._value
            self._count -= 1

            if previous is None:
                # Remove the first node.
                self._front = self._front._next

                if self._front is None:
                    # List is empty, update _rear.
                    self._rear = None
            else:
                # Remove any other node.
                previous._next = current._next

                if previous._next is None:
                    # Last node was removed, update _rear.
                    self._rear = previous
        return value

    def remove_front(self):
        """
        -------------------------------------------------------
        Removes the first node in the list and returns its value.
        Use: value = lst.remove_front()
        -------------------------------------------------------
        Returns:
            value - the first value in the list (?)
        -------------------------------------------------------
        """
        assert self._front is not None, "Cannot remove from an empty list"

        value = self._front._value
        self._front = self._front._next
        self._count -= 1

        if self._front is None:
            # Last node has been removed
            self._rear = None
        return value

    def remove_many(self, key):
        """
        -------------------------------------------------------
        Finds and removes all values in the list that match key.
        Use: l.remove_many(key)
        -------------------------------------------------------
        Parameters:
            key - a data element (?)
        Returns:
            All values matching key are removed from the list.
        -------------------------------------------------------
        """
        # Find the first occurrence of key.
        previous, current, _ = self._linear_search(key)
        count = 0

        while current is not None and current._value == key:
            # Walk through and count all values that match key.
            current = current._next
            count += 1

        if count == self._count:
            # all values have been removed
            self._front = None
            self._rear = None
            self._count = 0
        elif count > 0:
            self._count -= count
            # Link from previous to the first node past the key values.
            if previous is None:
                # Update the first node.
                self._front = current
            else:
                # Update any other node.
                previous._next = current

            if current is None:
                # Rear node has been removed
                self._rear = previous
        return

    def find(self, key):
        """
        -------------------------------------------------------
        Finds and returns a copy of value in list that matches key.
        Use: value = l.find( key )
        -------------------------------------------------------
        Parameters:
            key - a partial data element (?)
        Returns:
            value - a copy of the full value matching key, otherwise None (?)
        -------------------------------------------------------
        """
        _, current, i = self._linear_search(key)

        if i != -1:
            value = deepcopy(current._value)
        else:
            value = None
        return value

    def peek(self):
        """
        -------------------------------------------------------
        Returns a copy of the first value in list.
        Use: value = l.peek()
        -------------------------------------------------------
        Returns:
            value - a copy of the first value in the list (?)
        -------------------------------------------------------
        """
        assert self._front is not None, "Cannot peek at an empty list"

        value = deepcopy(self._front._value)
        return value

    def index(self, key):
        """
        -------------------------------------------------------
        Finds location of a value by key in list.
        Use: n = l.index( key )
        -------------------------------------------------------
        Parameters:
            key - a partial data element (?)
        Returns:
            i - the index of the location of key in the list, -1 if
              key is not in the list.
        -------------------------------------------------------
        """
        _, _, i = self._linear_search(key)
        return i

    def _is_valid_index(self, i):
        """
        -------------------------------------------------------
        Private helper method to validate an index value.
        Python index values can be positive or negative and range from
          -len(list) to len(list) - 1
        Use: assert self._is_valid_index(i)
        -------------------------------------------------------
        Parameters:
            i - an index value (int)
        Returns:
            True if i is a valid index, False otherwise.
        -------------------------------------------------------
        """
        n = self._count
        return -n <= i < n

    def __getitem__(self, i):
        """
        ---------------------------------------------------------
        Returns a copy of the nth element of the list.
        Use: value = l[i]
        -------------------------------------------------------
        Parameters:
            i - index of the element to access (int)
        Returns:
            value - the i-th element of list (?)
        -------------------------------------------------------
        """
        assert self._is_valid_index(i), "Invalid index value"

        current = self._front

        if i < 0:
            # negative index - convert to positive
            i = self._count + i
        j = 0

        while j < i:
            current = current._next
            j += 1

        value = deepcopy(current._value)
        return value

    def __contains__(self, key):
        """
        ---------------------------------------------------------
        Determines if the list contains key.
        Use: b = key in l
        -------------------------------------------------------
        Parameters:
            key - a partial data element (?)
        Returns:
            True if the list contains key, False otherwise.
        -------------------------------------------------------
        """
        _, _, i = self._linear_search(key)
        return i != -1

    def max(self):
        """
        -------------------------------------------------------
        Finds the maximum value in the sorted list.
        Use: value = sl.max()
        -------------------------------------------------------
        Returns:
            value - a copy of the maximum value in the sorted list (?)
        -------------------------------------------------------
        """
        assert self._front is not None, "Cannot find maximum of an empty list"

        value = deepcopy(self._rear._value)
        return value

    def min(self):
        """
        -------------------------------------------------------
        Finds the minimum value in the sorted list.
        Use: value = sl.min()
        -------------------------------------------------------
        Returns:
            value - a copy of the minimum value in the sorted list (?)
        -------------------------------------------------------
        """
        assert self._front is not None, "Cannot find minimum of an empty list"

        value = deepcopy(self._front._value)
        return value

    def count(self, key):
        """
        -------------------------------------------------------
        Determines the number of times key appears in the sorted list.
        Use: n = sl.count(key)
        -------------------------------------------------------
        Parameters:
            key - a data element (?)
        Returns:
            number - the number of times key appears in the sorted list (int)
        -------------------------------------------------------
        """
        number = 0
        _, current, i = self._linear_search(key)

        if i > -1:
            while current is not None and current._value == key:
                number += 1
                current = current._next

        return number

    def clean(self):
        """
        ---------------------------------------------------------
        Removes duplicates from the sorted list. The list contains
        one and only one of each value formerly present in the list.
        The first occurrence of each value is preserved.
        Use: sl.clean()
        -------------------------------------------------------
        Returns:
            None
        -------------------------------------------------------
        """
        key_node = self._front

        while key_node is not None:
            # Loop through every node - compare each node with the rest
            current = key_node._next

            while current is not None and current._value == key_node._value:
                # Skip over nodes with matching values
                key_node._next = current._next
                self._count -= 1
                current = current._next

            if current is None:
                # Reached the end of the list - update _rear
                self._rear = key_node
            key_node = key_node._next
        return

    def pop(self, *i):
        """
        -------------------------------------------------------
        Finds, removes, and returns the value in list whose index matches i.
        Use: value = l.remove(i)
        -------------------------------------------------------
        Parameters:
            i - an array of arguments (?)
                i[0], if it exists, is the index
        Returns:
            value - if i exists, the value at position i, otherwise the last
                value in the list, value is removed from the list (?)
        -------------------------------------------------------
        """
        assert self._front is not None, "Cannot pop from an empty list"
        assert len(i) <= 1, "No more than 1 argument allowed"

        previous = None
        current = self._front

        if len(i) == 1:

            if i[0] < 0:
                # index is negative
                n = self._count + i[0]
            else:
                n = i[0]
            j = 0

            while j < n:
                previous = current
                current = current._next
                j += 1
        else:
            # find and pop the last element
            j = 0

            while j < (self._count - 1):
                previous = current
                current = current._next
                j += 1

        value = current._value
        self._count -= 1

        if previous is None:
            # Remove the first node.
            self._front = self._front._next

            if self._front is None:
                # List is empty, update _rear.
                self._rear = None
        else:
            # Remove any other node.
            previous._next = current._next

            if previous._next is None:
                # Last node was removed, update _rear.
                self._rear = previous
        return value

    def intersection(self, source1, source2):
        """
        -------------------------------------------------------
        Update the current list with values that appear in both
        source1 and source2. Values do not repeat.
        (iterative algorithm)
        Use: target.intersection(source1, source2)
        -------------------------------------------------------
        Parameters:
            source1 - a linked list (Sorted_List)
            source2 - a linked list (Sorted_List)
        Returns:
            None
        -------------------------------------------------------
        """
        assert self._front is None, "Target list must be empty"

        source1_node = source1._front
        source2_node = source2._front

        while source1_node is not None and source2_node is not None:

            if source1_node._value < source2_node._value:
                # Data does not match - move to next node in self
                source1_node = source1_node._next
            elif source1_node._value > source2_node._value:
                # Data does not match - move to next node in rs
                source2_node = source2_node._next
            else:
                # Value exists in both lists.
                if self._front is None:
                    # Add new node to self
                    self._front = _SL_Node(source1_node._value, None)
                    self._rear = self._front
                    self._count += 1
                elif self._rear._value < source1_node._value:
                    # Add new node to the end of self
                    self._rear._next = _SL_Node(source1_node._value, None)
                    self._rear = self._rear._next
                    self._count += 1
                else:
                    # Value already in self - move to next node in both sources
                    source1_node = source1_node._next
                    source2_node = source2_node._next
        return

    def union(self, source1, source2):
        """
        -------------------------------------------------------
        Update the current list with all values that appear in
        source1 and source2. Values do not repeat.
        (iterative algorithm)
        Use: target.union(source1, source2)
        -------------------------------------------------------
        Parameters:
            source1 - an linked list (Sorted_List)
            source2 - an linked list (Sorted_List)
        Returns:
            None
        -------------------------------------------------------
        """
        assert self._front is None, "Target list must be empty"

        source1_node = source1._front
        source2_node = source2._front

        while source1_node is not None and source2_node is not None:

            if source1_node._value < source2_node._value:
                new_value = source1_node._value
                source1_node = source1_node._next
            elif source1_node._value > source2_node._value:
                new_value = source2_node._value
                source2_node = source2_node._next
            else:
                # Value exists in both lists.
                new_value = source1_node._value
                # Value already in self - move to next node in both sources
                source1_node = source1_node._next
                source2_node = source2_node._next

            if self._front is None:
                # Add new node to self
                self._front = _SL_Node(new_value, None)
                self._rear = self._front
                self._count += 1
            elif self._rear._value < new_value:
                # Add new node to the end of self
                self._rear._next = _SL_Node(new_value, None)
                self._rear = self._rear._next
                self._count += 1

        # Determine which source list still has data, if any
        if source1_node is not None:
            source_node = source1_node
        elif source2_node is not None:
            source_node = source2_node
        else:
            source_node = None

        if self._front is None and source_node is not None:
            # Add at least one value to the front of self
            self._front = _SL_Node(source_node._value, None)
            self._rear = self._front
            self._count += 1
            source_node = source_node._next

        # Unique occurrences of the remaining data are added.
        while source_node is not None:

            if self._rear._value < source_node._value:
                # Add new node to the end of self
                self._rear._next = _SL_Node(source_node._value, None)
                self._rear = self._rear._next
                self._count += 1
            source_node = source_node._next
        return

    def split_key(self, key):
        """
        -------------------------------------------------------
        Splits list so that target1 contains all values <= key,
        and target2 contains all values > key.
        Use: target1, target2 = lst.split_key(key)
        -------------------------------------------------------
        Returns:
            target1 - a new Sorted_List of values <= key (Sorted_List)
            target2 - a new Sorted_List of values > key (Sorted_List)
        -------------------------------------------------------
        """
        target1 = Sorted_List()
        target2 = Sorted_List()

        if self._count > 0:

            if key <= self._front._value:
                # All nodes go to target2.
                target2._front = self._front
                target2._rear = self._rear
                target2._count = self._count
            elif key > self._rear._value:
                # All nodes go to target1.
                target1._front = self._front
                target1._rear = self._rear
                target1._count = self._count
            else:
                # Nodes divided between targets.
                prev = None
                curr = self._front
                count = 0

                while curr is not None and curr._value < key:
                    # Find the location to split_key the list.
                    prev = curr
                    curr = curr._next
                    count += 1

                prev._next = None
                target1._front = self._front
                target1._rear = prev
                target1._count = count
                target2._front = curr
                target2._rear = self._rear
                target2._count = self._count - count

            # Empty the original queue
            self._front = None
            self._rear = None
            self._count = 0
        return target1, target2

    def split_alt(self):
        """
        -------------------------------------------------------
        Splits the source list into separate target lists with values
        alternating into the targets. At finish source list is empty.
        Order of source values is preserved.
        (iterative algorithm)
        Use: target1, target2 = source.split_alt()
        -------------------------------------------------------
        Returns:
            target1 - contains alternating values from source (Sorted_List)
            target2 - contains other alternating values from source (Sorted_List)
        -------------------------------------------------------
        """
        target1 = Sorted_List()
        target2 = Sorted_List()
        left = True

        while self._front is not None:

            if left:
                target1._move_front_to_rear(self)
            else:
                target2._move_front_to_rear(self)
            left = not left

        return target1, target2

    def split(self):
        """
        -------------------------------------------------------
        Splits list into two parts. target1 contains the first half,
        target2 the second half. Current list becomes empty.
        Use: target1, target2 = source.split()
        -------------------------------------------------------
        Returns:
            target1 - >= 50% of the source Sorted_List (Sorted_List)
            target2 - <= 50% of the source Sorted_List (Sorted_List)
        -------------------------------------------------------
        """
        target1 = Sorted_List()
        target2 = Sorted_List()
        # Split
        middle = self._count // 2 + self._count % 2
        prev = None
        curr = self._front

        for _ in range(middle):
            prev = curr
            curr = curr._next

        if prev is not None:
            # Break the source list between prev and curr
            prev._next = None

        # Define target1
        target1._count = middle
        target1._front = self._front
        target1._rear = prev

        # Define target2
        target2._count = self._count - middle
        target2._front = curr

        if target2._count > 0:
            target2._rear = self._rear

        # Clean up source
        self._front = None
        self._rear = None
        self._count = 0
        return target1, target2

    def _move_front_to_front(self, source):
        """
        -------------------------------------------------------
        Moves the front node from source to the front of the current Sorted_List.
        Both lists' counts are updated. Private helper method.
        Use: self._move_front_to_front(source)
        -------------------------------------------------------
        Parameters:
            source - a sorted linked List (Sorted_List)
        Returns:
            None
        -------------------------------------------------------
        """
        assert source._front is not None, \
            "Cannot move the front of an empty Sorted_List"

        temp = source._front
        source._front = source._front._next
        temp._next = self._front
        self._front = temp
        self._count += 1
        source._count -= 1
        return

    def _move_front_to_rear(self, source):
        """
        -------------------------------------------------------
        Moves the front node from source to the rear of the current Sorted_List.
        Both lists' counts are updated. Private helper method.
        Use: self._move_front_to_rear(source)
        -------------------------------------------------------
        Parameters:
            source - a non-empty linked List (Sorted_List)
        Returns:
            None
        -------------------------------------------------------
        """
        assert source._front is not None, \
            "Cannot move the front of an empty Sorted_List"

        node = source._front
        # Update the source list
        source._count -= 1
        source._front = source._front._next

        if source._front is None:
            # Clean up source list if empty.
            source._rear = None

        # Update the target list
        if self._rear is None:
            self._front = node
        else:
            self._rear._next = node

        node._next = None
        self._rear = node
        self._count += 1
        return

    def is_identical(self, target):
        """
        ---------------------------------------------------------
        Determines whether two lists are identical. (iterative version)
        Use: b = source.is_identical(target)
        -------------------------------------------------------
        Parameters:
            target - another list (Sorted_List)
        Returns:
            identical - True if this list contains the same values as
                target in the same order, otherwise False.
        -------------------------------------------------------
        """
        if self._count != target._count:
            identical = False
        else:
            current1 = self._front
            current2 = target._front

            while current1 is not None and current1._value == current2._value:
                current1 = current1._next
                current2 = current2._next

            identical = current1 is None
        return identical

    def copy(self):
        """
        -------------------------------------------------------
        Duplicates the current list to a new list in the same order.
        (iterative version)
        Use: new_list = l.copy()
        -------------------------------------------------------
        Returns:
            new_list - a copy of self (Sorted_List)
        -------------------------------------------------------
        """
        
        list = deepcopy(self)
   

        return list
    
    def combine(self, source1, source2):
        """
        -------------------------------------------------------
        Combines two source lists into the current target list.
        When finished, the contents of source1 and source2 are interlaced
        into target and source1 and source2 are empty.
        Order of source values is preserved.
        (iterative algorithm)
        Use: target.combine(source1, source2)
        -------------------------------------------------------
        Parameters:
            source1 - a linked list (Sorted_List)
            source2 - a linked list (Sorted_List)
        Returns:
            None
        -------------------------------------------------------
        """
        assert self._front is None, "Target list must be empty"

        while source1._front is not None and source2._front is not None:

            if source1._front._value <= source2._front._value:
                self._move_front_to_rear(source1)
            else:
                self._move_front_to_rear(source2)

        while source1._front is not None:
            self._move_front_to_rear(source1)

        while source2._front is not None:
            self._move_front_to_rear(source2)

        return

    def __iter__(self):
        """
        USE FOR TESTING ONLY
        -------------------------------------------------------
        Generates a Python iterator. Iterates through the list
        from front to rear.
        Use: for v in s:
        -------------------------------------------------------
        Returns:
            yields
            value - the next value in the list (?)
        -------------------------------------------------------
        """
        current = self._front

        while current is not None:
            yield current._value
            current = current._next
