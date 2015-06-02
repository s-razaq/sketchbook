__author__ = 'Saqib Razaq'

"""
This module implements a queue with 2 stacks. The queue has an enqueue and a dequeue function and work in "first in first out" (FIFO) order.
"""


class Stack(object):
    def __init__(self):
        self.data = []
        self.top = -1

    def put(self, item):
        self.data.append(item)
        self.top += 1

    def pop(self):
        element = self.data.pop(self.top)
        self.top -= 1
        return element

    def empty(self):
        return len(self.data) == 0

    def __len__(self):
        return len(self.data)


class Queue(object):
    def __init__(self):
        self.right = Stack()
        self.left = Stack()
        self.counter = 0

    def enqueue(self, item):
        self.left.put(item)

    def dequeue(self):
        if self.right.empty():
            for _ in xrange(len(self.left)):
                self.right.put(self.left.pop())
        return self.right.pop()


if __name__ == '__main__':
    my_queue = Queue()
    my_queue.enqueue(1)
    my_queue.enqueue(2)
    my_queue.enqueue(3)
    print my_queue.dequeue()
    print my_queue.dequeue()
    my_queue.enqueue(4)
    print my_queue.dequeue()