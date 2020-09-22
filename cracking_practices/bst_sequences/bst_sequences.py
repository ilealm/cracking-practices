# BST Sequence 4.9
# PROBLEM DOMAIN
# A binary search tree was created by traversing a through an array from left to right and inserting each element.
# Given a binary search tree with distinct elements, print all possible arrays that could have lead to this tree.

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
        result= []

        if not self.root : return result

        def traverse(current):
            if not current : return

            result.append(current.value)
            traverse(current.left)
            traverse(current.right)


        traverse(self.root)
        return result


    def BreadthFirst(self):
        result = []
        if not self.root :
            return result

        breadth = Queue()
        breadth.enqueue(self.root)

        while not breadth.is_empty():
            front = breadth.dequeue()
            result.append(front.value)

            if front.left :
                breadth.enqueue(front.left)
            if front.right :
                breadth.enqueue(front.right)

        return result


class BinarySearchTree(BinaryTree):
    def __str__(self):
        if not self.root:
            return "The tree is empty."


    def add(self ,value):
        new_node = Node(value)

        if not self.root:
            self.root = new_node
            return

        def traverse(current, new_node):
            if not current : return

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



def permutations(array, permutation=None, perms=None):
    if permutation is None:
        permutation = []
    if perms is None:
        perms = []

    if array == []:
        perms.append(permutation.copy())
        return

    for i in range(0, len(array)):
        permutation.append(array[i])
        sub_array = array[:i] + array[i + 1 :]
        permutations(sub_array, permutation, perms)
        permutation.pop()

    return perms


def bst_sequences(tree):
    # transform the tree to an array, using BreadthFirst, which will have the root at [0]
    array = tree.BreadthFirst()
    # I know array[0] is the root, so I will get the permutations of the rest of the array
    perms_lst = permutations(array[1:])
    # add the root to each permutation
    for i in range(0, len(perms_lst)):
        perms_lst[i].insert(0, array[0])

    return perms_lst


# if __name__ == "__main__":
BST = BinarySearchTree()
#     # level 0
BST.add(2)
BST.add(1)
BST.add(3)
BST.add(4)
print(bst_sequences(BST))
