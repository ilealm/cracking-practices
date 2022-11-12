class Tree():
    def __init__(self):
        self.root = None

    class _Node():
        def __init__(self, value):
            self.value = value
            self.left = None
            self.right = None


    def add(self, value):
        if not value : return

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


        # print(new_node.value)


if __name__ == '__main__':
    import os
    # os.system('cls||clear')
    os.system('clear')

    tree = Tree()
    tree.add("50")
    tree.add("25")
    tree.add("10")
    tree.add("70")

