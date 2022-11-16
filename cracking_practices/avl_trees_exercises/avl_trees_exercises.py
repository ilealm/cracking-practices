import os


class AVL_Tree:
    class _Node:
        def __init__(self, value):
            self.value = value
            self.left = None
            self.right = None

        def __str__(self):
            return f"Node: {self.value}"


    def __init__(self):
        self.root = None

    def __str__(self):
        return f"Root: {self.root.value}"


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

        traverse(self.root)

    def _tests_avl_tree(self):
        pass


if __name__ == "__main__":
    os.system("clear")
    avl = AVL_Tree()
    avl.insert(10)
    avl.insert(20)
    avl.insert(30)
    print(avl)
    # print(avl.root.left.value)
    # print(avl.root.left.left.value)
    # print(avl.root.right.value)
# __
