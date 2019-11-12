import unittest
import BinaryTree

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

        

    def test_get_root(self):
        self.assertEqual(self.tree.get_root().value, 30)

    def test_get_root_when_empty_tree(self):
        self.assertIsNone(self.empty_tree.get_root())

    def test_find_max_node(self):
        self.assertEqual(self.tree.find_max_node().value, 46)
    
    def test_find_max_node_when_empty_tree(self):
        self.assertEqual(self.empty_tree.find_max_node(), None)

    def test_find_min_node(self):
        self.assertEqual(self.tree.find_min_node().value, 10)

    def test_find_min_node_when_empty_tree(self):
        self.assertEqual(self.empty_tree.find_min_node(), None)
        
  
    #TODO: Test find(value)
    #TODO: Test remove(value)

if __name__ == '__main__':
    unittest.main()