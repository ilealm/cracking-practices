# MINIMAL TREE
# PROBLEM DOMAIN:

# Given a sorted (increasing order) array with unique integer elements, white an algorithm to create a
# binary search tree with minimal height.


# HELPER FUNCTIONS
from collections import deque


class Node:
    def __init__(self, value, left=None, rigth=None):
        self.value = value
        self.left = left
        self.right = rigth

    def __str__(self):
        return f"Node: {self.value}"


class BinaryTree:
    def __init__(self):
        self.root = None

    def __str__(self):
        if not self.root:
            return "The root is empty"

        return f"The root is {self.root.value}"

    def BreadthFirst(self):
        list_return = []
        breadth = Queue()

        if not self.root:
            return list_return

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
            return "The root is empty."

        return f"The root is {self.root.value}"

    def add(self, value):
        new_node = Node(value)

        if not self.root:
            self.root = new_node
            return

        def traverse(current_node, new_node):
            if not current_node:
                return

            if new_node.value < current_node.value:
                if current_node.left == None:
                    current_node.left = new_node
                else:
                    traverse(current_node.left, new_node)
            else:
                if current_node.right == None:
                    current_node.right = new_node
                else:
                    traverse(current_node.right, new_node)

        traverse(self.root, new_node)


class Queue:
    def __init__(self):
        self.storage = deque()

    def enqueue(self, value):
        self.storage.appendleft(value)

    def dequeue(self):
        if not self.is_empty():
            return self.storage.pop()

    def peek(self):
        return self.storage[-1]

    def is_empty(self):
        return len(self.storage) == 0


# # def minimal_tree(array, start, end, tree):
# def minimal_tree(array, start, end, tree):
#     print(array)
#     print("start: ", start, " end:", end)

#     if start == end:
#         tree.add(array[start])
#         return

#     middle = (end - start) // 2
#     tree.add(array[middle])
#     # here my problem is when I do the left part, the middle is not the middle in the left side

#     # recursive left part
#     minimal_tree(array, start, middle-1, tree)
#     # recursive right part
#     minimal_tree(array, middle+1, end, tree)

#     return tree


# def minimal_tree(array, start, end, tree):
def minimal_tree(array):
    tree = BinarySearchTree()

    def traverse_array(sub_array, tree):
        print(sub_array)

        if len(sub_array) == 1:
            tree.add(sub_array[0])
            return

        middle = len(sub_array) // 2
        tree.add(sub_array[middle])

        # recursion left part
        traverse_array(sub_array[0: middle], tree)
        # recursion right part
        traverse_array(sub_array[middle+1: ], tree)
        # minimal_tree(sub_array[middle+1: len(sub_array]), tree)


    traverse_array(array, tree)

    return tree


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
    BST.add(60)
    BST.add(90)
    BST.add(115)
    BST.add(140)
    BST.add(160)
    BST.add(190)
    # # level 4
    # BST.add(5)
    # BST.add(20)
    # BST.add(30)
    # BST.add(45)
    # BST.add(55)
    # BST.add(65)
    # BST.add(80)
    # BST.add(95)
    # BST.add(110)
    # BST.add(120)
    # BST.add(130)
    # BST.add(145)
    # BST.add(150)
    # BST.add(165)
    # BST.add(180)
    # BST.add(200)

    # print(BST.BreadthFirst())

    array = [15, 25, 40, 50, 60, 75, 90, 100, 115, 125, 140, 150, 160, 175, 190]

    # print(minimal_tree(array, 0, len(array), BinarySearchTree()))
    print(minimal_tree(array))

