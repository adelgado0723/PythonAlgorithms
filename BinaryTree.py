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
        if(node is not None and node.value is not None):
            print(f"Value: {node.value} - Count: {node.count}")
        else:
            print("Either the node or its value is None")

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

    def find_parent(self, value):
        return self._find_parent(value, self.root)

    def _find_parent(self, value, node):
        if(node is not None):
            if(node.left is not None and node.left.value == value):
                return node
            elif(node.right is not None and node.right.value == value):
                return node

            if (node.value > value):
                return self._find_parent(value, node.left)

            if (node.value < value):
                return self._find_parent(value, node.right)

    def find(self, value):
        return self._find(value, self.root)

    def _find(self, value, node):
        if(node is not None):
            if (node.value == value):
                return node
            if (node.value > value):
                return self._find(value, node.left)

            if (node.value < value):
                return self._find(value, node.right)

    # Remove Node Given a Value
    def remove(self, value):
        if(self.root is not None):
            return self.remove(value, self.root)

    def _remove(self, value, node):

        # Find if there is a node in the tree with that value
        # If not, just return
        to_be_removed = self._find(value, node)

        if(to_be_removed is None):
            return

        # If the count is greater than 1, decrement the count
        if(to_be_removed.count > 1):
            to_be_removed.count -= 1
            return

        # Fetch the parent
        parent = self._find_parent(value, node)
        is_left_child = False
        if(parent is None):
          # to_be_removed is the root
        else:
          # Is to_be_removed the left or right child
            if (parent.left.value == to_be_removed.value):
                is_left_child = True

        # If it is a leaf:
        if (to_be_removed.left is None and to_be_removed.right is None):
            # set the parent's reference to None
            if(is_left_child):
                parent.left = None
            else:
                parent.right = None

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

    # print("Printing In Order:")
    # tree.print_in_order()
    # print("\nPrinting Pre Order:")
    # tree.print_pre_order()
    # print("\nPrinting Post Order:")
    # tree.print_post_order()

    # print("\nHighest Value = ")
    # tree.print_value(tree.find_max_node())

    # print("\nLowest Value = ")
    # tree.print_value(tree.find_min_node())

    tree.print_value(tree.find(46))
    tree.print_value(tree.find(10))

    empty_tree = BinaryTree()

    empty_tree.print_value(empty_tree.find(10))
    empty_tree.print_value(empty_tree.find_max_node())
    empty_tree.print_value(empty_tree.find_min_node())


main()
