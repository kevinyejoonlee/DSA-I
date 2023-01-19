"""
-------------------------------------------------------
Simple Set testing
-------------------------------------------------------
Author: Kevin Lee
ID:     210872060
Email:  leex7206@mylaurier.ca
__updated__ = "2022-04-06"
-------------------------------------------------------
"""
# Imports
from Deque_Set_linked import Deque_Set

# Constants
SEP = '_' * 40

# Testing
source = Deque_Set()
print(SEP)
empty = source.is_empty()
print("Set is empty: {}".format(empty))
length = len(source)
print("Set length: {}".format(length))

print(SEP)
print("Insert values 0 - 4 to front")
print()
for i in range(5):
    source.insert_front(i)

empty = source.is_empty()
print("Set is empty: {}".format(empty))
length = len(source)
print("Set length: {}".format(length))

print("Values in set:")

for v in source:
    print(v, end=", ")
print()

print(SEP)
print("Peek at front:")
print()
value = source.peek_front()
print(f"Front value: {value}")
print(SEP)
print("Attempt to add a value already in set (1)")
print()
added = source.insert_front(1)
print("Added: {}".format(added))

print(SEP)
print("Remove 2")
print()
removed = source.remove(2)
print("Removed:", removed)
print("Values in set:")

for v in source:
    print(v, end=", ")
print()

print(SEP)
print("Remove Front")
print()
removed = source.remove_front()
print("Removed:", removed)
print("Values in set:")

for v in source:
    print(v, end=", ")
print()
print(SEP)
source = Deque_Set()
print("Insert values 0 - 7 to front")
print()
for i in range(8):
    source.insert_front(i)
print("Split on key 4")
target1, target2 = source.split_key(4)
print("source:")
for v in source:
    print(v, end=", ")
print()
print("target1:")
for v in target1:
    print(v, end=", ")
print()
print("target2:")
for v in target2:
    print(v, end=", ")
print()
print(SEP)
source = Deque_Set()

target1 = Deque_Set()
for i in range(5):
    target1.insert_front(i)

target2 = Deque_Set()
for i in range(6, 10):
    target2.insert_front(i)

print("combine target1 and target2 into source")
print()
source.combine(target1, target2)
print("target1:")
for v in target1:
    print(v, end=", ")
print()
print("target2:")
for v in target2:
    print(v, end=", ")
print()
print("source:")
for v in source:
    print(v, end=", ")
print()
print(SEP)
