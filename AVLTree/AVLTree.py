import os.path
import sys
rootdir = os.path.dirname(__file__)
sys.path.append(os.path.split(rootdir)[0])

from BinarySearchTree.BinarySearchTree import BinarySearchTree as bst

class AVLTree(bst):
    pass