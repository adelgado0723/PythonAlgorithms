# Data Structure Implementations in Python

## (Binary Search Tree)[./BinarySearchTree/BinarySearchTree.py]

The Binary Search Tree class is composed of Binary Nodes that each contain a
reference to their left and right child, as well as a value and a count for
keeping track of duplicate items. The class holds a reference to the root
node and can be manipulated with the following public methods:

- get_root()
- insert(value)
- print_value(node)
- list_in_order()
- list_pre_order()
- list_post_order()
- print_in_order()
- print_pre_order()
- print_post_order()
- find_max_node()
- find_min_node()
- find_parent(value)
- find(value)
- remove(value)
- height()
- size()
- size_no_dups()

## (Binary Search Tree Unit Tests)[./BinarySearchTree/Tests.py]

The TestBinarySearchTree class contains a catalog of unit tests that test
these public methods.

## (Utils)[./Utils/Utils.py]

Utils.py contains utility functions that can be used in the testing process.
These include:

- lists_have_same_elems_in_order(first, second)

## (Utils Unit Tests)[./Utils]

The TestUtils class contains unit tests for the functions in Utils.py.
