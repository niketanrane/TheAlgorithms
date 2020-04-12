__author__ = "Niketan Rane"

class Stack:

    def __init__(self):
        self.stack = []
        self.top = -1

    def is_empty(self):
        return self.top == -1

    def push(self, item):
        self.top += 1
        if self.top < len(self.stack):
            # replace existing entries
            self.stack[self.top] = item
        else:
            self.stack.append(item)

    def pop(self):
        if self.is_empty():
            return None
        to_pop = self.stack[self.top]
        self.top -= 1
        return to_pop

    def __str__(self):
        return str((self.stack, self.top))


if __name__ == "__main__":
    stack = Stack()
    stack.push(1)
    stack.push(2)
    print(stack.pop())
    print(stack.pop())
    stack.push(3)
    print(stack)





