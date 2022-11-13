class BinaryTree:
    def __init__(self):
        self.root = None

    def __str__(self):
        if not self.root:
            return "The root is empty."

        return f"The root is {self.root.value}"

    class _Node:
        def __init__(self, value):
            self.value = value
            self.left = None
            self.right = None

        def __str__(self):
            return f"Node: {self.value}"

    def insert(self, value):
        if not value:
            return

        new_node = self._Node(value)

        if self.root is None:
            self.root = new_node
            return

        current = self.root
        while current:
            if value < current.value:
                if current.left is None:
                    current.left = new_node
                    return
                else:
                    current = current.left
            else:
                if current.right is None:
                    current.right = new_node
                    return
                else:
                    current = current.right

    def find(self, value):
        if not value:
            return False

        if self.root is None:
            return False

        current = self.root

        while current:
            if current.value == value:
                return True

            if value < current.value:
                current = current.left
            else:
                current = current.right

        return False

    def pre_order(self):
        pre_order_result = ""

        def traverse(current_node):
            if not current_node:
                return

            nonlocal pre_order_result
            # print(current_node.value)
            pre_order_result += str(current_node.value) + " "
            traverse(current_node.left)
            traverse(current_node.right)

        traverse(self.root)
        return pre_order_result


    def in_order(self):
        in_order_result = ""

        def traverse(current_node):
            if not current_node:
                return

            nonlocal in_order_result

            traverse(current_node.left)
            in_order_result += str(current_node.value) + " "
            traverse(current_node.right)

        traverse(self.root)
        return in_order_result

    def post_order(self):
        post_order_result = ""

        def traverse(current_node):
            nonlocal post_order_result

            if current_node is None : return

            traverse(current_node.left)
            traverse(current_node.right)
            post_order_result += str(current_node.value) + " "



        traverse(self.root)

        return post_order_result

    def get_tree_asc_order(self):
        return self.in_order()


    def get_tree_desc_order(self):
        desc_order = ""

        def traverse(current):
            nonlocal desc_order
            if current is None : return desc_order

            #! same idea as in_order, but first visit RIGHT, then LETT
            traverse(current.right)
            desc_order += str(current.value) + " "
            traverse(current.left)

        traverse(self.root)
        return desc_order

if __name__ == "__main__":
    import os

    # os.system('cls||clear')
    os.system("clear")

    tree = BinaryTree()
    tree.insert(7)
    tree.insert(4)
    tree.insert(9)
    tree.insert(1)
    tree.insert(6)
    tree.insert(8)
    tree.insert(10)
    # print(tree.pre_order())
    # print(tree.in_order())
    # print(tree.post_order())
    print(tree.get_tree_asc_order())
    print(tree.get_tree_desc_order())

    # tree = BinaryTree()
    # tree.insert(10)
    # tree.insert(5)
    # tree.insert(15)
    # tree.insert(6)
    # tree.insert(1)
    # tree.insert(8)
    # tree.insert(12)
    # tree.insert(18)
    # tree.insert(17)
    # print(tree.find(15))

