from data_structures.node import Node


class Queue:
    def __init__(self):
        self.last = None
        self.first = None

    def is_empty(self):
        return self.last is None

    def enqueue(self, item):
        item = Node(item)

        if self.is_empty():
            self.last = Node(item)
            self.first = self.last
        else:
            self.last.set_next(item)
            self.last = item

    def dequeue(self):
        item = self.first.get_item()
        self.first = self.first.get_next()
        return item
