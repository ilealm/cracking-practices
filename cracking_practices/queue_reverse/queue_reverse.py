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


class Queue:
    def __init__(self) -> None:
        self.queue = deque()

    def is_empty(self):
        return len(self.queue) == 0

    def push(self, value):
        self.queue.appendleft(value)

    def pop(self):
        if not self.is_empty():
            return self.queue.popleft()
        else:
            raise Exception("The stack is empty.")


    def top(self):
        if not self.is_empty():
            return self.queue[0]
        else:
            raise Exception("The stack is empty.")


    def reverse(self):
        aux_stack = Stack()

        # save the queue to a stack
        while not self.is_empty():
            aux_stack.push(self.pop())

        # pass the stack value to the queue
        while not aux_stack.is_empty():
            self.push(aux_stack.pop())



# main
# stack = Stack()
# stack.push(10)
# stack.push(20)
# stack.push(30)
# print(stack.peek())
# stack.push(40)
# stack.push(50)
# print(stack.peek())

queue = Queue()
queue.push(10)
queue.push(20)
queue.push(30)
queue.push(40)
queue.push(50)
# print(queue.is_empty())
# print(queue.pop())
# print(queue.pop())
# print(queue.pop())
# print(queue.pop())
# print(queue.pop())

# print(queue.show_queue())
print(queue.top())
queue.reverse()
print(queue.top())
