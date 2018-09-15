from .node import Node


class LinkedStack:

    def __init__(self):
        self.last_ = None

    def push(self, item):
        self.last_ = Node(item, self.last_)

    def pop(self):
        item = self.last_.get_data()
        self.last_ = self.last_.get_next()
        return item