import sys
import os.path
utilsdir = os.path.dirname(__file__)
sys.path.append(os.path.split(utilsdir)[0])
import Utils.Utils as utils
import BinaryTree
import unittest

class TestBinaryTree(unittest.TestCase):

    def setUp(self):
# The testing tree should look like this:
#               30
#          /         \
#         /           \
#        /             \
#      10               43
#     /  \           /      \
#         21       34        45
#        /  \     /  \       / \
#      15             40        46
#         
# All nodes should have a count == 1
# except for 46 with count == 4

        self.empty_tree = BinaryTree.BinaryTree()
        self.tree = BinaryTree.BinaryTree()
        self.tree.add(30)
        self.tree.add(43)
        self.tree.add(10)
        self.tree.add(34)
        self.tree.add(21)
        self.tree.add(40)
        self.tree.add(15)
        self.tree.add(45)
        self.tree.add(44)
        self.tree.add(46)
        self.tree.add(46)
        self.tree.add(46)
        self.tree.add(46)

        
    # Testing get_root
    def test_get_root(self):
        self.assertEqual(self.tree.get_root().value, 30)

    def test_get_root_when_empty_tree(self):
        self.assertIsNone(self.empty_tree.get_root())

    # Testing find_max_node
    def test_find_max_node(self):
        self.assertEqual(self.tree.find_max_node().value, 46)
    
    def test_find_max_node_when_empty_tree(self):
        self.assertIsNone(self.empty_tree.find_max_node())

    # Testing find_min_node
    def test_find_min_node(self):
        self.assertEqual(self.tree.find_min_node().value, 10)

    def test_find_min_node_when_empty_tree(self):
        self.assertIsNone(self.empty_tree.find_min_node())
        
    #Testing find
    def test_find_value_in_tree(self):
        self.assertEqual(self.tree.find(46).value, 46)
    
    def test_find_value_not_in_tree(self):
        self.assertIsNone(self.tree.find(66))
    
    def test_find_when_empty_tree(self):
        self.assertIsNone(self.empty_tree.find(46))

    #Testing remove
    # def remove_node_in_tree(self):
        # self.assertEqual();
    

    # Testing get_height
    def test_height(self):
        self.assertEqual(self.tree.height(), 4)

    def test_height_when_empty_tree(self):
        self.assertEqual(self.empty_tree.height(), 0)

    # Testing list_in_order
    def test_list_in_order(self):
        in_order_list = [10, 15, 21, 30, 34, 40, 43, 44, 45, 46]
        in_order_from_tree = self.tree.list_in_order()
        self.assertTrue(utils.lists_have_same_elems_in_order(in_order_list, in_order_from_tree))
    
    def test_list_in_order_when_empty_tree(self):
        self.assertEqual(self.empty_tree.list_in_order(), [])
    

if __name__ == '__main__':
    unittest.main()