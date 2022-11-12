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


if __name__ == "__main__":
    import os

    # os.system('cls||clear')
    os.system("clear")

    tree = BinaryTree()
    tree.insert(10)
    tree.insert(5)
    tree.insert(15)
    tree.insert(6)
    tree.insert(1)
    tree.insert(8)
    tree.insert(12)
    tree.insert(18)
    tree.insert(17)
    print(tree.find(15))

