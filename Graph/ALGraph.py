from Vertex import Vertex as vertex

class ALGraph:
  def __init__(self, graph=None):
    if graph is None:
      graph = {}
    self.graph = graph

  def add_vertex(self, vertex):
    if vertex not in self.graph:
      self.graph[vertex] = []
    
  