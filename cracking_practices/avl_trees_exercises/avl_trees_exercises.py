import os


class AVL_Tree:
    class _Node:
        def __init__(self, value):
            self.value = value
            self.left = None
            self.right = None
            self.height = 0

        def __str__(self):
            return f"Node: {self.value}"

    def __init__(self):
        self.root = None

    def __str__(self):
        return f"Root: {self.root.value}, Height: {self.root.height}"


    def _set_node_height(self, node):
        node.height = (
            max(self._get_node_height(node.left), self._get_node_height(node.right))
        ) + 1

    def _get_node_height(self, node):
        return -1 if node is None else node.height

    def balance_factor(self, node):
        return (
            0
            if node is None
            else (self._get_node_height(node.left) - self._get_node_height(node.right))
        )

    def is_left_heavy(self, node):
        bf = self.balance_factor(node)
        return self.balance_factor(node) > 1

    def is_right_heavy(self, node):
        bf = self.balance_factor(node)
        return self.balance_factor(node) < -1


    def balance(self, node):
        if self.is_left_heavy(node):
            # print(self.root.value, " is Left heavy.")
            if self.balance_factor(node.left) < 0:
                print("Left rotate on ", node.left.value)

            # BC is LEFT heavy, ALWAYS perform a RIGHT rotation on the root
            print("Right rotate on ", node.value)

        #  BF < -1 => Right heavy
        if self.is_right_heavy(node):
            # print(self.root.value, " is Right heavy")
            # check if the right child needs rotation
            if self.balance_factor(node.right) > 0:
                print("Right rotate on ", node.right.value)
            # BC is right heavy, ALWAYS perform a left rotation on the root
            print("Left rotate on ", node.value)


    def insert(self, value):
        new_node = self._Node(value)

        if self.root is None:
            self.root = new_node
            return

        def traverse(current):
            nonlocal value, new_node
            if not current:
                return

            if value < current.value:
                if current.left is None:
                    current.left = new_node
                else:
                    traverse(current.left)
            else:
                if current.right is None:
                    current.right = new_node
                else:
                    traverse(current.right)

            self._set_node_height(current)


            self.balance(current)
            # if self.is_left_heavy(current):
            #     # right rotate, follow by left rotate
            #     print("Node: ", current.value, "   => Left heavy, rotate Right")

            # if self.is_right_heavy(current):
            #     print( "Node: ", current.value, ", height:", current.height, "   => Right heavy, rotate Left",  )

        traverse(self.root)


    def _tests_avl_tree(self):
        pass


if __name__ == "__main__":
    os.system("clear")
    avl = AVL_Tree()
    avl.insert(10)
    avl.insert(20)
    avl.insert(30)
    print("stop")
    # print(avl)
    # print(avl.root.left.value)
    # print(avl.root.left.left.value)
    # print(avl.root.right.value)
# __
