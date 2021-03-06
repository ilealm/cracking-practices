# List of Depths 4.3
# PROBLEM DOMAIN
# Given a binary tree, design an algorith which creates a link list of all the nodes at each level depth.
# If you have a tree with deep D, you will have D linked list.

# HELPER CLASSES


from collections import deque


class Queue:
    def __init__(self):
        self.storage = deque()

    def enqueue(self, value):
        self.storage.appendleft(value)

    def is_empty(self):
        return len(self.storage) == 0

    def dequeue(self):
        if not self.is_empty():
            return self.storage.pop()

    def peek(self):
        if not self.is_empty():
            return self.storage[-1]


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def __str__(self):
        return f"Node: {self.value}"


class BinaryTree:
    def __init__(self):
        self.root = None

    def __str__(self):
        return f"The root is {self.root}"

    def BreadthFirst(self):
        list_return = []

        if not self.root:
            return list_return

        breadth = Queue()
        breadth.enqueue(self.root)

        while not breadth.is_empty():
            front = breadth.dequeue()

            list_return.append(front.value)

            if front.left:
                breadth.enqueue(front.left)
            if front.right:
                breadth.enqueue(front.right)

        return list_return


class BinarySearchTree(BinaryTree):
    def __str__(self):
        if not self.root:
            return "The tree is empty."

    def add(self, value):
        new_node = Node(value)

        if not self.root:
            self.root = new_node
            return

        def traverse(current_node, new_node):
            if not current_node:
                return

            if new_node.value < current_node.value:
                if not current_node.left:
                    current_node.left = new_node
                else:
                    traverse(current_node.left, new_node)
            else:
                if not current_node.right:
                    current_node.right = new_node
                else:
                    traverse(current_node.right, new_node)

        traverse(self.root, new_node)


class NodeLinkedList:
    def __init__(self, value, next_=None):
        self.value = value
        self.next = next_

    def __str__(self):
        return f"{self.value} -> {self.next} "


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __repr__(self):
        return f"The head is {self.head}"

    def insert(self, value):
        new_node = NodeLinkedList(value)

        if self.head:
            new_node.next = self.head

        self.head = new_node

        if not self.tail:
            self.tail = new_node

    def append(self, value):
        if not self.head:
            self.insert(value)
            return

        # traverse all the LL to the end of the LL.
        # this could improve if I implement a tail artribute on the init of the class, so I'm implementing
        new_node = NodeLinkedList(value)
        self.tail.next = new_node
        self.tail = new_node


def list_of_depths(tree):
    return_List = []

    if not tree.root:
        return return_List

    liknedlist_level = LinkedList()
    current_level = Queue()
    next_level = Queue()

    current_level.enqueue(tree.root)

    while not current_level.is_empty():
        front = current_level.dequeue()
        # this add the node to the top of the LL, so the nodes of the tree will be inverted
        # liknedlist_level.insert(front.value)
        # so I'm appending at the tail of the ll
        liknedlist_level.append(front.value)

        if front.left:
            next_level.enqueue(front.left)
        if front.right:
            next_level.enqueue(front.right)

        # check if I'm changing levels, this is, when current_level is empty
        if current_level.is_empty():
            # store the linked list in the list, and reset it
            return_List.append(str(liknedlist_level).strip())
            liknedlist_level = LinkedList()

            # swap queues to change the level
            current_level, next_level = next_level, current_level

    return return_List


if __name__ == "__main__":

    BST = BinarySearchTree()
    # level 0
    BST.add(100)
    # level 1
    BST.add(50)
    BST.add(150)
    # level 2
    BST.add(25)
    BST.add(75)
    BST.add(125)
    BST.add(175)
    # level 3
    BST.add(15)
    BST.add(40)
    BST.add(90)
    BST.add(115)
    BST.add(160)
    BST.add(190)
    # level 4
    BST.add(5)
    BST.add(20)
    BST.add(45)
    BST.add(80)
    BST.add(95)
    BST.add(110)
    BST.add(150)
    BST.add(165)
    BST.add(180)
    print(list_of_depths(BST))

