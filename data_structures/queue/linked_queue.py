__author__ = "Niketan Rane"

from collections import deque

class Node:
    def __init__(self, item, next=None):
        self.item = item
        self.next = next

class Queue:
    def __init__(self, max_size=10**7):
        self.front = self.rear = None
        self._size = 0
        self.max_size = max_size

    def push(self, item):
        node = Node(item)
        if self.front is None:
            self.front = node
            self.rear = node
        else:
            self.rear.next = node
            self.rear = self.rear.next
        self._size += 1

    def pop(self):
        if not self.is_empty():
            popped = self.front.item
            self.front = self.front.next
            self._size -= 1
            return popped

    def peek(self):
        if not self.is_empty():
            return self.front.item

    def is_empty(self):
        return self._size == 0

    def size(self):
        return self._size

    def __str__(self):
        ptr = self.front
        strn = ''
        while ptr:
            strn = strn + ' ' + str(ptr.item)
            ptr = ptr.next
        return strn


if __name__ == "__main__":
    queue = Queue()
    for i in range(10):
        queue.push(i)

    print("Linked Queue demonstration:\n")
    print("Initial queue: " + str(queue))
    print("pop(): " + str(queue.pop()))
    print("After pop(), the queue is now: " + str(queue))
    print("peek(): " + str(queue.peek()))
    queue.push(100)
    print("After push(100), the queue is now: " + str(queue))
    print("is_empty(): " + str(queue.is_empty()))
    print("size(): " + str(queue.size()))