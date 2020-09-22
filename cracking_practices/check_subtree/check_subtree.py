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

    def preOrder():
        result = []

        if not self.root:
            return result

        def traverse(current):
            if not current:
                return

            result.append(current.value)
            traverse(current.left)
            traverse(current.right)

        traverse(self.root)
        return result

    def BreadthFirst(self):
        result = []
        if not self.root:
            return result

        breadth = Queue()
        breadth.enqueue(self.root)

        while not breadth.is_empty():
            front = breadth.dequeue()
            result.append(front.value)

            if front.left:
                breadth.enqueue(front.left)
            if front.right:
                breadth.enqueue(front.right)

        return result


class BinarySearchTree(BinaryTree):
    def __str__(self):
        if not self.root:
            return "The tree is empty."

    def add(self, value):
        new_node = Node(value)

        if not self.root:
            self.root = new_node
            return

        def traverse(current, new_node):
            if not current:
                return

            if new_node.value < current.value:
                if not current.left:
                    current.left = new_node
                else:
                    traverse(current.left, new_node)
            else:
                if not current.right:
                    current.right = new_node
                else:
                    traverse(current.right, new_node)

        traverse(self.root, new_node)


# END HELPER CLASSES

def are_equal_trees(tree1, tree2):
    are_equal = True
    breadth1 = Queue()
    breadth2 = Queue()

    breadth1.enqueue(tree1)
    breadth2.enqueue(tree2)
    while not breadth2.is_empty() and are_equal:
        front1 = breadth1.dequeue()
        front2 = breadth2.dequeue()

        if not front1.value == front2.value:
            are_equal = False
            return are_equal
        else:
            if front1.left :
                breadth1.enqueue(front1.left)
            if front1.right :
                breadth1.enqueue(front1.right)
            if front2.left :
                breadth2.enqueue(front2.left)
            if front2.right :
                breadth2.enqueue(front2.right)

    return are_equal


def check_subtree(tree1, tree2):
    is_subtree = False
    if not tree1 or not tree2 : return is_subtree

    breadht = Queue()
    breadht.enqueue(tree1.root)

    while not breadht.is_empty() and not is_subtree:
        front = breadht.dequeue()

        if front.value == tree2.root.value :
            is_subtree = are_equal_trees(front, tree2.root)

        if front.left:
            breadht.enqueue(front.left)
        if front.right:
            breadht.enqueue(front.right)

    return is_subtree
