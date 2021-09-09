import re

from _pytest.compat import is_generator
from _pytest.python_api import raises


class Queue:
    def __init__(self) -> None:
        self.size = 5
        self.queue = [None] * self.size
        self.items = 0
        self.front = 0
        self.rear = 0

    def __str__(self) -> str:
        return self.queue

    def is_empty(self):
        return self.items == 0

    def is_full(self):
        return self.items == self.size

    def peek(self):
        if self.is_empty():
            raise Exception("The array is empty.")

        return self.queue[self.front]

    def push(self, value):
        if self.is_full():
            raise Exception("The array is full.")

        self.queue[self.rear] = value

        # stablish new rear's value
        self.rear = (self.rear + 1) % self.size

        # increase the items
        self.items += 1


    def pop(self):
        if self.is_empty():
            raise Exception("The array is empty.")

        value = self.queue[self.front]

        # step to "clear" the array, is not needed but its helps in the development
        self.queue[self.front] = None

        # assign the new value of front
        self.front = (self.front + 1) % self.size

        # decrease the items
        self.items -= 1

        return value


