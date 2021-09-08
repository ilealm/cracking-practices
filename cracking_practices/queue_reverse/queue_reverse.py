# Reverse a queue

from collections import deque


class Stack:
    def __init__(self) -> None:
        self.stack = deque()

    def is_empty(self):
        return len(self.stack) == 0

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            raise Exception("The stack is empty.")

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        else:
            raise Exception("The stack is empty.")




