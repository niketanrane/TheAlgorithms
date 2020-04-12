__author__ = "Niketan Rane"

class Stack:

    def __init__(self, max_size=10**7):
        self.stack = []
        self.max_size = max_size

    def push(self, item):
        if self.is_full():
            raise StackOverFlowError
        self.stack.append(item)

    def pop(self):
        if self.is_empty():
            raise IndexError("Pop from emptry stack")
        return self.stack.pop()

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]

    def __str__(self):
        return str(self.stack)

    def size(self):
        return len(self.stack)

    def is_empty(self):
        return not bool(self.stack)

    def is_full(self):
        return len(self.stack) == self.max_size

class StackOverFlowError(BaseException):
    pass

if __name__ == "__main__":
    stack = Stack()
    for i in range(10):
        stack.push(i)

    print("Stack demonstration:\n")
    print("Initial stack: " + str(stack))
    print("pop(): " + str(stack.pop()))
    print("After pop(), the stack is now: " + str(stack))
    print("peek(): " + str(stack.peek()))
    stack.push(100)
    print("After push(100), the stack is now: " + str(stack))
    print("is_empty(): " + str(stack.is_empty()))
    print("size(): " + str(stack.size()))