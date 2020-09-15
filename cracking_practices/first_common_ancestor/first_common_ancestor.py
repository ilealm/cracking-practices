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



def get_node_path(tree, target):
    return_stack = Stack()
    founded = False

    # return_stack.push(tree.root.value)

    def traverse(current, target):
        nonlocal founded
        if founded : return
        if not current: return

        return_stack.push(current.value)

        if current.value == target.value:
            return

        if current.left :
            if not current.left.value == target.value:
                traverse(current.left, target)
            else:
                # the next node is my target, and I don't need to go there.
                founded = True
                return
        else:
            return_stack.pop()



        if current.right :
            if not current.right.value == target.value:
                traverse(current.right, target)
            else:
                # the next node is my target, and I don't need to go there.
                founded = True
        # else:
        #     return_stack.pop()



    traverse(tree.root, target)
    return return_stack






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

    # Node: 20
    node_a = BST.root.left.left.left.right
    print(BST, node_a.value)
    get_node_path(BST, node_a)



