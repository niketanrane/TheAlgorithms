__author__ = "Niketan Rane"


class Queue:
    def __init__(self, max_size=15):
        self.queue = []
        self.front = -1
        self.rear = -1
        self._size = 0
        self.max_size = max_size

    def is_empty(self):
        return self._size == 0

    def is_full(self):
        return self._size == self.max_size

    def __str__(self):
        printed = "<" + str(self.queue) + ">"
        printed += " <" + str((self.front, self.rear)) + ">"
        return printed

    def push(self, item):
        if self.is_full():
            raise StackOverFlowError
        if self.front == -1:
            self.front = 0
        self.rear = (self.rear + 1) % self.max_size
        if self.rear < len(self.queue):
            self.queue[self.rear] = item
        else:
            self.queue.append(item)
        self._size += 1

    def pop(self):
        if not self.is_empty():
            popped = self.queue[self.front]
            self.front = (self.front + 1) % self.max_size
            self._size -= 1
            return popped

    def size(self):
        return self._size

    def peek(self):
        if not self.is_empty():
            return self.queue[self.front]

class StackOverFlowError(BaseException):
    pass


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