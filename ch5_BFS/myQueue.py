# application:
# CPU scheduling
# asynchronous data between two processes
# graph traversal algorithm
# transport, operations management
# file servers, IO buffers, printer queues
# phone calls to customer service hotlines
# !! resource is shared among multiple consumers !!
# head <-> rear (tail)
# FIFO
# head: remove / rear: add
# operations: enqueue, dequeue

# using list to implement Queue is not efficient ! since insert, pop from the beginning of a list is slow !
# ==> use 'Deque' data structure (double-ended queue)

from collections import deque


class Queue:
    def __init__(self):
        self.items = deque()

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        return self.items.popleft()

    def is_empty(self):
        return not self.items

    def size(self):
        return len(self.items)

    def peek(self):
        return self.items[0]

    def __str__(self):
        return str(self.items)


if __name__ == '__main__':
    q = Queue()
    print(q)
    print(q.is_empty())
    q.enqueue('a')
    q.enqueue('b')
    q.enqueue('c')
    print(q)
    print(q.dequeue())
    print(q)
