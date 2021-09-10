from collections import deque


class Queue:
    def __init__(self) -> None:
        self.stack_in = deque()
        self.stack_out = deque()

    def __str__(self) -> str:
        return self.stack_in

    # checks that both stacks are empty
    def is_empty(self):
        return (len(self.stack_in) == 0) and (len(self.stack_out) == 0)


    def stack_in_is_empty(self):
        return len(self.stack_in) == 0


    def stack_out_is_empty(self):
        return len(self.stack_out) == 0


    def enqueue(self, value):
        self.stack_in.append(value)


    def dequeue(self):
        if self.is_empty():
            raise Exception("The queue is empty.")

        if self.stack_out_is_empty():
            self.fill_stack_out()

        return self.stack_out.pop()


    # method that dequeue() each value of stack_in and insert it on stack_out.
    # At the end stack_out will have the stack_in values in reverse order
    def fill_stack_out(self):
        while not self.stack_in_is_empty():
            # print("in fill stack", self.stack_in.pop())
            self.stack_out.append(self.stack_in.pop())




