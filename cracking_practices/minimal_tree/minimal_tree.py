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



def minimal_tree(array):
    tree = BinarySearchTree()

    def traverse_array(sub_array, tree):
        print(sub_array)

        if len(sub_array) == 0 : return

        if len(sub_array) == 1:
            tree.add(sub_array[0])
            return

        middle = len(sub_array) // 2
        tree.add(sub_array[middle])

        # recursion left part. REMEMBER, THE END IS NOT INCLUDING, SO DON'T DO MIDDLE -1
        traverse_array(sub_array[0: middle], tree)
        # recursion right part
        traverse_array(sub_array[middle+1: ], tree)


    traverse_array(array, tree)

    return tree


if __name__ == "__main__":

#     # print(BST.BreadthFirst())

    array = [25, 50, 75, 100, 130, 150, 175]

#     # => [100, 50, 150, 25, 75, 125, 175, 15, 40, 60, 90, 115, 140, 160, 190]
#     array = [5, 15, 20,25, 30,40,45,50,55,60,65]
#     # =>[40, 20, 55, 15, 30, 50, 65, 5, 25, 45, 60]
#     array = [5, 15, 20,25, 30,40,45, 50,55, 60,65, 75, 80,90, 95, 100, 110, 115, 120, 130, 125, 140, 145, 150, 160, 165, 180, 175, 190, 200]
#     =>[100, 50, 150, 25, 75, 130, 175, 15, 40, 60, 90, 115, 140, 165, 180, 5, 20, 30, 45, 55, 65, 80, 95, 110, 120, 145, 160, 200, 125, 190]


    my_tree = minimal_tree(array)
    print( my_tree.BreadthFirst())

