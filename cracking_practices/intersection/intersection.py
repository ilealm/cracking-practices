class Node():
    def __init__ (self, value, next_ = None):
        self.value =  value
        self.next = next_

        if (not next_ == None) and ( not isinstance(next_, Node)):
            raise TypeError("The value of the next node MUST be a node")


    def __repr__(self):
        return f"{self.value} -> {self.next}"


# I updated insert method to allows to set the next value, and to return the inserted node.
class LinkedList():
    def __init__(self):
        self.head = None

    def __repr__(self):
        return f"The head is {self.head}"

    def insert(self, value, next_ = None):
        new_node = Node(value,next_)
        if self.head : new_node.next = self.head
        self.head = new_node
        return new_node


def interseccion_approach_one(one, two):
    if not one:
        raise Exception('First linked list must be valid.')
        return False
    if not two:
        raise Exception('Second linked list must be valid.')
        return False

    one_current = one.head
    two_current = None
    while one_current:
        two_current = two.head
        while two_current:
            if one_current == two_current:
                return one_current
            two_current = two_current.next

        one_current = one_current.next

    return False



if __name__ == "__main__":
    one = LinkedList()
    one.insert('E')
    one.insert('D')
    node_c = one.insert('C')
    one.insert('B')
    one.insert('A')

    two = LinkedList()
    two.insert('Z')
    # two.insert('Z',node_c)
    two.insert('Y')
    two.insert('X')

    print(one)
    print(two)
    print(interseccion_approach_one(one, two))
