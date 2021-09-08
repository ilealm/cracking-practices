from collections import deque


class Stack:
    def __init__(self) -> None:
        self.stack = deque()
        self.min_stack = deque()

    # stack methods
    def push(self, value):
        self.stack.append(value)

        # if min_is_empty, I have to add the value BC is always going to be < infinite
        # check is the value is less than the top of min_stack, if so, push the value to min_top
        if self.min_is_empty():
            self.min_push(value)
        else:
            if value < self.min_top():
                self.min_push(value)

    # here, if the top of both stacks are the same, I will pop from both stacks
    def pop(self):
        if not self.is_empty():
            if self.top() == self.min_top():
                self.min_pop()
            return self.stack.pop()
        else:
            raise Exception("The stack is empty.")

    def top(self):
        if not self.is_empty():
            return self.stack[-1]  # peek at rightmost item
        else:
            raise Exception("The stack is empty.")

    def is_empty(self):
        return len(self.stack) == 0

    # min_stack methods
    def min_push(self, value):
        self.min_stack.append(value)

    def min_top(self):
        if not self.min_is_empty():
            return self.min_stack[-1]  # peek at rightmost item
        else:
            raise Exception("The min_stack is empty.")

    def min_is_empty(self):
        return len(self.min_stack) == 0

    def min_pop(self):
        return self.min_stack.pop()

    def min(self):
        return self.min_top()

