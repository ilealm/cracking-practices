# PROBLEM DOMAIN
# Validate BST 4.5
# Implement a function that checks if a binary tree is a BST

class Node():
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def __str__(self):
        return f"Node: {self.value}"

class BinaryTree():
    def __init__(self):
        self.root = None

    def __str__(self):
        if not self.root : return 'The root is empty.'

        return f"The root is {self.root.value}"


    def preOrder(self):
        return_list = []
        if not self.root : return return_list

        def traverse(current):
            if not current : return

            return_list.append(current.value)
            traverse(current.left)
            traverse(current.right)


        traverse(self.root)
        return return_list


    def inOrder(self):
        return_list = []
        if not self.root : return return_list

        def traverse(current):
            if not current : return

            traverse(current.left)
            return_list.append(current.value)
            traverse(current.right)


        traverse(self.root)
        return return_list



class BinarySearchTree(BinaryTree):
    def __str__(self):
        if not self.root : return 'The root is empty.'

        return f'The root is {self.root.value}'


    def add(self, value):
        new_node = Node(value)

        if not self.root :
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


def get_max_value(current):
    if not current : return None
    max_value = current.value

    def traverse(current):
        nonlocal max_value
        if not current : return

        if current.value > max_value :
            max_value = current.value

        if current.left:
            traverse(current.left)
        if current.right:
            traverse(current.right)

    traverse(current)
    return max_value


def get_min_value(current):
    if not current : return None
    min_value = current.value

    def traverse(current):
        nonlocal min_value
        if not current : return

        if current.value < min_value :
            min_value = current.value

        if current.left:
            traverse(current.left)
        if current.right:
            traverse(current.right)

    traverse(current)
    return min_value


# APPROACH: From root, I'm going to get the max value of left subtree, then the min value of right subtree, and then compare to the root of the tree.
def validate_bst(tree):
    if not tree.root : return False

    max_value_on_right = get_max_value(tree.root.left)
    min_value_on_left = get_min_value(tree.root.right)
    if max_value_on_right <= tree.root.value and min_value_on_left >= tree.root.value :
        return True
    else:
        return False
