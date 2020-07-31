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




if __name__ == "__main__":
    # singly_ll = LinkedList()
    # singly_ll.insert('k')
    # singly_ll.insert('a')
    # singly_ll.insert('y')
    # singly_ll.insert('a')
    # singly_ll.insert('k')
    # print('kayak:', palindrome_singly_ll(singly_ll))

    singly_ll = LinkedList()
    singly_ll.insert('M')
    singly_ll.insert('o')
    singly_ll.insert('m')
    print('Mom:', palindrome_singly_ll(singly_ll))

    singly_ll = LinkedList()
    singly_ll.insert('a')
    singly_ll.insert('b')
    singly_ll.insert('c')
    singly_ll.insert('d')
    singly_ll.insert('e')
    print('abcde:', palindrome_singly_ll(singly_ll))


    # singly_ll = LinkedList()
    # singly_ll.insert('r')
    # singly_ll.insert('o')
    # singly_ll.insert('t')
    # singly_ll.insert('a')
    # singly_ll.insert('t')
    # singly_ll.insert('o')
    # singly_ll.insert('r')
    # print('Rotator:', palindrome_singly_ll(singly_ll))



