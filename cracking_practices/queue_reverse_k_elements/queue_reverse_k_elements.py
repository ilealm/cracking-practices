# Reverse the K left part of a queue

# Input:  Q = [10, 20, 30, 40, 50]
# K = 3O
# 0utput: Q = [30, 20, 10, 40, 50]

from collections import deque

class Stack:
    def __init__(self) -> None:
        self.stack = deque()

    def __str__(self) -> str:
        return self.stack

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


class Queue:
    def __init__(self) -> None:
        self.queue = deque()

    def __str__(self) -> str:
        return self.queue

    def is_empty(self):
        return len(self.queue) == 0

    def push(self, value):
        self.queue.appendleft(value)
        # change so the begining of the line is at the left
        # self.queue.append(value)

    def pop(self):
        if not self.is_empty():
            return self.queue.pop()
            # change so the begining of the line is at the left
            # return self.queue.popleft()
        else:
            raise Exception("The stack is empty.")

    def top(self):
        if not self.is_empty():
            return self.queue[-1]
            # change so the begining of the line is at the left
            # return self.queue[0]
        else:
            raise Exception("The stack is empty.")

    def reverse(self, k):
        stack_temp = Stack()
        queue_temp = Queue()

        if k > len(self.queue):
            raise Exception("K is bigger than the queue.")

        # pass the first k part of the queue
        for i in range(k):
            stack_temp.push(self.queue.pop())

        # pass the rest of the queue to a queue
        while not self.is_empty():
            queue_temp.push(self.queue.pop())

        # merge the queue with the stack
        while not stack_temp.is_empty():
            # self.queue.appendleft(stack_temp.pop())
            self.queue.appendleft(stack_temp.pop())

        while not queue_temp.is_empty():
            self.queue.appendleft(queue_temp.pop())

