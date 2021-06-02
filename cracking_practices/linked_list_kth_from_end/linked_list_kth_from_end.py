# PROBLEM: Using a linked list, return the kth node value from the end.
# Use O(n) for time and space.

class Node:
    def __init__(self, value, _next=None):
        self.value = value
        self.next = _next

    def __repr__(self):
        return f"[{self.value}] -> {self.next}"


class LinkedList(Node):
    def __init__(self):
        self.head = None

    def __str__(self):
        if not self.head:
            return "The linked list is empty."

        return f"The head is {self.head.value}"


    def traverse(self):
        if not self.head:
            return "The linked list is empty"

        # if I use self.head, will auto create a traverse in all the linkedlist.
        # if I use self.head.value, will just return the head value
        return f"The head is {self.head}"


    def add(self, value):
        new_node = Node(value)

        new_node.next = self.head

        self.head = new_node


    def kth_from_end(self, k):
        if k < 0 : return
        if not self.head:
            return "The linked list is empty."

        current = runner = self.head

        # create the runner gap
        i = 0
        while runner and i<k:
            i += 1
            runner = runner.next

        if i<k:
            return "Kth value is bigger than the linked list."


        while runner.next:
            runner = runner.next
            current = current.next


        return current.value


