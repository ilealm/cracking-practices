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
# From root, I will move to right to start the zigzag traverse.
# level = 0, pow(2,level) => 1
# level = 1, pow(2,level) => 2
# level = 2, pow(2,level) => 4
# level = 3, pow(2,level) => 8
# level = 4, pow(2,level) => 16
# level = 5, pow(2,level) => 32
def zig_zag_tree(tree):
    zig_zag_list = []

    if not tree or not tree.root : return zig_zag_list

    bf_list = tree.BreadthFirst(tree)
    print(bf_list)

    pointer = 0 # is a pointer to the current position in the list
    level = 0   # is the level of the tree where I'm now

    zig_zag_list.append(bf_list[pointer])

    pointer += 1
    level += 1
    starting_on_right = True

    while len(zig_zag_list) < len(bf_list):
        possitions_to_move = pow(2, level)
        # for unperfectly balanced trees..
        if possitions_to_move > (len(bf_list) - len(zig_zag_list) ) :
            possitions_to_move = len(bf_list) - len(zig_zag_list)

        if starting_on_right:
            rightest_position = (possitions_to_move + pointer) - 1 # because I'm using indices in the list
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


# IMPLEMENTING BREADTH FIRST. Traverse the tree in a breath way, and create a temp list to save the nodes of each level.
# Depending on if the level is even or odd, the node will be appended to the end or inserted at the top of the temp list.
# When I change level, before doing that I will insert the temp list to my return list.
def zig_zag_tree_v2(tree):
    list_breadth = []

    # if not tree.root : return 'The Tree is empty.'
    if not tree.root : return list_breadth

    breadth = Queue()
    breadth.enqueue(tree.root)
    level = 0
    num_ele_this_level = pow(2,level)
    ele_added_this_level = 0
    is_even_level = True  # BC starts on level 0
    temp_list = [] # here I'm going to save the array of only the current level, and I will insert/append depending on is_even_level

    while not breadth.is_empty():

        front = breadth.dequeue()
        if front.left:
            breadth.enqueue(front.left)
        if front.right:
            breadth.enqueue(front.right)


        if is_even_level:
            temp_list.append(front.value)
        else:
            temp_list.insert(0, front.value)

        ele_added_this_level += 1


        if ele_added_this_level == num_ele_this_level:
            #  I just moved one level down
            level += 1
            list_breadth += temp_list
            temp_list.clear()
            # list_breadth.append('Level ' + str(level))

            num_ele_this_level = pow(2,level)
            ele_added_this_level = 0
            is_even_level = not is_even_level


    # if the tree is unbalance in the last level, add the rest of the list
    if ele_added_this_level < num_ele_this_level : list_breadth += temp_list

    return list_breadth


# Approach 3. Implement 2 queues, one for actual level and second for next level.
# THIS IS THE BETTER APPROACH, THE TREE DOESN'T NEED TO BE BALANCED
# Use a flag to know where to move: left_to_rigth, based on this flag, I can know if insert left or right next.
# Based on: https://www.youtube.com/watch?v=PwEmiE5u3tE
# But I did some changes
def zig_zag_tree_two_queues(tree):
    list_return = []
    list_level = []

    if not tree.root : return list_return

    current_level = Queue()
    next_level = Queue()
    left_to_rigth = False

    current_level.enqueue(tree.root)

    while not current_level.is_empty():
        front = current_level.dequeue()

        if front.left :
            next_level.enqueue(front.left)
        if front.right :
            next_level.enqueue(front.right)


        if left_to_rigth:
            list_level.append(front.value)
        else:
            list_level.insert(0, front.value)


        if current_level.is_empty():
            # this means I ended current level
            list_return += list_level
            list_level.clear()
            # change the flow of the zig zag
            left_to_rigth = not left_to_rigth
            # swap queues
            current_level, next_level = next_level, current_level

    return list_return



