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



def palindrome_singly_ll(linked_list):
    if not linked_list:
        raise Exception('The linked list must be valid.')
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


def palindrome_doubly_ll(double_ll):
    if not double_ll:
        raise Exception('The double linked list must be valid.')
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



if __name__ == "__main__":
    # singly_ll = LinkedList()
    # singly_ll.insert('k')
    # singly_ll.insert('a')
    # singly_ll.insert('y')
    # singly_ll.insert('a')
    # singly_ll.insert('k')
    # print('kayak:', palindrome_singly_ll(singly_ll))

    # singly_ll = LinkedList()
    # singly_ll.insert('M')
    # singly_ll.insert('o')
    # singly_ll.insert('m')
    # print('Mom:', palindrome_singly_ll(singly_ll))

    # singly_ll = LinkedList()
    # singly_ll.insert('a')
    # singly_ll.insert('b')
    # singly_ll.insert('c')
    # singly_ll.insert('d')
    # singly_ll.insert('e')
    # print('abcde:', palindrome_singly_ll(singly_ll))


    # singly_ll = LinkedList()
    # singly_ll.insert('r')
    # singly_ll.insert('o')
    # singly_ll.insert('t')
    # singly_ll.insert('a')
    # singly_ll.insert('t')
    # singly_ll.insert('o')
    # singly_ll.insert('r')
    # print('Rotator:', palindrome_singly_ll(singly_ll))


    # doubly_ll = DoublyLinkedList()
    # doubly_ll.insert('a')
    # doubly_ll.insert('b')
    # doubly_ll.insert('c')
    # doubly_ll.insert('d')
    # doubly_ll.insert('e')



    # print(doubly_ll.head.next.previous.value)
    # print(doubly_ll.head.next.value)
    # print(doubly_ll.head.next.next.value)

    # print('----- ')
    # print(doubly_ll.head.next.next.previous.value)
    # print(doubly_ll.head.next.next.value)
    # print(doubly_ll.head.next.next.next.value)

    doubly_ll = DoublyLinkedList()
    doubly_ll.insert('k')
    doubly_ll.insert('a')
    doubly_ll.insert('y')
    doubly_ll.insert('a')
    doubly_ll.insert('k')
    print('doubly_ll kayak:', palindrome_doubly_ll(doubly_ll))


    doubly_ll = DoublyLinkedList()
    doubly_ll.insert('M')
    doubly_ll.insert('o')
    doubly_ll.insert('m')
    print('doubly_ll Mom:', palindrome_doubly_ll(doubly_ll))


    doubly_ll = DoublyLinkedList()
    doubly_ll.insert('a')
    doubly_ll.insert('b')
    doubly_ll.insert('c')
    doubly_ll.insert('d')
    doubly_ll.insert('e')
    print('doubly_ll abcde:', palindrome_doubly_ll(doubly_ll))


    doubly_ll = DoublyLinkedList()
    doubly_ll.insert('a')
    doubly_ll.insert('b')
    print('doubly_ll a:', palindrome_doubly_ll(doubly_ll))
