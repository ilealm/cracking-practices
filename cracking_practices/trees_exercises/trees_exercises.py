import os
import math


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

            if current_node is None:
                return

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
            if current is None:
                return desc_order

            #! same idea as in_order, but first visit RIGHT, then LETT
            traverse(current.right)
            desc_order += str(current.value) + " "
            traverse(current.left)

        traverse(self.root)
        return desc_order

    def height(self):
        if self.root is None:
            return -1

        def traverse(current):
            if current.left is None and current.right is None:
                return 0

            return 1 + max(traverse(current.left), traverse(current.right))

        return traverse(self.root)

    # helper function to test other functions
    def swap_tree(self):
        self.root.right, self.root.left = self.root.left, self.root.right
        return "Tree swapped"

    def get_min_value(self):
        if self.root is None:
            return -1

        min_value = math.inf

        def traverse(current):
            if current is None:
                return
            nonlocal min_value

            if current.value < min_value:
                min_value = current.value
            traverse(current.left)
            traverse(current.right)

        traverse(self.root)
        return min_value

    def get_max_value(self):
        if self.root is None:
            return -1

        max_value = -math.inf

        def traverse(current):
            if current is None:
                return
            nonlocal max_value

            if current.value > max_value:
                max_value = current.value
            traverse(current.left)
            traverse(current.right)

        traverse(self.root)
        return max_value

    def are_equal_trees(self, second_tree):
        if not self.root or not second_tree.root:
            return False

        def traverse(current_A, current_B):
            if current_A is None or current_B is None:
                return True

            if not current_A is None and not current_B is None:
                return (
                    (current_A.value == current_B.value)
                    and traverse(current_A.left, current_B.left)
                    and traverse(current_A.right, current_B.right)
                )

            return False

        return traverse(self.root, second_tree.root)

    def is_BinarySearchTree(self):
        if self.root is None:
            return True

        def traverse(current, range_min, range_max):
            if not current:
                return True
            # preorder traversal

            if not ((range_min < current.value) and (current.value < range_max)):
                return False

            return traverse(current.left, range_min, current.value) and traverse(
                current.right, current.value, range_max
            )

        return traverse(self.root, -math.inf, math.inf)

    # ! This method also PRINT THE NODES AT K DEEP
    def get_nodes_k_distance(self, k):
        kth_nodes = ""

        def traverse(current, k):
            nonlocal kth_nodes
            if not current:
                return

            if k == 0:
                kth_nodes += str(current.value) + " "
                return

            k -= 1
            traverse(current.left, k)
            traverse(current.right, k)

        traverse(self.root, k)

        return kth_nodes if not kth_nodes == "" else "There is not kth distance."

    def get_nodes_at_kth_deep(self, k):
        return self.get_nodes_k_distance(k)


    def traverse_level_order(self):
        if self.root is None :
            return

        tree_hight = self.height() + 1
        for i in range(0,tree_hight):
            print(self.get_nodes_k_distance(i))




def tests_on_binary_search_trees():
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
    # print(tree.get_tree_asc_order())
    # print(tree.get_tree_desc_order())
    # print(tree.height())
    # print(tree.swap_tree())
    # print(tree.pre_order())
    # print(tree.get_min_value())
    # print(tree.get_max_value())
    # second_tree = BinaryTree()
    # second_tree.insert(7)
    # second_tree.insert(4)
    # second_tree.insert(88)
    # second_tree.insert(10)
    # print(tree.are_equal_trees(second_tree))
    # print(tree.is_BinarySearchTree())
    # print(tree.get_nodes_k_distance(2))
    # print(tree.get_nodes_at_kth_deep(1))
    print(tree.traverse_level_order())


if __name__ == "__main__":
    tests_on_binary_search_trees()

