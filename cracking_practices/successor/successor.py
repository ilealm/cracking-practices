# Successor 4.6
# PROBLEM DOMAIN
# Write an algorithm to find the "next" node (i.e in-order successor) of a given node in a BST. You may assume that each node has a link to its parent.


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.parent = None


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

# APPROACH 1. From the input node, and from there, get the right node, then most left node value.
def successor(node):
    successor_node = None
    if not node : return successor_node

    def traverse(current):
        nonlocal successor_node

        if not current : return successor_node

        if current.left :
            traverse(current.left)
        else:
            successor_node = current

    traverse(node.right)

    if successor_node:
        return successor_node.value
    else:
        return successor_node





	# set successor to None
	# create a inside function called traverse, to get to the left-most node
	# send traverse(node.right)
	# return successor

	# create helper inside function: traverse, which receives a node (current)
	# 	set successor as nonlocal
	# 	add base case to exit the recursion
	# 		if current is not truty, return
	# 		if current has left, recurse on it:
	# 			traverse(current.left)
	# 		else
	# 			#I got to the left-most node
	# 			set successor to current


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
    BST.add(151)
    BST.add(165)
    BST.add(180)
    BST.add(200)
    # print(BST.inOrder())
    # node 150
    node = BST.root.right.left.left.left
    print(node.value)
    # print(successor(node))

