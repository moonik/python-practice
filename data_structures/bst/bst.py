from queue import Queue


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

    def put(self, key, value):
        self.root = self.__put(self.root, key, value)

    def __put(self, node, key, value):
        if node is None:
            return BST.Node(key, value)

        if key < node.key:
            node = self.__put(node.left, key, value)

        elif key > node.key:
            node = self.__put(node.right, key, value)

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

    def delete_min(self):
        self.root = self.__delete_min(self.root)

    def __delete_min(self, n):
        if n.left is None:
            return n.right
        n.left = self.__delete_min(n.left)
        n.count = 1 + self.__size(n.left) + self.__size(n.right)
        return n

    def delete(self, key):
        self.root = self.__delete(self.root, key)

    def __delete(self, n, key):
        if n is None:
            return None
        if key < n.key:
            n.left = self.__delete(n.left, key)  # search for a key
        elif key > n.key:
            n.right = self.__delete(n.right, key)  # search for a key
        else:
            if n.right is None:  # has no right child
                return n.left
            if n.left is None:
                return n.right
            t = n
            n = self.__min(t.right)
            n.right = self.__delete_min(n.right)  # replace with successor
            n.left = t.left
        n.count = self.__size(n.left) + self.__size(n.right) + 1  # update counts
        return n

    def min(self):
        return self.__min(self.root).key

    def __min(self, n):
        if n.left is None:
            return n
        else:
            return self.__min(n.left)

    def contains(self, key):
        return self.get(key) is not None

    def keys(self):  # in order
        que = Queue()
        self.in_order(self.root, que)
        return que

    def in_order(self, n, q):
        if n is None:
            return

        self.in_order(n.left, q)  # puts all from the left to the queue
        q.put(n.key)
        self.in_order(n.right, q)  # puts all from the left to the queue


bst = BST()

bst.put('first', 'f')
print(bst.get('first'))
