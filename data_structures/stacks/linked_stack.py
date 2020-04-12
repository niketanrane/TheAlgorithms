__author__ = "Niketan Rane"


class Node:
    def __init__(self, item=None):
        self.item = item
        self.next = None

class LinkedStack:

    def __init__(self, max_size=10**7):
        self.top = None

    def push(self, item):
        node = Node(item)
        node.next = self.top
        self.top = node

    def pop(self):
        if self.top is None:
            raise IndexError("Pop from empty stack")
        popped = self.top
        self.top = self.top.next
        return popped

    def peek(self):
        if self.top:
            return self.top.item

    def is_empty(self):
        return self.top is None

    def __str__(self):
        ptr = self.top
        strn = ''
        while ptr:
            strn = strn + ' ' + str(ptr.item)
            ptr = ptr.next
        return strn


class StackOverFlowError(BaseException):
    pass

if __name__ == "__main__":
    stack = LinkedStack()
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
    # print("size(): " + str(stack.size()))