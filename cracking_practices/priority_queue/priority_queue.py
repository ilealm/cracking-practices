# Priority Queue
# Implement a Priority Queue using an array. The methods should include add and remove.
# The remove method should return the greatest value in the array.

from typing import Sized


class PriorityQueue:
    def __init__(self) -> None:
        self.size = 5
        self.queue = [None] * self.size
        self.count = 0

    def is_empty(self):
        return self.count == 0

    def is_full(self):
        return self.count == self.size

    def peek(self):
        if self.is_empty():
            raise Exception("The queue is empty.")

        return self.queue[0]

    def add(self, value):
        if self.is_full():
            raise Exception("The queue is full.")

        if self.count == 0:
            i = 0
        else:
            i = self.switch_graters_to_right(value)

        self.queue[i] = value
        self.count += 1
        

    def switch_graters_to_right(self, value):
        current = self.count - 1
        while (current >= 0) and (value < self.queue[current]):
            self.queue[current + 1] = self.queue[current]
            current -= 1

        return current + 1


    def remove(self):
        if self.is_empty():
            raise Exception('The queue is empty.')

        self.count -= 1

        return self.queue[self.count]



