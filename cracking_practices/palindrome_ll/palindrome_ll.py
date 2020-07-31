# PROBLEM DOMAIN - 2.6 Palindrome in Linked List
# Implement a function to check is a linked list is a palindrome. Each node contains a letter of the word to check.

class Node():
    def __init__ (self, value, next_ = None):
        self.value =  value
        self.next = next_

        if (not next_ == None) and ( not isinstance(next_, Node)):
            raise TypeError("The value of the next node MUST be a node")


    def __repr__(self):
        return f"{self.value} -> {self.next}"


class LinkedList():
    def __init__(self):
        self.head = None

    def __repr__(self):
        return f"The head is {self.head}"

    def insert(self, value):
        new_node = Node(value)
        if self.head : new_node.next = self.head
        self.head = new_node


class DoublyNode():
    def __init__ (self, value, next_ = None, previous = None):
        self.value =  value
        self.next = next_
        self.previous = previous

        if (not next_ == None) and ( not isinstance(next_, DoublyNode)):
            raise TypeError("The value of the next node MUST be a DoublyNode")

        if (not previous == None) and ( not isinstance(previous, DoublyNode)):
            raise TypeError("The value of the previous node MUST be a DoublyNode")

    def __repr__(self):
        return f"{self.value}"
        # return f"{self.previous} -> {self.value} -> {self.next}"


class DoublyLinkedList():
    def __init__(self):
        self.head = None
        self.tail = None

    def __repr__(self):
        return f"The head is {self.head} and the tail is {self.tail}"

    def insert(self, value):
        new_node = DoublyNode(value)
        if self.head :
            self.head.previous = new_node
            new_node.next = self.head

        if not self.tail : self.tail = new_node

        self.head = new_node


# APPROACH 1, Traverse the list and create a variable with all the nodes.value.
def palindrome_singly_ll(linked_list):
    if not linked_list:
        raise Exception('The linked list must be valid.')
        return False

    if linked_list.head == None:
        return False

    word = ''
    current = linked_list.head

    while current:
        word += current.value
        current = current.next

    middle = len(word) // 2
    left = 0
    right = len(word) -1

    for i in range(0, middle):
        if word[left].lower() == word[right].lower():
            left += 1
            right -= 1
        else:
            return False

    return True


# APPROACH 2, Change the linked list to a doubly linked list, and compare head to tail and move pointers to each other.
def palindrome_doubly_ll(double_ll):
    if not double_ll:
        raise Exception('The double linked list must be valid.')
        return False

    if double_ll.head == None:
        return False

    left = doubly_ll.head
    right = doubly_ll.tail


    while not left == right:
        if left.value.lower() == right.value.lower():
            left = left.next
            right = right.previous
        else:
            return False

    return True
