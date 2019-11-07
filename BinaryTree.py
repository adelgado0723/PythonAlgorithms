import BinaryNode


class BinaryTree:

    def __init__(self):
            self.root = None

    def add(self, value):
        if(self.root is None):
            self.root = BinaryNode.BinaryNode(value)
        else:
            self._add_in_order(value, self.root)

    def _add_in_order(self, value, node):
        if(value < node.value):
            if(node.left is None):
                node.left = BinaryNode.BinaryNode(value)
            else:
                self._add_in_order(value, node.left)
        elif(value > node.value):
            if(node.right is None):
                node.right = BinaryNode.BinaryNode(value)
            else:
                self._add_in_order(value, node.right)
        else:
            node.count += 1

    def print_value(self, node):
        print(f"Value: {node.value} - Count: {node.count}")

    def print_in_order(self):
        self._traverse_in_order(self.root, self.print_value)

    def _traverse_in_order(self, node, fn):
        if(node is not None):
            self._traverse_in_order(node.left, fn)
            fn(node)
            self._traverse_in_order(node.right, fn)

    def print_pre_order(self):
          self._traverse_pre_order(self.root, self.print_value)

    def _traverse_pre_order(self, node, fn):
        if(node is not None):
            fn(node)
            self._traverse_pre_order(node.left, fn)
            self._traverse_pre_order(node.right, fn)

    def print_post_order(self):
          self._traverse_post_order(self.root, self.print_value)

    def _traverse_post_order(self, node, fn):
        if(node is not None):
            self._traverse_post_order(node.left, fn)
            self._traverse_post_order(node.right, fn)
            fn(node)


    def find_max_node(self):
      if(self.root is not None):
        return self._find_max_node(self.root)

    def _find_max_node(self, node):
      if(node.right is None):
        return node
      else:
        return self._find_max_node(node.right)

    def find_min_node(self):
      if(self.root is not None):
        return self._find_min_node(self.root)

    def _find_min_node(self, node):
      if(node.left is None):
        return node
      else:
        return self._find_min_node(node.left)

    # Remove Node Given a Value

    # Find if there is a node in the tree with that value
      # If not, just return

    # If the count is greater than 1
      # Decrement the count
    
    #Else
        # If it is a leaf: 
            # set the parent's reference to None
        # Else If it has a right child
            # Set the parent's reference to the right child sub-tree
        # Else If it has a left child
            # Set the parent's reference to the left child sub-tree
        # Else if it has two children
            # Set the parent's reference to the left child sub-tree
            # then, find the max node in that left sub-tree and 
            # attach the right sub-tree to that node's right reference
    

def main():
    tree = BinaryTree()

    tree.add(30)
    tree.add(43)
    tree.add(10)
    tree.add(34)
    tree.add(21)
    tree.add(40)
    tree.add(15)
    tree.add(45)
    tree.add(44)
    tree.add(46)
    tree.add(46)
    tree.add(46)
    tree.add(46)

    print("Printing In Order:")
    tree.print_in_order()
    print("\nPrinting Pre Order:")
    tree.print_pre_order()
    print("\nPrinting Post Order:")
    tree.print_post_order()

    print("\nHighest Value = ")
    tree.print_value(tree.find_max_node());

    print("\nLowest Value = ")
    tree.print_value(tree.find_min_node());

main()
