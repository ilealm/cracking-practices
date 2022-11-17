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


    def _get_node_left_height(self, node):
        return 0 if node.left is None else node.left.height

    def _get_node_right_height(self, node):
        return 0 if node.right is None else node.right.height


    def _get_node_height(self, node):
        return (max(self._get_node_left_height(node), self._get_node_right_height(node))) + 1


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

            current.height = self._get_node_height(current)

            # Check if the tree is unbalanced
            balanceFactor = self._get_node_left_height(current) - self._get_node_right_height(current)

            if balanceFactor >= 1:
                print("   => Left heavy, rotate Right")
            if balanceFactor <= -1:
                print(
                    "Node: ",
                    current.value,
                    ", height:",
                    current.height,
                    "   => Right heavy, rotate Left",
                )

        traverse(self.root)



    def insert_v1(self, value):
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
            current_left_height = 0 if current.left is None else current.left.height
            current_right_height = 0 if current.right is None else current.right.height

            current.height = (max(current_left_height, current_right_height)) + 1

            # Check if the tree is unbalanced
            # balanceFactor = height(L) - heigh(Right)
            # > 1  => Left heavy, so rotate Right
            # < -1 => Right heavy, so rotate Left
            balanceFactor = current_left_height - current_right_height

            if balanceFactor >= 1:
                print("   => Left heavy, rotate Right")
            if balanceFactor <= -1:
                print(
                    "Node: ",
                    current.value,
                    ", height:",
                    current.height,
                    "   => Right heavy, rotate Left",
                )

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
