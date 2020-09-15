class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.parent = None

    def __str__(self):
        return f"Node: {self.value}"


class BinarySearch:
    def __init__(self):
        self.root = None

    def __str__(self):
        return f"The root is {self.root}"

    def inOrder(self):
        return_array = []

        if not self.root:
            return return_array

        def traverse(current):
            if not current:
                return

            traverse(current.left)
            return_array.append(current.value)
            traverse(current.right)

        traverse(self.root)

        return return_array


class BinarySearchTree(BinarySearch):
    def __str__(self):
        return f"The root is {self.root}"

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
                    new_node.parent = current
                    current.left = new_node
                else:
                    traverse(current.left, new_node)
            else:
                if not current.right:
                    new_node.parent = current
                    current.right = new_node
                else:
                    traverse(current.right, new_node)

        traverse(self.root, new_node)


class NodeStack:
    def __init__(self, value, next_=None):
        self.value = value
        self.next = next_

    def __repr__(self):
        return f"{self.value} -> {self.next}"


class Stack:
    def __init__(self):
        self.top = None

    def __repr__(self):
        return f"The top is {self.top}"

    def __str__(self):
        return f"The top is {self.top}"

    def push(self, value):
        new_node = NodeStack(value, self.top)
        self.top = new_node

    def is_empty(self):
        return self.top == None

    def peek(self):
        if not self.is_empty():
            return self.top.value
        else:
            return "Can't peek on an empty stack."
            raise Exception("Can't peek on an empty stack.")

    def pop(self):
        if not self.is_empty():
            temp_node = self.top
            self.top = self.top.next
            temp_node.next = None
            return temp_node.value
        else:
            return "Can't pop from an empty stack."
            raise Exception("Can't pop from an empty stack.")


# Function that returns the path of a node in the tree. It receives a tree and a node, to search it value in the tree.
# This function can be changed to return a Stack() obj. of the nodes of the path
def get_node_path(tree, node):
    # for returning a stack
    # return_stack = Stack()  # this works perfect, if I want to have a nodes instead of a list
    # for return a list:
    return_stack = []   # this is for returning list
    founded = False

    if not tree or not node : return return_stack

    def traverse(current, target):
        nonlocal founded
        if founded:
            return
        if not current:
            return

        # for returning a stack
        # return_stack.push(current.value)

        # for return a list:
        return_stack.insert(0, current.value)

        if current.value == target.value:
            founded = True
            return

        if current.left:
            if not current.left.value == target.value:
                traverse(current.left, target)
            else:
                founded = True
                return

        if current.right:
            if not current.right.value == target.value:
                traverse(current.right, target)
            else:
                founded = True

        if not founded:
            # for return a list:
            return_stack.pop(0)
            # for return a stack:
            # return_stack.pop()


    traverse(tree.root, node)
    return return_stack

