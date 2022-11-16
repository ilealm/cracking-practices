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

            # height calculation
            left_height = 0 if current.left is None else current.left.height
            right_height = 0 if current.right is None else current.right.height

            current.height = (max(left_height, right_height)) + 1

            # Check if the tree is unbalanced
            # balanceFactor = height(L) - heigh(Right)
            # > 1  => Left heavy, so rotate Right
            # < -1 => Right heavy, so rotate Left
            balanceFactor = left_height - right_height

            if balanceFactor > 1:
                print("   => Left heavy, rotate Right")
            if balanceFactor <= -1:
                print("Node: ", current.value, ", height:", current.height, "   => Right heavy, rotate Left")

        traverse(self.root)

    def _tests_avl_tree(self):
        pass


if __name__ == "__main__":
    os.system("clear")
    avl = AVL_Tree()
    avl.insert(10)
    # avl.insert(5)
    avl.insert(20)
    avl.insert(30)
    # avl.insert(40)
    # avl.insert(50)
    print(avl)
    # print(avl.root.left.value)
    # print(avl.root.left.left.value)
    # print(avl.root.right.value)
# __
