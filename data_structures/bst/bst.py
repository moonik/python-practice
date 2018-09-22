class BST:

    def __init__(self):
        self.root = None

    class Node:
        def __init__(self, key=None, value=None):
            self.key = key
            self.value = value
            self.left = None
            self.right = None
            self.count = 0

    def put(self, node, key, value):
        if node is None:
            return BST.Node(key, value)

        if key < node.key:
            node = self.put(node.left, key, value)

        elif key > node.key:
            node = self.put(node.right, key, value)

        else:
            node.value = value

        node.count = 1 + self.__size(node.left) + self.__size(node.right)
        return node

    def get(self, key):
        n = self.root
        while n is not None:
            if key < n.key:
                n = n.left
            elif key > n.key:
                n = n.right
            else:
                return n.value
        return None

    def size(self):
        return self.root.count

    def __size(self, node):
        if node is None:
            return 0
        return node.count
