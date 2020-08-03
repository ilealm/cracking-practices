# Given a circular linked list, implement an algorithm that returns the node at
# the beginning of the loop.


class Node():
    def __init__ (self, value, next_ = None):
        self.value =  value
        self.next = next_

        if (not next_ == None) and ( not isinstance(next_, Node)):
            raise TypeError("The value of the next node MUST be a node")


    #  I had to change this BC it got cycled on the return of the value
    def __repr__(self):
        # return f"{self.value} -> {self.next}"
        return f"{self.value}"


# I updated insert method to allows to set the next value, and to return the inserted node.
class LinkedList():
    def __init__(self):
        self.head = None

    def __repr__(self):
        return f"The head is {self.head}"

    def insert(self, value, next_ = None):
        new_node = Node(value, next_)
        if self.head : new_node.next = self.head
        self.head = new_node
        return new_node

    def append(self,value, next_ = None):
        new_node = Node(value, next_)
        current = self.head

        # if the head is none, then call insert function
        if not current :
            self.insert(value)
            return

        while current.next:
            current = current.next
        current.next = new_node


def loop_detection(circular_ll):
    if not circular_ll:
        raise Exception('The circular linked list is not valid.')
        return False

    current = circular_ll.head
    circular_set = set()
    while current:
        if current in circular_set:
            return current
        circular_set.add(current)
        current = current.next

    return False




