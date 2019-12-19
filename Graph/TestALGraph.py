from ALGraph import ALGraph as graph
import unittest


class TestALGraph(unittest.TestCase):
    def setUp(self):
      self.empty_graph = graph()
      
    def test_empy_graph_is_none(self):
      self.assertIsNone(self.empty_graph.graph)
      
if __name__ == '__main__':
    unittest.main()

