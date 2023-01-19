"""
-------------------------------------------------------
Linked version of the BST ADT - Exam
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

class BST:

    def reverse(self):
        """
        See the example of reverse on the Exam web page for clarity
        ---------------------------------------------------------
        Changes the current BST into a reverse image of itself. All nodes
        are swapped with nodes on the other side of a tree. Nodes may take
        the place of an empty spot. The resulting tree is a reverse image
        of the original tree. (Note that the reversed tree is not a BST.)
        Use: bst.reverse()
        ---------------------------------------------------------
        Returns‌‌​​​‌‌​:
            None
        ---------------------------------------------------------
        """

        self._reverse_aux(self._root)

    def _reverse_aux(self, n):  
        """
        ---------------------------------------------------------
        Changes the current subtree into a reverse image of itself. All nodes
        are swapped with nodes on the other side of a tree. Nodes may take
        the place of an empty spot. The resulting subtree is a reverse image
        of the original subtree.
        Use: # your code here
        ---------------------------------------------------------
        Parameters:
            n
        Returns‌​​‌‌‌‌‌‌:
            # your code here
        ---------------------------------------------------------
        """
        if n is not None:
            
            swap = n._right
            n._right = n._left
            n._left = swap
            self._reverse_aux(n._right)
            self._reverse_aux(n._left)
            
        return

    def _shift_left(self, parent):
        """
        -------------------------------------------------------
        shifts the parent n to its left around its right child.
        Updates the heights of the shifted nodes.
        Use: parent = self._shift_left(parent)
        -------------------------------------------------------
        Parameters:
            parent - the pivot n to shift around (_BST_Node)
        Returns‌‌​​​‌‌​:
            updated - the n that replaces the parent n (_BST_Node)
        -------------------------------------------------------
        """
        updated = None
        updated = parent._right
        parent._right = updated._left
        updated._left = parent
        parent._update_height()
        updated._update_height()
        
        return updated



# DO NOT CHANGE CODE BELOW THIS LINE
# =======================================================================

    def __init__(self):
        """
        -------------------------------------------------------
        Initializes an empty BST.
        Use: bst = BST()
        -------------------------------------------------------
        Returns‌‌​​​‌‌​:
            A BST object (BST)
        -------------------------------------------------------
        """
        self._root = None
        self._count = 0

    def insert(self, value):
        """
        -------------------------------------------------------
        Inserts a copy of value into bst. Values may appear
        only once in a tree.
        Use: b = bst.insert(value)
        -------------------------------------------------------
        Parameters:
            value - data to be inserted into bst (?)
        Returns‌‌​​​‌‌​:
            inserted - True if value is inserted into bst,
                False otherwise. (boolean)
        -------------------------------------------------------
        """
        self._root, inserted = self._insert_aux(self._root, value)
        return inserted

    def _insert_aux(self, n, value):
        """
        -------------------------------------------------------
        Inserts a copy of value into n.
        Private recursive operation called only by insert.
        Use: n, inserted = self._insert_aux(n, value)
        -------------------------------------------------------
        Parameters:
            n - a bst n (_BST_Node)
            value - data to be inserted into the n (?)
        Returns‌‌​​​‌‌​:
            n - the current n (_BST_Node)
            inserted - True if value is inserted into n,
                False otherwise. (boolean)
        -------------------------------------------------------
        """
        if n is None:
            # Base case: add a new n containing the value.
            n = _BST_Node(value)
            self._count += 1
            inserted = True
        elif value < n._value:
            # General case: check the left subtree.
            n._left, inserted = self._insert_aux(n._left, value)
        elif value > n._value:
            # General case: check the right subtree.
            n._right, inserted = self._insert_aux(n._right, value)
        else:
            # Base case: value is already in the BST.
            inserted = False

        if inserted:
            # Update the n height if any of its children have been changed.
            n._update_height()
        return n, inserted

    def retrieve(self, key):
        """
        -------------------------------------------------------
        Retrieves a copy of a value matching key in bst. (Iterative)
        Use: v = bst.retrieve(key)
        -------------------------------------------------------
        Parameters:
            key - data to search for (?)
        Returns‌‌​​​‌‌​:
            value - value in the n containing key, otherwise None (?)
        -------------------------------------------------------
        """
        n = self._root
        value = None

        while n is not None and value is None:

            if n._value > key:
                n = n._left
            elif n._value < key:
                n = n._right
            elif n._value == key:
                # for comparison counting
                value = deepcopy(n._value)
        return value

    def inorder(self):
        """
        -------------------------------------------------------
        Generates a list of the contents of the tree in inorder order.
        Use: a = bst.inorder()
        -------------------------------------------------------
        Returns‌‌​​​‌‌​:
            a - copy of the contents of the tree in inorder (list of ?)
        -------------------------------------------------------
        """
        a = []
        self._inorder_aux(self._root, a)
        return a

    def _inorder_aux(self, n, a):
        """
        ---------------------------------------------------------
        Traverses n subtree in inorder. a contains the contents of
        n and its children in inorder.
        Private recursive operation called only by inorder.
        Use: self._inorder_aux(n, a)
        ---------------------------------------------------------
        Parameters:
            n - an BST n (_BST_Node)
            a - target list of data (list of ?)
        Returns‌‌​​​‌‌​:
            None
        ---------------------------------------------------------
        """
        if n is not None:
            self._inorder_aux(n._left, a)
            a.append(deepcopy(n._value))
            self._inorder_aux(n._right, a)
        return

    def preorder(self):
        """
        -------------------------------------------------------
        Generates a list of the contents of the tree in preorder order.
        Use: a = bst.preorder()
        -------------------------------------------------------
        Returns‌‌​​​‌‌​:
            a - copy of the contents of the tree in preorder (list of ?)
        -------------------------------------------------------
        """
        a = []
        self._preorder_aux(self._root, a)
        return a

    def _preorder_aux(self, n, a):
        """
        ---------------------------------------------------------
        Traverses n subtree in preorder. a contains the contents of
        n and its children in preorder.
        Private recursive operation called only by preorder.
        Use: self._preorder_aux(n, a)
        ---------------------------------------------------------
        Parameters:
            n - an BST n (_BST_Node)
            a - target of data (list of ?)
        Returns‌‌​​​‌‌​:
            None
        ---------------------------------------------------------
        """
        if n is not None:
            a.append(deepcopy(n._value))
            self._preorder_aux(n._left, a)
            self._preorder_aux(n._right, a)
        return

    def _node_height(self, n):
        """
        ---------------------------------------------------------
        Helper function to determine the height of n - handles empty n.
        Private operation called only by _is_valid_aux.
        Use: h = self._node_height(n)
        ---------------------------------------------------------
        Parameters:
            n - the n to get the height of (_BST_Node)
        Returns‌‌​​​‌‌​:
            height - 0 if n is None, n._height otherwise (int)
        ---------------------------------------------------------
        """
        if n is None:
            height = 0
        else:
            height = n._height
        return height

    def is_valid(self):
        """
        ---------------------------------------------------------
        Determines if a tree is a is_valid BST, i.e. the values in all left nodes
        are smaller than their parent, and the values in all right nodes are
        larger than their parent, and height of any n is 1 + max height of
        its children.
        Use: b = bst.is_valid()
        ---------------------------------------------------------
        Returns‌‌​​​‌‌​:
            valid - True if tree is a BST, False otherwise (boolean)
        ---------------------------------------------------------
        """
        valid = self._is_valid_aux(self._root, None, None)
        return valid

    def _is_valid_aux(self, n, min_node, max_node):
        """
        ---------------------------------------------------------
        Private recursive method to determine the BST validity of n,
        used only by is_valid.
        Use: valid = self._is_valid_aux(n, min_node, max_node)
        ---------------------------------------------------------
        Parameters:
            n - a binary tree n (_BST_Node)
            min_node - the n with the minimum value for the current tree (_BST_Node)
            max_node - the n with the maximum value for the current tree (_BST_Node)
        Returns‌‌​​​‌‌​:
            valid - True if n is root of a valid BST, False otherwise (boolean)
        ---------------------------------------------------------
        """
        if n is None:
            valid = True
        elif min_node is not None and n._value <= min_node._value:
            # print("BST left value violation at value: {}".format(n._value))
            valid = False
        elif max_node is not None and n._value >= max_node._value:
            # print("BST right value violation at value: {}".format(n._value))
            valid = False
        elif n._height != max(self._node_height(n._left), self._node_height(n._right)) + 1:
            # print("BST height violation at value: {}".format(n._value))
            valid = False
        else:
            # n becomes max n of left tree, min n of right tree
            valid = self._is_valid_aux(n._left, min_node, n) \
                and self._is_valid_aux(n._right, n, max_node)
        return valid


class _BST_Node:

    def __init__(self, value):
        """
        -------------------------------------------------------
        Initializes a BST n containing value. Child pointers
        are None, height is 1.
        Use: n = _BST_Node(value)
        -------------------------------------------------------
        Parameters:
            value - value for the n (?)
        Returns‌‌​​​‌‌​:
            A _BST_Node object (_BST_Node)
        -------------------------------------------------------
        """
        self._value = deepcopy(value)
        self._left = None
        self._right = None
        self._height = 1
        self._count = 0

    def _update_height(self):
        """
        -------------------------------------------------------
        Updates the height of the current n. _height is 1 plus
        the maximum of the n's (up to) two child heights.
        Use: n._update_height()
        -------------------------------------------------------
        Returns‌‌​​​‌‌​:
            None
        -------------------------------------------------------
        """
        if self._left is None:
            left_height = 0
        else:
            left_height = self._left._height

        if self._right is None:
            right_height = 0
        else:
            right_height = self._right._height

        self._height = max(left_height, right_height) + 1
        return

    def __str__(self):
        """
        USE FOR TESTING ONLY
        -------------------------------------------------------
        Returns n height and value as a string - for debugging.
        -------------------------------------------------------
        """
        return f"h: {self._height}, v: {self._value}"
