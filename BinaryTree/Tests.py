import unittest
import BinaryTree

class TestBinaryTree(unittest.TestCase):

    def setUp(self):
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
        empty_tree = BinaryTree.BinaryTree()
        self.assertIsNone(empty_tree.get_root())

    def test_find_max_node(self):
        self.assertEqual(self.tree.find_max_node().value, 46)

    def test_find_min_node(self):
        self.assertEqual(self.tree.find_min_node().value, 10)


if __name__ == '__main__':
    unittest.main()