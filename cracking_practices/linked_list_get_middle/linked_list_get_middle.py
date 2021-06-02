# Problem Get middle node of Linked List
# Using a linked list, return the middle node value from the end.  Use O(n) for time and space.

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
        return f"The head is {self.head.value}"

    def traverse(self):
        return f"The head is {self.head}"

    def add(self, value):
        new_node = Node(value)

        new_node.next = self.head

        self.head = new_node


    def get_middle_node(self):
        if not self.head:
            return "The list is empty."

        current = runner = self.head

        while runner and runner.next:
            runner = runner.next.next
            # this line is to get the right node for odd lists
            if runner:
                current = current.next

        return current.value
