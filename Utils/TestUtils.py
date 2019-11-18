import Utils
import unittest

class TestUtils(unittest.TestCase):

    # Testing lists_have_same_elems_in_order
    def test_lists_have_same_elems_in_order_with_same_elems_not_in_order(self):
        first = [1, 2, 3, 4]
        second = [1, 3, 4, 2]
        self.assertFalse(Utils.lists_have_same_elems_in_order(first, second))
    
    def test_lists_have_same_elems_in_order_with_same_elems_in_order(self):
        first = [1, 2, 3, 4]
        second = [1, 2, 3, 4]
        self.assertTrue(Utils.lists_have_same_elems_in_order(first, second))
    
    def test_lists_have_same_elems_in_order_with_different_elems(self):
        first = [1, 2, 3, 4]
        second = [1, 2, 3, 5]
        self.assertFalse(Utils.lists_have_same_elems_in_order(first, second))
    
    def test_lists_have_same_elems_in_order_with_different_number_elems(self):
        first = [1, 2, 3, 4]
        second = [1, 2, 3, 4, 5]
        self.assertFalse(Utils.lists_have_same_elems_in_order(first, second))
        

if __name__ == '__main__':
    unittest.main()