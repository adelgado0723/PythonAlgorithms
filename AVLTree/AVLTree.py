import os.path
import sys
rootdir = os.path.dirname(__file__)
sys.path.append(os.path.split(rootdir)[0])

import BinarySearchTree.BinaryNode as BinaryNode
import BinarySearchTree.BinarySearchTree as bst

class AVLTree(bst):
    pass