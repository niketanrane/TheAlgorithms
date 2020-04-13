__author__ = "Niketan Rane"

from collections import deque


class Queue:
    def __init__(self, max_size=10**7):
        self.queue = deque()
        self.front = -1

    def push(self, item):
        self.queue.append(item)

    def pop(self):
        return self.queue.popleft()

    def peek(self):
        if self.queue:
            return self.queue[0]

    def is_empty(self):
        return not bool(self.queue)

    def size(self):
        return len(self.queue)

    def __str__(self):
        printed = "<" + str(self.queue) + ">"
        return printed

if __name__ == "__main__":
    queue = Queue()
    for i in range(10):
        queue.push(i)

    print("Queue demonstration:\n")
    print("Initial queue: " + str(queue))
    print("pop(): " + str(queue.pop()))
    print("After pop(), the queue is now: " + str(queue))
    print("peek(): " + str(queue.peek()))
    queue.push(100)
    print("After push(100), the queue is now: " + str(queue))
    print("is_empty(): " + str(queue.is_empty()))
    print("size(): " + str(queue.size()))