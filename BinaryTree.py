import BinaryNode


class BinaryTree:

    def __init__(self, rootValue=None):
        self.root = BinaryNode.BinaryNode(rootValue)

    def add(self, value):
        if(self.root.value is None):
            self.root.value = value
        else:
            self.addInOrder(value, self.root)

    def addInOrder(self, value, node):
        if(value < node.value):
            if(node.left is None):
                node.left = BinaryNode.BinaryNode(value)
            else:
                self.addInOrder(value, node.left)
        else:
            if(node.right is None):
                node.right = BinaryNode.BinaryNode(value)
            else:
                self.addInOrder(value, node.right)

    def printInOrder(self):
        if(self.root is not None):
            self._printInOrder(self.root)

    def _printInOrder(self, node):
        if(node is not None):
            self._printInOrder(node.left)
            print(node.value)
            self._printInOrder(node.right)


def main():
    tree = BinaryTree(24)
    # print(tree.root.value)

    tree.add(30)

    tree.add(10)
    tree.add(34)
    tree.add(21)
    tree.add(40)
    tree.add(15)
    tree.printInOrder()


main()
