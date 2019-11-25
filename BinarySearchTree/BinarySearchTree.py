import BinaryNode


class BinarySearchTree:

    def __init__(self):
        self.root = None

    def get_root(self):
        return self.root

    def insert(self, value):
        if(self.root is None):
            self.root = BinaryNode.BinaryNode(value)
        else:
            self._insert_in_order(value, self.root)

    def _insert_in_order(self, value, node):
        if(value < node.value):
            if(node.left is None):
                node.left = BinaryNode.BinaryNode(value)
            else:
                self._insert_in_order(value, node.left)
        elif(value > node.value):
            if(node.right is None):
                node.right = BinaryNode.BinaryNode(value)
            else:
                self._insert_in_order(value, node.right)
        else:
            node.count += 1

    def print_value(self, node):
        if(node is not None and node.value is not None):
            print(f"Value: {node.value} - Count: {node.count}")
        else:
            print("Either the node or its value is None")

    def _insert_into_list(self, node, node_list):
        if(node is not None and node.value is not None):
            for i in range(node.count):
                node_list.append(node.value)

    def _make_list(self, traversal_method):
        node_list = []
        traversal_method(self.root, self._insert_into_list, node_list)
        return node_list

    def list_in_order(self):
        return self._make_list(self._traverse_in_order)

    def list_pre_order(self):
        return self._make_list(self._traverse_pre_order)

    def list_post_order(self):
        return self._make_list(self._traverse_post_order)

    def print_in_order(self):
        self._traverse_in_order(self.root, self.print_value)

    def _traverse_in_order(self, node, fn, *args):
        if(node is not None):
            self._traverse_in_order(node.left, fn, *args)
            fn(node, *args)
            self._traverse_in_order(node.right, fn, *args)

    def print_pre_order(self):
        self._traverse_pre_order(self.root, self.print_value)

    def _traverse_pre_order(self, node, fn, *args):
        if(node is not None):
            fn(node, *args)
            self._traverse_pre_order(node.left, fn, *args)
            self._traverse_pre_order(node.right, fn, *args)

    def print_post_order(self):
        self._traverse_post_order(self.root, self.print_value)

    def _traverse_post_order(self, node, fn, *args):
        if(node is not None):
            self._traverse_post_order(node.left, fn, *args)
            self._traverse_post_order(node.right, fn, *args)
            fn(node, *args)

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
            self.root = self._remove(self.root, value)

    # Given a binary search tree and a key, this function
    # delete the key and returns the new node

    # Returns either the node itself when coming back up the call stack
    # or the node replacing the deleted node when it is found

    # From: https://www.geeksforgeeks.org/binary-search-tree-set-2-delete/
    def _remove(self, node, key):

        # Base Case
        if node is None:
            return node

        # If the key to be deleted is smaller than the node's
        # key then it lies in  left subtree
        if key < node.value:
            node.left = self._remove(node.left, key)

        # If the kye to be delete is greater than the node's key
        # then it lies in right subtree
        elif(key > node.value):
            node.right = self._remove(node.right, key)

        # If key is same as node's key, then this is the node
        # to be deleted
        else:
            if node.count > 1:
                node.count -= 1
                return node

            # Node with only one child or no child
            if node.left is None:
                temp = node.right
                node = None
                return temp

            elif node.right is None:
                temp = node.left
                node = None
                return temp

            # Node with two children: Get the inorder successor
            # (smallest in the right subtree)
            temp = self._find_min_node(node.right)

            # Copy the inorder successor's content to this node
            node.value = temp.value

            # Delete the inorder successor
            node.right = self._remove(node.right, temp.value)

        return node

    # Returns height in terms of number of nodes from root to furthest leaf
    def height(self):
        return self._get_height(self.root)

    def _get_height(self, node):
        # This if statement could be changed to:
        # if(node is None or (node.left is None and node.right is None)):
        # if we wanted a height based on the number of edges
        if(node is None):
            return 0

        left_tree_height = self._get_height(node.left)
        right_tree_height = self._get_height(node.right)

        if (left_tree_height > right_tree_height):
            return left_tree_height + 1
        else:
            return right_tree_height + 1

    def size(self):
        return self._size(self.root)

    def _size(self, node):
        if node is None:
            return 0
        return self._size(node.left) + self._size(node.right) + node.count

    def size_no_dups(self):
        return self._size_no_dups(self.root)

    def _size_no_dups(self, node):
        if node is None:
            return 0
        return self._size_no_dups(node.left) + self._size_no_dups(node.right) + 1


if __name__ == "__main__":
    tree = BinarySearchTree()
    tree.insert(10)
    tree.insert(3)
    tree.insert(14)
    tree.insert(9)
    tree.insert(12)
    tree.insert(18)

    tree.print_in_order()
    tree_list = tree.list_in_order()
    for item in tree_list:
        print(item)
