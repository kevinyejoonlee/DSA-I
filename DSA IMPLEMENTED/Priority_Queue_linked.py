"""
-------------------------------------------------------
linked version of the Priority Queue ADT.
-------------------------------------------------------
Author: Kevin Lee
ID:     210872060
Email:  leex7206@mylaurier.ca
__updated__ = '2022-01-15'
-------------------------------------------------------
"""


# pylint: disable=protected-access

# Imports
from copy import deepcopy


class _PQ_Node:

    def __init__(self, value, _next):
        """
        -------------------------------------------------------
        Initializes a priority queue node that contains a copy of value
        and a link to the next node in the priority queue
        Use: node = _PQ_Node(value, _next)
        -------------------------------------------------------
        Parameters:
            value - value value for node (?)
            _next - another priority queue node (_PQ_Node)
        Returns:
            a new Priority_Queue object (_PQ_Node)
        -------------------------------------------------------
        """
        self._value = deepcopy(value)
        self._next = _next


class Priority_Queue:

    def __init__(self):
        """
        -------------------------------------------------------
        Initializes an empty priority queue.
        Use: pq = Priority_Queue()
        -------------------------------------------------------
        Returns:
            a new Priority_Queue object (Priority_Queue)
        -------------------------------------------------------
        """
        self._front = None
        self._rear = None
        self._count = 0

    def is_empty(self):
        """
        -------------------------------------------------------
        Determines if the priority queue is empty.
        Use: b = pq.is_empty()
        -------------------------------------------------------
        Returns:
            True if priority queue is empty, False otherwise.
        -------------------------------------------------------
        """
        return self._front is None

    def __len__(self):
        """
        -------------------------------------------------------
        Returns the length of the priority queue.
        Use: n = len(pq)
        -------------------------------------------------------
        Returns:
            the number of values in the priority queue.
        -------------------------------------------------------
        """
        return self._count

    def insert(self, value):
        """
        -------------------------------------------------------
        A copy of value is inserted into the priority queue.
        Values are stored in priority order.
        Use: pq.insert(value)
        -------------------------------------------------------
        Parameters:
            value - a data element (?)
        Returns:
            None
        -------------------------------------------------------
        """
        if self._front is None:
            # Priority queue is empty
            node = _PQ_Node(value, None)
            self._front = node
            self._rear = node
        elif value < self._front._value:
            # New value has highest priority
            self._front = _PQ_Node(value, self._front)
        elif value >= self._rear._value:
            # New value has lowest priority
            node = _PQ_Node(value, None)
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
            prev._next = _PQ_Node(value, curr)
        # Increment the priority queue size.
        self._count += 1
        return

    def remove(self):
        """
        -------------------------------------------------------
        Removes and returns the highest priority value from the priority queue.
        Use: value = pq.remove()
        -------------------------------------------------------
        Returns:
            value - the highest priority value in the priority queue -
                the value is removed from the priority queue. (?)
        -------------------------------------------------------
        """
        assert self._count > 0, "Cannot remove from an empty priority queue"

        value = self._front._value
        self._front = self._front._next
        self._count -= 1

        if self._front is None:
            # Remove the last element in the list
            self._rear = None
        return value

    def peek(self):
        """
        -------------------------------------------------------
        Peeks at the highest priority value of the priority queue.
        Use: v = pq.peek()
        -------------------------------------------------------
        Returns:
            a copy of the highest priority value in the priority queue -
                the value is not removed from the priority queue. (?)
        -------------------------------------------------------
        """
        assert self._count > 0, "Cannot peek at an empty priority queue"

        return deepcopy(self._front._value)

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
        target1 = Priority_Queue()
        target2 = Priority_Queue()
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

    def split_alt(self):
        """
        -------------------------------------------------------
        Splits a priority queue into two with values going to alternating
        priority queues. The source priority queue is empty when the method
        ends. The order of the values in source is preserved.
        Use: target1, target2 = source.split_alt()
        -------------------------------------------------------
        Returns:
            target1 - a priority queue that contains alternating values
                from the curr queue (Priority_Queue)
            target2 - priority queue that contains  alternating values
                from the curr queue  (Priority_Queue)
        -------------------------------------------------------
        """
        target1 = Priority_Queue()
        target2 = Priority_Queue()
        left = True

        while self._front is not None:
            # Move nodes to alternate queues.
            if left:
                target1._move_front_to_rear(self)
            else:
                target2._move_front_to_rear(self)
            left = not left
        return target1, target2

    def split_key(self, key):
        """
        -------------------------------------------------------
        Splits a priority queue into two depending on an external
        priority key. The source priority queue is empty when the method
        ends. The order of the values in source is preserved.
        Use: target1, target2 = source.split_key(key)
        -------------------------------------------------------
        Parameters:
            key - a data object (?)
        Returns:
            target1 - a priority queue that contains all values
                with priority higher than key (Priority_Queue)
            target2 - priority queue that contains all values with
                priority lower than or equal to key (Priority_Queue)
        -------------------------------------------------------
        """
        target1 = Priority_Queue()
        target2 = Priority_Queue()

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

    def combine(self, source1, source2):
        """
        -------------------------------------------------------
        Combines two source queues into the curr target priority queue.
        When finished, the contents of source1 and source2 are inserted
        into target and source1 and source2 are empty. Order is preserved
        with source1 elements having priority over source2 elements with the
        same priority value.
        (iterative algorithm)
        Use: target.combine(source1, source2)
        -------------------------------------------------------
        Parameters:
            source1 - a linked priority queue (Priority_Queue)
            source2 - a linked priority queue (Priority_Queue)
        Returns:
            None
        -------------------------------------------------------
        """
        while source1._front is not None and source2._front is not None:
            # Move higher priority nodes into target
            # source1 nodes have higher priority, all else being equal
            if source1._front._value <= source2._front._value:
                self._move_front_to_rear(source1)
            else:
                self._move_front_to_rear(source2)

        if source1._front is not None:
            self._append_queue(source1)

        if source2._front is not None:
            self._append_queue(source2)
        return

    def _append_queue(self, source):
        """
        -------------------------------------------------------
        Appends the entire source queue to the rear of the target queue.
        The source queue becomes empty.
        Use: target._append_queue(source)
        -------------------------------------------------------
        Parameters:
            source - an linked-based queue (Priority_Queue)
        Returns:
            None
        -------------------------------------------------------
        """
        assert source._front is not None, "Cannot append an empty priority queue"

        # Update the target priority queue
        if self._front is None:
            # current priority queue is empty.
            self._front = source._front
        else:
            self._rear._next = source._front
        self._rear = source._rear
        self._count += source._count
        # Empty the source priority queue.
        source._front = None
        source._rear = None
        source._count = 0
        return

    def _move_front_to_rear(self, source):
        """
        -------------------------------------------------------
        Moves the front node from the source queue to the rear of the target queue.
        The target queue contains the old front node of the source queue.
        The source queue front is updated. Order is preserved.
        Use: target._move_front_to_rear(source)
        -------------------------------------------------------
        Parameters:
            source - a linked queue (Priority_Queue)
        Returns:
            None
        -------------------------------------------------------
        """
        assert source._front is not None, "Cannot move the front of an empty priority queue"

        node = source._front
        # Update the source queue
        source._count -= 1
        source._front = source._front._next

        if source._front is None:
            # Clean up source queue if empty.
            source._rear = None

        # Update the target queue
        if self._front is None:
            self._front = node
        else:
            self._rear._next = node

        self._rear = node
        self._rear._next = None
        self._count += 1
        return

    def __iter__(self):
        """
        USE FOR TESTING ONLY
        -------------------------------------------------------
        Generates a Python iterator. Iterates through the queue
        from front to rear.
        Use: for value in pq:
        -------------------------------------------------------
        Returns:
            value - the next value in the priority queue (?)
        -------------------------------------------------------
        """
        curr = self._front

        while curr is not None:
            yield curr._value
            curr = curr._next
