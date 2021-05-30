from typing import Counter


class Node:
    def __init__(self, value, next_=None):
        self.value = value
        self.next = next_

    def __repl__(self):
        return f"{self.value} -> {self.next}"


class LinkedList(Node):
    def __init__(self):
        self.head = None

    def __repl__(self):
        return f"The head is {self.head.value}"

    def append_top(self, value):
        new_node = Node(value)
        if self.head:
            new_node.next = self.head

        self.head = new_node

    def traverse(self):
        if not self.head:
            return None

        ll_values = ""
        current = self.head
        while current:
            ll_values += "[" + str(current.value) + "] -> "
            current = current.next

        return "Head => " + ll_values + " None"


    def reverse(self):
        if not self.head:
            return

        previous = None
        current = self.head

        while current:
            # save the next link
            next = current.next
            # change the link to the previous
            current.next = previous
            # set the previous as my current possition (for the next round)
            previous = current
            # stablish my new possition
            current = next

        # here, I need to set the head to previous, BC current is NONE!
        self.head = previous



ll = LinkedList()
ll.append_top(40)
ll.append_top(30)
ll.append_top(20)
ll.append_top(10)
print("Original \n", ll.traverse())
ll.reverse()
print("Reversed \n", ll.traverse())
# Original
#  Head => [10] -> [20] -> [30] -> [40] ->  None
# Reversed
#  Head => [40] -> [30] -> [20] -> [10] ->  None
