from collections import deque

# HELPER FUNCTIONS

class Node:
    def __init__(self, value, left = None,  rigth = None):
        self.value = value
        self.left = left
        self.right = rigth

    def __str__(self):
        return f"Node: {self.value}"

class BinaryTree:
    def __init__(self):
        self.root = None

    def __str__(self):
        if not self.root : return 'The root is empty.'

        return f'The root is {self.root.value}'


    def BreadthFirst(self,tree):
        list_return = []

        # if not tree.root : return 'The Tree is empty.'
        if not tree.root : return list_return

        breadth = Queue()

        breadth.enqueue(tree.root)

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
        if not self.root : return 'The root is empty.'

        return f'The root is {self.root.value}'


    def add(self, value):
        new_node = Node(value)

        if self.root == None :
            self.root = new_node
            return

        def traverse(current_node, new_node):

            if not current_node : return

            if new_node.value < current_node.value:
                if current_node.left == None :
                    current_node.left = new_node
                else:
                    traverse(current_node.left, new_node)
            else:
                if current_node.right == None :
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


# Approach Brute Force: Call helper function to create a list with all the tree traversed in Breath First fashion.
# From there, I will start moving in the list level by level.
# level = 0, pow(2,level) => 1
# level = 1, pow(2,level) => 2
# level = 2, pow(2,level) => 4
# level = 3, pow(2,level) => 8
# level = 4, pow(2,level) => 16
# level = 5, pow(2,level) => 32

def zig_zag_tree(tree):
    zig_zag_list = []

    if not tree: return
    bf_list = tree.BreadthFirst(tree)

    pointer = 0 # is a pointer to the current position in the list
    level = 0   # is the level of the tree where I'm now

    zig_zag_list.append(bf_list[pointer])

    pointer += 1
    level += 1
    starting_on_right = True

    while len(zig_zag_list) < len(bf_list):
        possitions_to_move = pow(2, level)
        if starting_on_right:
            rightest_position = (possitions_to_move + pointer) - 1 # because I'm using indices
            for i in range(possitions_to_move):
                zig_zag_list.append(bf_list[rightest_position - i])
                pointer += 1

            starting_on_right = False
        else:

            for i in range(possitions_to_move):
                zig_zag_list.append(bf_list[pointer])
                pointer += 1
            starting_on_right = True

        level += 1


    return zig_zag_list

    # print(bf_list)


def return_dummy_tree():
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
    # level 4
    BST.add(5)
    BST.add(20)
    BST.add(30)
    BST.add(45)
    BST.add(55)
    BST.add(65)
    BST.add(80)
    BST.add(95)
    BST.add(110)
    BST.add(120)
    BST.add(130)
    BST.add(145)
    BST.add(150)
    BST.add(165)
    BST.add(180)
    BST.add(200)

    return BST

if __name__ == "__main__":
    print(zig_zag_tree(return_dummy_tree()))

