import os.path
import sys
import BinarySearchTree as bst
import unittest
utilsdir = os.path.dirname(__file__)
sys.path.append(os.path.split(utilsdir)[0])

import Utils.Utils as utils


class TestBinaryTree(unittest.TestCase):
    def setUp(self):
        # The testing tree should look like this:
        #               30s
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

        self.empty_tree = bst.BinarySearchTree()
        self.tree = bst.BinarySearchTree()
        self.tree.insert(30)
        self.tree.insert(43)
        self.tree.insert(10)
        self.tree.insert(34)
        self.tree.insert(21)
        self.tree.insert(40)
        self.tree.insert(15)
        self.tree.insert(45)
        self.tree.insert(44)
        self.tree.insert(46)
        self.tree.insert(46)
        self.tree.insert(46)
        self.tree.insert(46)

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

    # Testing find
    def test_find_value_in_tree(self):
        self.assertEqual(self.tree.find(46).value, 46)

    def test_find_value_not_in_tree(self):
        self.assertIsNone(self.tree.find(66))

    def test_find_when_empty_tree(self):
        self.assertIsNone(self.empty_tree.find(46))

    # Testing remove
    def test_remove_duplicate_node_in_tree(self):
        remove_test_tree = bst.BinarySearchTree()
        remove_test_tree.insert(40)
        remove_test_tree.insert(46)
        remove_test_tree.insert(46)
        remove_test_tree.remove(46)
        self.assertEqual(remove_test_tree.find(46).count, 1)
        self.assertEqual(remove_test_tree.size(), 2)
    
    def test_remove_root_from_single_node_tree(self):
        remove_test_tree = bst.BinarySearchTree()
        remove_test_tree.insert(40)
        remove_test_tree.remove(40)
        root = remove_test_tree.get_root()
        self.assertIsNone(root);
        self.assertEqual(remove_test_tree.size(), 0)

    def test_remove_single_node_in_tree_with_no_children(self):
        remove_test_tree = bst.BinarySearchTree();
        remove_test_tree.insert(20)
        remove_test_tree.insert(46)
        remove_test_tree.insert(16)
        remove_test_tree.remove(16)
        self.assertEqual(remove_test_tree.size(), 2)
        self.assertIsNone(remove_test_tree.find(16))

    def test_remove_single_node_in_tree_with_left_child(self):
        remove_test_tree = bst.BinarySearchTree();
        remove_test_tree.insert(20)
        remove_test_tree.insert(46)
        remove_test_tree.insert(16)
        remove_test_tree.insert(15)
        remove_test_tree.remove(16)
        self.assertEqual(remove_test_tree.size(), 3)
        self.assertIsNone(remove_test_tree.find(16))
        self.assertEqual(remove_test_tree.find(20).left.value, 15)

    def test_remove_single_node_in_tree_with_right_child(self):
        remove_test_tree = bst.BinarySearchTree();
        remove_test_tree.insert(20)
        remove_test_tree.insert(46)
        remove_test_tree.insert(16)
        remove_test_tree.insert(17)
        remove_test_tree.remove(16)
        self.assertEqual(remove_test_tree.size(), 3)
        self.assertIsNone(remove_test_tree.find(16))
        self.assertEqual(remove_test_tree.find(20).left.value, 17)

    def test_remove_single_node_in_tree_with_two_children(self):
        remove_test_tree = bst.BinarySearchTree();
        remove_test_tree.insert(20)
        remove_test_tree.insert(46)
        remove_test_tree.insert(16)
        remove_test_tree.insert(15)
        remove_test_tree.insert(17)
        remove_test_tree.remove(16)
        self.assertEqual(remove_test_tree.size(), 4)
        self.assertIsNone(remove_test_tree.find(16))
        self.assertEqual(remove_test_tree.find(20).left.value, 17)
        self.assertEqual(remove_test_tree.find(17).left.value, 15)

    #NOTE: remove function doesn't account for count


    # Testing get_height

    def test_height(self):
        self.assertEqual(self.tree.height(), 4)

    def test_height_when_empty_tree(self):
        self.assertEqual(self.empty_tree.height(), 0)

    # Testing list_in_order
    def test_list_in_order(self):
        in_order_list = [10, 15, 21, 30, 34, 40, 43, 44, 45, 46, 46, 46, 46]
        in_order_from_tree = self.tree.list_in_order()
        self.assertTrue(
            utils.lists_have_same_elems_in_order(in_order_list,
                                                 in_order_from_tree))

    def test_list_in_order_when_empty_tree(self):
        self.assertEqual(self.empty_tree.list_in_order(), [])

    # Testing size
    def test_size(self):
        self.assertEqual(self.tree.size(), 13)

    def test_size_when_empty_tree(self):
        self.assertEqual(self.empty_tree.size(), 0)

    # Testing size_no_dups
    def test_size_no_dups(self):
        self.assertEqual(self.tree.size_no_dups(), 10)

    def test_size_no_dups_when_empty_tree(self):
        self.assertEqual(self.empty_tree.size_no_dups(), 0)


if __name__ == '__main__':
    unittest.main()
