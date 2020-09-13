# Check Balanced 4.4
# PROBLEM DOMAIN
# Implement a function to check if a binary tree is balanced.
# For the purpose of this question, a balanced tree is defined  to be a tree
# such  as the hights of the two subtrees of any node never differ by more than one.
from collections import deque

class Node():
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def __str__(self):
        return f"Node: {self.node}"

class BinaryTree():
    def __init__(self):
        self.root = None

    def __str__(self):
        return f"The root is {self.root}"

    def preorder(self):
        return_list = []
        if not self.root : return return_list

        def traverse(current):
            if not current : return

            return_list.append(current.value)
            traverse(current.left)
            traverse(current.right)

        traverse(self.root)
        return return_list


class BinarySearchTree(BinaryTree):
    def __str__(self):
        return f"The root is {self.root}"

    def add(self, value):

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



class Queue():
    def __init__(self):
        self.storage = deque()

    def enqueue(self, value):
        self.storage.appendleft(value)

    def is_empty(self):
        return len(self.storage) == 0

    def dequeue(self):
        if not self.is_empty():
            return self.storage.pop()


def get_hight(tree):
    num_levels = 0

    current_level = Queue()
    next_level = Queue()

    current_level.enqueue(tree)

    while not current_level.is_empty():

        front = current_level.dequeue()
        if front.left:
            next_level.enqueue(front.left)
        if front.right:
            next_level.enqueue(front.right)

        if current_level.is_empty():
            num_levels +=1
            current_level, next_level = next_level, current_level


    return num_levels



def check_balanced(tree):
    if not tree.root : return False

    if tree.root.left:
        left_height = get_hight(tree.root.left)
    else:
        left_height = 0

    if tree.root.right:
        right_height = get_hight(tree.root.right)
    else:
        right_height = 0

    if (left_height - right_height ) == 0 or (left_height - right_height) == 1:
        return True
    else:
        return False


