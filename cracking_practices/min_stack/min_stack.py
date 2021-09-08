from collections import deque


class Stack:
    def __init__(self) -> None:
        self.stack = deque()
        self.min_stack = deque()

    # stack methods
    def push(self, value):
        self.stack.append(value)

    def top(self):
        if not self.is_empty():
            return self.stack[-1]  # peek at rightmost item
        else:
            raise Exception ("The stack is empty.")


    def is_empty(self):
        return len(self.stack) == 0


# stack = Stack()

# stack.push(50)
# # print(stack.is_empty())
# print(stack.top())


# test
