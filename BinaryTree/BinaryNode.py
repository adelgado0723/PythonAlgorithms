class BinaryNode:
    def __init__(self, value=None):
        self.left = None
        self.right = None
        self.value = value
        if(value is not None):
          self.count = 1
        else:
          self.count = 0
